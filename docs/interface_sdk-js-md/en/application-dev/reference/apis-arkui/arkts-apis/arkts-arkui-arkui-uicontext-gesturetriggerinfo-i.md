# GestureTriggerInfo

Defines the information provided when a specific gesture callback is triggered.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** -1

<!--Device-unnamed-export interface GestureTriggerInfo--><!--Device-unnamed-export interface GestureTriggerInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AtomicServiceBar } from 'AtomicServiceBar';
import { ComponentUtils } from 'ComponentUtils';
import { ContextMenuController } from 'ContextMenuController';
import { CursorController } from 'CursorController';
import { DialogPresenter } from 'DialogPresenter';
import { DragController } from 'DragController';
import { Font } from 'Font';
import { KeyboardAvoidMode } from 'KeyboardAvoidMode';
import { MediaQuery } from 'MediaQuery';
import { OverlayManager } from 'OverlayManager';
import { PromptAction } from 'PromptAction';
import { Router } from 'Router';
import { UIContext } from 'UIContext';
import { UIInspector } from 'UIInspector';
import { UIObserver } from 'UIObserver';
import { PageInfo } from 'PageInfo';
import { SwiperDynamicSyncScene } from 'SwiperDynamicSyncScene';
import { SwiperDynamicSyncSceneType } from 'SwiperDynamicSyncSceneType';
import { MarqueeDynamicSyncScene } from 'MarqueeDynamicSyncScene';
import { MarqueeDynamicSyncSceneType } from 'MarqueeDynamicSyncSceneType';
import { MeasureUtils } from 'MeasureUtils';
import { FrameCallback } from 'FrameCallback';
import { OverlayManagerOptions } from 'OverlayManagerOptions';
import { TargetInfo } from 'TargetInfo';
import { TextMenuController } from 'TextMenuController';
import { NodeIdentity } from 'NodeIdentity';
import { NodeRenderState } from 'NodeRenderState';
import { NodeRenderStateChangeCallback } from 'NodeRenderStateChangeCallback';
import { Magnifier } from 'Magnifier';
import { ResolvedUIContext } from 'ResolvedUIContext';
import { TextSelectionClearPolicy } from 'TextSelectionClearPolicy';
import { CustomKeyboardContinueFeature } from 'CustomKeyboardContinueFeature';
```

## current

```TypeScript
current: GestureRecognizer
```

Gesture recognizer object. Detailed gesture information can be obtained from this object. However, avoid retaining this object locally as it may become invalid after the node is released.

**Type:** GestureRecognizer

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-GestureTriggerInfo-current: GestureRecognizer--><!--Device-GestureTriggerInfo-current: GestureRecognizer-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## currentPhase

```TypeScript
currentPhase: GestureActionPhase
```

Phase of the gesture action callback.

**Type:** [GestureActionPhase](arkts-arkui-arkui-uicontext-gestureactionphase-e.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-GestureTriggerInfo-currentPhase: GestureActionPhase--><!--Device-GestureTriggerInfo-currentPhase: GestureActionPhase-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## event

```TypeScript
event: GestureEvent
```

Gesture event object.

**Type:** GestureEvent

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-GestureTriggerInfo-event: GestureEvent--><!--Device-GestureTriggerInfo-event: GestureEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## node

```TypeScript
node?: FrameNode
```

Node that triggers the gesture. The default value is **null**, indicating that no specific node triggers the gesture.

**Type:** FrameNode

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-GestureTriggerInfo-node?: FrameNode--><!--Device-GestureTriggerInfo-node?: FrameNode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

