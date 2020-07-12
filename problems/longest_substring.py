def length_of_longest_substring(s: str) -> int:
    known_chars = []
    record = 0

    for i in range(0, len(s)):

        if s[i] in known_chars:

            if len(known_chars) > record:
                record = len(known_chars)

            index = known_chars.index(s[i])
            known_chars = known_chars[index+1:]

            known_chars.append(s[i])

        else:
            known_chars.append(s[i])

    if len(known_chars) > record:
        record = len(known_chars)

    return record


def main():
    result = length_of_longest_substring("ohvhjdml")
    print(result)

    known_chars = ["a", "b", "c", "d"]
    print(known_chars)
    print(known_chars[1:])


if __name__ == "__main__":
    main()
