# @ohos.selectionInput.SelectionPanel(Word Selection Panel)

The text selection panel is an operation panel that pops up after a user selects text. This module is applicable when
 quick operations such as translation and search need to be provided for the selected text. This helps developers
 quickly integrate the text selection capability and improve user interaction experience. The panel adopts a two-level
 architecture design. The menu panel (**MENU_PANEL**) is the level-1 panel, which displays the function entries (such
 as translation and search) provided by the current app. The main panel (**MAIN_PANEL**) is the level-2 panel, which
 pops up after a user taps a function button on the menu panel and displays the specific function result. This module
 provides the attributes and types of the word selection panel. You can use [PanelInfo](arkts-basicservices-selectioninput-selectionpanel-panelinfo-i.md) to set the
 position and size of the panel and use [PanelType](arkts-basicservices-selectioninput-selectionpanel-paneltype-e.md) to specify the panel type.
 [createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createpanel) and
 [show](arkts-basicservices-selectionmanager-panel-i.md#show) are used to create and display the
 word selection panel.
 > **NOTE**
 >
 > - This module is supported only on PCs/2-in-1 devices. You can use **canIUse('
 > SystemCapability.SelectionInput.Selection')** to check whether the current device supports this function.


## Modules to Import

```TypeScript
import { PanelInfo, PanelType } from 'kits/@kit.BasicServicesKit';
```

## Summary

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [PanelInfo](arkts-basicservices-selectioninput-selectionpanel-panelinfo-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [PanelType](arkts-basicservices-selectioninput-selectionpanel-paneltype-e.md) |
