# createPixelMapFromParcel

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## createPixelMapFromParcel

```TypeScript
function createPixelMapFromParcel(sequence: rpc.MessageSequence): PixelMap
```

Creates a PixelMap object based on MessageSequence parameter.

**Since:** 11

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sequence | rpc.MessageSequence | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PixelMap](arkts-image-image-pixelmap-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [62980096](../errorcode-image.md#62980096-operation-failed) |
| [62980097](../errorcode-image.md#62980097-pixelmap-serialization-failed) |
| [62980115](../errorcode-image.md#62980115-invalid-image-parameter) |
| [62980105](../errorcode-image.md#62980105-failure-in-obtaining-image-data) |
| [62980177](../errorcode-image.md#62980177-abnormal-api-environment) |
| [62980178](../errorcode-image.md#62980178-failure-in-creating-a-pixelmap) |
| [62980179](../errorcode-image.md#62980179-abnormal-buffer-size) |
| [62980180](../errorcode-image.md#62980180-failure-in-mapping-the-file-descriptor) |
| [62980246](../errorcode-image.md#62980246-failure-in-reading-the-pixelmap) |
