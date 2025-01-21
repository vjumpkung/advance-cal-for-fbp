class PreviewImage:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
            },
        }

    RETURN_TYPES = ()
    FUNCTION = "preview_image"

    OUTPUT_NODE = True

    CATEGORY = "image"

    def preview_image(self, image):
        return {"ui": {"images": (image,)}}
