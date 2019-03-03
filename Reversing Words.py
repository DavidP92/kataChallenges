def reverse(st):
    list = st.split()  ##First we will split the string into the a variable called list
    list.reverse()      ## Then reverse the string
    return(" ".join(list))    ##Finally rejoin the list together and return to screen 
