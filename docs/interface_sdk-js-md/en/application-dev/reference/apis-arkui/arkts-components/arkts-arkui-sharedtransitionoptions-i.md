# sharedTransitionOptions

共享元素转场动画参数。

> **说明：**
> 
> type为SharedTransitionEffectType.Exchange时motionPath才会生效。
> 
> type为SharedTransitionEffectType.Exchange时，效果为对匹配的共享元素产生位置、大小的过渡（可通过配置组件的border观察），不支持内容的过渡效果。例如，Text组件在两个页面上使用不同的
> fontSize属性值，即绘制内容有大小差异，在sharedTransition动画结束后的最后一帧，Text的fontSize效果会突变为跳转目标页fontSize的效果。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-unnamed-declare interface sharedTransitionOptions--><!--Device-unnamed-declare interface sharedTransitionOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## curve

```TypeScript
curve?: Curve | string | ICurve
```

动画曲线。

推荐以Curve或ICurve形式指定。

当类型为string时，为动画插值曲线，取值参考  
[AnimateParam](../../../reference/apis-arkui/arkui-ts/ts-explicit-animation.md#animateparam对象说明)的curve参数。

默认值：Curve.Linear

**Type:** [Curve](../arkts-apis/arkts-arkui-curve-e.md) \| string \| ICurve

**Default:** Curve.Linear

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-sharedTransitionOptions-curve?: Curve | string | ICurve--><!--Device-sharedTransitionOptions-curve?: Curve | string | ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## delay

```TypeScript
delay?: number
```

延迟播放时间。

取值范围：[0, +∞)

默认值：0 

单位：毫秒

**Type:** number

**Default:** 0

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-sharedTransitionOptions-delay?: number--><!--Device-sharedTransitionOptions-delay?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## duration

```TypeScript
duration?: number
```

描述共享元素转场动效播放时长。

默认值：1000 

单位：毫秒

取值范围：[0, +∞)

**Type:** number

**Default:** 1000

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-sharedTransitionOptions-duration?: number--><!--Device-sharedTransitionOptions-duration?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## motionPath

```TypeScript
motionPath?: MotionPathOptions
```

运动路径信息。

**Type:** [MotionPathOptions](../arkts-apis/arkts-arkui-common-motionpathoptions-i.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-sharedTransitionOptions-motionPath?: MotionPathOptions--><!--Device-sharedTransitionOptions-motionPath?: MotionPathOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type?: SharedTransitionEffectType
```

动画类型。

默认值：SharedTransitionEffectType.Exchange

**Type:** [SharedTransitionEffectType](../arkts-apis/arkts-arkui-sharedtransitioneffecttype-e.md)

**Default:** SharedTransitionEffectType.Exchange

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-sharedTransitionOptions-type?: SharedTransitionEffectType--><!--Device-sharedTransitionOptions-type?: SharedTransitionEffectType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## zIndex

```TypeScript
zIndex?: number
```

设置Z轴。

取值范围：(-∞, +∞)

默认值：0

**Type:** number

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-sharedTransitionOptions-zIndex?: number--><!--Device-sharedTransitionOptions-zIndex?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

