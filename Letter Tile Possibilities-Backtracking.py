
def helper(string, path, res):
            if path not in res:
                res.add(path)
                if len(path) == len(tiles): return
                for i in range(len(string)):
                    helper(string[:i] + string[i + 1:], path + string[i], res)
            else:
                return

res = set()
tiles=input()
helper(tiles, '', res)

print(len(res) - 1)
