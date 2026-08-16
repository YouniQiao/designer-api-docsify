# FocusController

Provides capabilities to control focus, including features such as clearing, moving, and activating focus. > **NOTE：**> > In the following API examples, you must first use [getFocusController()](arkts-arkui-arkui-uicontext-uicontext-c.md#getFocusController) in > **UIContext** to obtain a **FocusController** instance, and then call the APIs using the obtained instance.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

<!--Device-unnamed-export class FocusController--><!--Device-unnamed-export class FocusController-End-->

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

## activate

```TypeScript
activate(isActive: boolean, autoInactive?: boolean): void
```

Sets the [focus activation state](../../../ui/arkts-common-events-focus-event.md) of this page.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-FocusController-activate(isActive: boolean, autoInactive?: boolean): void--><!--Device-FocusController-activate(isActive: boolean, autoInactive?: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isActive | boolean | Yes | Whether to enter or exit the focus activation state.<br>The value **true** means to enter the focus activation state, and **false** means to exit the focus activation state. |
| autoInactive | boolean | No | Logic for exiting the focus activation state.<br>The value **true** means the focus activation state will be exited automatically when touch or mouse events are triggered, and **false** means the state is controlled solely by API calls.<br>Default value: **true |

## clearFocus

```TypeScript
clearFocus(): void
```

Clears the focus and forcibly moves the focus to the root container node of the page, causing other nodes in the focus chain to lose focus.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FocusController-clearFocus(): void--><!--Device-FocusController-clearFocus(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isActive

```TypeScript
isActive(): boolean
```

Obtains the focus activation state of the UI instance. For details about the focus activation state, see [Basic Concepts](../../../ui/arkts-common-events-focus-event.md#basic-concepts).

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FocusController-isActive(): boolean--><!--Device-FocusController-isActive(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Focus activation state of the UI instance. The value **true** means that the instance has entered the focus activation state, and **false** means that the instance has exited the focus activation state. |

## requestFocus

```TypeScript
requestFocus(key: string): void
```

Transfers focus to a component node by the component ID, which is effective immediately.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FocusController-requestFocus(key: string): void--><!--Device-FocusController-requestFocus(key: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | Component ID of the target node. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [150002](../errorcode-focus.md#150002-ancestor-component-not-focusable) | This component has an unfocusable ancestor. |
| [150003](../errorcode-focus.md#150003-component-does-not-exist) | the component is not on tree or does not exist. |
| [150001](../errorcode-focus.md#150001-component-not-focusable) | the component cannot be focused. |

## setAutoFocusTransfer

```TypeScript
setAutoFocusTransfer(isAutoFocusTransfer: boolean): void
```

Sets whether the new page automatically obtains focus during page switching.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-FocusController-setAutoFocusTransfer(isAutoFocusTransfer: boolean): void--><!--Device-FocusController-setAutoFocusTransfer(isAutoFocusTransfer: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isAutoFocusTransfer | boolean | Yes | Whether the new page automatically obtains focus during page switching using navigation components or APIs, such as [Router](../../apis-na/arkts-apis/arkts-router.md#@ohos.router), Navigation, Menu, Dialog, and Popup. The value **true** means the new page automatically obtains focus, and **false** means the opposite. Default value: **true**. |

## setKeyProcessingMode

```TypeScript
setKeyProcessingMode(mode: KeyProcessingMode): void
```

Sets the mode for processing key events.

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-FocusController-setKeyProcessingMode(mode: KeyProcessingMode): void--><!--Device-FocusController-setKeyProcessingMode(mode: KeyProcessingMode): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | KeyProcessingMode | Yes | Mode for processing key events. |

