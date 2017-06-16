#include<stdio.h>
#include<time.h>

int _leap_months[12] = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
int _months[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

int *total_months(int m1, int y1, int m2, int y2) {
  int years, first, last, rest;
  static int result[2];

  years = y2 - y1;
  first = 12 - m1;
  last = 12 - m2;
  rest = years * 12;
  result[0] = m1 + 1;
  result[1] = first - last + rest - 1;

  return result;
}

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
  int val = 0;

  if(month == 2)
    val = isleap(year);
  if(val == 1){
    return _leap_months[month-1];
  } else {
    return _months[month-1];
  }
}

int days_bw_dates(int d1, int m1, int y1, int d2, int m2, int y2) {
  int total, count, initial_month_days, month, no_months;
  int *p;

  total = 0;
  count = 0;
  initial_month_days = days_in_month(m1, y1);
  initial_month_days = initial_month_days - d1;
  if (y1 == y2 && m1 == m2){
    return d2 - d1;
  }
  p = total_months(m1, y1, m2, y2);
  month = p[0];
  no_months = p[1];
  for(int i = 1; i<no_months+1;i++){
    count = count + 1;
    if(month>12){
      month = month - 12;
      y1 = y1 + 1;
    }
    total = total + days_in_month(month, y1);
    month = month+1;
  }
  return initial_month_days + total + d2;
}

int main(){
  double t1;
  clock_t tic, toc;
  tic = clock();

  printf("days: %d\n", days_bw_dates(5, 5, 2017, 14, 6, 2017));
  printf("days: %d\n", days_bw_dates(23, 4, 2017, 24, 8, 2017));
  printf("days: %d\n", days_bw_dates(26, 8, 1993, 11, 1, 2021));
  printf("days: %d\n", days_bw_dates(26, 8, 1993, 15, 6, 2017));
  printf("days: %d\n", days_bw_dates(14, 1, 2016, 28, 4, 2017));

  toc = clock();
  t1 = (double) (toc-tic)/CLOCKS_PER_SEC;

  printf("avg time: %f\n", (double)t1/5);

  return 0;
}
