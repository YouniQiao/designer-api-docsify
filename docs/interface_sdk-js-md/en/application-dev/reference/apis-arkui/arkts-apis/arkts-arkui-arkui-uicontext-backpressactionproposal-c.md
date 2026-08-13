# BackPressActionProposal

Smart gesture back press action handling. When dynamically customizing smart gesture behavior through the [registerMonitor](arkts-arkui-arkui-uicontext-smartgesturecontroller-c.md#registerMonitor) API, setting the return value [GestureHandlingResolution](arkts-arkui-arkui-uicontext-gesturehandlingresolution-c.md#GestureHandlingResolution)'s **selectedProposal** to an object of this type navigates back to the previous page.

**Inheritance/Implementation:** BackPressActionProposal extends [BaseGestureHandlingProposal](arkts-arkui-arkui-uicontext-basegesturehandlingproposal-c.md#BaseGestureHandlingProposal)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export class BackPressActionProposal--><!--Device-unnamed-export class BackPressActionProposal-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { OverlayManager, FrameCallback, ResolvedUIContext, NodeRenderStateChangeCallback, MediaQuery, OverlayManagerOptions, TextMenuController, UIObserver, Font, KeyboardAvoidMode, MarqueeDynamicSyncScene, PromptAction, NodeRenderState, UIContext, TextSelectionClearPolicy, SwiperDynamicSyncScene, Router, MarqueeDynamicSyncSceneType, DialogPresenter, Magnifier, ContextMenuController, UIInspector, CustomKeyboardContinueFeature, CursorController, SwiperDynamicSyncSceneType, AtomicServiceBar, PageInfo, TargetInfo, ComponentUtils, DragController, MeasureUtils, NodeIdentity } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor()
```

Constructor for the smart gesture back press action handling.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-BackPressActionProposal-constructor()--><!--Device-BackPressActionProposal-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

