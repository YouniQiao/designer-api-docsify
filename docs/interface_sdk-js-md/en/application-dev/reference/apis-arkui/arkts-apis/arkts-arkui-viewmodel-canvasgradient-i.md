# CanvasGradient

You can create a gradient object on the canvas by calling CanvasRenderingContext2D.createLinearGradient().@interface CanvasGradient

**Since:** 4

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## addColorStop

```TypeScript
addColorStop(offset: number, color: string): void
```

Adds a color stop for the CanvasGradient object based on the specified offset and gradient color.

**Since:** 4

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| offset | number | Yes |
| color | string | Yes |
