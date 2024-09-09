###############################################################################
# Collaboration                                                               #
# -------------                                                               #
# You can collaborate with up to 3 classmates (for a total of 4 students per  #
# group). If you do so, remember not to share code directly. Discussions are  #
# fine, code sharing is not. Also note that all have to submit individually.  #
#                                                                             #
# Enter any collaborators here:                                               #
# Collaborator 1: Jubei Ellis                                                 #
# Collaborator 2:                                                             #
# Collaborator 3:                                                             #
###############################################################################


def fizzbuzz(start, finish):
    '''fizzbuzz(start, finish)
    Prints all numbers between int start and int finish.

    When printing, if the number is a multiple of 3, it instead says "fizz".
    Likewise, it says "buzz" if it is a multiple of 5,
    and "fizzbuzz" if both of these conditions are true.'''

    for n in range(start, (finish + 1)):
        # Look for fizz condition
        fizz = (
            True if (n % 3 == 0)
            else True if "3" in str(n)
            else False
        )

        # Look for buzz condition
        buzz = (
            True if (n % 5 == 0)
            else True if "5" in str(n)
            else False
        )
        
        # Ternary op; checks if function is cleanly divisible by 3 and/or 5
        print(
            "fizzbuzz" if fizz and buzz
            else "fizz" if fizz
            else "buzz" if buzz
            else n
        )
