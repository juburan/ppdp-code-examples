from abc import ABC, abstractmethod


class Director(ABC):
    def _init__(self):
        self._builder = None

    @abstractmethod
    def constrcut(self, field_list):
        raise NotImplementedError

    def set_builder(self, builder):
        self._builder = builder

    def get_construct_object(self):
        return self._builder.constructed_object


class Builder(ABC):
    def __init__(self, constructed_object):
        self.constructed_object = constructed_object


class Product:
    def __init__(self):
        pass

    def _repr__(self):
        pass


class ConcreteBuilder(Builder):
    pass


class ConcreteDirector(Director):
    pass


class AbstractFormBuilder(ABC):
    def __init__(self):
        self.constructed_object = None

    @abstractmethod
    def add_text_field(self, field_dict):
        pass

    @abstractmethod
    def add_checkbox(self, field_dict):
        pass

    @abstractmethod
    def add_button(self, field_dict):
        pass


class HtmlForm:
    def __init__(self):
        self.field_list = []

    def __repr__(self) -> str:
        return "<form>{}</form>".format("".join(self.field_list))


class HtmlFormBuilder(AbstractFormBuilder):
    def __init__(self):
        self.constructed_object = HtmlForm()

    def add_text_field(self, field_dict):
        self.constructed_object.field_list.append(
            '{0}:<br><input type="text" name="{1}"><br>'.format(
                field_dict["label"], field_dict["field_name"]
            )
        )

    def add_checkbox(self, field_dict):
        self.constructed_object.field_list.append(
            '<br><input type="checkbox" id="{0}" value="{1}">{2}<br>'.format(
                field_dict["field_id"], field_dict["value"], field_dict["label"]
            )
        )

    def add_button(self, field_dict):
        self.constructed_object.field_list.append(
            '<button type="button">{}</button>'.format(field_dict["text"])
        )

    def add_radio(self, field_dict):
        self.constructed_object.field_list.append(
            '<br><input type="radio" value="{0}" id="{1}" name="radio-group"><label for="{1}">{2}</label>'.format(
                field_dict["value"],
                field_dict["field_id"],
                field_dict["label"],
            )
        )


class FormDirector(Director):
    def __init__(self) -> None:
        Director.__init__(self)

    def constrcut(self, field_list):
        for field in field_list:
            if field["field_type"] == "text_field":
                self._builder.add_text_field(field)
            elif field["field_type"] == "checkbox":
                self._builder.add_checkbox(field)
            elif field["field_type"] == "button":
                self._builder.add_button(field)
            elif field["field_type"] == "radio":
                self._builder.add_radio(field)


if __name__ == "__main__":
    director = FormDirector()
    html_form_builder = HtmlFormBuilder()
    director.set_builder(html_form_builder)
    field_list = [
        {
            "field_type": "text_field",
            "label": "Best text ever",
            "field_name": "Field One",
        },
        {
            "field_type": "checkbox",
            "field_id": "check_it",
            "value": "1",
            "label": "Check for on",
        },
        {
            "field_type": "text_field",
            "label": "Another text field",
            "field_name": "Field One",
        },
        {
            "field_type": "button",
            "text": "DONE",
        },
        {
            "field_type": "radio",
            "field_id": "id1",
            "value": "v1",
            "label": "label1",
        },
        {
            "field_type": "radio",
            "field_id": "id2",
            "value": "v2",
            "label": "label2",
        },
    ]
    director.constrcut(field_list)

    with open("form_file.html", "w") as f:
        f.write(
            "<html><body>{0!r}</body></html>".format(director.get_construct_object())
        )
