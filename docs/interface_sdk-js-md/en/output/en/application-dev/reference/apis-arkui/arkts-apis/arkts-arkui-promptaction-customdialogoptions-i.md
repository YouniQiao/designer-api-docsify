# CustomDialogOptions

Extends \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ to provide enhanced customization capabilities for the dialog box.

**Inheritance/Implementation:** CustomDialogOptions extends [BaseDialogOptions](arkts-arkui-promptaction-basedialogoptions-i.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-promptAction-interface CustomDialogOptions extends BaseDialogOptions--><!--Device-promptAction-interface CustomDialogOptions extends BaseDialogOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundBlurStyle

```TypeScript
backgroundBlurStyle?: BlurStyle
```

Background blur style of the dialog box. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_Default value: **BlurStyle.COMPONENT\_ULTRA\_THICK** \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_**NOTE** \_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_Setting this parameter to **BlurStyle.NONE** disables the background blur. When **backgroundBlurStyle** is set to a value other than **NONE**, do not set **backgroundColor**. If you do, the color display may not produce the expected visual effect.

**Type:** BlurStyle

**Default:** BlurStyle.COMPONENT_ULTRA_THICK

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CustomDialogOptions-backgroundBlurStyle?: BlurStyle--><!--Device-CustomDialogOptions-backgroundBlurStyle?: BlurStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundColor

```TypeScript
backgroundColor?: ResourceColor
```

Background color of the dialog box.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_Default value: **Color.Transparent**. \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_**NOTE** \_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_When **backgroundColor** is set to a non-transparent color, **backgroundBlurStyle** must be set to **BlurStyle.NONE**; otherwise, the color display may not meet the expected effect.

**Type:** ResourceColor

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CustomDialogOptions-backgroundColor?: ResourceColor--><!--Device-CustomDialogOptions-backgroundColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderColor

```TypeScript
borderColor?: ResourceColor | EdgeColors
```

Border color of the dialog box. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_Default value: **Color.Black**. \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_ **borderColor** must be used with **borderWidth** in pairs.

**Type:** ResourceColor \| EdgeColors

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CustomDialogOptions-borderColor?: ResourceColor | EdgeColors--><!--Device-CustomDialogOptions-borderColor?: ResourceColor | EdgeColors-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderStyle

```TypeScript
borderStyle?: BorderStyle | EdgeStyles
```

Border style of the dialog box. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_Default value: **BorderStyle.Solid**. \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_ **borderStyle** must be used with **borderWidth** in pairs.

**Type:** BorderStyle \| EdgeStyles

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CustomDialogOptions-borderStyle?: BorderStyle | EdgeStyles--><!--Device-CustomDialogOptions-borderStyle?: BorderStyle | EdgeStyles-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderWidth

```TypeScript
borderWidth?: Dimension | EdgeWidths
```

Border width of the dialog box. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_You can set the width for all four sides or set separate widths for individual sides. \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_Default value: **0**. \_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_Unit: vp. \_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_ When set to a percentage, the value defines the border width as a percentage of the parent dialog box's width. \_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_If the left and right borders are greater than its width, or the top and bottom borders are greater than its height, the dialog box may not display as expected.

**Type:** Dimension \| EdgeWidths

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CustomDialogOptions-borderWidth?: Dimension | EdgeWidths--><!--Device-CustomDialogOptions-borderWidth?: Dimension | EdgeWidths-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## builder

```TypeScript
builder: CustomBuilder
```

Custom content of the dialog box. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_**NOTE** \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_The builder needs to be assigned an arrow function in the following format: () => { this.XXX() }, where XXX indicates the internal builder name. \_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_Global builders must be created inside the component and called within the internal builder. \_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_The width and height percentages of the builder's root node are relative to the size of the dialog box container. \_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_The width and height percentages of non-root nodes are relative to the size of their parent node.

**Type:** CustomBuilder

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CustomDialogOptions-builder: CustomBuilder--><!--Device-CustomDialogOptions-builder: CustomBuilder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## cornerRadius

```TypeScript
cornerRadius?: Dimension | BorderRadiuses
```

Corner radius of the background. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_You can set separate radii for the four corners. \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_Default value: **{ topLeft: '32vp', topRight: '32vp', bottomLeft: '32vp', bottomRight: '32vp' }** \_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_ The radius of the rounded corners is subject to the component size. Its maximum value is half of the component width or height. If the value is negative, the default value is used. \_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_ When set to a percentage, the value defines the radius as a percentage of the parent dialog box's width or height.

**Type:** Dimension \| BorderRadiuses

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CustomDialogOptions-cornerRadius?: Dimension | BorderRadiuses--><!--Device-CustomDialogOptions-cornerRadius?: Dimension | BorderRadiuses-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## height

```TypeScript
height?: Dimension
```

Height of the dialog box. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_**NOTE** \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_- Default maximum height of the dialog box: 0.9 x (Window height – Safe area) \_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_- When this parameter is set to a percentage, the reference height of the dialog box is the height of the window where the dialog box is located minus the safe area. You can decrease or increase the height as needed.

**Type:** Dimension

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CustomDialogOptions-height?: Dimension--><!--Device-CustomDialogOptions-height?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadow

```TypeScript
shadow?: ShadowOptions | ShadowStyle
```

Shadow of the dialog box. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_Default value on 2-in-1 devices: **ShadowStyle.OUTER\_FLOATING\_MD** when the dialog box is focused and **ShadowStyle.OUTER\_FLOATING\_SM** otherwise On other devices, the dialog box has no shadow by default.

**Type:** ShadowOptions \| ShadowStyle

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CustomDialogOptions-shadow?: ShadowOptions | ShadowStyle--><!--Device-CustomDialogOptions-shadow?: ShadowOptions | ShadowStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
width?: Dimension
```

Width of the dialog box. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_**NOTE** \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_- Default maximum width of the dialog box: 400 vp \_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_- Percentage-based configuration: The reference width of the dialog box is adjusted based on the width of the window where the dialog box is located.

**Type:** Dimension

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CustomDialogOptions-width?: Dimension--><!--Device-CustomDialogOptions-width?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

