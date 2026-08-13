# UIInspector

Provides APIs for registering the component layout and drawing display completion callbacks.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-unnamed-export class UIInspector--><!--Device-unnamed-export class UIInspector-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { OverlayManager, FrameCallback, ResolvedUIContext, NodeRenderStateChangeCallback, MediaQuery, OverlayManagerOptions, TextMenuController, UIObserver, Font, KeyboardAvoidMode, MarqueeDynamicSyncScene, PromptAction, NodeRenderState, UIContext, TextSelectionClearPolicy, SwiperDynamicSyncScene, Router, MarqueeDynamicSyncSceneType, DialogPresenter, Magnifier, ContextMenuController, UIInspector, CustomKeyboardContinueFeature, CursorController, SwiperDynamicSyncSceneType, AtomicServiceBar, PageInfo, TargetInfo, ComponentUtils, DragController, MeasureUtils, NodeIdentity } from '@kit.ArkUI';
```

## createComponentObserver

```TypeScript
createComponentObserver(id: string): inspector.ComponentObserver
```

Registers a callback for layout and drawing display completion notifications for a specific component.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-UIInspector-createComponentObserver(id: string): inspector.ComponentObserver--><!--Device-UIInspector-createComponentObserver(id: string): inspector.ComponentObserver-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | Yes | ID of the target component, set using the universal attributes id or key. |

**Return value:**

| Type | Description |
| --- | --- |
| inspector.ComponentObserver | Component observer, which is used to register or unregister listeners for completion of component layout or drawing display. |

## createComponentObserver

```TypeScript
createComponentObserver(id: string | number): inspector.ComponentObserver
```

Registers a callback for layout and drawing display completion notifications for a specific component. &lt;br&gt;Display refers to the process of sending the drawing command of a node to the graphics service and completing &lt;br&gt;the display. Compared with createComponentObserver, this API supports the input of **UniqueID** (the unique ID &lt;br&gt;allocated by the system to a node).

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-UIInspector-createComponentObserver(id: string | number): inspector.ComponentObserver--><!--Device-UIInspector-createComponentObserver(id: string | number): inspector.ComponentObserver-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string \| number | Yes | When the type is string, it indicates the ID of the specified component, set using the universal attributes id or key. &lt;br&gt;When the type is number, it indicates the unique ID of the node allocated by the system, obtained through &lt;br&gt;getUniqueId. When using the unique ID to create a listener handle, &lt;br&gt;ensure that the node corresponding to the unique ID exists. Otherwise, the listener does not take effect. &lt;br&gt;The value of the parameter in the number type is an integer ranging from 1 to 2147483647. |

**Return value:**

| Type | Description |
| --- | --- |
| inspector.ComponentObserver | Component observer, which is used to register or unregister listeners for completion of component layout or drawing display. |

