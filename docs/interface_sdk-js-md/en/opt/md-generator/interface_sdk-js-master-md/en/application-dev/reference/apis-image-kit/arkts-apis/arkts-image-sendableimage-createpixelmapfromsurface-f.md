# createPixelMapFromSurface

## Modules to Import

```TypeScript
import { sendableImage } from '@kit.ImageKit';
```

## createPixelMapFromSurface

```TypeScript
function createPixelMapFromSurface(surfaceId: string, region: image.Region): Promise<PixelMap>
```

Creates a PixelMap object from surface id.

**Since:** 12

**Deprecated since:** -1

<!--Device-sendableImage-function createPixelMapFromSurface(surfaceId: string, region: image.Region): Promise<PixelMap>--><!--Device-sendableImage-function createPixelMapFromSurface(surfaceId: string, region: image.Region): Promise<PixelMap>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| surfaceId | string | Yes |
| region | image.Region | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;PixelMap & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [62980115](../errorcode-image.md#62980115-invalid-image-parameter) |
| [62980178](../errorcode-image.md#62980178-failure-in-creating-a-pixelmap) |
| [62980105](../errorcode-image.md#62980105-failure-in-obtaining-image-data) |

## Examples

```TypeScript
import { sendableImage } from '@kit.ImageKit';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function CreatePixelMapFromSurface(surfaceId: string) {
  let region: image.Region = { x: 0, y: 0, size: { height: 100, width: 100 } };
  sendableImage.createPixelMapFromSurface(surfaceId, region).then(() => {
    console.info('Succeeded in creating pixelmap from Surface');
  }).catch((error: BusinessError) => {
    console.error(`Failed to create pixelmap. code is ${error.code}, message is ${error.message}`);
  });
}
```
