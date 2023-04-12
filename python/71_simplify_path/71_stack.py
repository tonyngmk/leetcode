class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []
        files_splitted = path.split("/")

        for f in files_splitted:
            if not f or f == ".": continue
            elif f == "..":
                if stack: stack.pop()
            else: stack.append(f)
        
        return "/" + "/".join(stack)
