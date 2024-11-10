import json

class JsonToTSClass:
    
    sub_class_list = []
    
    def __init__(self):
        pass

    def convert(self, json_str):
        self.sub_class_list = []
        data = json.loads(json_str)
        ts_classes = self._parse_dict(data, "Root")
        return ts_classes

    def _parse_dict(self, data, class_name):
        ts_code = f"export class {class_name} {{\n"
        constructor_params = []
        constructor_body = []
        for key, value in data.items():
            if isinstance(value, dict):
                nested_class_name = f"{class_name}_{key.capitalize()}"
                ts_code += f"    {key}: {nested_class_name};\n"
                self.sub_class_list.append(self._parse_dict(value, nested_class_name))
                constructor_params.append(f"{key}: {nested_class_name} = new {nested_class_name}()")
                constructor_body.append(f"        this.{key} = {key};")
            elif isinstance(value, list):
                if value and isinstance(value[0], dict):
                    nested_class_name = f"{class_name}{key.capitalize()}"
                    ts_code += f"    {key}: {nested_class_name}[];\n"
                    self.sub_class_list.append(self._parse_dict(value[0], nested_class_name))
                    constructor_params.append(f"{key}: {nested_class_name}[] = []")
                    constructor_body.append(f"        this.{key} = {key};")
                else:
                    ts_type = self._get_ts_type(type(value[0]))
                    ts_code += f"    {key}: {ts_type}[];\n"
                    constructor_params.append(f"{key}: {ts_type}[] = []")
                    constructor_body.append(f"        this.{key} = {key};")
            else:
                ts_type = self._get_ts_type(type(value))
                ts_code += f"    {key}: {ts_type};\n"
                constructor_params.append(f"{key}: {ts_type}={self._get_default_value(ts_type)}")
                constructor_body.append(f"        this.{key} = {key};")
        # Add constructor
        ts_code += "\n    constructor(" + ", ".join(constructor_params) + ") {\n"
        ts_code += "\n".join(constructor_body) + "\n    }\n"
        ts_code += "}\n"
        return ts_code + "\n" + "\n\n".join(self.sub_class_list)

    def _get_default_value(self, ts_type):
        defaults = {
            "string": '""',
            "number": "0",
            "boolean": "false",
            "any": "null"
        }
        return defaults.get(ts_type, "null")
    def _get_ts_type(self, py_type):
        mapping = {
            str: "string",
            int: "number",
            float: "number",
            bool: "boolean",
            None: "any"
        }
        return mapping.get(py_type, "any")

# 示例使用
if __name__ == "__main__":
    converter = JsonToTSClass()
    json_input = '{"name": "John", "age": 30, "address": {"street": "123 Main St", "city": "Anytown"}}'
    ts_output = converter.convert(json_input)
    print(ts_output) 