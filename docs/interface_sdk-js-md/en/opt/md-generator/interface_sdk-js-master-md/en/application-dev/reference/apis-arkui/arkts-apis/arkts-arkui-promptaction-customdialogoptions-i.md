# CustomDialogOptions

Extends [BaseDialogOptions](#basedialogoptions11) to provide enhanced customization capabilities for the dialog box.

**Inheritance/Implementation:** CustomDialogOptions extends [BaseDialogOptions](arkts-arkui-promptaction-basedialogoptions-i.md)

**Since:** 11

<!--Device-promptAction-interface CustomDialogOptions extends BaseDialogOptions--><!--Device-promptAction-interface CustomDialogOptions extends BaseDialogOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { LevelMode, ImmersiveMode, LevelOrder } from 'kits/@kit.ArkUI';
```

## backgroundBlurStyle

```TypeScript
backgroundBlurStyle?: BlurStyle
```

Background blur style of the dialog box.&lt;br&gt;Default value: **BlurStyle.COMPONENT_ULTRA_THICK**&lt;br&gt;**NOTE：**&lt;br&gt;Setting this parameter to **BlurStyle.NONE** disables the background blur. When **backgroundBlurStyle** is set to a value other than **NONE**, do not set **backgroundColor**. If you do, the color display may not produce the expected visual effect.

**Type:** [BlurStyle](../arkts-components/arkts-arkui-blurstyle-e.md)

**Default:** BlurStyle.COMPONENT_ULTRA_THICK

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CustomDialogOptions-backgroundBlurStyle?: BlurStyle--><!--Device-CustomDialogOptions-backgroundBlurStyle?: BlurStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundColor

```TypeScript
backgroundColor?: ResourceColor
```

Background color of the dialog box.&lt;br&gt;Default value: **Color.Transparent**.&lt;br&gt;**NOTE：**&lt;br&gt;When **backgroundColor** is set to a non-transparent color, **backgroundBlurStyle** must be set to **BlurStyle.NONE**; otherwise, the color display may not meet the expected effect.

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CustomDialogOptions-backgroundColor?: ResourceColor--><!--Device-CustomDialogOptions-backgroundColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderColor

```TypeScript
borderColor?: ResourceColor | EdgeColors
```

Border color of the dialog box.&lt;br&gt;Default value: **Color.Black**.&lt;br&gt; **borderColor** must be used with **borderWidth** in pairs.

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md) \| EdgeColors

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CustomDialogOptions-borderColor?: ResourceColor | EdgeColors--><!--Device-CustomDialogOptions-borderColor?: ResourceColor | EdgeColors-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderStyle

```TypeScript
borderStyle?: BorderStyle | EdgeStyles
```

Border style of the dialog box.&lt;br&gt;Default value: **BorderStyle.Solid**.&lt;br&gt; **borderStyle** must be used with **borderWidth** in pairs.

**Type:** [BorderStyle](arkts-arkui-borderstyle-e.md) \| EdgeStyles

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CustomDialogOptions-borderStyle?: BorderStyle | EdgeStyles--><!--Device-CustomDialogOptions-borderStyle?: BorderStyle | EdgeStyles-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderWidth

```TypeScript
borderWidth?: Dimension | EdgeWidths
```

Border width of the dialog box.&lt;br&gt;You can set the width for all four sides or set separate widths for individual sides.&lt;br&gt;Default value: **0**.&lt;br&gt;Unit: vp.&lt;br&gt; When set to a percentage, the value defines the border width as a percentage of the parent dialog box's width.&lt;br&gt;If the left and right borders are greater than its width, or the top and bottom borders are greater than its height, the dialog box may not display as expected.

**Type:** [Dimension](arkts-arkui-dimension-t.md) \| EdgeWidths

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CustomDialogOptions-borderWidth?: Dimension | EdgeWidths--><!--Device-CustomDialogOptions-borderWidth?: Dimension | EdgeWidths-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## builder

```TypeScript
builder: CustomBuilder
```

Custom content of the dialog box.&lt;br&gt;**NOTE：**&lt;br&gt;The builder needs to be assigned an arrow function in the following format: () => { this.XXX() }, where XXX indicates the internal builder name.&lt;br&gt;Global builders must be created inside the component and called within the internal builder.&lt;br&gt;The width and height percentages of the builder's root node are relative to the size of the dialog box container.&lt;br&gt;The width and height percentages of non-root nodes are relative to the size of their parent node.

**Type:** [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md)

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CustomDialogOptions-builder: CustomBuilder--><!--Device-CustomDialogOptions-builder: CustomBuilder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## cornerRadius

```TypeScript
cornerRadius?: Dimension | BorderRadiuses
```

Corner radius of the background.&lt;br&gt;You can set separate radii for the four corners.&lt;br&gt;Default value: **{ topLeft: '32vp', topRight: '32vp', bottomLeft: '32vp', bottomRight: '32vp' }**&lt;br&gt; The radius of the rounded corners is subject to the component size. Its maximum value is half of the component width or height. If the value is negative, the default value is used.&lt;br&gt; When set to a percentage, the value defines the radius as a percentage of the parent dialog box's width or height.

**Type:** [Dimension](arkts-arkui-dimension-t.md) \| BorderRadiuses

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CustomDialogOptions-cornerRadius?: Dimension | BorderRadiuses--><!--Device-CustomDialogOptions-cornerRadius?: Dimension | BorderRadiuses-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## height

```TypeScript
height?: Dimension
```

Height of the dialog box.&lt;br&gt;**NOTE：**&lt;br&gt;- Default maximum height of the dialog box: 0.9 x (Window height – Safe area)&lt;br&gt;- When this parameter is set to a percentage, the reference height of the dialog box is the height of the window where the dialog box is located minus the safe area. You can decrease or increase the height as needed.

**Type:** [Dimension](arkts-arkui-dimension-t.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CustomDialogOptions-height?: Dimension--><!--Device-CustomDialogOptions-height?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadow

```TypeScript
shadow?: ShadowOptions | ShadowStyle
```

Shadow of the dialog box.&lt;br&gt;Default value on 2-in-1 devices: **ShadowStyle.OUTER_FLOATING_MD** when the dialog box is focused and **ShadowStyle.OUTER_FLOATING_SM** otherwise On other devices, the dialog box has no shadow by default.

**Type:** [ShadowOptions](../arkts-components/arkts-arkui-shadowoptions-i.md) \| ShadowStyle

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CustomDialogOptions-shadow?: ShadowOptions | ShadowStyle--><!--Device-CustomDialogOptions-shadow?: ShadowOptions | ShadowStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
width?: Dimension
```

Width of the dialog box.&lt;br&gt;**NOTE：**&lt;br&gt;- Default maximum width of the dialog box: 400 vp&lt;br&gt;- Percentage-based configuration: The reference width of the dialog box is adjusted based on the width of the window where the dialog box is located.

**Type:** [Dimension](arkts-arkui-dimension-t.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CustomDialogOptions-width?: Dimension--><!--Device-CustomDialogOptions-width?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
