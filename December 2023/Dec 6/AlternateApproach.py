#TODO convert to python
'''class Solution {
public:
    long long int countXHelper(long long int N, int X)
    {

        long long int cnt = 0;

        for (long long int i = 1; i <= N; i *= 10) {
            long long int divi = i * 10;
            long long int quot = N / divi;
            long long int rem = N % divi;

            if (quot > 0) {
                cnt = cnt + (quot * i);
            }

            if (X == 0) {
                cnt = cnt - i;
            }

            if (rem >= X * i) {
                cnt = cnt + (min(rem - X * i + 1, i));
            }
        }

        return cnt;
    }

    int countX(int L, int R, int X)
    {

        return countXHelper(R - 1, X) - countXHelper(L, X);
    }
};'''