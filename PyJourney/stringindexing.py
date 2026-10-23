# =====================================================================
# STRING INDEXING IN PYTHON
# =====================================================================
# Python uses 0-based indexing to access individual characters.
# You can count forward from the left (0) or backward from the right (-1).
# =====================================================================

# CONCEPTUAL VISUALIZATION:
# String:       [  'P'  |  'Y'  |  'T'  |  'H'  |  'O'  |  'N'  ]
# Positive Idx:     0       1       2       3       4       5    (Left to Right)
# Negative Idx:    -6      -5      -4      -3      -2      -1    (Right to Left)

# Define our sample string variable
#[start:end:steps]
alphabets = "abcdefghijklmnopqrstuvwxyz"

indexing = alphabets[1]
indexing2 = alphabets[1:26:2]
indexing3 = alphabets[::-1]
print(indexing2)