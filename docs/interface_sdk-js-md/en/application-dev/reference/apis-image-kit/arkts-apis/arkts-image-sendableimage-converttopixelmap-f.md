# convertToPixelMap

## Modules to Import

```TypeScript
import { sendableImage } from 'kits/@kit.ImageKit';
```

## convertToPixelMap

```TypeScript
function convertToPixelMap(pixelmap: PixelMap): image.PixelMap
```

Creates a image PixelMap from sendable image PixelMap.

**Since:** 12

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pixelmap | [PixelMap](arkts-image-image-pixelmap-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| image.PixelMap |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [62980104](../errorcode-image.md#62980104-image-initialization-error) |
