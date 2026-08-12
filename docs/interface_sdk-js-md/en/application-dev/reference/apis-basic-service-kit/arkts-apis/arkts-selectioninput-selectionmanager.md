# @ohos.selectionInput.selectionManager(Word Selection Management)

This module provides word selection management capabilities, including creating, displaying, moving, hiding, and destroying panels, listening for word selection events using a mouse or touchpad, and retrieving the selected text.The typical usage process is as follows:1. Call [on('selectionCompleted')](selectionManager.on) to subscribe to the selection completion event.2. In the callback, call [getSelectionContent](arkts-basicservices-selectionmanager-getselectioncontent-f.md#getSelectionContent) to obtain the selected text.3. Call [createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createPanel) to create a word selection panel.4. Call [setUiContent](arkts-basicservices-selectionmanager-panel-i.md#setUiContent) to load the page content.5. Call [moveToGlobalDisplay](arkts-basicservices-selectionmanager-panel-i.md#moveToGlobalDisplay) to move the panel to the specified position.6. Call [show](arkts-basicservices-selectionmanager-panel-i.md#show) to display the panel.7. Call [destroyPanel](arkts-basicservices-selectionmanager-destroypanel-f.md#destroyPanel) to destroy the panel.8. Call [off('selectionCompleted')](../../apis-user-authentication-kit/arkts-apis/arkts-userauthentication-userauth-authinstance-i.md#off) to unsubscribe from the selection completion event.

> **NOTE：**
> 
> - This module is supported only on PCs/2-in-1 devices. You can use
> **canIUse('SystemCapability.SelectionInput.Selection')** to check whether the current device supports this
> function.
> - APIs of this module can be called only by apps that integrate the extension ability for word selection. For
> details about how to implement the extension ability for word selection, see
> [SelectionExtensionAbility](arkts-basicservices-selectioninput-selectionextensionability-selectionextensionability-c.md#SelectionExtensionAbility).

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace selectionManager--><!--Device-unnamed-declare namespace selectionManager-End-->

**System capability:** SystemCapability.SelectionInput.Selection

## Modules to Import

```TypeScript
import { selectionManager } from '@kit.BasicServicesKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createpanel) | Creates a word selection panel, which is used to display the service-related operation UI or text processing result. After the panel is used, call [destroyPanel](arkts-basicservices-selectionmanager-destroypanel-f.md#destroyPanel) to destroy the panel and release resources. This API uses a promise to return the result.  Only one [MENU_PANEL](arkts-basicservices-selectioninput-selectionpanel-paneltype-e.md#PanelType) and one  [MAIN_PANEL](arkts-basicservices-selectioninput-selectionpanel-paneltype-e.md#PanelType) can be created for one word selection application. |
| [destroyPanel](arkts-basicservices-selectionmanager-destroypanel-f.md#destroypanel) | Destroys the word selection panel. This API is used together with [createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createPanel)to destroy the panel object created by **createPanel()**. This API uses a promise to return the result. |
| [getSelectionContent](arkts-basicservices-selectionmanager-getselectioncontent-f.md#getselectioncontent) | Obtains the content of the selected text. This API uses a promise to return the result. This API must be called in the  [on('selectionCompleted')](selectionManager.on(type: 'selectionCompleted', callback: Callback&lt;SelectionInfo&gt;))callback and is valid only after the word selection completion event is triggered. |
| [off](arkts-basicservices-selectionmanager-off-f.md#off) | Unsubscribes from the word selection completion event. This API is used together with  [on('selectionCompleted')](selectionManager.on(type: 'selectionCompleted', callback: Callback&lt;SelectionInfo&gt;)). |
| [offSelectionComplete](arkts-basicservices-selectionmanager-offselectioncomplete-f.md#offselectioncomplete) | Unregisters the callback used to listen for the word selection completion event. This API uses an asynchronous callback to return the result.  **ArkTS mode:** This API applies only to ArkTS-Sta. |
| [on](arkts-basicservices-selectionmanager-on-f.md#on) | Subscribes to the word selection completion event. This API is used together with  [off('selectionCompleted')](../../apis-user-authentication-kit/arkts-apis/arkts-userauthentication-userauth-authinstance-i.md#off).  [off('selectionCompleted')](../../apis-user-authentication-kit/arkts-apis/arkts-userauthentication-userauth-authinstance-i.md#off)is used to unsubscribe from the event. |
| [onSelectionComplete](arkts-basicservices-selectionmanager-onselectioncomplete-f.md#onselectioncomplete) | Registers a callback to listen for the word selection completion event. This API uses an asynchronous callback to return the result.  **ArkTS mode:** This API applies only to ArkTS-Sta. |

### Interfaces

| Name | Description |
| --- | --- |
| [Panel](arkts-basicservices-selectionmanager-panel-i.md) | Describes a **Panel** object, which is created using [createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createPanel). This method can be used to set, display, hide, and move the panel, as well as subscribe to events. It is applicable to scenarios where a custom operation UI needs to be displayed to users after word selection is complete. |
| [SelectionInfo](arkts-basicservices-selectionmanager-selectioninfo-i.md) | Defines the information of a word selection event. |

### Enums

| Name | Description |
| --- | --- |
| [SelectionType](arkts-basicservices-selectionmanager-selectiontype-e.md) | Enumerates the word selection types.  \| Name \| Value\| Description \|  \| ------------ \| -- \| ------------------ \|  \| MOUSE_MOVE \| 1 \| Word selection by sliding the mouse or touchpad. \|  \| DOUBLE_CLICK \| 2 \| Word selection by double-clicking the mouse or touchpad. \|  \| TRIPLE_CLICK \| 3 \| Word selection by triple-clicking the mouse or touchpad. \| |

