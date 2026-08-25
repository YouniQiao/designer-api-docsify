# createAuxiliaryPictureUsingAllocator

## Modules to Import

```TypeScript
import { image } from '@kit.ImageKit';
```

## createAuxiliaryPictureUsingAllocator

```TypeScript
function createAuxiliaryPictureUsingAllocator(auxiliaryPictureInfo: AuxiliaryPictureInfo,
    allocatorType?: AllocatorType, pixels?: ArrayBuffer): AuxiliaryPicture
```

Create an &lt;b&gt;AuxiliaryPicture&lt;/b&gt; object, the memory type used by the AuxiliaryPicture can be specified by allocatorType IMAGE_ALLOCATOR_TYPE. By default, the system selects the memory type based on the image type, image size, platform capability, etc. When processing the AuxiliaryPicture returned by this interface, please always consider the impact of stride. The created auxiliary picture is initialized with the input pixels.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| auxiliaryPictureInfo | [AuxiliaryPictureInfo](arkts-image-image-auxiliarypictureinfo-i.md) | Yes |
| allocatorType | [AllocatorType](arkts-image-image-allocatortype-e.md) | No |
| [pixels](arkts-image-image-positionarea-i.md) | ArrayBuffer | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AuxiliaryPicture](arkts-image-image-auxiliarypicture-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [7600205](../errorcode-image.md#7600205-unsupported-format) |
| [7600206](../errorcode-image.md#7600206-invalid-parameter) |
| [7600301](../errorcode-image.md#7600301-memory-allocation-failure) |
