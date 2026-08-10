# getImageSourceSupportedFormats

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## getImageSourceSupportedFormats

```TypeScript
function getImageSourceSupportedFormats(): string[]
```

获取支持解码的图片格式，图片格式以mime type表示。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-image-function getImageSourceSupportedFormats(): string[]--><!--Device-image-function getImageSourceSupportedFormats(): string[]-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Return value:**

| Type | Description |
| --- | --- |
| string[] | 支持解码的图片格式（mime type）列表。 |

## Examples

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

