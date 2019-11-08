import json
import requests


class LeetHelper:
    def __init__(self):
        self.leet = {
            "a": ["4", "@", "∂", "q"],
            "b": ["8", "6", "ß"],
            "c": ["(", "¢", "<", "[", "©"],
            "d": ["?", "|)"],
            "e": ["3", "€", "£", "є", "ë"],
            "f": ["ƒ"],
            "g": ["9"],
            "h": ["#"],
            "i": ["1", "!", "|", "]", ":"],
            "j": ["¿", "ʝ", ";"],
            "k": ["X", "ɮ"],
            "l": ["ℓ"],
            "m": ["M", "m"],
            "n": ["^", "₪"],
            "o": ["0", "¤", "°"],
            "p": ["¶"],
            "q": ["Q", "q"],
            "r": ["®", "Я", "ʁ"],
            "s": ["5", "$", "z", "§"],
            "t": ["7", "+", "†"],
            "u": ["µ", "J", "|_|"],
            "v": ["V", "v"],
            "w": ["w", "ɰ"],
            "x": ["Ж", "×", "8"],
            "y": ["Ψ", "φ", "λ", "Ч", "¥"],
            "z": ["≥", "2", "%"],
            " ": [" "]
        }

    def sortByLen(self, e):
        return len(self.leet[e][0])

    def encode(self, string, level):
        encoded_string = ""
        for i in range(0, len(string)):
            char = string[i].lower()

            if self.leet.__contains__(char):
                if len(self.leet[char]) >= level + 1:
                    encoded_string += self.leet[char][level]
                else:
                    encoded_string += self.leet[char][-1]

            else:
                return "Please only enter valid chars!"

        return encoded_string

    def decode(self, string):
        decoded_string = string
        keys = list(self.leet.keys())

        for i in list(self.leet.keys()):
            self.leet[i].sort(key=len, reverse=True)

        keys.sort(key=self.sortByLen, reverse=True)

        for i in keys:
            for k in self.leet[i]:
                if string.__contains__(k):
                    decoded_string = decoded_string.replace(k, i)

        for s in decoded_string.split(" "):
            response = requests.get(f"https://api.datamuse.com/words?sp={s}")

            if response.status_code == 200:
                result = json.loads(response.content.decode('utf-8'))
                if len(result) > 0:
                    if result[0]["word"]:
                        decoded_string = decoded_string.replace(s, result[0]["word"])

        return decoded_string
