# @ohos.selectionInput.selectionManager

This module provides word selection management capabilities, including creating, displaying, moving, hiding, and destroying panels, listening for word selection events using a mouse or touchpad, and retrieving the selected text. The typical usage process is as follows:
1. Call [on('selectionCompleted')](arkts-basicservices-selectionmanager-onselectioncompleted-f-sys.md#onselectioncompleted) to subscribe to the selection completion event.
2. In the callback, call [getSelectionContent](arkts-basicservices-selectionmanager-getselectioncontent-f-sys.md) to obtain the selected text.
3. Call [createPanel](arkts-basicservices-selectionmanager-createpanel-f-sys.md) to create a word selection panel.
4. Call [setUiContent](arkts-basicservices-selectionmanager-panel-i-sys.md#setuicontent) to load the page content.
5. Call [moveToGlobalDisplay](arkts-basicservices-selectionmanager-panel-i.md#movetoglobaldisplay) to move the panel to the specified position.
6. Call [show](arkts-basicservices-selectionmanager-panel-i-sys.md#show) to display the panel.
7. Call [destroyPanel](arkts-basicservices-selectionmanager-destroypanel-f-sys.md) to destroy the panel.
8. Call [off('selectionCompleted')](arkts-basicservices-selectionmanager-offselectioncompleted-f-sys.md#offselectioncompleted) to unsubscribe from the selection completion event.

> **NOTE：**&gt;
> - This module is supported only on PCs/2-in-1 devices. You can use
> **canIUse('SystemCapability.SelectionInput.Selection')** to check whether the current device supports this
> function.
> - APIs of this module can be called only by apps that integrate the extension ability for word selection. For
> details about how to implement the extension ability for word selection, see
> [SelectionExtensionAbility](arkts-basicservices-selectioninput-selectionextensionability-selectionextensionability-c-sys.md).

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace selectionManager--><!--Device-unnamed-declare namespace selectionManager-End-->

**System capability:** SystemCapability.SelectionInput.Selection

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { selectionManager } from '@kit.BasicServicesKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [offSelectionComplete](arkts-basicservices-selectionmanager-offselectioncomplete-f.md) | Unregisters the callback used to listen for the word selection completion event. This API uses an asynchronous callback to return the result.  **ArkTS mode:** This API applies only to ArkTS-Sta. |
| [onSelectionComplete](arkts-basicservices-selectionmanager-onselectioncomplete-f.md) | Registers a callback to listen for the word selection completion event. This API uses an asynchronous callback to return the result.  **ArkTS mode:** This API applies only to ArkTS-Sta. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [createPanel](arkts-basicservices-selectionmanager-createpanel-f-sys.md) | Creates a word selection panel, which is used to display the service-related operation UI or text processing result. After the panel is used, call [destroyPanel](arkts-basicservices-selectionmanager-destroypanel-f-sys.md) to destroy the panel and release resources. This API uses a promise to return the result.Only one [MENU_PANEL](arkts-basicservices-selectioninput-selectionpanel-paneltype-e-sys.md) and one [MAIN_PANEL](arkts-basicservices-selectioninput-selectionpanel-paneltype-e-sys.md) can be created for one word selection application. |
| [destroyPanel](arkts-basicservices-selectionmanager-destroypanel-f-sys.md) | Destroys the word selection panel. This API is used together with [createPanel](arkts-basicservices-selectionmanager-createpanel-f-sys.md) to destroy the panel object created by **createPanel()**. This API uses a promise to return the result. |
| [getSelectionContent](arkts-basicservices-selectionmanager-getselectioncontent-f-sys.md) | Obtains the content of the selected text. This API uses a promise to return the result. This API must be called in the [on('selectionCompleted')](arkts-basicservices-selectionmanager-onselectioncompleted-f-sys.md#onselectioncompleted) callback and is valid only after the word selection completion event is triggered. |
| [off_selectionCompleted](arkts-basicservices-selectionmanager-offselectioncompleted-f-sys.md#offselectioncompleted) | Unsubscribes from the word selection completion event. This API is used together with [on('selectionCompleted')](arkts-basicservices-selectionmanager-onselectioncompleted-f-sys.md#onselectioncompleted). |
| [on_selectionCompleted](arkts-basicservices-selectionmanager-onselectioncompleted-f-sys.md#onselectioncompleted) | Subscribes to the word selection completion event. This API is used together with [off('selectionCompleted')](arkts-basicservices-selectionmanager-offselectioncompleted-f-sys.md#offselectioncompleted).  [off('selectionCompleted')](arkts-basicservices-selectionmanager-offselectioncompleted-f-sys.md#offselectioncompleted) is used to unsubscribe from the event. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [Panel](arkts-basicservices-selectionmanager-panel-i.md) | Describes a **Panel** object, which is created using [createPanel](arkts-basicservices-selectionmanager-createpanel-f-sys.md). This method can be used to set, display, hide, and move the panel, as well as subscribe to events. It is applicable to scenarios where a custom operation UI needs to be displayed to users after word selection is complete. |

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [Panel](arkts-basicservices-selectionmanager-panel-i-sys.md) | Describes a **Panel** object, which is created using [createPanel](arkts-basicservices-selectionmanager-createpanel-f-sys.md). This method can be used to set, display, hide, and move the panel, as well as subscribe to events. It is applicable to scenarios where a custom operation UI needs to be displayed to users after word selection is complete. |
| [SelectionInfo](arkts-basicservices-selectionmanager-selectioninfo-i-sys.md) | Defines the information of a word selection event. |
<!--DelEnd-->

<!--Del-->
### Enums(System API)

| Name | Description |
| --- | --- |
| [SelectionType](arkts-basicservices-selectionmanager-selectiontype-e-sys.md) | Enumerates the word selection types.  \| Name \| Value\| Description \| \| ------------ \| -- \| ------------------ \| \| MOUSE_MOVE \| 1 \| Word selection by sliding the mouse or touchpad. \| \| DOUBLE_CLICK \| 2 \| Word selection by double-clicking the mouse or touchpad. \| \| TRIPLE_CLICK \| 3 \| Word selection by triple-clicking the mouse or touchpad. \| |
<!--DelEnd-->

