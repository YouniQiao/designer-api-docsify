# TextPickerTextStyle

文本样式选项，继承自[PickerTextStyle](arkts-arkui-common-pickertextstyle-i.md)。

**Inheritance/Implementation:** TextPickerTextStyle extends [PickerTextStyle](arkts-arkui-common-pickertextstyle-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface TextPickerTextStyle extends PickerTextStyle--><!--Device-unnamed-export declare interface TextPickerTextStyle extends PickerTextStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maxFontSize

```TypeScript
maxFontSize?: double | string | Resource
```

文本最大显示字号。详细规则请参考Text组件的[maxFontSize](arkts-arkui-text-textattribute-i.md#maxfontsize)属性。

**Type:** double \| string \| Resource

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerTextStyle-maxFontSize?: double | string | Resource--><!--Device-TextPickerTextStyle-maxFontSize?: double | string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## minFontSize

```TypeScript
minFontSize?: double | string | Resource
```

文本最小显示字号，与maxFontSize配合使用。当设置minFontSize和maxFontSize时，font中的size将不生效。默认最大行数为1，自适应高度方式为MIN_FONT_SIZE_FIRST。详细规则请参考Text组件的[minFontSize](arkts-arkui-text-textattribute-i.md#minfontsize)属性。

**Type:** double \| string \| Resource

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerTextStyle-minFontSize?: double | string | Resource--><!--Device-TextPickerTextStyle-minFontSize?: double | string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## overflow

```TypeScript
overflow?: TextOverflow
```

文本截断方式。当设置为MARQUEE时，该属性不生效。详细规则请参考Text组件的[textOverflow](arkts-arkui-text-textattribute-i.md#textoverflow)属性。

**Type:** [TextOverflow](arkts-arkui-textoverflow-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerTextStyle-overflow?: TextOverflow--><!--Device-TextPickerTextStyle-overflow?: TextOverflow-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

