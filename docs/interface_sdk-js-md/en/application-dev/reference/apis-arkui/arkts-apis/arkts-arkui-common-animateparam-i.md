# AnimateParam

Defines the animate function params.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface AnimateParam--><!--Device-unnamed-export declare interface AnimateParam-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onFinish

```TypeScript
onFinish?: () => void
```

Callback invoked when the animation playback is complete.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimateParam-onFinish?: () => void--><!--Device-AnimateParam-onFinish?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## curve

```TypeScript
curve?: Curve | string | ICurve
```

Animation curve.

**Type:** [Curve](arkts-arkui-curve-e.md) \| string \| ICurve

**Default:** Curve.EaseInOut

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimateParam-curve?: Curve | string | ICurve--><!--Device-AnimateParam-curve?: Curve | string | ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## delay

```TypeScript
delay?: int
```

Animation delay time, in ms. By default, the animation has no delay.

**Type:** int

**Default:** 0

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimateParam-delay?: int--><!--Device-AnimateParam-delay?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## duration

```TypeScript
duration?: int
```

Animation duration, in ms.

**Type:** int

**Default:** 1000

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimateParam-duration?: int--><!--Device-AnimateParam-duration?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## expectedFrameRateRange

```TypeScript
expectedFrameRateRange?: ExpectedFrameRateRange
```

Expected frame rate range of the animation.

**Type:** [ExpectedFrameRateRange](../arkts-components/arkts-arkui-expectedframeraterange-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimateParam-expectedFrameRateRange?: ExpectedFrameRateRange--><!--Device-AnimateParam-expectedFrameRateRange?: ExpectedFrameRateRange-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## finishCallbackType

```TypeScript
finishCallbackType?: FinishCallbackType
```

Type of the **onFinish** callback.Default value: FinishCallbackType.REMOVED.

**Type:** [FinishCallbackType](arkts-arkui-common-finishcallbacktype-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimateParam-finishCallbackType?: FinishCallbackType--><!--Device-AnimateParam-finishCallbackType?: FinishCallbackType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## iterations

```TypeScript
iterations?: int
```

Number of times that the animation is played. By default, the animation is played once.The value **-1** indicates that the animation is played for an unlimited number of times.The value **0** indicates that there is no animation.

**Type:** int

**Default:** 1

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimateParam-iterations?: int--><!--Device-AnimateParam-iterations?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## playMode

```TypeScript
playMode?: PlayMode
```

Playback mode. By default, the animation is played from the beginning after the playback is complete.

**Type:** [PlayMode](arkts-arkui-playmode-e.md)

**Default:** PlayMode.Normal

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimateParam-playMode?: PlayMode--><!--Device-AnimateParam-playMode?: PlayMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## tempo

```TypeScript
tempo?: double
```

Animation playback speed. A larger value indicates faster animation playback, and a smaller value indicates slower animation playback. The value 0 means that there is no animation.

**Type:** double

**Default:** 1.0

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AnimateParam-tempo?: double--><!--Device-AnimateParam-tempo?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

