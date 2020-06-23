#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>

int printf(const char *format, ...);
int infinite_while(void);

/**
 * main - Creates zombie processes.
 *
 * Return: Always returns 0.
 */

int main(void)
{
	int i;
	pid_t child_pid;

	printf("Parent → %i\n", getpid());

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();
		if (child_pid > 0)
			sleep(50);
		else
		{
			printf("Zombie process created, PID: %i\n", getpid());
			exit (0);
		}
	}

	infinite_while();

	return (0);
}

/**
 * infinite_while - It's a infinite loop.
 *
 * Return: Always returns 0.
 */

int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}
