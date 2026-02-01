#include <stdio.h>

int main(void){
	
	int t;
	scanf("%d", &t);
	
	
	int x, n;
	for(int i = 0; i < t; i++){
		scanf("%d %d", &x, &n);
		
		int count = 0;
		for(int c = x; c <= n+1; c++){
			int val = x+2*n+1;
			if(c-1-x<=0 && val%(2*c)==0){
				count++;
				//printf("%d/",c);
			}
			else if(x==c){
			count++;
			}
			
		}
		if(x==1){
			count++;
			//printf("%d/",n+1);
		}
		else if(x==n){
			count++;
			//printf("%d/",n);
		}

		
		printf("%d\n", count);
	}
	
	return 0;
}
