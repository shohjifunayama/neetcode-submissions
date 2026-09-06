class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if set(s) & set(t) != set(t):
            return ""

        if len(t) == 1:
            if t in s:
                return t
            else:
                return ""
        else:
            def is_included(d, a):
                for key, num in a.items():
                    if d[key] < num:
                        return False
                return True
            
            d = dict.fromkeys(set(s)|set(t), 0)
            ans = {}
            for c in set(t): ans[c] = t.count(c)
            
            l, r = 0, 0
            res = ""
            

            while r < len(s):
                while r < len(s):
                    d[s[r]] += 1
                    r += 1
                    if is_included(d, ans):
                        break
                sw = False
                while is_included(d, ans):
                    d[s[l]] -= 1
                    l += 1
                    sw = True
                
                res = s[l-1:r] if sw and (r - l + 1 < len(res) or res == "") else res

        return res
