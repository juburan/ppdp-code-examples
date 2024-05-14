def generate_webform(field_list):
    generated_fields = "\n".join(
        map(
            lambda x: f'{x}: <br><input type="text"/ name="{x}"></br>',
            field_list,
        )
    )
    return f"<form>{generated_fields}</form>"


if __name__ == "__main__":
    fields = ["name", "age", "email", "telephone"]
    print(generate_webform(fields))
