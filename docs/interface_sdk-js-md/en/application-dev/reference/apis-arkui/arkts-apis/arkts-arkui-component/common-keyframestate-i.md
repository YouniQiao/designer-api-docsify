# KeyframeState

Defines a keyframe state.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface KeyframeState--><!--Device-unnamed-export declare interface KeyframeState-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## event

```TypeScript
event: () => void
```

The closure function to specify the terminating state of this keyframe.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-KeyframeState-event: () => void--><!--Device-KeyframeState-event: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## curve

```TypeScript
curve?: Curve | string | ICurve
```

Animation curve of this keyframe.

**Type:** Curve \| string \| ICurve

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-KeyframeState-curve?: Curve | string | ICurve--><!--Device-KeyframeState-curve?: Curve | string | ICurve-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## duration

```TypeScript
duration: int
```

Animation duration of this keyframe, in ms.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-KeyframeState-duration: int--><!--Device-KeyframeState-duration: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

