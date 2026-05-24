class Solution:
    def simplifyPath(self, path: str) -> str:
        dir = []
        pl = list(filter(lambda x: len(x) > 0, path.split("/")))
        for pt in pl:
            match pt:
                case str() if pt.startswith("/"): 
                    pass
                case "..":
                    if len(dir) > 0:
                        dir.pop()
                case ".":
                    pass
                case _:
                    dir.append(pt)
        d = list(filter(lambda x: len(x) > 0, dir))
        return "/" + "/".join(d)
