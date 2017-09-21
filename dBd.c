#include<stdio.h>
#include<time.h>

int _months[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

int isleap(int year) {
  return (year%4 == 0 && year%100 != 0) || (year%400 == 0) ? 1 : 0;
}

int days_in_month(int month, int year){
  if(month == 2)
    return isleap(year) == 1 ? 29 : 28;
  return _months[month-1];
  }

int find(int d1, int m1, int y1, int d2, int m2, int y2, int count) {
  if(y1 == y2 && m1 == m2)
    return count + d2 - d1;
  count += days_in_month(m1, y1) - d1 + 1;
  if (m1 == 12)
    y1 += 1, m1 = 1;
  else
    m1 += 1;
  return find(1, m1, y1, d2, m2, y2, count);
}

int main(){
  double t1;
  clock_t tic, toc;
  tic = clock();


  printf("days: %d\n", find(05, 5, 2017, 14, 6, 2017, 0));
  printf("days: %d\n", find(23, 4, 2017, 24, 8, 2017, 0));
  printf("days: %d\n", find(26, 8, 1993, 11, 1, 2021, 0));
  printf("days: %d\n", find(26, 8, 1993, 21, 9, 2017, 0));
  printf("days: %d\n", find(24, 11, 1986, 21, 9, 2017, 0));

  toc = clock();
  t1 = (double) (toc-tic)/CLOCKS_PER_SEC;

  printf("avg time: %f\n", (double)t1/5);

  return 0;
}
