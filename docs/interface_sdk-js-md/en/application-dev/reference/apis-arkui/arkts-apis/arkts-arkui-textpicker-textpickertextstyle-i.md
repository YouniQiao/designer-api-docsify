# TextPickerTextStyle

Defines the text style options.@extends PickerTextStyle @interface TextPickerTextStyle

**Inheritance/Implementation:** TextPickerTextStyle extends PickerTextStyle

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maxFontSize

```TypeScript
maxFontSize?: double | string | Resource
```

Maximum font size.

**Type:** double \| string \| [Resource](arkts-arkui-resource-t.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## minFontSize

```TypeScript
minFontSize?: double | string | Resource
```

Minimum font size, used in conjunction with maxFontSize. When minFontSize and maxFontSize are set, the size setting in font is ineffective. The default maximum number of lines is 1, and the default height adaptation mode is MIN_FONT_SIZE_FIRST.

**Type:** double \| string \| [Resource](arkts-arkui-resource-t.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## overflow

```TypeScript
overflow?: TextOverflow
```

Display mode when the text is too long.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: Ineffective when set to MARQUEE. </p>

**Type:** [TextOverflow](arkts-arkui-textoverflow-e.md)

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
