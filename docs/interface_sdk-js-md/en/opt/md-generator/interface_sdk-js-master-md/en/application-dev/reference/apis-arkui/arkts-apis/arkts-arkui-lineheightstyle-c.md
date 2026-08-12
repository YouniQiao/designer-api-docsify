# LineHeightStyle

Describes the text line height style.

**Since:** 12

<!--Device-unnamed-declare class LineHeightStyle--><!--Device-unnamed-declare class LineHeightStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(lineHeight: LengthMetrics)
```

A constructor used to create a text line height style.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LineHeightStyle-constructor(lineHeight: LengthMetrics)--><!--Device-LineHeightStyle-constructor(lineHeight: LengthMetrics)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [lineHeight](#lineheight) | [LengthMetrics](arkts-arkui-lengthmetrics-t.md) | Yes |

## constructor

```TypeScript
constructor(lineHeight: LengthMetrics, lineHeightMultiple?: number)
```

A constructor used to create a text line height and multiple.

> **NOTE：**
> 
> - When **lineHeightMultiple** is set together with **lineHeight** or [LineSpacingStyle](arkts-arkui-linespacingstyle-c.md#LineSpacingStyle),
> only **lineHeightMultiple** takes effect. The line height is the product of the highest font height in the line
> and the multiplier.
> 
> - When **lineHeightMultiple** is less than 0 or **undefined**, it does not take effect. Use **lineHeight** and
> [LineSpacingStyle](arkts-arkui-linespacingstyle-c.md#LineSpacingStyle) to set the line height and line spacing.
> 
> - When **lineHeightMultiple** is set to 0, it is equivalent to setting it to 1.

**Since**: 26.0.0

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-LineHeightStyle-constructor(lineHeight: LengthMetrics, lineHeightMultiple?: number)--><!--Device-LineHeightStyle-constructor(lineHeight: LengthMetrics, lineHeightMultiple?: number)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [lineHeight](#lineheight) | [LengthMetrics](arkts-arkui-lengthmetrics-t.md) | Yes |
| [lineHeightMultiple](#lineheightmultiple) | number | No |

## lineHeight

```TypeScript
readonly lineHeight: number
```

Text line height of the styled string.

Unit: [vp](common)

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LineHeightStyle-readonly lineHeight: number--><!--Device-LineHeightStyle-readonly lineHeight: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## lineHeightMultiple

```TypeScript
readonly lineHeightMultiple?: number
```

Multiplier for the text line height. The effective line height is the product of the highest font height in the line and the multiplier.

**Since**: 26.0.0

**Type:** number

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-LineHeightStyle-readonly lineHeightMultiple?: number--><!--Device-LineHeightStyle-readonly lineHeightMultiple?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
