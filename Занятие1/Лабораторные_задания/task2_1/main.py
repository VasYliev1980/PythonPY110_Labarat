def task(camel_case_str: str) -> str:
    return "".join ([c for c in camel_case_str if c.islower()]) # TODO отфильтровать только буквы нижнего регистра


if __name__ == "__main__":
    word = "AbCdEfGh"
    print(task(word))
