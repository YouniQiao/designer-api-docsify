# encodeImage (System API)

## Modules to Import

```TypeScript
```

## encodeImage

```TypeScript
function encodeImage(srcImage: image.PixelMap, metadata: string): Promise<image.PixelMap>
```

Encodes metadata into an image. This API uses a promise to return the result.

**Since:** 23

<!--Device-metadataBinding-function encodeImage(srcImage: image.PixelMap, metadata: string): Promise<image.PixelMap>--><!--Device-metadataBinding-function encodeImage(srcImage: image.PixelMap, metadata: string): Promise<image.PixelMap>-End-->

**System capability:** SystemCapability.MultimodalAwareness.MetadataBinding

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| srcImage | image.PixelMap | Yes |
| metadata | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;image.PixelMap & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [32100001](../../apis-multimodalawareness-kit/errorcode-metadataBinding.md#32100001-file-creation-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [32100002](../../apis-multimodalawareness-kit/errorcode-metadataBinding.md#32100002-encoding-failed) |

**Examples**

```TypeScript
import { image } from '@kit.ImageKit';
import { metadataBinding } from '@kit.MultimodalAwarenessKit';
import { BusinessError } from '@kit.BasicServicesKit';

let captureImage: image.PixelMap | undefined = undefined;
let metadata: string = "";
let srcImage: image.PixelMap | undefined = undefined;
metadataBinding.encodeImage(srcImage, metadata).then((pixelMap: image.PixelMap) => {
  captureImage = pixelMap;
}).catch((error: BusinessError) => {
  console.error("encode image error" + error);
});
```
