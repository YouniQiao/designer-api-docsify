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

**System capability:** SystemCapability.MultimodalAwareness.MetadataBinding

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| encodedImage | image.PixelMap | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [32100001](../errorcode-metadataBinding.md#32100001-file-creation-failed) |
| [32100003](../errorcode-metadataBinding.md#32100003-decoding-failed) |
