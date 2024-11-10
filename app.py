import gradio as gr
import json

from json_to_ts_class import JsonToTSClass
from json_to_ts_class2 import JsonToTSClass2
from json_to_ts_interface import JsonToTSInterface

# test data
TEST_JSON = '{"pg_size":20,"pg_index":1,"s_name":""}'

converterOfClass = JsonToTSClass()
converterOfClass2 = JsonToTSClass2()
converterOfInterface = JsonToTSInterface()

def convert_to_arkts(input_json, selected_option):
    try:
        if selected_option == "interface":
            # 转换为 Interface
            arkts_code = converterOfInterface.convert(input_json)
            
        elif selected_option == "class":
            # 转换为 Class
            arkts_code = converterOfClass.convert(input_json)
            
        elif selected_option == "class2":
            # 转换为 Class 样式2：没有构造函数，直接在类变量中赋默认值
            arkts_code = converterOfClass2.convert(input_json)
            
        else:
            arkts_code = "暂不支持该转换类型。"
        
        return arkts_code
    except json.JSONDecodeError:
        return "输入的JSON格式有误。"
    except Exception as e:
        return f"转换过程错误：{e}"

with gr.Blocks() as demo:
    gr.Markdown("### JSON转鸿蒙ArkTS（Interface/Class）")
    
    with gr.Row():
        with gr.Column():
            json_input = gr.Textbox(
            label="输入JSON",
            lines=4,
            placeholder='例如: {"type": "interface", "name": "ExampleInterface"}',
            value=TEST_JSON
            )

            dropdown = gr.Dropdown(label="选择类型", choices=["interface", "class", "class2"], interactive=True, value="class")
            convert_button = gr.Button("转换为ArkTS代码")
        output_code = gr.Code(label="生成的ArkTS代码")
        convert_button.click(convert_to_arkts, inputs=[json_input, dropdown], outputs=output_code)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)