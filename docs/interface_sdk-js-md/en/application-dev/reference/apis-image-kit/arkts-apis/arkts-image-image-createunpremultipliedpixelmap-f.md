# createUnpremultipliedPixelMap

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## createUnpremultipliedPixelMap

```TypeScript
function createUnpremultipliedPixelMap(src: PixelMap, dst: PixelMap, callback: AsyncCallback<void>): void
```

Transforms pixelmap from premultiplied alpha format to unpremultiplied alpha format.

**Since:** 12

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | [PixelMap](arkts-image-image-pixelmap-i.md) | Yes |
| [dst](../../apis-arkui/arkts-apis/arkts-arkui-matrix4-polytopolyoptions-i.md) | [PixelMap](arkts-image-image-pixelmap-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [62980103](../errorcode-image.md#62980103-unsupported-image-type) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [62980246](../errorcode-image.md#62980246-failure-in-reading-the-pixelmap) |
| [62980248](../errorcode-image.md#62980248-no-modification-to-the-pixelmap) |


## createUnpremultipliedPixelMap

```TypeScript
function createUnpremultipliedPixelMap(src: PixelMap, dst: PixelMap): Promise<void>
```

Transforms pixelmap from premultiplied alpha format to unpremultiplied alpha format.

**Since:** 12

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | [PixelMap](arkts-image-image-pixelmap-i.md) | Yes |
| [dst](../../apis-arkui/arkts-apis/arkts-arkui-matrix4-polytopolyoptions-i.md) | [PixelMap](arkts-image-image-pixelmap-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [62980103](../errorcode-image.md#62980103-unsupported-image-type) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [62980246](../errorcode-image.md#62980246-failure-in-reading-the-pixelmap) |
| [62980248](../errorcode-image.md#62980248-no-modification-to-the-pixelmap) |
