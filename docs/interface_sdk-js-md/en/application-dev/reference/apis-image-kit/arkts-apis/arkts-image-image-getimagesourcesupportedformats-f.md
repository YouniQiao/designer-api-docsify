# getImageSourceSupportedFormats

## Modules to Import

```TypeScript
import { image } from 'image';
```

## getImageSourceSupportedFormats

```TypeScript
function getImageSourceSupportedFormats(): string[]
```

Obtains the supported decoding formats, represented by MIME types.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-image-function getImageSourceSupportedFormats(): string[]--><!--Device-image-function getImageSourceSupportedFormats(): string[]-End-->

**System capability:** SystemCapability.Multimedia.Image.ImageSource

**Return value:**

| Type | Description |
| --- | --- |
| string[] | List of supported decoding formats (MIME types). |

## Examples

```TypeScript
async function GetImageSourceSupportedFormats() {
    let formats = image.getImageSourceSupportedFormats();
    console.info('formats:', formats);
}
```

