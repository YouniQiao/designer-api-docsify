# TargetedGestureProposal

Base class for smart gesture handling with a target node.

**Inheritance/Implementation:** TargetedGestureProposal extends [BaseGestureHandlingProposal](arkts-arkui-arkui-uicontext-basegesturehandlingproposal-c.md#BaseGestureHandlingProposal)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export abstract class TargetedGestureProposal--><!--Device-unnamed-export abstract class TargetedGestureProposal-End-->

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

## node

```TypeScript
node: FrameNode
```

Target node that handles the current smart gesture.

**Type:** FrameNode

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-TargetedGestureProposal-node: FrameNode--><!--Device-TargetedGestureProposal-node: FrameNode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

