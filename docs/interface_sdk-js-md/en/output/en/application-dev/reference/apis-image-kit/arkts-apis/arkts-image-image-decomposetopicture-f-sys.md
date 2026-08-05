# decomposeToPicture (System API)

## decomposeToPicture

```TypeScript
function decomposeToPicture(hdrPixelMap : PixelMap, options?: HdrDecomposeOptions): Promise<Picture | undefined>
```

Decomposes an HDR Pixelmap object to a Picture object which contains an SDR PixelMap and a gainmap. This API uses a promise to return the result.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-image-function decomposeToPicture(hdrPixelMap : PixelMap, options?: HdrDecomposeOptions): Promise<Picture | undefined>--><!--Device-image-function decomposeToPicture(hdrPixelMap : PixelMap, options?: HdrDecomposeOptions): Promise<Picture | undefined>-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| hdrPixelMap | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | An HDR PixelMap, whose PixelMapFormat should be RGBA\_\_\_ESCAPED\_UNDERSCORE\_\_\_F16\RGBA\_\_\_ESCAPED\_UNDERSCORE\_\_\_1010102\YCBCR\_\_\_ESCAPED\_UNDERSCORE\_\_\_P010\YCRCB\_\_\_ESCAPED\_UNDERSCORE\_\_\_P010. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | The HDR decomposition configurations. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Picture \| undefined&gt; | Promise used to return the Picture object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications are not allowed to use system APIs. |
| [7600201](../errorcode-image.md#7600201-unsupported-operation) | Unsupported operation. hdrPixelMap's PixelMapFormat is not RGBA\_\_\_ESCAPED\_UNDERSCORE\_\_\_F16\RGBA\_\_\_ESCAPED\_UNDERSCORE\_\_\_1010102\YCBCR\_\_\_ESCAPED\_UNDERSCORE\_\_\_P010\YCRCB\_\_\_ESCAPED\_UNDERSCORE\_\_\_P010. |
| [7600206](../errorcode-image.md#7600206-invalid-parameter) | Invalid parameter. Possible cause: hdrPixelMap is empty. |
| [7600208](../errorcode-image.md#7600208-failed-to-decompose-an-hdr-image) | HDR image decomposition failed. Possible causes: 1. Decomposition processing is not supported. 2. Processing error occurs. |
| [7600301](../errorcode-image.md#7600301-memory-allocation-failure) | Alloc memory failed. |

