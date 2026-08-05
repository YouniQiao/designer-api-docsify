# DialogOptions

Extends \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ to provide enhanced customization capabilities for the dialog box.

**Inheritance/Implementation:** DialogOptions extends [BaseDialogOptions](arkts-arkui-promptaction-basedialogoptions-i.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-promptAction-interface DialogOptions extends BaseDialogOptions--><!--Device-promptAction-interface DialogOptions extends BaseDialogOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyle

```TypeScript
backgroundBlurStyle?: BlurStyle
```

Background blur style of the dialog box. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_Default value: **BlurStyle.COMPONENT\_ULTRA\_THICK** \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_**NOTE** \_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_Setting this parameter to **BlurStyle.NONE** disables the background blur. When **backgroundBlurStyle** is set to a value other than **NONE**, do not set **backgroundColor**. If you do, the color display may not produce the expected visual effect.

**Type:** BlurStyle

**Default:** BlurStyle.COMPONENT_ULTRA_THICK

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-DialogOptions-backgroundBlurStyle?: BlurStyle--><!--Device-DialogOptions-backgroundBlurStyle?: BlurStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundColor

```TypeScript
backgroundColor?: ResourceColor
```

Background color of the dialog box.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_Default value: **Color.Transparent**. \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_**NOTE** \_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_The background color will be visually combined with the blur effect when both properties are set. If the resulting effect does not match your design requirements, you can disable the blur effect entirely by explicitly setting the **backgroundBlurStyle** property to **BlurStyle.NONE**.

**Type:** ResourceColor

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-DialogOptions-backgroundColor?: ResourceColor--><!--Device-DialogOptions-backgroundColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderColor

```TypeScript
borderColor?: DialogOptionsBorderColor
```

Border color of the dialog box. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_Default value: **Color.Black**. \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_ **borderColor** must be used with **borderWidth** in pairs.

**Type:** DialogOptionsBorderColor

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-DialogOptions-borderColor?: DialogOptionsBorderColor--><!--Device-DialogOptions-borderColor?: DialogOptionsBorderColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderStyle

```TypeScript
borderStyle?: DialogOptionsBorderStyle
```

Border style of the dialog box. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_Default value: **BorderStyle.Solid**. \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_ **borderStyle** must be used with **borderWidth** in pairs.

**Type:** DialogOptionsBorderStyle

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-DialogOptions-borderStyle?: DialogOptionsBorderStyle--><!--Device-DialogOptions-borderStyle?: DialogOptionsBorderStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderWidth

```TypeScript
borderWidth?: DialogOptionsBorderWidth
```

Border width of the dialog box. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_You can set the width for all four sides or set separate widths for individual sides. \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_Default value: **0**. \_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_Unit: vp. \_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_ When set to a percentage, the value defines the border width as a percentage of the parent dialog box's width. \_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_If the left and right borders are greater than its width, or the top and bottom borders are greater than its height, the dialog box may not display as expected.

**Type:** DialogOptionsBorderWidth

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-DialogOptions-borderWidth?: DialogOptionsBorderWidth--><!--Device-DialogOptions-borderWidth?: DialogOptionsBorderWidth-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## cornerRadius

```TypeScript
cornerRadius?: DialogOptionsCornerRadius
```

Background corner radius of the dialog box.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_You can set separate radii for the four corners. \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_Default value: **{ topLeft: '32vp', topRight: '32vp', bottomLeft: '32vp', bottomRight: '32vp' }** \_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_ The radius of the rounded corners is subject to the component size. Its maximum value is half of the component width or height. If the value is negative, the default value is used. \_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_ When set to a percentage, the value defines the radius as a percentage of the parent dialog box's width or height.

**Type:** DialogOptionsCornerRadius

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-DialogOptions-cornerRadius?: DialogOptionsCornerRadius--><!--Device-DialogOptions-cornerRadius?: DialogOptionsCornerRadius-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## height

```TypeScript
height?: Dimension
```

Height of the dialog box. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_**NOTE** \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_- Default maximum value: 0.9 x (Window height – Safe area) \_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_- When this parameter is set to a percentage, the reference height of the dialog box is the height of the window where the dialog box is located minus the safe area. You can decrease or increase the height as needed.

**Type:** Dimension

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-DialogOptions-height?: Dimension--><!--Device-DialogOptions-height?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadow

```TypeScript
shadow?: DialogOptionsShadow
```

Shadow of the dialog box. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_Default value on 2-in-1 devices: **ShadowStyle.OUTER\_FLOATING\_MD** when the dialog box is focused and **ShadowStyle.OUTER\_FLOATING\_SM** otherwise On other devices, the dialog box has no shadow by default.

**Type:** DialogOptionsShadow

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-DialogOptions-shadow?: DialogOptionsShadow--><!--Device-DialogOptions-shadow?: DialogOptionsShadow-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
width?: Dimension
```

Width of the dialog box. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_**NOTE** \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_- Default maximum value: 400vp \_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_- Percentage-based configuration: The reference width of the dialog box is adjusted based on the width of the window where the dialog box is located.

**Type:** Dimension

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-DialogOptions-width?: Dimension--><!--Device-DialogOptions-width?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

