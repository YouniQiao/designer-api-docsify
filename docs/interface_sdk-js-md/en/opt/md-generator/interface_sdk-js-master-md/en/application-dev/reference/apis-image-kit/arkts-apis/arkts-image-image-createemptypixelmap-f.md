# createEmptyPixelMap

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## createEmptyPixelMap

```TypeScript
function createEmptyPixelMap(param: InitializationOptions): PixelMap
```

Creates an empty PixelMap.

The following pixel format is not supported for PixelMap creation: ASTC_4x4.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-image-function createEmptyPixelMap(param: InitializationOptions): PixelMap--><!--Device-image-function createEmptyPixelMap(param: InitializationOptions): PixelMap-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| param | [InitializationOptions](arkts-image-image-initializationoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PixelMap](arkts-image-image-pixelmap-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [7600305](../errorcode-image.md#7600305-failed-to-create-the-pixelmap) |
| [7600206](../errorcode-image.md#7600206-invalid-parameter) |
| [7600301](../errorcode-image.md#7600301-memory-allocation-failure) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function createEmptyPixelMap() {
  const config: image.InitializationOptions = {
    size: { width: 6, height: 4 },
    pixelFormat: image.PixelMapFormat.RGBA_1010102, // Pixel format of the newly created PixelMap.
    editable: true
  };

  try {
    const pixelMap = image.createEmptyPixelMap(config);
    console.info('Succeeded in creating the empty PixelMap.');
  } catch (e) {
    const err = e as BusinessError;
    console.error(`Failed to create the empty PixelMap. Code: ${err.code}, message: ${err.message}`);
  }
}
```
