from diffusers import StableDiffusionPipline
pipe = StableDiffusionPipline.from_pretrained(
    "runway/stable-diffussion-v1-5").to("cpu")
print("Success")