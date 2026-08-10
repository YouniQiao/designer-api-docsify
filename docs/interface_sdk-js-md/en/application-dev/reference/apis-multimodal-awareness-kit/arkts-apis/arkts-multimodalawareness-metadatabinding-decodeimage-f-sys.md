# decodeImage (System API)

## Modules to Import

```TypeScript
import { metadataBinding } from 'kits/@kit.MultimodalAwarenessKit';
```

## decodeImage

```TypeScript
function decodeImage(encodedImage: image.PixelMap): Promise<string>
```

Decodes the information carried in the image. This API uses a promise to return the result.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-metadataBinding-function decodeImage(encodedImage: image.PixelMap): Promise<string>--><!--Device-metadataBinding-function decodeImage(encodedImage: image.PixelMap): Promise<string>-End-->

**System capability:** SystemCapability.MultimodalAwareness.MetadataBinding

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| encodedImage | image.PixelMap | Yes | Image with metadata encoded. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise object, which is used to return the encoded metadata of the image. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 32100001 | Internal handling failed. |
| 202 | Permission check failed. A non-system application uses the system API. |
| 32100003 | Decode process fail. Possible causes: &lt;br&gt;1. Image is not an encoded Image. &lt;br&gt;2. Image destroyed, decoding failed. |

## Examples

```TypeScript
import { image } from '@kit.ImageKit';
import { metadataBinding } from '@kit.MultimodalAwarenessKit';
import { BusinessError } from '@kit.BasicServicesKit';

let encodeImage: image.PixelMap | undefined = undefined;
let captureMetadata: string = "";
metadataBinding.decodeImage(encodeImage).then((metadata: string) => {
  captureMetadata = metadata;
}).catch((error: BusinessError) => {
  console.error("decode image error" + error);
});
```

