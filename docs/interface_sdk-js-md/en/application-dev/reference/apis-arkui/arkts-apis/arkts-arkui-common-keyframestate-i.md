# KeyframeState

设置关键帧选项。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface KeyframeState--><!--Device-unnamed-export declare interface KeyframeState-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## event

```TypeScript
event: () => void
```

指定在该关键帧时刻状态的闭包函数，即在该关键帧时刻要达到的状态。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

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

由于[springMotion](arkts-arkui-curves-springmotion-f.md#springmotion)、  
[responsiveSpringMotion](arkts-arkui-curves-responsivespringmotion-f.md#responsivespringmotion)、  
[interpolatingSpring](arkts-arkui-curves-interpolatingspring-f.md#interpolatingspring)曲线时长不生效，故不支持这三种曲线。

**Type:** [Curve](arkts-arkui-curve-e.md) \| string \| ICurve

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-KeyframeState-curve?: Curve | string | ICurve--><!--Device-KeyframeState-curve?: Curve | string | ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## duration

```TypeScript
duration: int
```

该段关键帧动画的持续时间，单位为毫秒。

取值范围：[0, +∞)

**说明：**

- 设置小于0的值时按0处理。

- 设置浮点型类型的值时，向下取整。例如，设置值为1.2，按照1处理。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-KeyframeState-duration: int--><!--Device-KeyframeState-duration: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

