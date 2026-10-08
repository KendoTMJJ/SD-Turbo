# Laboratorio: Generación de imágenes con SD-Turbo

Laboratorio de IA generativa texto-a-imagen usando la librería `diffusers` de Hugging Face.

## Modelo utilizado

**[stabilityai/sd-turbo](https://huggingface.co/stabilityai/sd-turbo)**, cargado con `AutoPipelineForText2Image` y ejecutado en CPU (`float32`).

Parámetros de generación:

| Parámetro             | Valor |
| --------------------- | ----- |
| `num_inference_steps` | 10    |
| `guidance_scale`      | 2.0   |

## Prompt utilizado

```text
Epic cinematic battle between Hulk and Wolverine in the middle of a destroyed city street, Hulk roaring furiously and smashing the ground with enormous strength, Wolverine charging toward Hulk with his adamantium claws extended, intense face expressions, powerful muscular poses, debris and dust flying through the air, shattered concrete, dramatic stormy sky, cinematic lighting, strong backlight, dynamic action composition, low camera angle, dramatic perspective, detailed superhero costumes, realistic skin and textures, highly detailed characters, intense atmosphere, photorealistic, sharp focus, high contrast, blockbuster superhero movie poster, epic scale, masterpiece, 8k
```

Además se usó un *negative prompt* para evitar imágenes borrosas, deformaciones, texto o marcas de agua (ver [src/sd_turbo_genai/__init__.py](src/sd_turbo_genai/__init__.py)).

## Imagen generada

![Imagen generada](imagen.png)

## Ejecución

```bash
uv run src\sd-turbo_genai
```

El programa pide el prompt por consola y guarda el resultado en `imagen.png`.
