def generate_webform(field_dict_list):
    generated_field_list = []

    for field_dict in field_dict_list:
        if field_dict["type"] == "text_field":
            generated_field_list.append(
                '{0}<br><input type="text" name="{1}"/></br>'.format(
                    field_dict["label"],
                    field_dict["name"],
                )
            )

        elif field_dict["type"] == "checkbox":
            generated_field_list.append(
                '<br><input type="checkbox" id={0} value={1}"/>{2}</br>'.format(
                    field_dict["id"],
                    field_dict["value"],
                    field_dict["label"],
                )
            )

    generated_fields = "\n".join(generated_field_list)

    return f"<form>{generated_fields}</form>"


def build_html_webform(field_list):
    with open("form_file.html", "w") as f:
        f.write("<html><body>{}</body><html>".format(generate_webform(field_list)))


if __name__ == "__main__":
    field_list = [
        {
            "type": "text_field",
            "label": "Best text you have ever written",
            "name": "best_text",
        },
        {
            "type": "checkbox",
            "id": "check_it",
            "value": 1,
            "label": "Check for one",
        },
        {
            "type": "text_field",
            "label": "Another text field",
            "name": "text_filed2",
        },
    ]
    build_html_webform(field_list)
