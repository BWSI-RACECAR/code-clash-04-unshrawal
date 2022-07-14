class Solution:
    def validateName(self,input):
        # type input: string
        # return: bool
            
        # TODO: Write code below to return a bool with the solution to the prompt
        for i in range(0, len(input)):
            for j in range(0, len(input)):
                if i == j:
                    continue
                if input[i] == input[j]:
                    return False
        return True
        pass

def main():
    string1 = input()

    tc1 = Solution()
    ans = tc1.validateName(string1)
    print(ans)

if __name__ == "__main__":
    main()