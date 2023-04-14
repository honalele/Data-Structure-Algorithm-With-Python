import gradio as gr

def greet(name):
    """_summary_

    Args:
        name (_type_): _description_
        

    Returns:
        _type_: _description_
    """    
    return "Hello " + name + "!"


def test_gradio():
    """_summary_
    fn: the function to wrap a UI around
    inputs: which component(s) to use for the input (e.g. "text", "image" or "audio")
    outputs: which component(s) to use for the output (e.g. "text", "image" or "label")
          """
    demo = gr.Interface(fn=greet, inputs="text", outputs="text")

    demo.launch()

if "__name__" == "__main__":
    test_gradio()
        