from num2words import num2words
import tts


class Plugin:
    name = "math"
    keywords = ["math"]
    author = "neb"
    version = 0.01
    commands = []

    def process(self, text):

        if "plus" in text:
            result = self.text2int(text.split("plus")[0]) + self.text2int(text.split("plus")[1])
            tts.speak(num2words(result))
        if "minus" in text:
            result = self.text2int(text.split("minus")[0]) - self.text2int(text.split("minus")[1])
            tts.speak(num2words(result))
        if "times" in text:
            result = self.text2int(text.split("times")[0]) * self.text2int(text.split("times")[1])
            tts.speak(num2words(result))
        if "divided by" in text:
            result = self.text2int(text.split("divided by")[0]) / self.text2int(text.split("divided by")[1])
            tts.speak(num2words(result))

    def text2int(self, textnum, numwords={}):
        if not numwords:
            units = [
                "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
                "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
                "sixteen", "seventeen", "eighteen", "nineteen",
            ]

            tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

            scales = ["hundred", "thousand", "million", "billion", "trillion"]

            numwords["and"] = (1, 0)
            for idx, word in enumerate(units):    numwords[word] = (1, idx)
            for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
            for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

        current = result = 0
        for word in textnum.split():
            if word not in numwords:
                raise Exception("Illegal word: " + word)

            scale, increment = numwords[word]
            current = current * scale + increment
            if scale > 100:
                result += current
                current = 0

        return result + current

    def int2text(self, num):
        d = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
             6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
             11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
             15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
             19: 'nineteen', 20: 'twenty',
             30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
             70: 'seventy', 80: 'eighty', 90: 'ninety'}
        k = 1000
        m = k * 1000
        b = m * 1000
        t = b * 1000

        assert (0 <= num)

        if (num < 20):
            return d[num]

        if (num < 100):
            if num % 10 == 0:
                return d[num]
            else:
                return d[num // 10 * 10] + '-' + d[num % 10]

        if (num < k):
            if num % 100 == 0:
                return d[num // 100] + ' hundred'
            else:
                return d[num // 100] + ' hundred and ' + self.int2text(num % 100)

        if (num < m):
            if num % k == 0:
                return self.int2text(num // k) + ' thousand'
            else:
                return self.int2text(num // k) + ' thousand, ' + self.int2text(num % k)

        if (num < b):
            if (num % m) == 0:
                return self.int2text(num // m) + ' million'
            else:
                return self.int2text(num // m) + ' million, ' + self.int2text(num % m)
