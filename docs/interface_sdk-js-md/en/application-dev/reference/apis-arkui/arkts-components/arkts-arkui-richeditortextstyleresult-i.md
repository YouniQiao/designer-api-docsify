# RichEditorTextStyleResult

Provides the text span style information returned by the backend.

While **fontWeight** in **RichEditorTextStyle** sets the font weight, **fontWeight** in **RichEditorTextStyleResult** returns the set font weight after conversion to digits.

Conversion relationship between fontWeight in RichEditorSymbolSpanStyle and RichEditorSymbolSpanStyleResult, the conversion relationship is the same as that of fontWeight in RichEditorTextStyle and RichEditorTextStyleResult.

**Since:** 10

<!--Device-unnamed-declare interface RichEditorTextStyleResult--><!--Device-unnamed-declare interface RichEditorTextStyleResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## decoration

```TypeScript
decoration: DecorationStyleResult
```

Text decorative line.

**Type:** DecorationStyleResult

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RichEditorTextStyleResult-decoration: DecorationStyleResult--><!--Device-RichEditorTextStyleResult-decoration: DecorationStyleResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontColor

```TypeScript
fontColor: ResourceColor
```

Font color.

**Type:** ResourceColor

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RichEditorTextStyleResult-fontColor: ResourceColor--><!--Device-RichEditorTextStyleResult-fontColor: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontFamily

```TypeScript
fontFamily: string
```

Font family.

**Type:** string

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RichEditorTextStyleResult-fontFamily: string--><!--Device-RichEditorTextStyleResult-fontFamily: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontFeature

```TypeScript
fontFeature?: string
```

Font feature.

**Type:** string

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorTextStyleResult-fontFeature?: string--><!--Device-RichEditorTextStyleResult-fontFeature?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontSize

```TypeScript
fontSize: number
```

Font size. The default unit is fp.

**Type:** number

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RichEditorTextStyleResult-fontSize: number--><!--Device-RichEditorTextStyleResult-fontSize: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontStyle

```TypeScript
fontStyle: FontStyle
```

Font style.

**Type:** FontStyle

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RichEditorTextStyleResult-fontStyle: FontStyle--><!--Device-RichEditorTextStyleResult-fontStyle: FontStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontWeight

```TypeScript
fontWeight: number
```

Font weight.

**Type:** number

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RichEditorTextStyleResult-fontWeight: number--><!--Device-RichEditorTextStyleResult-fontWeight: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## halfLeading

```TypeScript
halfLeading?: boolean
```

Whether half leading is enabled.

Whether half leading is enabled. Half leading is the leading split in half and applied equally to the top and bottom edges. The value **true** means that half leading is enabled, and **false** means the opposite.

Default value: **false**

**Type:** boolean

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-RichEditorTextStyleResult-halfLeading?: boolean--><!--Device-RichEditorTextStyleResult-halfLeading?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## letterSpacing

```TypeScript
letterSpacing?: number
```

Letter spacing. The default unit is fp.

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorTextStyleResult-letterSpacing?: number--><!--Device-RichEditorTextStyleResult-letterSpacing?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## lineHeight

```TypeScript
lineHeight?: number
```

Line height. The default unit is fp.

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorTextStyleResult-lineHeight?: number--><!--Device-RichEditorTextStyleResult-lineHeight?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## strokeColor

```TypeScript
strokeColor?: ResourceColor
```

Text stroke color.

**Type:** ResourceColor

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-RichEditorTextStyleResult-strokeColor?: ResourceColor--><!--Device-RichEditorTextStyleResult-strokeColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## strokeJoinStyle

```TypeScript
strokeJoinStyle?: StrokeJoinStyle
```

Get the stroke join style of the text.

**Type:** StrokeJoinStyle

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-RichEditorTextStyleResult-strokeJoinStyle?: StrokeJoinStyle--><!--Device-RichEditorTextStyleResult-strokeJoinStyle?: StrokeJoinStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## strokeWidth

```TypeScript
strokeWidth?: number
```

Text stroke width.

The unit is [vp](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md).

**Type:** number

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-RichEditorTextStyleResult-strokeWidth?: number--><!--Device-RichEditorTextStyleResult-strokeWidth?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textBackgroundStyle

```TypeScript
textBackgroundStyle?: TextBackgroundStyle
```

Text background style.

Default value:

{

color: Color.Transparent,

radius: 0

}

**Type:** TextBackgroundStyle

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-RichEditorTextStyleResult-textBackgroundStyle?: TextBackgroundStyle--><!--Device-RichEditorTextStyleResult-textBackgroundStyle?: TextBackgroundStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textShadow

```TypeScript
textShadow?: Array<ShadowOptions>
```

Text shadow.

**NOTE**

Only the shadow blur radius, shadow color, and shadow offset can be queried.

**Type:** Array&lt;ShadowOptions&gt;

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorTextStyleResult-textShadow?: Array<ShadowOptions>--><!--Device-RichEditorTextStyleResult-textShadow?: Array<ShadowOptions>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

