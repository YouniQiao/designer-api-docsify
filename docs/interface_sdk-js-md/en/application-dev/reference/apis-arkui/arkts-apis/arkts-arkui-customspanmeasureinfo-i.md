# CustomSpanMeasureInfo

定义自定义绘制Span的测量信息接口。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface CustomSpanMeasureInfo--><!--Device-unnamed-declare interface CustomSpanMeasureInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontSize

```TypeScript
fontSize: number
```

设置文本字体大小。

单位：[fp](../../../reference/apis-arkui/arkui-ts/ts-pixel-units.md#基本像素单位)

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CustomSpanMeasureInfo-fontSize: number--><!--Device-CustomSpanMeasureInfo-fontSize: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## layoutPolicy

```TypeScript
layoutPolicy?: LayoutPolicy
```

自定义span所在父组件的宽度布局策略。

**说明：**

当值为null或undefined时，表示父组件没有设置宽度布局策略。

**Type:** [LayoutPolicy](arkts-arkui-common-layoutpolicy-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CustomSpanMeasureInfo-layoutPolicy?: LayoutPolicy--><!--Device-CustomSpanMeasureInfo-layoutPolicy?: LayoutPolicy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maxWidth

```TypeScript
maxWidth?: number
```

自定义span所在父组件的内容区的最大宽度约束。

默认值：使用自身宽度。

单位：[px](../../../reference/apis-arkui/arkui-ts/ts-pixel-units.md#基本像素单位)

**Type:** number

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-CustomSpanMeasureInfo-maxWidth?: number--><!--Device-CustomSpanMeasureInfo-maxWidth?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

