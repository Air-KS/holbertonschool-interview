#include "slide_line.h"

/**
 * slide_line - reproduce the 2048 game(NSFW !!) mechanics on a single
 * horizontal line.
 * @line: Pointer to the line array
 * @size: Size of array
 * @direction: Direction eft or right
 * Return: 1 upon success, or 0 upon failure
 */

int slide_line(int *line, size_t size, int direction)
{
	size_t targetIndex = 0, moveIndex = 0, step = 0, stop = size;
	int tempo;

	if (!line || (direction != SLIDE_LEFT && direction != SLIDE_RIGHT))
		return (0);

	if (direction == SLIDE_RIGHT)
	{
		targetIndex = size - 1;
		moveIndex = size -1;
		step = -1;
		stop = -1;
	}

	while (targetIndex != stop)
	{
		if (*(line + targetIndex) != 0)
		{
			if (tempo == *(line + targetIndex))
			{
				*(line + targetIndex) += tempo;
				tempo = -1;
			}
			else
			{
				tempo = *(line + targetIndex);
				if ((direction == SLIDE_LEFT && targetIndex != 0)
				||
				(direction == SLIDE_RIGHT && targetIndex != (size - 1)))
					if (*(line + moveIndex) != 0)
						moveIndex += step;
			}
			*(line + moveIndex) = *(line + targetIndex);
			if (moveIndex != targetIndex)
				*(line + targetIndex) = 0;
		}
		targetIndex += step;
	}

	return (1);
}
