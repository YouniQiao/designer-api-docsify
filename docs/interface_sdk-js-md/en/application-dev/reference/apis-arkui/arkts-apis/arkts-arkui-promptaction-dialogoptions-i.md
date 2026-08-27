# DialogOptions

Extends [BaseDialogOptions](arkts-arkui-promptaction-basedialogoptions-i.md) to provide enhanced customization capabilities for the dialog box.

**Inheritance/Implementation:** DialogOptions extends [BaseDialogOptions](arkts-arkui-promptaction-basedialogoptions-i.md)

**Since:** 18

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { promptAction, LevelMode, ImmersiveMode, LevelOrder } from '@kit.ArkUI';
```

## backgroundBlurStyle

```TypeScript
backgroundBlurStyle?: BlurStyle
```

Background blur style of the dialog box. Default value: **BlurStyle.COMPONENT_ULTRA_THICK**   
**NOTE：**Setting this parameter to **BlurStyle.NONE** disables the background blur. When **backgroundBlurStyle** is set to a value other than **NONE**, do not set **backgroundColor**. If you do, the color display may not produce the expected visual effect.

**Type:** BlurStyle

**Default:** BlurStyle.COMPONENT_ULTRA_THICK

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundColor

```TypeScript
backgroundColor?: ResourceColor
```

Background color of the dialog box.Default value: **Color.Transparent**.   
**NOTE：**The background color will be visually combined with the blur effect when both properties are set. If the resulting effect does not match your design requirements, you can disable the blur effect entirely by explicitly setting the **backgroundBlurStyle** property to **BlurStyle.NONE**.

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderColor

```TypeScript
borderColor?: DialogOptionsBorderColor
```

Border color of the dialog box. Default value: **Color.Black**.   
 **borderColor** must be used with **borderWidth** in pairs.

**Type:** [DialogOptionsBorderColor](arkts-arkui-promptaction-dialogoptionsbordercolor-t.md)

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderStyle

```TypeScript
borderStyle?: DialogOptionsBorderStyle
```

Border style of the dialog box. Default value: **BorderStyle.Solid**.   
 **borderStyle** must be used with **borderWidth** in pairs.

**Type:** [DialogOptionsBorderStyle](arkts-arkui-promptaction-dialogoptionsborderstyle-t.md)

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderWidth

```TypeScript
borderWidth?: DialogOptionsBorderWidth
```

Border width of the dialog box. You can set the width for all four sides or set separate widths for individual sides. Default value: **0**. Unit: vp. When set to a percentage, the value defines the border width as a percentage of the parent dialog box's width. If the left and right borders are greater than its width, or the top and bottom borders are greater than its height, the dialog box may not display as expected.

**Type:** [DialogOptionsBorderWidth](arkts-arkui-promptaction-dialogoptionsborderwidth-t.md)

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## cornerRadius

```TypeScript
cornerRadius?: DialogOptionsCornerRadius
```

Background corner radius of the dialog box.You can set separate radii for the four corners. Default value: **{ topLeft: '32vp', topRight: '32vp', bottomLeft: '32vp', bottomRight: '32vp' }** The radius of the rounded corners is subject to the component size. Its maximum value is half of the component width or height. If the value is negative, the default value is used. When set to a percentage, the value defines the radius as a percentage of the parent dialog box's width or height.

**Type:** [DialogOptionsCornerRadius](arkts-arkui-promptaction-dialogoptionscornerradius-t.md)

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## height

```TypeScript
height?: Dimension
```

Height of the dialog box.   
**NOTE：**
- Default maximum value: 0.9 x (Window height – Safe area)
- When this parameter is set to a percentage, the reference height of the dialog box is the height of the window where the dialog box is located minus the safe area. You can decrease or increase the height as needed.

**Type:** [Dimension](arkts-arkui-dimension-t.md)

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadow

```TypeScript
shadow?: DialogOptionsShadow
```

Shadow of the dialog box. Default value on 2-in-1 devices: **ShadowStyle.OUTER_FLOATING_MD** when the dialog box is focused and **ShadowStyle.OUTER_FLOATING_SM** otherwise On other devices, the dialog box has no shadow by default.

**Type:** [DialogOptionsShadow](arkts-arkui-promptaction-dialogoptionsshadow-t.md)

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
width?: Dimension
```

Width of the dialog box.   
**NOTE：**
- Default maximum value: 400vp
- Percentage-based configuration: The reference width of the dialog box is adjusted based on the width of the window where the dialog box is located.

**Type:** [Dimension](arkts-arkui-dimension-t.md)

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
