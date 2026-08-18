# getImageSourceSupportedFormats

## Modules to Import

```TypeScript
```

## getImageSourceSupportedFormats

```TypeScript
function getImageSourceSupportedFormats(): string[]
```

Obtains the supported decoding formats, represented by MIME types.

**Since:** 23

<!--Device-image-function getImageSourceSupportedFormats(): string[]--><!--Device-image-function getImageSourceSupportedFormats(): string[]-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string[] |

**Examples**

```TypeScript
async function GetImageSourceSupportedFormats() {
    let formats = image.getImageSourceSupportedFormats();
    console.info('formats:', formats);
}

async function IsSupportedTiffFormat() {
    let formats = image.getImageSourceSupportedFormats();
    return formats.includes("image/tiff");
}
```
