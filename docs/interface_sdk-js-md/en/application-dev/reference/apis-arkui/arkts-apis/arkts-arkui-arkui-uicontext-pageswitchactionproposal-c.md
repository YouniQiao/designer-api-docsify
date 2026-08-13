# PageSwitchActionProposal

Smart gesture page switch action handling. The default direction is forward page switching, including right and down. When dynamically customizing smart gesture behavior through the [registerMonitor](arkts-arkui-arkui-uicontext-smartgesturecontroller-c.md#registerMonitor) API, setting the return value [GestureHandlingResolution](arkts-arkui-arkui-uicontext-gesturehandlingresolution-c.md#GestureHandlingResolution)'s **selectedProposal** to an object of this type triggers a page switching operation on the target component.

**Inheritance/Implementation:** PageSwitchActionProposal extends [TargetedGestureProposal](arkts-arkui-arkui-uicontext-targetedgestureproposal-c.md#TargetedGestureProposal)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export class PageSwitchActionProposal--><!--Device-unnamed-export class PageSwitchActionProposal-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { OverlayManager, FrameCallback, ResolvedUIContext, NodeRenderStateChangeCallback, MediaQuery, OverlayManagerOptions, TextMenuController, UIObserver, Font, KeyboardAvoidMode, MarqueeDynamicSyncScene, PromptAction, NodeRenderState, UIContext, TextSelectionClearPolicy, SwiperDynamicSyncScene, Router, MarqueeDynamicSyncSceneType, DialogPresenter, Magnifier, ContextMenuController, UIInspector, CustomKeyboardContinueFeature, CursorController, SwiperDynamicSyncSceneType, AtomicServiceBar, PageInfo, TargetInfo, ComponentUtils, DragController, MeasureUtils, NodeIdentity } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(node: FrameNode, pageCount: int)
```

Constructor for the smart gesture page switch action handling.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-PageSwitchActionProposal-constructor(node: FrameNode, pageCount: int)--><!--Device-PageSwitchActionProposal-constructor(node: FrameNode, pageCount: int)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | FrameNode | Yes | Target node that responds to the page switch action. |
| pageCount | int | Yes | Number of pages to switch.&lt;br/&gt;Value range: [0, +∞). Values less than 0 are treated as 0.&lt;br/&gt;Unit: pages. |

## pageCount

```TypeScript
pageCount: int
```

Number of pages to switch in the smart gesture. Value range: [0, +∞). Values less than 0 are treated as 0. Unit: pages.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-PageSwitchActionProposal-pageCount: int--><!--Device-PageSwitchActionProposal-pageCount: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

