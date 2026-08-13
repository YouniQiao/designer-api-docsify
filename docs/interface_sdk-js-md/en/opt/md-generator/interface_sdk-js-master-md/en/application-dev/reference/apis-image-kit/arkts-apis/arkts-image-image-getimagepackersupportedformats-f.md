# getImagePackerSupportedFormats

## Modules to Import

```TypeScript
import { image } from '@kit.ImageKit';
```

## getImagePackerSupportedFormats

```TypeScript
function getImagePackerSupportedFormats(): string[]
```

Obtains the supported encoding formats, represented by MIME types.

**Since:** 23

**Deprecated since:** -1

<!--Device-image-function getImagePackerSupportedFormats(): string[]--><!--Device-image-function getImagePackerSupportedFormats(): string[]-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string[] |

## Examples

```TypeScript
async function GetImagePackerSupportedFormats() {
    let formats = image.getImagePackerSupportedFormats();
    console.info('formats:', formats);
}
```
