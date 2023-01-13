class CPFValidator:
    LENGTH_DIGITS = 11
    FIRST_CHECK_DIGIT = LENGTH_DIGITS - 1

    def __init__(self, document):
        self.__documentNumber = document

    def isCPF(self):
        if len(self.__documentNumber) != self.LENGTH_DIGITS:
            return False

        if not self.__isDigitsValid():
            return False

        if not self.__isLastDigitValid():
            return False

        if not self.__isNextToLastDigitValid():
            return False

        return True

    def __isDigitsValid(self):
        validDigits = 0
        for digit in range(0,self.LENGTH_DIGITS):
                validDigits += int(self.__documentNumber[digit])
                digit += 1
        if int(self.__documentNumber[0]) == validDigits / self.LENGTH_DIGITS:
            return False
        return True
    
    def __calculateDigit(self, digitPosition):
        total = 0
        multiplier = 10
        index = digitPosition - multiplier
        for i in range(index, digitPosition-1):
            value = int(self.__documentNumber[i])
            total += (value * multiplier)
            i += 1
            multiplier -= 1
        digit = self.LENGTH_DIGITS - (total % self.LENGTH_DIGITS)
        return 0 if digit >= 10 else digit

    def __isNextToLastDigitValid(self):
        return int(self.__documentNumber[9]) == self.__calculateDigit(self.FIRST_CHECK_DIGIT)

    def __isLastDigitValid(self):
        return int(self.__documentNumber[10]) == self.__calculateDigit(self.LENGTH_DIGITS)