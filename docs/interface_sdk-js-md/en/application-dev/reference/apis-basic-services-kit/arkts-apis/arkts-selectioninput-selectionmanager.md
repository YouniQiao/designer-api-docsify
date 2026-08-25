# @ohos.selectionInput.selectionManager(Word Selection Management)

This module provides word selection management capabilities, including creating, displaying, moving, hiding, and destroying panels, listening for word selection events using a mouse or touchpad, and retrieving the selected text. The typical usage process is as follows:
1. Call [on('selectionCompleted')](arkts-basicservices-selectionmanager-on-f.md#onselectioncompleted) to subscribe to the selection completion event.
2. In the callback, call [getSelectionContent](arkts-basicservices-selectionmanager-getselectioncontent-f.md) to obtain the selected text.
3. Call [createPanel](arkts-basicservices-selectionmanager-createpanel-f.md) to create a word selection panel.
4. Call [setUiContent](arkts-basicservices-selectionmanager-panel-i.md#setuicontent) to load the page content.
5. Call [moveToGlobalDisplay](arkts-basicservices-selectionmanager-panel-i.md#movetoglobaldisplay) to move the panel to the specified position.
6. Call [show](arkts-basicservices-selectionmanager-panel-i.md#show) to display the panel.
7. Call [destroyPanel](arkts-basicservices-selectionmanager-destroypanel-f.md) to destroy the panel.
8. Call [off('selectionCompleted')](arkts-basicservices-selectionmanager-off-f.md#offselectioncompleted) to unsubscribe from the selection completion event.

> **NOTE：**&gt;
> - This module is supported only on PCs/2-in-1 devices. You can use
> **canIUse('SystemCapability.SelectionInput.Selection')** to check whether the current device supports this
> function.
> - APIs of this module can be called only by apps that integrate the extension ability for word selection. For
> details about how to implement the extension ability for word selection, see
> [SelectionExtensionAbility](arkts-basicservices-selectioninput-selectionextensionability-selectionextensionability-c.md).

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.SelectionInput.Selection

## Modules to Import

```TypeScript
import { selectionManager } from '@kit.BasicServicesKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [createPanel(Word Selection Management)](arkts-basicservices-selectionmanager-createpanel-f.md) |
| [destroyPanel(Word Selection Management)](arkts-basicservices-selectionmanager-destroypanel-f.md) |
| [getSelectionContent(Word Selection Management)](arkts-basicservices-selectionmanager-getselectioncontent-f.md) |
| [off(Word Selection Management)](arkts-basicservices-selectionmanager-off-f.md#offselectioncompleted) |
| [offSelectionComplete(Word Selection Management)](arkts-basicservices-selectionmanager-offselectioncomplete-f.md) |
| [on(Word Selection Management)](arkts-basicservices-selectionmanager-on-f.md#onselectioncompleted) |
| [onSelectionComplete(Word Selection Management)](arkts-basicservices-selectionmanager-onselectioncomplete-f.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Panel(Word Selection Management)](arkts-basicservices-selectionmanager-panel-i.md) |
| [SelectionInfo(Word Selection Management)](arkts-basicservices-selectionmanager-selectioninfo-i.md) |

<!--Del-->
### Interfaces(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Panel(Word Selection Management)](arkts-basicservices-selectionmanager-panel-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [SelectionType(Word Selection Management)](arkts-basicservices-selectionmanager-selectiontype-e.md) | Enumerates the word selection types.  \| Name \| Value\| Description \| \| ------------ \| -- \| ------------------ \| \| MOUSE_MOVE \| 1 \| Word selection by sliding the mouse or touchpad. \| \| DOUBLE_CLICK \| 2 \| Word selection by double-clicking the mouse or touchpad. \| \| TRIPLE_CLICK \| 3 \| Word selection by triple-clicking the mouse or touchpad. \|
