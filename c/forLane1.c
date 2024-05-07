#include <stdio.h>

int main() {
	int length, width, height;
	
	printf("What is the length of the object?\n");
	scanf("%d", &length);
	
	printf("What is the width of the object?\n");
	scanf("%d", &width);
	
	printf("What is the height of the object?\n");
	scanf("%d", &height);
	
	int objectSurfaceArea = 2 * (width * length + length * height + height * width);
	
	printf("%d", objectSurfaceArea);
	return 0;
}