# ResolvedUIContext

**ResolvedUIContext** instance object. > **NOTE：**> > - You can preview how this component looks on a real device, but not in DevEco Studio Previewer. > > - **ResolvedUIContext** is inherited from [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md#UIContext). Objects of this class contain > the [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md#UIContext) instance and its parsing policy.

**Inheritance/Implementation:** ResolvedUIContext extends [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md#UIContext)

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Deprecated since:** -1

<!--Device-unnamed-export class ResolvedUIContext--><!--Device-unnamed-export class ResolvedUIContext-End-->

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

## strategy

```TypeScript
strategy: ResolveStrategy
```

Resolving strategy of the UIContext.

**Type:** [ResolveStrategy](arkts-arkui-arkui-uicontext-resolvestrategy-e.md)

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-ResolvedUIContext-strategy: ResolveStrategy--><!--Device-ResolvedUIContext-strategy: ResolveStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

