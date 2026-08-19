# BackPressActionProposal

Smart gesture back press action handling. When dynamically customizing smart gesture behavior through the [registerMonitor](../../apis-na/arkts-apis/arkts-na-arkui-uicontext-smartgesturecontroller-c.md#registermonitor) API, setting the return value [GestureHandlingResolution](../../apis-na/arkts-apis/arkts-na-arkui-uicontext-gesturehandlingresolution-c.md)'s **selectedProposal** to an object of this type navigates back to the previous page.

**Inheritance/Implementation:** BackPressActionProposal extends [BaseGestureHandlingProposal](../../apis-na/arkts-apis/arkts-na-arkui-uicontext-basegesturehandlingproposal-c.md)

**Since:** 26.0.0

<!--Device-unnamed-export class BackPressActionProposal--><!--Device-unnamed-export class BackPressActionProposal-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AtomicServiceBar, ComponentUtils, ContextMenuController, CursorController, DialogPresenter, DragController, Font, KeyboardAvoidMode, MediaQuery, OverlayManager, PromptAction, Router, UIContext, UIInspector, UIObserver, PageInfo, SwiperDynamicSyncScene, SwiperDynamicSyncSceneType, MarqueeDynamicSyncScene, MarqueeDynamicSyncSceneType, MeasureUtils, FrameCallback, OverlayManagerOptions, TargetInfo, TextMenuController, NodeIdentity, NodeRenderState, NodeRenderStateChangeCallback, Magnifier, ResolvedUIContext, TextSelectionClearPolicy, CustomKeyboardContinueFeature, BackgroundLuminanceSamplingConfigs, LuminanceSampler } from '@kit.ArkUI';
import { GestureListenerType, GestureActionPhase, GestureTriggerInfo, GestureObserverConfigs, GestureListenerCallback } from '@kit.ArkUI';
import { SwiperContentInfo, SwiperItemInfo } from '@kit.ArkUI';
import { BackPressActionProposal, BaseGestureHandlingProposal, ClickActionProposal, GestureHandlingResolution, NoneActionProposal, PageSwitchActionProposal, ScrollActionProposal, SelectActionProposal, SmartGestureController, TargetedGestureProposal } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor()
```

Constructor for the smart gesture back press action handling.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-BackPressActionProposal-constructor()--><!--Device-BackPressActionProposal-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

