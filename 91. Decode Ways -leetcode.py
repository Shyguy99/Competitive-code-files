class Solution:
    def numDecodings(self, s: str) -> int:

        def tra(n, s, dp):

            if n - 1 == -1:
                dp[n] = 1
                return dp[n]
            if n - 1 == 0:
                if s[n - 1] == '0':
                    dp[n] = 0
                    return dp[n]
                dp[n] = 1
                return dp[n]

            if dp[n] != -1: return dp[n]

            if s[n - 1] == '0':
                if int(s[n - 2]) <= 2 and int(s[n - 2]) >= 1:
                    dp[n] = tra(n - 2, s, dp)
                    return dp[n]
                else:
                    dp[n] = 0
                    return dp[n]
            else:
                if int(s[n - 1]) > 6:
                    if int(s[n - 2]) == 1:
                        dp[n] = tra(n - 1, s, dp) + tra(n - 2, s, dp)
                        return dp[n]
                    else:
                        dp[n] = tra(n - 1, s, dp)
                        return dp[n]
                else:
                    if int(s[n - 2]) <= 2 and int(s[n - 2]) >= 1:
                        dp[n] = tra(n - 1, s, dp) + tra(n - 2, s, dp)
                        return dp[n]

                    else:
                        dp[n] = tra(n - 1, s, dp)
                        return dp[n]

        dp = [-1 for i in range(len(s) + 1)]
        return tra(len(s), s, dp)

