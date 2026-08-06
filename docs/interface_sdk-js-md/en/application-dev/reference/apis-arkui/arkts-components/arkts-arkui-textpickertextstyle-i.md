# TextPickerTextStyle

Defines the text style options for the text picker. Inherits from [PickerTextStyle]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

**Inheritance/Implementation:** TextPickerTextStyle extends [PickerTextStyle](../arkts-apis/arkts-arkui-component/common-pickertextstyle-i.md)

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

<!--Device-unnamed-declare interface TextPickerTextStyle extends PickerTextStyle--><!--Device-unnamed-declare interface TextPickerTextStyle extends PickerTextStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maxFontSize

```TypeScript
maxFontSize?: number | string | Resource
```

Maximum font size for the text. For details, see [maxFontSize]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

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

Minimum font size for the text. Used with **maxFontSize** to enable font scaling. When both **minFontSize** and  
**maxFontSize** are set, the **size** property in **font** is ignored. By default, the maximum number of lines is1, with the **MIN\_FONT\_SIZE\_FIRST** adaptation strategy. For details, see  
[minFontSize]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

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

Text overflow behavior. This property has no effect when set to **MARQUEE**. For details, see  
[textOverflow]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

**Type:** TextOverflow

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-TextPickerTextStyle-overflow?: TextOverflow--><!--Device-TextPickerTextStyle-overflow?: TextOverflow-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

