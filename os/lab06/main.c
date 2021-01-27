#include <stdio.h>
#include <stdbool.h>
#include <windows.h>

#define READERS 5
#define WRITERS 3
#define ITERS 7

HANDLE mutex;
HANDLE can_read;
HANDLE can_write;

int waiting_writers = 0;
int waiting_readers = 0;
int active_readers = 0;

bool is_writer_active = false;
int value = 0;

void start_read()
{
    InterlockedIncrement(&waiting_readers);
    if (waiting_writers > 0 || is_writer_active)
    {
        WaitForSingleObject(can_read, INFINITE);
    }
    WaitForSingleObject(mutex, INFINITE);

    InterlockedDecrement(&waiting_readers);
    InterlockedIncrement(&active_readers);

    SetEvent(can_read);
    ReleaseMutex(mutex);
}

void stop_read()
{
    InterlockedDecrement(&active_readers);
    if (waiting_readers == 0)
    {
        SetEvent(can_write);
    }
}

void start_write()

{
    InterlockedIncrement(&waiting_writers);
    if (active_readers > 0 || is_writer_active)
    {
        WaitForSingleObject(can_write, INFINITE);
    }
    InterlockedDecrement(&waiting_writers);
    is_writer_active = true;
    ResetEvent(can_write);
}

void stop_write(void)
{
    is_writer_active = false;
    if (!waiting_writers)
    {
        SetEvent(can_read);
    }
    else
    {
        SetEvent(can_write);
    }
}

DWORD WINAPI reader()
{
    while (value < WRITERS * ITERS)
    {
        start_read();
        printf("Reader #%ld read value: %d\n", GetCurrentThreadId(), value);
        stop_read();
        Sleep(1000);
    }
    return 0;
}

DWORD WINAPI writer()
{
    for (int i = 0; i < ITERS; i++)
    {
        start_write();
        value++;
        printf("Writer #%ld wrote value: %d\n", GetCurrentThreadId(), value);
        stop_write();
        Sleep(2000);
    }
    return 0;
}

int main(void)
{
    HANDLE wThread[WRITERS];
    HANDLE rThread[READERS];
    if ((mutex = CreateMutex(NULL, FALSE, NULL)) == NULL) 
    {
        perror("CreateMutex");
        return EXIT_FAILURE;
    }

    if ((can_read = CreateEvent(NULL, FALSE, TRUE, NULL)) == NULL) 
    {
        perror("CreateEvent can_read");
        return EXIT_FAILURE;
    }
    if ((can_write = CreateEvent(NULL, TRUE, TRUE, NULL)) == NULL) 
    {
        perror("CreateEvent can write");
        return EXIT_FAILURE;
    }

    for (int i = 0; i < WRITERS; i++)
    {
        wThread[i] = CreateThread(NULL, 0, &writer, NULL, 0, NULL);
        if (wThread[i] == NULL)
        {
            perror("Couldn't create thread");
            return EXIT_FAILURE;
        }
    }

    for (int i = 0; i < READERS; i++)
    {
        rThread[i] = CreateThread(NULL, 0, &reader, NULL, 0, NULL);
        if (rThread[i] == NULL)
        {
            perror("Couldn't create thread");
            return EXIT_FAILURE;
        }
    }

    WaitForMultipleObjects(WRITERS, wThread, TRUE, INFINITE);
    WaitForMultipleObjects(READERS, rThread, TRUE, INFINITE);

    CloseHandle(mutex);
    CloseHandle(can_read);
    CloseHandle(can_write);

    return EXIT_SUCCESS;
}