# OffscreenCanvasRenderingContext2D

Draw context object for the OffscreenCanvas component.

**Inheritance/Implementation:** OffscreenCanvasRenderingContext2D extends [CanvasRenderer](canvas-canvasrenderer-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class OffscreenCanvasRenderingContext2D extends CanvasRenderer--><!--Device-unnamed-export declare class OffscreenCanvasRenderingContext2D extends CanvasRenderer-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(width: double, height: double, settings?: RenderingContextSettings, unit?: LengthMetricsUnit)
```

Constructor of the canvas drawing context object, which is used to create a drawing context object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OffscreenCanvasRenderingContext2D-constructor(width: double, height: double, settings?: RenderingContextSettings, unit?: LengthMetricsUnit)--><!--Device-OffscreenCanvasRenderingContext2D-constructor(width: double, height: double, settings?: RenderingContextSettings, unit?: LengthMetricsUnit)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| width | double | Yes | the width of the OffscreenCanvas |
| height | double | Yes | the height of the OffscreenCanvas |
| settings | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Drawing attribute. For details, see \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. |
| unit | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | the unit mode |

## toDataURL

```TypeScript
toDataURL(type?: string, quality?: double): string
```

Generate a character string in the data url format.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OffscreenCanvasRenderingContext2D-toDataURL(type?: string, quality?: double): string--><!--Device-OffscreenCanvasRenderingContext2D-toDataURL(type?: string, quality?: double): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | string | No | Image format. The default value is image/png. |
| quality | double | No | If the image format is image/jpeg or image/webp, you can select the image quality from 0 to 1. If the value is out of the range, the default value 0.92 is used. |

**Return value:**

| Type | Description |
| --- | --- |
| string |  |

## transferToImageBitmap

```TypeScript
transferToImageBitmap(): ImageBitmap | undefined
```

transfer the content to ImageBitmap

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OffscreenCanvasRenderingContext2D-transferToImageBitmap(): ImageBitmap | undefined--><!--Device-OffscreenCanvasRenderingContext2D-transferToImageBitmap(): ImageBitmap | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ |  |

