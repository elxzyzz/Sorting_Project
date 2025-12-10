import gradio as gr

def bubble_sort(text_input):
    """Sorts numbers and records steps."""
    try:
        # 1. Input: Turn string into list
        nums = [int(x) for x in text_input.split(',')]
    except:
        return "Error: Use format 5, 1, 3", "Invalid Input"

    steps = []
    steps.append(f"Start: {nums}")

    # 2. Sort Logic
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Compare
            if nums[j] > nums[j + 1]:
                # Swap
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                steps.append(f"Swap {nums[j]} & {nums[j+1]}: {nums}")

    # 3. Output
    return str(nums), "\n".join(steps)

# 4. GUI Setup
with gr.Blocks() as app:
    gr.Markdown("# Simple Bubble Sort App")
    
    inp = gr.Textbox(label="Input (e.g., 5, 3, 8, 1)")
    btn = gr.Button("Run Sort")
    
    out_final = gr.Textbox(label="Final Result")
    out_steps = gr.Textbox(label="Steps Log")

    btn.click(bubble_sort, inputs=inp, outputs=[out_final, out_steps])

if __name__ == "__main__":
    app.launch()