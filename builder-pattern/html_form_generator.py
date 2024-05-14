def generate_webform(text_field_list=[], checkbox_field_list=[]):
    generated_fields = "\n".join(
        map(
            lambda x: f'{x}: <br><input type="text" name="{x}/"></br>',
            text_field_list,
        )
    )
    generated_fields += "\n".join(
        map(
            lambda x: f'{x}: <br><input type="checkbox" name="{x}/"></br>',
            checkbox_field_list,
        )
    )
    return f"<form>{generated_fields}</form>"


def build_html_form(text_field_list=[], checkbox_field_list=[]):
    with open("form_file.html", "w") as f:
        f.write(
            f"<html><body>{generate_webform( text_field_list=text_field_list, checkbox_field_list=checkbox_field_list,)}</body></html>"
        )


if __name__ == "__main__":
    text_fields = ["name", "age", "email", "telephone"]
    checkbox_fields = ["awesome", "bad"]
    build_html_form(text_field_list=text_fields, checkbox_field_list=checkbox_fields)
