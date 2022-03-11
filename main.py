class Roman:
    romans = {
        1000: 'M',
        500: 'D',
        100: 'C',
        50: 'L',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I',
    }
    def convert_if(self, number: int, acc: str = ''):
        if number <= 0:
            return acc

        if number >= 1000:
            number -= 1000
            acc += 'M'
        if number >= 500:
            number -= 500
            acc += 'D'
        if number >= 100:
            number -= 100
            acc += 'C'
        if number >= 50:
            number -= 50
            acc += 'L'
        if number >= 10:
            number -= 10
            acc += 'X'
        if number >= 9:
            number -= 9
            acc += 'IX'
        if number >= 5:
            number -= 5
            acc += 'V'
        if number >= 4:
            number -= 4
            acc += 'IV'
        if number >= 1:
            number -= 1
            acc += 'I'

        return self.convert_if(number, acc)

    def convert_for(self, number: int, acc: str = ''):
        for index in self.romans:
            if index > number:
                continue

            count = number // index
            number -= index * count
            if count > 0:
                acc += self.romans[index] * count

            if number <= 0:
                break

        return acc

    def convert(self, number: int, acc: str = ''):
        return self.convert_if(number, acc)