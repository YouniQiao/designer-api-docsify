# @ohos.selectionInput.selectionManager

This module provides word selection management capabilities, including creating, displaying, moving, hiding, and destroying panels, listening for word selection events using a mouse or touchpad, and retrieving the selected text. The typical usage process is as follows: 1. Call [on('selectionCompleted')](arkts-basicservices-selectionmanager-onselectioncompleted-f-sys.md#on_selectionCompleted) to subscribe to the selection completion event. 2. In the callback, call [getSelectionContent](arkts-basicservices-selectionmanager-getselectioncontent-f-sys.md#getSelectionContent-(System-API)) to obtain the selected text. 3. Call [createPanel](arkts-basicservices-selectionmanager-createpanel-f-sys.md#createPanel-(System-API)) to create a word selection panel. 4. Call [setUiContent](arkts-basicservices-selectionmanager-panel-i-sys.md#setUiContent) to load the page content. 5. Call [moveToGlobalDisplay](arkts-basicservices-selectionmanager-panel-i.md#moveToGlobalDisplay) to move the panel to the specified position. 6. Call [show](arkts-basicservices-selectionmanager-panel-i-sys.md#show) to display the panel. 7. Call [destroyPanel](arkts-basicservices-selectionmanager-destroypanel-f-sys.md#destroyPanel-(System-API)) to destroy the panel. 8. Call [off('selectionCompleted')](arkts-basicservices-selectionmanager-offselectioncompleted-f-sys.md#off_selectionCompleted) to unsubscribe from the selection completion event. > **NOTE：**> > - This module is supported only on PCs/2-in-1 devices. You can use > **canIUse('SystemCapability.SelectionInput.Selection')** to check whether the current device supports this > function. > - APIs of this module can be called only by apps that integrate the extension ability for word selection. For > details about how to implement the extension ability for word selection, see > [SelectionExtensionAbility](arkts-basicservices-selectioninput-selectionextensionability-selectionextensionability-c-sys.md#SelectionExtensionAbility-(System-API)).

**Since:** 24

**Deprecated since:** -1

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

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [offSelectionComplete](arkts-basicservices-selectionmanager-offselectioncomplete-f.md#offSelectionComplete) |
| [onSelectionComplete](arkts-basicservices-selectionmanager-onselectioncomplete-f.md#onSelectionComplete) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [createPanel](arkts-basicservices-selectionmanager-createpanel-f-sys.md#createPanel-(System-API)) |
| [destroyPanel](arkts-basicservices-selectionmanager-destroypanel-f-sys.md#destroyPanel-(System-API)) |
| [getSelectionContent](arkts-basicservices-selectionmanager-getselectioncontent-f-sys.md#getSelectionContent-(System-API)) |
| [off_selectionCompleted](arkts-basicservices-selectionmanager-offselectioncompleted-f-sys.md#off_selectionCompleted) |
| [on_selectionCompleted](arkts-basicservices-selectionmanager-onselectioncompleted-f-sys.md#on_selectionCompleted) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Panel](arkts-basicservices-selectionmanager-panel-i.md) |

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Panel](arkts-basicservices-selectionmanager-panel-i-sys.md) |
| [SelectionInfo](arkts-basicservices-selectionmanager-selectioninfo-i-sys.md) |
<!--DelEnd-->

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [SelectionType](arkts-basicservices-selectionmanager-selectiontype-e-sys.md) | Enumerates the word selection types. \| Name \| Value\| Description \| \| ------------ \| -- \| ------------------ \| \| MOUSE_MOVE \| 1 \| Word selection by sliding the mouse or touchpad. \| \| DOUBLE_CLICK \| 2 \| Word selection by double-clicking the mouse or touchpad. \| \| TRIPLE_CLICK \| 3 \| Word selection by triple-clicking the mouse or touchpad. \|
<!--DelEnd-->
