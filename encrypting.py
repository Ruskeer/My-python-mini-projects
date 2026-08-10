master_key = "938201924853984"

def encrypting_nu(pin, key, method):
    key_index = 0
    numbers = "1234098765"
    result = ""
    translation = ""

    #for number in pin:
        #turned_number = str(number)
        #translation += turned_number

    for char in pin:

            # 9[0] -> 3[1] -> 8[2] -> etc...
            indexofkey = key_index % len(key)
            # 9 -> 3 -> 8 -> etc...
            showkey = key[indexofkey]
            # 9[5] -> 3[2] -> 8[6] -> etc...
            shift = numbers.index(showkey)

            # example. PIN CODE IS : 4425
            # 4[3] -> 4[3] -> 2[1] -> 5[9]
            indexofchar = numbers.index(char)

            if method == "encrypt":
                # [3] - [5] = answer is 6 from the value of number
                formula = (indexofchar + shift) % len(numbers)
                tweak = (formula - 88)  %len(numbers)

            elif method == "decrypt":
                formula = (indexofchar - shift) % len(numbers)
                tweak = (formula + 88) %len(numbers)

            result += numbers[tweak]
            key_index += 1
    return result



