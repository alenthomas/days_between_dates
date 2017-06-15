#include<stdio.h>
#include<time.h>

int _leap_months[12] = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
int _months[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

int isleap(int year) {
  if(year%400 == 0)
    return 1;
  else if(year%100 == 0)
    return 0;
  else if(year%4 == 0)
    return 1;
  else
    return 0;
}

int days_in_month(int month, int year){
  int val = isleap(year);
  if(val == 1){
    return _leap_months[month-1];
      } else {
    return _months[month-1];
  }
}

int find(int d1, int m1, int y1, int d2, int m2, int y2, int count){
  if(y1 == y2 && m1 == m2){
    return count + d2 - d1;
  }
  count = count + days_in_month(m1, y1) -d1 + 1;
  d1 = 1;
  if (m1 == 12){
    y1 = y1 + 1;
    m1 = 1;
  } else {
    m1 = m1 + 1;
  }
  return find(d1, m1, y1, d2, m2, y2, count);
}
int main(){
  double t1;
  clock_t tic, toc;
  tic = clock();

  printf("days: %d\n", find(05, 5, 2017, 14, 6, 2017, 0));
  printf("days: %d\n", find(23, 4, 2017, 24, 8, 2017, 0));
  printf("days: %d\n", find(26, 8, 1993, 11, 1, 2021, 0));
  printf("days: %d\n", find(26, 8, 1993, 15, 6, 2017, 0));
  printf("days: %d\n", find(14, 1, 2016, 28, 4, 2017, 0));

  toc = clock();
  t1 = (double) (toc-tic)/CLOCKS_PER_SEC;

  printf("avg time: %f\n", (double)t1/5);

  return 0;
}
