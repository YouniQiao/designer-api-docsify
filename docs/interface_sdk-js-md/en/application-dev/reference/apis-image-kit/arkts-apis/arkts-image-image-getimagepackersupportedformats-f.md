# getImagePackerSupportedFormats

## Modules to Import

```TypeScript
import { image } from 'image';
```

## getImagePackerSupportedFormats

```TypeScript
function getImagePackerSupportedFormats(): string[]
```

Obtains the supported encoding formats, represented by MIME types.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-image-function getImagePackerSupportedFormats(): string[]--><!--Device-image-function getImagePackerSupportedFormats(): string[]-End-->

**System capability:** SystemCapability.Multimedia.Image.ImagePacker

**Return value:**

| Type | Description |
| --- | --- |
| string[] | List of supported encoding formats (MIME types). |

## Examples

```TypeScript
async function GetImagePackerSupportedFormats() {
    let formats = image.getImagePackerSupportedFormats();
    console.info('formats:', formats);
}
```

