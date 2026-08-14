# GestureHandlingResolution

Class for declaring the result of smart gesture handling.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export class GestureHandlingResolution--><!--Device-unnamed-export class GestureHandlingResolution-End-->

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

## constructor

```TypeScript
constructor(isConsumed: boolean)
```

Constructor for the smart gesture handling result.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-GestureHandlingResolution-constructor(isConsumed: boolean)--><!--Device-GestureHandlingResolution-constructor(isConsumed: boolean)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isConsumed | boolean | Yes | Whether to consume the current smart gesture.<br/>**true**: The smart gesture is consumed. If [selectedProposal](#selectedProposal) is not set, the system default action handling is used. If **selectedProposal** is set, the custom action handling is used.<br/>**false**: The smart gesture is not consumed, and the system treats it as unhandled. |

## isConsumed

```TypeScript
isConsumed: boolean
```

Whether to consume the current smart gesture. **true**: The smart gesture is consumed. If **selectedProposal** is not set, the system default action handling is used. If **selectedProposal** is set, the custom action handling is used. **false**: The smart gesture is not consumed, and the system treats it as unhandled.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-GestureHandlingResolution-isConsumed: boolean--><!--Device-GestureHandlingResolution-isConsumed: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedProposal

```TypeScript
selectedProposal?: BaseGestureHandlingProposal
```

The smart gesture handling behavior specified by the user. When **isConsumed** is **true**: If **selectedProposal** is not set, the system default action handling is used. If **selectedProposal** is set, the custom action handling is used. When **isConsumed** is **false**, the **selectedProposal** setting does not take effect.

**Type:** [BaseGestureHandlingProposal](arkts-arkui-arkui-uicontext-basegesturehandlingproposal-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-GestureHandlingResolution-selectedProposal?: BaseGestureHandlingProposal--><!--Device-GestureHandlingResolution-selectedProposal?: BaseGestureHandlingProposal-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

