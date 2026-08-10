# sharedTransitionOptions

共享元素转场动画参数。

> **说明：**
> 
> type为SharedTransitionEffectType.Exchange时motionPath才会生效。
> 
> type为SharedTransitionEffectType.Exchange时，效果为对匹配的共享元素产生位置、大小的过渡（可通过配置组件的border观察），不支持内容的过渡效果。例如，Text组件在两个页面上使用不同的
> fontSize属性值，即绘制内容有大小差异，在sharedTransition动画结束后的最后一帧，Text的fontSize效果会突变为跳转目标页fontSize的效果。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface sharedTransitionOptions--><!--Device-unnamed-export declare interface sharedTransitionOptions-End-->

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

**Type:** [Curve](arkts-arkui-curve-e.md) \| string \| ICurve

**Default:** 1000

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-sharedTransitionOptions-curve?: Curve | string | ICurve--><!--Device-sharedTransitionOptions-curve?: Curve | string | ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## delay

```TypeScript
delay?: int
```

延迟播放时间。

取值范围：[0, +∞)

默认值：0 

单位：毫秒

**Type:** int

**Default:** 0

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-sharedTransitionOptions-delay?: int--><!--Device-sharedTransitionOptions-delay?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## duration

```TypeScript
duration?: int
```

描述共享元素转场动效播放时长。

默认值：1000 

单位：毫秒

取值范围：[0, +∞)

**Type:** int

**Default:** 1000

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-sharedTransitionOptions-duration?: int--><!--Device-sharedTransitionOptions-duration?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## motionPath

```TypeScript
motionPath?: MotionPathOptions
```

运动路径信息。

**Type:** [MotionPathOptions](arkts-arkui-common-motionpathoptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-sharedTransitionOptions-motionPath?: MotionPathOptions--><!--Device-sharedTransitionOptions-motionPath?: MotionPathOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## type

```TypeScript
type?: SharedTransitionEffectType
```

动画类型。

默认值：SharedTransitionEffectType.Exchange

**Type:** [SharedTransitionEffectType](arkts-arkui-sharedtransitioneffecttype-e.md)

**Default:** SharedTransitionEffectType.Exchange

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-sharedTransitionOptions-type?: SharedTransitionEffectType--><!--Device-sharedTransitionOptions-type?: SharedTransitionEffectType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## zIndex

```TypeScript
zIndex?: int
```

设置Z轴。

取值范围：(-∞, +∞)

默认值：0

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-sharedTransitionOptions-zIndex?: int--><!--Device-sharedTransitionOptions-zIndex?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

