# createEmptyPixelMap

## createEmptyPixelMap

```TypeScript
function createEmptyPixelMap(param: InitializationOptions): PixelMap
```

Creates an empty PixelMap. The following pixel format is not supported for PixelMap creation: ASTC\_4x4.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-image-function createEmptyPixelMap(param: InitializationOptions): PixelMap--><!--Device-image-function createEmptyPixelMap(param: InitializationOptions): PixelMap-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| param | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Initialization options for the PixelMap.If InitializationOptions.pixelFormat is set to ASTC\_\_\_ESCAPED\_UNDERSCORE\_\_\_4x4, it will be reset to the default value RGBA\_\_\_ESCAPED\_UNDERSCORE\_\_\_8888. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | The new PixelMap created. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600206](../errorcode-image.md#7600206-invalid-parameter) | Invalid parameter. |
| [7600301](../errorcode-image.md#7600301-memory-allocation-failure) | Failed to allocate memory.Possible causes: 1. The resulting PixelMap size is too large. 2. The system is out of memory. |
| [7600305](../errorcode-image.md#7600305-failed-to-create-the-pixelmap) | Failed to create the PixelMap.Possible cause: Internal data is corrupted. Please check the logs for detailed information. |

