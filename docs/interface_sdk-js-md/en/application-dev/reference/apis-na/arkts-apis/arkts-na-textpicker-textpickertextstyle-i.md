# TextPickerTextStyle

Defines the text style options.

**Inheritance/Implementation:** TextPickerTextStyle extends PickerTextStyle

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface TextPickerTextStyle--><!--Device-unnamed-export declare interface TextPickerTextStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maxFontSize

```TypeScript
maxFontSize?: double | string | Resource
```

Maximum font size.

**Type:** double \| string \| [Resource](../../apis-arkui/arkts-apis/arkts-arkui-resource-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerTextStyle-maxFontSize?: double | string | Resource--><!--Device-TextPickerTextStyle-maxFontSize?: double | string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## minFontSize

```TypeScript
minFontSize?: double | string | Resource
```

Minimum font size, used in conjunction with maxFontSize. When minFontSize and maxFontSize are set, the size setting in font is ineffective. The default maximum number of lines is 1, and the default height adaptation mode is MIN_FONT_SIZE_FIRST.

**Type:** double \| string \| [Resource](../../apis-arkui/arkts-apis/arkts-arkui-resource-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerTextStyle-minFontSize?: double | string | Resource--><!--Device-TextPickerTextStyle-minFontSize?: double | string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## overflow

```TypeScript
overflow?: TextOverflow
```

Display mode when the text is too long. &lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;: Ineffective when set to MARQUEE. &lt;/p&gt;

**Type:** [TextOverflow](../../apis-arkui/arkts-apis/arkts-arkui-textoverflow-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerTextStyle-overflow?: TextOverflow--><!--Device-TextPickerTextStyle-overflow?: TextOverflow-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

