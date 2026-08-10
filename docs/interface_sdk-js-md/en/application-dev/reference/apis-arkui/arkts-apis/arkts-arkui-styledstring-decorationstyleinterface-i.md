# DecorationStyleInterface

文本装饰线样式接口对象说明。

> **说明：**
> 
> 当文字的下边缘轮廓与装饰线位置相交时，会触发下划线避让规则，下划线将在这些字符处避让文字。常见“gjyqp”等英文字符。
> 
> 当文本装饰线的颜色设置为Color.Transparent时，装饰线颜色设置为跟随每行第一个字的字体颜色。当文本装饰线的颜色设置为透明色16进制对应值“#00FFFFFF”时，装饰线颜色设置为透明色。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface DecorationStyleInterface--><!--Device-unnamed-export declare interface DecorationStyleInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## color

```TypeScript
color?: ResourceColor
```

装饰线颜色。

默认值：Color.Black

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DecorationStyleInterface-color?: ResourceColor--><!--Device-DecorationStyleInterface-color?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## style

```TypeScript
style?: TextDecorationStyle
```

装饰线样式。

默认值：TextDecorationStyle.SOLID

**Type:** [TextDecorationStyle](arkts-arkui-textdecorationstyle-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DecorationStyleInterface-style?: TextDecorationStyle--><!--Device-DecorationStyleInterface-style?: TextDecorationStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## thicknessScale

```TypeScript
thicknessScale?: double
```

装饰线粗细缩放。

默认值：1.0

取值范围：[0, +∞)

**说明：** 负值按默认值处理。

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DecorationStyleInterface-thicknessScale?: double--><!--Device-DecorationStyleInterface-thicknessScale?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type: TextDecorationType | undefined
```

装饰线类型。

默认值：TextDecorationType.None

取值undefined时，按默认值处理。

**Type:** [TextDecorationType](arkts-arkui-textdecorationtype-e.md) \| undefined

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DecorationStyleInterface-type: TextDecorationType | undefined--><!--Device-DecorationStyleInterface-type: TextDecorationType | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

