#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main()
{
    int child1 = fork();
    if (child1 == -1)
    {
        perror("Can't fork");
        exit(1);
    }
    else if (child1 == 0)
    {
        printf("Child: pid=%d, pidid=%d, groupid=%d\n", getpid(), getppid(), getpgrp());
        sleep(2);
        printf("Child: pid=%d, pidid=%d, groupid=%d\n", getpid(), getppid(), getpgrp());
        return 0;
    }
    printf("Parent: pid=%d, childpid=%d, groupid=%d\n", getpid(), child1, getpgrp());

    int child2 = fork();
    if (child2 == -1)
    {
        perror("Can't fork");
        exit(1);
    }
    else if (child2 == 0)
    {
        printf("Child: pid=%d, pidid=%d, groupid=%d\n", getpid(), getppid(), getpgrp());
        sleep(2);
        printf("Child: pid=%d, pidid=%d, groupid=%d\n", getpid(), getppid(), getpgrp());
        return 0;
    }
    printf("Parent: pid=%d, childpid=%d, groupid=%d\n", getpid(), child2, getpgrp());
    
    return 0;
}