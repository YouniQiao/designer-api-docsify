# convertFromPixelMap

## Modules to Import

```TypeScript
import { sendableImage } from 'kits/@kit.ImageKit';
```

## convertFromPixelMap

```TypeScript
function convertFromPixelMap(pixelmap: image.PixelMap): PixelMap
```

Creates a sendable image PixelMap from image PixelMap.

**Since:** 12

<!--Device-sendableImage-function convertFromPixelMap(pixelmap: image.PixelMap): PixelMap--><!--Device-sendableImage-function convertFromPixelMap(pixelmap: image.PixelMap): PixelMap-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pixelmap | image.PixelMap | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PixelMap](arkts-image-image-pixelmap-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [62980104](../errorcode-image.md#62980104-image-initialization-error) |

## Examples

```TypeScript
import { sendableImage } from '@kit.ImageKit';
import { image } from '@kit.ImageKit';

async function ConvertFromPixelMap() {
  const color: ArrayBuffer = new ArrayBuffer(96); // 96 is the size of the pixel buffer to create. The value is calculated as follows: height * width *4.
  let opts: image.InitializationOptions = { editable: true, pixelFormat: 3, size: { height: 4, width: 6 } }
  let pixelMap : image.PixelMap = image.createPixelMapSync(color, opts);
  let sendablePixelMap : sendableImage.PixelMap = sendableImage.convertFromPixelMap(pixelMap);
  return sendablePixelMap;
}
```
