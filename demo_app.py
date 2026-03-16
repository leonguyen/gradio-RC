import gradio as gr

# This runs Gradio's built-in Spaces gallery/demo
demo = gr.load("spaces/gradio/calculator", src="http")
demo.queue()
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=10000)
