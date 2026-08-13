# KeyframeState

Defines a keyframe state.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface KeyframeState--><!--Device-unnamed-export declare interface KeyframeState-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## curve

```TypeScript
curve?: Curve | string | ICurve
```

Animation curve of this keyframe.

**Type:** [Curve](../../apis-arkui/arkts-apis/arkts-arkui-curve-e.md) \| string \| [ICurve](arkts-na-icurve-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

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

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-KeyframeState-duration: int--><!--Device-KeyframeState-duration: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## event

```TypeScript
event: () => void
```

The closure function to specify the terminating state of this keyframe.

**Type:** () =&gt; void

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-KeyframeState-event: () => void--><!--Device-KeyframeState-event: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

