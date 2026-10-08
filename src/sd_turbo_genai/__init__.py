import torch #Ejecuta operaciones matematicas del modelo de IA
from diffusers import AutoPipelineForText2Image
#Diffusers es una libreria especializada en modelos generativos
#


print("Cargando el modelo ...")

modelo = AutoPipelineForText2Image.from_pretrained(
    "stabilityai/sd-turbo",
    torch_dtype=torch.float32 #float16 o float32, con ese tipo de torch
    # Nos indica la precisión numerica con que se cargan los pesos
    
)

modelo = modelo.to("cpu")

prompt = input("Escribe el promt de la imagen que quieres crear: ")

negative_prompt = (
    "blurry, low quality, low resolution, pixelated, jpeg artifacts, "
    "noise, grainy, deformed, distorted, disfigured, bad anatomy, "
    "extra limbs, extra fingers, missing fingers, fused fingers, "
    "mutated hands, poorly drawn face, asymmetric eyes, cropped, "
    "out of frame, watermark, text, signature, logo, oversaturated, "
    "overexposed, duplicate"
)

print("Generando imagen...")

imagen = modelo(
    prompt=prompt,#instrucciónes o detalle oara crear la imagen
    negative_prompt=negative_prompt,
    num_inference_steps=10, #Las veces que va a tardar de crear o refinar
    guidance_scale=2.0 #Que tan fiel debe ser al prompt
).images[0]

imagen.save("imagen.png")
print("Imagen guardada.")
