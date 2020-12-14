#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <string.h>

int main()
{
    int fd[2];

    if (pipe(fd) == -1)
    {
        perror("Couldn't pipe");
        exit(1);
    }
    
    int child1 = fork();
    if (child1 == -1)
    {
        perror("Can't fork");
        exit(1);
    }
    else if (child1 == 0)
    {
        close(fd[0]);
        char msg1[] = "Message from child1";
        write(fd[1], msg1, 64);
        exit(0);
    }   

    int child2 = fork();
    if (child2 == -1)
    {
        perror("Can't fork");
        exit(1);
    }
    else if (child2 == 0)
    {
        close(fd[0]);
        char msg2[] = "Message from child2";
        write(fd[1], msg2, 64);
        exit(0);
    }

    if (child1 != 0 && child2 != 0)
    {
        close(fd[1]);
        char msg1[64];
        read(fd[0], msg1, 64);
        char msg2[64];
        read(fd[0], msg2, 64);
        printf("Parent: read %s %s\n", msg1, msg2);

        int status1;
        pid_t ret1 = wait(&status1);

        if (WIFEXITED(status1))
            printf("Parent: child %d finished with %d code.\n", ret1, WEXITSTATUS(status1));
        else if (WIFSIGNALED(status1))
            printf("Parent: child %d finished from signal with %d code.\n", ret1, WTERMSIG(status1));
        else if (WIFSTOPPED(status1))
            printf("Parent: child %d finished from signal with %d code.\n", ret1, WSTOPSIG(status1));
        
        int status2;
        pid_t ret2 = wait(&status2);

        if (WIFEXITED(status2))
            printf("Parent: child %d finished with %d code.\n", ret2, WEXITSTATUS(status2));
        else if (WIFSIGNALED(status2))
            printf("Parent: child %d finished from signal with %d code.\n", ret2, WTERMSIG(status2));
        else if (WIFSTOPPED(status2))
            printf("Parent: child %d finished from signal with %d code.\n", ret2, WSTOPSIG(status2));
    }
    return 0;
}