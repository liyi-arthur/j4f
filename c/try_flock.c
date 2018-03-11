#include <unistd.h>
#include <stdio.h>
#include <sys/file.h>

int main()
{
    int fd, ret;
    int pid;

    fd = open("./test.txt", O_RDWR);
    if (-1 == fd)
    {
        printf("Open failed!\n");
        return -1;
    }

    printf("begin lock!\n");
    ret = flock(fd, LOCK_EX);
    printf("locked!\n");

    while (1)
    {
        sleep(1000);
    }
}

