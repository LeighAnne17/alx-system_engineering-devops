#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

int main(void)
{
	pid_t zombie_pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		zombie_pid = fork();

		if (zombie_pid == -1)
		{
			perror("fork");
			return (1);
		}

		if (zombie_pid == 0)
			exit(0);
		printf("Zombie process created, PID: %d\n", zombie_pid);
	}
	infinite_while();
	return (0);
}
