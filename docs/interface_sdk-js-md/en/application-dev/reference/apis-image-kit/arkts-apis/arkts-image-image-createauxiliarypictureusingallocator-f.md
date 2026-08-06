# createAuxiliaryPictureUsingAllocator

## createAuxiliaryPictureUsingAllocator

```TypeScript
function createAuxiliaryPictureUsingAllocator(auxiliaryPictureInfo: AuxiliaryPictureInfo,
    allocatorType?: AllocatorType, pixels?: ArrayBuffer): AuxiliaryPicture
```

Create an \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_AuxiliaryPicture\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_ object, the memory type used by the AuxiliaryPicture can be specified by allocatorType \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_. By default, the system selects the memory type based on the image type,image size, platform capability, etc. When processing the AuxiliaryPicture returned by this interface, please always consider the impact of stride. The created auxiliary picture is initialized with the input pixels.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-image-function createAuxiliaryPictureUsingAllocator(auxiliaryPictureInfo: AuxiliaryPictureInfo,    allocatorType?: AllocatorType, pixels?: ArrayBuffer): AuxiliaryPicture--><!--Device-image-function createAuxiliaryPictureUsingAllocator(auxiliaryPictureInfo: AuxiliaryPictureInfo,    allocatorType?: AllocatorType, pixels?: ArrayBuffer): AuxiliaryPicture-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| auxiliaryPictureInfo | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The basic information of the auxiliary picture. |
| allocatorType | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Memory type. |
| pixels | ArrayBuffer | No | Pixel data used to initialize the auxiliary picture. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | The AuxiliaryPicture object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600205](../errorcode-image.md#7600205-unsupported-format) | Unsupported allocator type, e.g., use shared memory to create a gainmap as only DMA supported hdr metadata. |
| [7600206](../errorcode-image.md#7600206-invalid-parameter) | Invalid parameter, size.height or size.width is less than or equal to 0. |
| [7600301](../errorcode-image.md#7600301-memory-allocation-failure) | Alloc memory failed. |

