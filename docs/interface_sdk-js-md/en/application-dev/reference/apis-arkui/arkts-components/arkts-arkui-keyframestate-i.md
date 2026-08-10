# KeyframeState

设置关键帧选项。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-declare interface KeyframeState--><!--Device-unnamed-declare interface KeyframeState-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## event

```TypeScript
event: () => void
```

指定在该关键帧时刻状态的闭包函数，即在该关键帧时刻要达到的状态。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-KeyframeState-event: () => void--><!--Device-KeyframeState-event: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## curve

```TypeScript
curve?: Curve | string | ICurve
```

该关键帧使用的动画曲线。

推荐以Curve或ICurve形式指定。

当类型为string时，为动画插值曲线，取值参考  
[AnimateParam](../../../reference/apis-arkui/arkui-ts/ts-explicit-animation.md#animateparam对象说明)的curve参数。

默认值：Curve.EaseInOut

**说明：**

由于[springMotion](../arkts-apis/arkts-arkui-curves-springmotion-f.md/arkts-arkui-curves-springmotion-f.md#springmotion)、  
[responsiveSpringMotion](../arkts-apis/arkts-arkui-curves-responsivespringmotion-f.md/arkts-arkui-curves-responsivespringmotion-f.md#responsivespringmotion)、  
[interpolatingSpring](../arkts-apis/arkts-arkui-curves-interpolatingspring-f.md/arkts-arkui-curves-interpolatingspring-f.md#interpolatingspring)曲线时长不生效，故不支持这三种曲线。

**Type:** [Curve](../arkts-apis/arkts-arkui-curve-e.md) \| string \| ICurve

**Default:** Curve.EaseInOut

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-KeyframeState-curve?: Curve | string | ICurve--><!--Device-KeyframeState-curve?: Curve | string | ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## duration

```TypeScript
duration: number
```

该段关键帧动画的持续时间，单位为毫秒。

取值范围：[0, +∞)

**说明：**

- 设置小于0的值时按0处理。

- 设置浮点型的值时，向下取整。例如，设置值为1.2，按照1处理。

**Type:** number

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-KeyframeState-duration: number--><!--Device-KeyframeState-duration: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

