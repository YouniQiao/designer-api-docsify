# createPixelMapFromPixelsSync

## Modules to Import

```TypeScript
```

## createPixelMapFromPixelsSync

```TypeScript
function createPixelMapFromPixelsSync(pixels: ArrayBuffer, param: InitializationOptions): PixelMap
```

Creates a PixelMap from existing pixel data. The pixel data will be copied and converted to the specified pixel format to initialize the PixelMap. The following pixel formats are not supported for PixelMap creation: RGBA_1010102, YCBCR_P010, YCRCB_P010, ASTC_4x4.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-image-function createPixelMapFromPixelsSync(pixels: ArrayBuffer, param: InitializationOptions): PixelMap--><!--Device-image-function createPixelMapFromPixelsSync(pixels: ArrayBuffer, param: InitializationOptions): PixelMap-End-->

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
| [7600305](../errorcode-image.md#7600305-failed-to-create-the-pixelmap) |
| [7600207](../errorcode-image.md#7600207-unsupported-data-format) |
| [7600206](../errorcode-image.md#7600206-invalid-parameter) |
| [7600301](../errorcode-image.md#7600301-memory-allocation-failure) |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function createPixelMapFromPixelsSync() {
  const size: image.Size = {
    width: 6,
    height: 4
  };
  const pixels = new ArrayBuffer(size.width * size.height * 4); // 4 is the number of bytes per pixel for the RGBA pixel format.
  const pixelsArr = new Uint8Array(pixels);
  for (let i = 0; i < pixelsArr.length; i += 4) {
    // In RGBA_8888 format, the following array indexes correspond to the R, G, B, and A channels in sequence.
    pixelsArr[i] = 0xFF;
    pixelsArr[i + 1] = 0x00;
    pixelsArr[i + 2] = 0x00;
    pixelsArr[i + 3] = 0xFF;
  }
  const config: image.InitializationOptions = {
    size,
    srcPixelFormat: image.PixelMapFormat.RGBA_8888, // Pixel format of the source pixel data in the buffer.
    pixelFormat: image.PixelMapFormat.BGRA_8888, // Pixel format of the new PixelMap.
    editable: true
  };

  try {
    const pixelMap = image.createPixelMapFromPixelsSync(pixels, config);
    console.info('Succeeded in creating the PixelMap.');
  } catch (e) {
    const err = e as BusinessError;
    console.error(`Failed to create the PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```
