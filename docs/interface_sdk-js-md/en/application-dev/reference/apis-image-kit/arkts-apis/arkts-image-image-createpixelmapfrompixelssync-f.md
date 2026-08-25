# createPixelMapFromPixelsSync

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## createPixelMapFromPixelsSync

```TypeScript
function createPixelMapFromPixelsSync(pixels: ArrayBuffer, param: InitializationOptions): PixelMap
```

Creates a PixelMap from existing pixel data. The pixel data will be copied and converted to the specified pixel format to initialize the PixelMap.The following pixel formats are not supported for PixelMap creation: RGBA_1010102, YCBCR_P010, YCRCB_P010, ASTC_4x4.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [pixels](arkts-image-image-positionarea-i.md) | ArrayBuffer | Yes |
| param | [InitializationOptions](arkts-image-image-initializationoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PixelMap](arkts-image-image-pixelmap-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [7600206](../errorcode-image.md#7600206-invalid-parameter) |
| [7600207](../errorcode-image.md#7600207-unsupported-data-format) |
| [7600301](../errorcode-image.md#7600301-memory-allocation-failure) |
| [7600305](../errorcode-image.md#7600305-failed-to-create-the-pixelmap) |
