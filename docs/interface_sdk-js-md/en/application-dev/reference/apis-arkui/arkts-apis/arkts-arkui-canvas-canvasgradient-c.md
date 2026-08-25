# CanvasGradient

Opaque objects that describe gradients, created by createLinearGradient() or createRadialGradient()

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## addColorStop

```TypeScript
addColorStop(offset: double, color: string | ColorMetrics): void
```

Add a breakpoint defined by offset and color to the gradient

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | double | Yes |
| color | string \| [ColorMetrics](arkts-arkui-colormetrics-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [103701](../errorcode-canvas.md#103701-parameter-error) |
