# TextPickerTextStyle

文本样式选项，继承自[PickerTextStyle](../arkts-apis/arkts-arkui-common-pickertextstyle-i.md/arkts-arkui-common-pickertextstyle-i.md)。

**Inheritance/Implementation:** TextPickerTextStyle extends [PickerTextStyle](../arkts-apis/arkts-arkui-common-pickertextstyle-i.md/arkts-arkui-common-pickertextstyle-i.md)

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

<!--Device-unnamed-declare interface TextPickerTextStyle extends PickerTextStyle--><!--Device-unnamed-declare interface TextPickerTextStyle extends PickerTextStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maxFontSize

```TypeScript
maxFontSize?: number | string | Resource
```

设置文本最大显示字号，与minFontSize配合使用。当需要限制文本的最大显示尺寸以避免文本过大或需要实现字号自适应时传入此参数。

> **说明：**当设置minFontSize和maxFontSize时，font中的size将不生效。详细规则请参考Text组件的
> [maxFontSize](../arkts-apis/arkts-arkui-text-textattribute-i.md/arkts-arkui-text-textattribute-i.md#maxfontsize)属性。

**Type:** number \| string \| Resource

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-TextPickerTextStyle-maxFontSize?: number | string | Resource--><!--Device-TextPickerTextStyle-maxFontSize?: number | string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## minFontSize

```TypeScript
minFontSize?: number | string | Resource
```

设置文本最小显示字号，与maxFontSize配合使用。当需要限制文本的最小显示尺寸以避免文本过小或需要实现字号自适应时传入此参数。

> **说明：**当设置minFontSize和maxFontSize时，font中的size将不生效。默认最大行数为1，自适应高度方式为MIN_FONT_SIZE_FIRST。详细
> 规则请参考Text组件的[minFontSize](../arkts-apis/arkts-arkui-text-textattribute-i.md/arkts-arkui-text-textattribute-i.md#minfontsize)属性。

**Type:** number \| string \| Resource

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-TextPickerTextStyle-minFontSize?: number | string | Resource--><!--Device-TextPickerTextStyle-minFontSize?: number | string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## overflow

```TypeScript
overflow?: TextOverflow
```

文本截断方式。当设置为MARQUEE时，该属性不生效。详细规则请参考Text组件的[textOverflow](../arkts-apis/arkts-arkui-text-textattribute-i.md/arkts-arkui-text-textattribute-i.md#textoverflow)属性。

**Type:** [TextOverflow](../arkts-apis/arkts-arkui-enums-textoverflow-e.md)

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-TextPickerTextStyle-overflow?: TextOverflow--><!--Device-TextPickerTextStyle-overflow?: TextOverflow-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

