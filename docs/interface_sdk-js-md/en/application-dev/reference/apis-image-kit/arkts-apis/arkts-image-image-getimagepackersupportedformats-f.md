# getImagePackerSupportedFormats

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## getImagePackerSupportedFormats

```TypeScript
function getImagePackerSupportedFormats(): string[]
```

获取支持编码的图片格式，图片格式以mime type表示。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-image-function getImagePackerSupportedFormats(): string[]--><!--Device-image-function getImagePackerSupportedFormats(): string[]-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Return value:**

| Type | Description |
| --- | --- |
| string[] | 支持编码的图片格式（mime type）列表。 |

## Examples

```TypeScript
async function GetImagePackerSupportedFormats() {
    let formats = image.getImagePackerSupportedFormats();
    console.info('formats:', formats);
}
```

