# @ohos.selectionInput.selectionManager

This module provides word selection management capabilities, including creating, displaying, moving, hiding, and destroying windows, listening for word selection events, and retrieving the selected text. > **NOTE** > - This module is supported only on PCs/2-in-1 devices. > - APIs of this module can be called only by applications that integrate the ExtensionAbility for word selection.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

<!--Device-unnamed-declare namespace selectionManager--><!--Device-unnamed-declare namespace selectionManager-End-->

**System capability:** SystemCapability.SelectionInput.Selection

## Summary

### Functions

| Name | Description |
| --- | --- |
| [createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createpanel) | Creates a word selection panel. This API uses a promise to return the result. Only one [MENU\_\_\_ESCAPED\_UNDERSCORE\_\_\_PANEL]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ and one [MAIN\_\_\_ESCAPED\_UNDERSCORE\_\_\_PANEL]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ can be created for one word selection application. |
| [destroyPanel](arkts-basicservices-selectionmanager-destroypanel-f.md#destroypanel) | Destroys the word selection panel. This API uses a promise to return the result. |
| [getSelectionContent](arkts-basicservices-selectionmanager-getselectioncontent-f.md#getselectioncontent) | Obtains this selected text content. This API uses a promise to return the result. |
| [off](arkts-basicservices-selectionmanager-off-f.md#off) | Unregisters the callback used to listen for the word selection completion event. This API uses an asynchronous callback to return the result. |
| [offSelectionComplete](arkts-basicservices-selectionmanager-offselectioncomplete-f.md#offselectioncomplete) | Unregisters the callback used to listen for the word selection completion event. This API uses an asynchronous callback to return the result. |
| [on](arkts-basicservices-selectionmanager-on-f.md#on) | Registers a callback to listen for the word selection completion event. This API uses an asynchronous callback to return the result. |
| [onSelectionComplete](arkts-basicservices-selectionmanager-onselectioncomplete-f.md#onselectioncomplete) | Registers a callback to listen for the word selection completion event. This API uses an asynchronous callback to return the result. |

### Interfaces

| Name | Description |
| --- | --- |
| [Panel](arkts-basicservices-selectionmanager-panel-i.md) | Represents the word selection panel. |
| [SelectionInfo](arkts-basicservices-selectionmanager-selectioninfo-i.md) | Defines the information of a word selection event. |

### Enums

| Name | Description |
| --- | --- |
| [SelectionType](arkts-basicservices-selectionmanager-selectiontype-e.md) | Enumerates the operations for selecting words. |

