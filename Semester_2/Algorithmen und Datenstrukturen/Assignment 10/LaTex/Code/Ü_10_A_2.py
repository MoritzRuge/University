def edit_distance(str1, str2):
    matrix = [[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # i and j mark the current substring of the respective string. if i or j == 0 than the total amount of edits needed is 
            # exactly j / i because "" needs i / j edits to reach str1[:i] / str2[:j]
            if i == 0:
                matrix[i][j] = j
            elif j == 0:
                    matrix[i][j] = i
            elif str1[i-1] == str2[j-1]: # If the last characters in each string match then the required amount of edits to reach that substring is the amount of edits from the previous substring
                    matrix[i][j] = matrix[i-1][j-1]
            else:  # If the last chars in both string dont match.
                matrix[i][j] = 1+ min(matrix[i][j-1], matrix[i-1][j], matrix[i-1][j-1])
                # matrix[i][j-1]: insert / append to str1, matrix[i-1][j] remove last char from str1: appending , matrix[i-1][j-1]: replace char in 
    return matrix[len(str1)][len(str2)] # the bottom right index stores the minimal edits needed to convert str1 to str2. 

def main():
    print(edit_distance("apfel","pferd")) # converting apfel to pferd. The order of strings matters for the order of operations

main()
# this algorithmn creats a matrix (dictionary) that stores the amount of edits necesarry to convert every substring of str1 to every substring in str2,
# where index matrix[len(str1)][len(str2)] gives the amount of edits needed to convert str1 to str2. operations are always performed on the ast char of str1
# not performing a operation is equivalent to dropping last char from both strings.
# example run -> The goal is to convert str1 to str2
#[ ][i][a][p][f][e][l]
#[j][0][1][2][3][4][5]
#[p][1][1][1][2][3][4]
#[f][2][2][2][1][2][3]
#[e][3][3][3][2][1][2]
#[r][4][4][4][3][2][2]
#[d][5][5][5][4][3][3]
# matrix[0][j] and matrix[i][0] store how many chars need to be added to "" to reach str2 and str1 
# e.g: "" to "ap" needs to edits the same counts for "" to "pf"
# e.g: "ap" to "pf" needs 1 edit. 
# e.g matrix[3][1] ==> str1[2] = f != str2[0] = p -> matrix[3][1] = 1+min(matrix_left,matrix_top,matrix_top_left) = 1+1 = 2 matrix[3][1]
# check: "p" to "apf" -> insert(a), insert(f)

# this alogrithmn has O(kl) because in the worst-case of two completly different strings l operations have to be performed on k chars., where k = len(str1), l = len(str2)
# The reason this aproach is faster, is because it is using previous calculated edits -> recursion for every path no longer needed.
# for every index matrix[i][j] it is checking previous calculations -> lookup O(1)  

# idea to track operations taken (this is an conceptual idea not an error proof implementation):
# add paramter list[] to track the path of operations  -> append,delete,swap -> edit_distance(str1,str2,opt_taken)
# the list starts of empty  
# After every opertaion return the name of the operation taken is appended to the list -> done by checking which index in matrix in min() was chosen.
# cases:
# 1. nothing: str1[i-1] == str2[j-1] -> nothing
# 2. appending a char -> opt_take.append("append")
# 3. deleting a char -> opt_take.append("delete")
# 4. swapping a char -> opt_take.append("swap")
