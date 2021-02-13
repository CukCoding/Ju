#include <stdio.h>

int main()
{

	int i, j,z, n,m;
	int arr[20][20] = { 0 };
	int sum[20] = { 0 };
	int count[20] = { 0 };
	double result[20] = { 0.0 };

	scanf_s("%d", &n);

	for (i = 0; i < n; i++)
	{
		scanf_s("%d", &m);
		for (j = 0; j < m; j++)
		{
			scanf_s("%d", &arr[i][j]);
			sum[i] += arr[i][j];
		}
		result[i] = sum[i] / m;
		

		for (z = 0; z < m; z++)
		{
			if (arr[i][z]>result[i])
				count[i] += 100;
			//printf("count: %d \n", count[i]);
		
		}
		result[i] =  (double)count[i] / (double)m;

	}

	for (i = 0; i < n; i++)
		printf("%.3f%%\n", result[i]);
		

}