# createPixelMapFromPixels

## createPixelMapFromPixels

```TypeScript
function createPixelMapFromPixels(pixels: ArrayBuffer, param: InitializationOptions): Promise<PixelMap>
```

Creates a PixelMap from existing pixel data. The pixel data will be copied and converted to the specified pixel format to initialize the PixelMap.

The following pixel formats are not supported for PixelMap creation:RGBA\_1010102, YCBCR\_P010, YCRCB\_P010, ASTC\_4x4.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

<!--Device-image-function createPixelMapFromPixels(pixels: ArrayBuffer, param: InitializationOptions): Promise<PixelMap>--><!--Device-image-function createPixelMapFromPixels(pixels: ArrayBuffer, param: InitializationOptions): Promise<PixelMap>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pixels | ArrayBuffer | Yes | The pixel data buffer used to initialize the PixelMap. The format of the pixel data can be specified by InitializationOptions.srcPixelFormat. The size of the buffer should be: image width image height bytes per pixel. |
| param | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Initialization options for the PixelMap. If InitializationOptions.pixelFormat is set to ASTC\_\_\_ESCAPED\_UNDERSCORE\_\_\_4x4, it will be reset to the default value RGBA\_\_\_ESCAPED\_UNDERSCORE\_\_\_8888. If InitializationOptions.srcPixelFormat is set to ASTC\_\_\_ESCAPED\_UNDERSCORE\_\_\_4x4, it will be reset to the default value BGRA\_\_\_ESCAPED\_UNDERSCORE\_\_\_8888. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PixelMap&gt; | A Promise of the new PixelMap created. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [7600206](../errorcode-image.md#7600206-invalid-parameter) | Invalid parameter. Possible cause: Size of the pixel data buffer does not match InitializationOptions.size. |
| [7600207](../errorcode-image.md#7600207-unsupported-data-format) | Unsupported pixel format. |
| [7600301](../errorcode-image.md#7600301-memory-allocation-failure) | Failed to allocate memory. Possible causes: 1. The resulting PixelMap size is too large. 2. The system is out of memory. |
| [7600305](../errorcode-image.md#7600305-failed-to-create-the-pixelmap) | Failed to create the PixelMap. Possible causes: 1. Failed to perform pixel format conversion. 2. Internal data is corrupted. Please check the logs for detailed information. |

