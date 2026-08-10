# CapsuleStyleOptions

胶囊样式选项。

继承自[ScanEffectOptions](arkts-arkui-scaneffectoptions-i.md)和[CommonProgressStyleOptions](arkts-arkui-commonprogressstyleoptions-i.md)。

**Inheritance/Implementation:** CapsuleStyleOptions extends [ScanEffectOptions](arkts-arkui-scaneffectoptions-i.md), [CommonProgressStyleOptions](arkts-arkui-commonprogressstyleoptions-i.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare interface CapsuleStyleOptions extends ScanEffectOptions, CommonProgressStyleOptions--><!--Device-unnamed-declare interface CapsuleStyleOptions extends ScanEffectOptions, CommonProgressStyleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderColor

```TypeScript
borderColor?: ResourceColor
```

内描边颜色。

默认值：

API version 10：'#33006cde'

API version 11及以上：'#33007dff'

**Type:** [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CapsuleStyleOptions-borderColor?: ResourceColor--><!--Device-CapsuleStyleOptions-borderColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderRadius

```TypeScript
borderRadius?: LengthMetrics
```

Capsule进度条圆角半径（不支持百分比设置）。

取值范围：[0, 组件高度/2]。默认值：组件高度 / 2。

设置非法数值时，按照默认值处理。

**Type:** [LengthMetrics](../arkts-apis/arkts-arkui-graphics-lengthmetrics-c.md)

**Default:** min(width, height) / 2

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-CapsuleStyleOptions-borderRadius?: LengthMetrics--><!--Device-CapsuleStyleOptions-borderRadius?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderWidth

```TypeScript
borderWidth?: Length
```

内描边宽度。

默认值：1vp

取值范围：大于等于0的数值，不支持百分比设置。

超出取值范围或设置非法值时按默认值处理。

**Type:** [Length](../arkts-apis/arkts-arkui-length-t.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CapsuleStyleOptions-borderWidth?: Length--><!--Device-CapsuleStyleOptions-borderWidth?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## content

```TypeScript
content?: ResourceStr
```

文本内容，应用可自定义。

当需要在Capsule进度条上显示自定义文本时传入此参数；不传入时不显示文本内容（若需显示百分比文本，可设置showDefaultPercentage为true）。

从API version 20开始，支持Resource类型。

**Type:** [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CapsuleStyleOptions-content?: ResourceStr--><!--Device-CapsuleStyleOptions-content?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## font

```TypeScript
font?: Font
```

文本样式。

默认值：

文本大小（不支持百分比设置）：12fp 

其他文本参数跟随[Text](../../apis-arkgraphics2d/arkts-apis/arkts-graphics-text.md/arkts-graphics-text.md)组件的主题值。

**Type:** [Font](../arkts-apis/arkts-arkui-font-i.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CapsuleStyleOptions-font?: Font--><!--Device-CapsuleStyleOptions-font?: Font-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontColor

```TypeScript
fontColor?: ResourceColor
```

文本颜色。

默认值：'#ff182431'

**Type:** [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CapsuleStyleOptions-fontColor?: ResourceColor--><!--Device-CapsuleStyleOptions-fontColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## showDefaultPercentage

```TypeScript
showDefaultPercentage?: boolean
```

显示百分比文本的开关。开启后，进度条上显示当前进度的百分比。设置了content属性时该属性不生效。

true：表示显示百分比文本；false：表示不显示百分比文本。

默认值：false

**Type:** boolean

**Default:** false

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CapsuleStyleOptions-showDefaultPercentage?: boolean--><!--Device-CapsuleStyleOptions-showDefaultPercentage?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

