#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){
	
	
	int min = 0;
	int max = 2025;
	int temp = (min+max)/2;
	
	char str[1000];
	
	printf("? %d\n", temp);
	fflush(stdout);
	
	while(1){
						
		scanf("%s", str);
		
		if(str[0] == 'H'){ // temp > curr
			min = (temp+min)/2;
			max = temp;
		}
		else if (str[0] == 'C'){ // temp < curr
			min = temp;
			max = (temp+max)/2;
		}
		else{ // success
			printf("! %d\n", temp);
			break;
		}
		
		temp = (max+min)/2;
		printf("? %d\n", temp);
		fflush(stdout);
		
	}
	return 0;
}
