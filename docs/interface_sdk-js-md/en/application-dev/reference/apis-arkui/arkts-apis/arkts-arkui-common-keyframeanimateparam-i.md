# KeyframeAnimateParam

Defines the overall animation parameters of the keyframe animation.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface KeyframeAnimateParam--><!--Device-unnamed-export declare interface KeyframeAnimateParam-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onFinish

```TypeScript
onFinish?: () => void
```

Callback invoked when the whole keyframe animation is complete or the ability is about to enter the background.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-KeyframeAnimateParam-onFinish?: () => void--><!--Device-KeyframeAnimateParam-onFinish?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## delay

```TypeScript
delay?: int
```

Animation delay time, in ms.

**Type:** int

**Default:** 0

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-KeyframeAnimateParam-delay?: int--><!--Device-KeyframeAnimateParam-delay?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## expectedFrameRateRange

```TypeScript
expectedFrameRateRange?: ExpectedFrameRateRange
```

Indicates expectedFrameRateRange of keyframe animation.

**Type:** [ExpectedFrameRateRange](../arkts-components/arkts-arkui-expectedframeraterange-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-KeyframeAnimateParam-expectedFrameRateRange?: ExpectedFrameRateRange--><!--Device-KeyframeAnimateParam-expectedFrameRateRange?: ExpectedFrameRateRange-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## iterations

```TypeScript
iterations?: int
```

Animation iterations. When set to -1, the animation playing it repeatedly. The value range is greater than or equal to -1.

**Type:** int

**Default:** 1

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-KeyframeAnimateParam-iterations?: int--><!--Device-KeyframeAnimateParam-iterations?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

