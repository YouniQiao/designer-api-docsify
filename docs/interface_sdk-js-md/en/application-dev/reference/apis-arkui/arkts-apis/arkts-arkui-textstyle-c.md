# TextStyle

```TypeScript
declare class TextStyle
```

Describes the text style.

**Since:** 12

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(value?: TextStyleInterface)
```

A constructor used to create a text style.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [TextStyleInterface](arkts-arkui-textstyleinterface-i.md) | No | Font style setting item.<br>Default value: when not passed, inherits the default values of the **TextStyleInterface** properties. |

## fontColor

```TypeScript
readonly fontColor?: ResourceColor
```

Text color of the styled string.

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontConfigs

```TypeScript
readonly fontConfigs?: FontConfigs
```

Font configuration of the styled string. indicating that **fontConfigs** is not set. Default value: **undefined**.

**Type:** [FontConfigs](arkts-arkui-fontconfigs-i.md)

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontFamily

```TypeScript
readonly fontFamily?: string
```

Text font of the styled string.

Default value: **undefined**.

**Type:** string

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontSize

```TypeScript
readonly fontSize?: number
```

Text font size of the styled string.

Unit: [vp](../../../reference/apis-arkui/arkui-ts/ts-pixel-units.md#basic-pixel-units)

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontStyle

```TypeScript
readonly fontStyle?: FontStyle
```

Text font style of the styled string.

**Type:** [FontStyle](arkts-arkui-fontstyle-e.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontVariations

```TypeScript
readonly fontVariations?: Array<FontVariation>
```

Attribute array of the variable font. indicating that the variable font attributes are not set. Default value: **undefined**.

**Type:** Array&lt;[FontVariation](arkts-arkui-fontvariation-t.md)&gt;

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontWeight

```TypeScript
readonly fontWeight?: number
```

Text font weight of the styled string.

Default value: **400**

**NOTE:** 

The return value is of the string type. For details about the relationship between the return value and the set value, see the table below.

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## strokeColor

```TypeScript
readonly strokeColor?: ResourceColor
```

Text stroke color of the styled string.

Default value: the font color.

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## strokeJoinStyle

```TypeScript
readonly strokeJoinStyle?: StrokeJoinStyle
```

Text stroke join style of the styled string. For details about the enum values, see **StrokeJoinStyle**.

Default value: **StrokeJoinStyle.MITER_JOIN**, indicating a miter join with a sharp corner.

**Type:** [StrokeJoinStyle](arkts-arkui-strokejoinstyle-e.md)

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## strokeWidth

```TypeScript
readonly strokeWidth?: number
```

Text stroke width of the styled string.

Default value: **0**, in [vp](../../../reference/apis-arkui/arkui-ts/ts-pixel-units.md#basic-pixel-units).

**Type:** number

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## superscript

```TypeScript
readonly superscript?: SuperscriptStyle
```

Superscript and subscript of the styled string.

Default value: **SuperscriptStyle.NORMAL**.

**Type:** [SuperscriptStyle](arkts-arkui-superscriptstyle-e.md)

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
