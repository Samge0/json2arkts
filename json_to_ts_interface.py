import json

class JsonToTSInterface:
    
    sub_class_list = []
    
    def __init__(self):
        pass

    def convert(self, json_str):
        self.sub_class_list = []
        data = json.loads(json_str)
        ts_classes = self._parse_dict(data, "Root")
        return ts_classes

    def _parse_dict(self, data, class_name):
        ts_code = f"export interface {class_name} {{\n"
        for key, value in data.items():
            if isinstance(value, dict):
                nested_class_name = f"{class_name}_{key.capitalize()}"
                ts_code += f"    {key}: {nested_class_name};\n"
                self.sub_class_list.append(self._parse_dict(value, nested_class_name))
            elif isinstance(value, list):
                if value and isinstance(value[0], dict):
                    nested_class_name = f"{class_name}{key.capitalize()}"
                    ts_code += f"    {key}: {nested_class_name}[];\n"
                    self.sub_class_list.append(self._parse_dict(value[0], nested_class_name))
                else:
                    ts_type = self._get_ts_type(type(value[0]))
                    ts_code += f"    {key}: {ts_type}[];\n"
            else:
                ts_type = self._get_ts_type(type(value))
                ts_code += f"    {key}: {ts_type};\n"
        ts_code += "}\n"
        return ts_code + "\n" + "\n\n".join(self.sub_class_list)

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
    converter = JsonToTSInterface()
    json_input = '{"name": "John", "age": 30, "address": {"street": "123 Main St", "city": "Anytown"}}'
    ts_output = converter.convert(json_input)
    print(ts_output) 