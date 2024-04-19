def longest_common_substring(s1, s2):
    matrix = [[0]*(1+len(s2)) for i in range(1+len(s1))]
    longest, x_longest = 0, 0
    for x in range(1, 1+len(s1)):
        for y in range(1, 1+len(s2)):
            if s1[x-1] == s2[y-1]:
                matrix[x][y] = matrix[x-1][y-1] + 1
                if matrix[x][y]>longest:
                    longest = matrix[x][y]
                    x_longest  = x
            else:
                matrix[x][y] = 0
    return s1[x_longest-longest: x_longest]

# Test the function with sample strings
s1 = "Hello, how are you?"
s2 = "Hello, how have you been?"
print(longest_common_substring(s1, s2))
