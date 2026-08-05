# TextPickerTextStyle

Defines the text style options.

**Inheritance/Implementation:** TextPickerTextStyle extends [PickerTextStyle](../../../apis-na/arkts-apis/arkts-na-component/common-pickertextstyle-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface TextPickerTextStyle extends PickerTextStyle--><!--Device-unnamed-export declare interface TextPickerTextStyle extends PickerTextStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maxFontSize

```TypeScript
maxFontSize?: double | string | Resource
```

Maximum font size.

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

Minimum font size, used in conjunction with maxFontSize. When minFontSize and maxFontSize are set, the size setting in font is ineffective. The default maximum number of lines is 1, and the default height adaptation mode is MIN\_FONT\_SIZE\_FIRST.

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

Display mode when the text is too long. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_NOTE\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_: Ineffective when set to MARQUEE. \_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_

**Type:** TextOverflow

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerTextStyle-overflow?: TextOverflow--><!--Device-TextPickerTextStyle-overflow?: TextOverflow-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

