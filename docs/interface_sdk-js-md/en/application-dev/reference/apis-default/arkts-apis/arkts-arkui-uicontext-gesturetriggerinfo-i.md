# GestureTriggerInfo

The information when one gesture specific callback is triggered.@interface GestureTriggerInfo

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

<!--Device-unnamed-export interface GestureTriggerInfo--><!--Device-unnamed-export interface GestureTriggerInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## current

```TypeScript
current: GestureRecognizer
```

The gesture recognizer object. You can obtain the detailed information of the gesture from it, but please do not keep this object locally, as it might be unavailable when the node is released.

**Type:** GestureRecognizer

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureTriggerInfo-current: GestureRecognizer--><!--Device-GestureTriggerInfo-current: GestureRecognizer-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## currentPhase

```TypeScript
currentPhase: GestureActionPhase
```

The gesture action callback phase.

**Type:** [GestureActionPhase](arkts-arkui-uicontext-gestureactionphase-e.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureTriggerInfo-currentPhase: GestureActionPhase--><!--Device-GestureTriggerInfo-currentPhase: GestureActionPhase-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## event

```TypeScript
event: GestureEvent
```

The gesture event object.

**Type:** GestureEvent

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureTriggerInfo-event: GestureEvent--><!--Device-GestureTriggerInfo-event: GestureEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## node

```TypeScript
node?: FrameNode
```

The node which the gesture is being triggered on.

**Type:** FrameNode

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureTriggerInfo-node?: FrameNode--><!--Device-GestureTriggerInfo-node?: FrameNode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

