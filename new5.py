def palindrome(str):
    if str == str[::-1]:
	    return True
    else:
	    return False

print(palindrome("caabbaac"))
print(palindrome("abcdf"))
print(palindrome("radar"))