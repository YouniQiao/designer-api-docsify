# BadgeStyle

Badge的样式。包括文本颜色、尺寸、字重、圆点颜色和尺寸等。

> **说明：**
> > 当`borderWidth`大于0且`borderColor`与`badgeColor`颜色不一致时，先绘制角标，再绘制描边。由于边缘像素经过抗锯齿处理，抗锯齿产生半透明像素，四角会出现 `badgeColor` 颜色的描边
> 线。如需实现相关场景，建议使用[Text](../../apis-arkgraphics2d/arkts-apis/arkts-graphics-text.md/arkts-graphics-text.md)组件设置[outline](arkts-arkui-common-commonmethod-i.md#outline)代替Badge组件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface BadgeStyle--><!--Device-unnamed-export declare interface BadgeStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## badgeColor

```TypeScript
badgeColor?: ResourceColor
```

Badge的颜色。默认值：Color.Red 。

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Default:** Color.Red

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BadgeStyle-badgeColor?: ResourceColor--><!--Device-BadgeStyle-badgeColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## badgeSize

```TypeScript
badgeSize?: double | ResourceStr
```

Badge的大小。string类型支持number类型取值的字符串形式，可以附带单位，，支持的单位有"px"、"vp"、"fp"、"lpx"，例如"16"、"16vp"，不附带单位时默认单位为"fp"。默认值：16vp。

**Type:** double \| ResourceStr

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BadgeStyle-badgeSize?: double | ResourceStr--><!--Device-BadgeStyle-badgeSize?: double | ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderColor

```TypeScript
borderColor?: ResourceColor
```

底板描边颜色。默认值：Color.Red 。

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Default:** Color.Red

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BadgeStyle-borderColor?: ResourceColor--><!--Device-BadgeStyle-borderColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## borderWidth

```TypeScript
borderWidth?: Length
```

底板描边粗细,不支持设置百分比，当设置为百分比时，按照默认值处理。单位为：vp。默认值：1。

**Type:** [Length](arkts-arkui-length-t.md)

**Default:** 1

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BadgeStyle-borderWidth?: Length--><!--Device-BadgeStyle-borderWidth?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## color

```TypeScript
color?: ResourceColor
```

文本颜色。默认值：Color.White 。

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Default:** Color.White

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BadgeStyle-color?: ResourceColor--><!--Device-BadgeStyle-color?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableAutoAvoidance

```TypeScript
enableAutoAvoidance?: boolean
```

增加角标文本延伸显示时是否避让。true表示避让，false表示不避让。默认值：false。&lt;br&gt;**说明：**1. 避让效果为角标文本向组件内部延伸显示。2. 当外描边的宽度大于0时，角标的延伸起点为外描边的内侧。3. 当position设置为具体坐标值时，角标不进行避让处理。

**Type:** boolean

**Default:** false

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BadgeStyle-enableAutoAvoidance?: boolean--><!--Device-BadgeStyle-enableAutoAvoidance?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontSize

```TypeScript
fontSize?: double | ResourceStr
```

文本大小。string类型仅支持number类型取值的字符串形式，可以附带单位，支持的单位有"px"、"vp"、"fp"、"lpx"，例如"10"、"10fp"，不附带单位时默认单位为"fp"。默认值：10vp。

**Type:** double \| ResourceStr

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BadgeStyle-fontSize?: double | ResourceStr--><!--Device-BadgeStyle-fontSize?: double | ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontWeight

```TypeScript
fontWeight?: int | FontWeight | ResourceStr
```

设置文本的字体粗细。默认值：FontWeight.Normal。&lt;br&gt;number类型取值范围：[100,900]，取值间隔为100。取值越大，字体越粗。设置number类型在取值范围外时，按默认值400处理。string类型仅支持number类型取值的字符串形式，例如"400"，以及"bold"、"bolder"、"lighter"、"regular"、"medium"，分别对应FontWeight中相应的枚举值。

**Type:** int \| FontWeight \| ResourceStr

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BadgeStyle-fontWeight?: int | FontWeight | ResourceStr--><!--Device-BadgeStyle-fontWeight?: int | FontWeight | ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## outerBorderColor

```TypeScript
outerBorderColor?: ResourceColor
```

底板外描边颜色。默认值：Color.White 。

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Default:** Color.White

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BadgeStyle-outerBorderColor?: ResourceColor--><!--Device-BadgeStyle-outerBorderColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## outerBorderWidth

```TypeScript
outerBorderWidth?: LengthMetrics
```

底板外描边粗细。

默认值：0

单位：vp

不支持设置百分比，当设置为百分比时，按照默认值处理。

**Type:** [LengthMetrics](arkts-arkui-lengthmetrics-t.md)

**Default:** 0

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BadgeStyle-outerBorderWidth?: LengthMetrics--><!--Device-BadgeStyle-outerBorderWidth?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

