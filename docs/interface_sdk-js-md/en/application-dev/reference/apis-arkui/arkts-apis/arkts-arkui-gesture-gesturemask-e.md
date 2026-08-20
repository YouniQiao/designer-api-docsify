# GestureMask

Creating an Object

@enum { number }

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare enum GestureMask--><!--Device-unnamed-export declare enum GestureMask-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Normal

```TypeScript
Normal
```

High-priority response to the current gesture.When the current gesture fails to be recognized, other gesture responses are triggered.For gestures with the same priority, responses are performed based on the recognition sequence.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureMask-Normal--><!--Device-GestureMask-Normal-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## IgnoreInternal

```TypeScript
IgnoreInternal
```

Ignore internal gestures and recognize the current gesture first.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureMask-IgnoreInternal--><!--Device-GestureMask-IgnoreInternal-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

