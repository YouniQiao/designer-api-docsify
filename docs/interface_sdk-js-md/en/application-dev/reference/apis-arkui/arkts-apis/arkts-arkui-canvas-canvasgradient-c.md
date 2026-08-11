# CanvasGradient

Opaque objects that describe gradients, created by createLinearGradient() or createRadialGradient()

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class CanvasGradient--><!--Device-unnamed-export declare class CanvasGradient-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## addColorStop

```TypeScript
addColorStop(offset: double, color: string | ColorMetrics): void
```

Add a breakpoint defined by offset and color to the gradient

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CanvasGradient-addColorStop(offset: double, color: string | ColorMetrics): void--><!--Device-CanvasGradient-addColorStop(offset: double, color: string | ColorMetrics): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | double | Yes | Value between 0 and 1. |
| color | string \| ColorMetrics | Yes | Set the gradient color. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [103701](../errorcode-canvas.md#103701-parameter-error) | The color's ColorSpace is not the same as the last color's. |

