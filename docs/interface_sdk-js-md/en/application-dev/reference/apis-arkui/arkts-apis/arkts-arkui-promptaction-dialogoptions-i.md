# DialogOptions

自定义弹窗的内容，继承自[BaseDialogOptions](../../../reference/apis-arkui/js-apis-promptAction copy.md#basedialogoptions11)。

**Inheritance/Implementation:** DialogOptions extends [BaseDialogOptions](arkts-arkui-promptaction-basedialogoptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-promptAction-export interface DialogOptions extends BaseDialogOptions--><!--Device-promptAction-export interface DialogOptions extends BaseDialogOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { LevelMode, ImmersiveMode, LevelOrder } from 'kits/@kit.ArkUI';
```

## backgroundBlurStyle

```TypeScript
backgroundBlurStyle?: BlurStyle
```

弹窗背板模糊材质。&lt;br/&gt;默认值：从API版本26.0.0开始，为BlurStyle.NONE，API版本26.0.0之前，为BlurStyle.COMPONENT_ULTRA_THICK。&lt;br/&gt;**说明：** &lt;br/&gt;设置为BlurStyle.NONE即可关闭背景虚化。当设置了backgroundBlurStyle为非NONE值时，则不要设置backgroundColor，否则颜色显示将不符合预期效果。

**Type:** [BlurStyle](../arkts-components/arkts-arkui-blurstyle-e.md)

**Default:** BlurStyle.COMPONENT_ULTRA_THICK

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DialogOptions-backgroundBlurStyle?: BlurStyle--><!--Device-DialogOptions-backgroundBlurStyle?: BlurStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## backgroundColor

```TypeScript
backgroundColor?: ResourceColor
```

设置弹窗背板颜色。&lt;br/&gt;默认值：Color.Transparent&lt;br/&gt;**说明：** &lt;br/&gt;backgroundColor会与模糊属性backgroundBlurStyle叠加产生效果，如果不符合预期，可将backgroundBlurStyle设置为BlurStyle.NONE，即可取消模糊。

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DialogOptions-backgroundColor?: ResourceColor--><!--Device-DialogOptions-backgroundColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderColor

```TypeScript
borderColor?: DialogOptionsBorderColor
```

设置弹窗背板的边框颜色。&lt;br/&gt;默认值：Color.Black &lt;br/&gt; 如果使用borderColor属性，需要和borderWidth属性一起使用。

**Type:** [DialogOptionsBorderColor](arkts-arkui-promptaction-dialogoptionsbordercolor-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DialogOptions-borderColor?: DialogOptionsBorderColor--><!--Device-DialogOptions-borderColor?: DialogOptionsBorderColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderStyle

```TypeScript
borderStyle?: DialogOptionsBorderStyle
```

设置弹窗背板的边框样式。&lt;br/&gt;默认值：BorderStyle.Solid。&lt;br/&gt; 如果使用borderStyle属性，需要和borderWidth属性一起使用。

**Type:** [DialogOptionsBorderStyle](arkts-arkui-promptaction-dialogoptionsborderstyle-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DialogOptions-borderStyle?: DialogOptionsBorderStyle--><!--Device-DialogOptions-borderStyle?: DialogOptionsBorderStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderWidth

```TypeScript
borderWidth?: DialogOptionsBorderWidth
```

设置弹窗背板的边框宽度。&lt;br /&gt;可分别设置4个边框宽度。&lt;br /&gt;默认值：0 &lt;br /&gt;单位：vp &lt;br /&gt; 百分比参数方式：以父元素弹窗宽的百分比来设置弹窗的边框宽度。&lt;br /&gt;当弹窗左边框和右边框大于弹窗宽度，弹窗上边框和下边框大于弹窗高度，显示可能不符合预期。

**Type:** [DialogOptionsBorderWidth](arkts-arkui-promptaction-dialogoptionsborderwidth-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DialogOptions-borderWidth?: DialogOptionsBorderWidth--><!--Device-DialogOptions-borderWidth?: DialogOptionsBorderWidth-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## cornerRadius

```TypeScript
cornerRadius?: DialogOptionsCornerRadius
```

设置弹窗背板的圆角半径。&lt;br /&gt;可分别设置4个圆角的半径。&lt;br /&gt;默认值：{ topLeft: '32vp', topRight: '32vp', bottomLeft: '32vp', bottomRight: '32vp' }&lt;br /&gt; 圆角大小受组件尺寸限制，最大值为组件宽或高的一半，若值为负，则按照默认值处理。 &lt;br /&gt; 百分比参数方式：以父元素弹窗宽和高的百分比来设置弹窗的圆角。

**Type:** [DialogOptionsCornerRadius](arkts-arkui-promptaction-dialogoptionscornerradius-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DialogOptions-cornerRadius?: DialogOptionsCornerRadius--><!--Device-DialogOptions-cornerRadius?: DialogOptionsCornerRadius-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## height

```TypeScript
height?: Dimension
```

设置弹窗背板的高度。&lt;br /&gt;**说明：**&lt;br /&gt;- 默认最大值：0.9 *（窗口高度 - 安全区域）。&lt;br /&gt;- 百分比参数方式：弹窗参考高度为（窗口高度 - 安全区域），在此基础上调小或调大。

**Type:** [Dimension](arkts-arkui-dimension-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DialogOptions-height?: Dimension--><!--Device-DialogOptions-height?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## shadow

```TypeScript
shadow?: DialogOptionsShadow
```

设置弹窗背板的阴影。&lt;br /&gt;当设备为2in1时，默认场景下获焦阴影值为ShadowStyle.OUTER_FLOATING_MD，失焦为ShadowStyle.OUTER_FLOATING_SM。其他设备默认无阴影。

**Type:** [DialogOptionsShadow](arkts-arkui-promptaction-dialogoptionsshadow-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DialogOptions-shadow?: DialogOptionsShadow--><!--Device-DialogOptions-shadow?: DialogOptionsShadow-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
width?: Dimension
```

设置弹窗背板的宽度。&lt;br /&gt;**说明：**&lt;br&gt;- 默认最大值：400vp &lt;br /&gt;- 百分比参数方式：弹窗参考宽度基于所在窗口宽度调整。

**Type:** [Dimension](arkts-arkui-dimension-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DialogOptions-width?: Dimension--><!--Device-DialogOptions-width?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

