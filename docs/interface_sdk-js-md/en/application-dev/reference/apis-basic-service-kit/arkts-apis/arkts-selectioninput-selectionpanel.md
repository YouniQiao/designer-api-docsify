# @ohos.selectionInput.SelectionPanel(Word Selection Panel)

/*
 Copyright (c) 2025 Huawei Device Co., Ltd.
 Licensed under the Apache License, Version 2.0 (the "License"),
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 /
 The text selection panel is an operation panel that pops up after a user selects text. This module is applicable when
 quick operations such as translation and search need to be provided for the selected text. This helps developers
 quickly integrate the text selection capability and improve user interaction experience. The panel adopts a two-level
 architecture design. The menu panel (**MENU_PANEL**) is the level-1 panel, which displays the function entries (such
 as translation and search) provided by the current app. The main panel (**MAIN_PANEL**) is the level-2 panel, which
 pops up after a user taps a function button on the menu panel and displays the specific function result. This module
 provides the attributes and types of the word selection panel. You can use [PanelInfo](arkts-basicservices-selectioninput-selectionpanel-panelinfo-i-sys.md#PanelInfo-(System-API)) to set the
 position and size of the panel and use [PanelType](arkts-basicservices-selectioninput-selectionpanel-paneltype-e-sys.md#PanelType-(System-API)) to specify the panel type.
 [createPanel](arkts-basicservices-selectionmanager-createpanel-f-sys.md#createPanel-(System-API)) and
 [show](arkts-basicservices-selectionmanager-panel-i-sys.md#show) are used to create and display the
 word selection panel.
 > **NOTE**
 >
 > - This module is supported only on PCs/2-in-1 devices. You can use **canIUse('
 > SystemCapability.SelectionInput.Selection')** to check whether the current device supports this function.


## Modules to Import

```TypeScript
import { PanelInfo } from 'PanelInfo';
import { PanelType } from 'PanelType';
```

## Summary

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [PanelInfo](arkts-basicservices-selectioninput-selectionpanel-panelinfo-i-sys.md) | Defines attributes of the word selection panel, including its type, position, and size. You can specify the panel type (menu panel or main panel) using **panelType**, set the coordinates of the upper left corner of the panel using **x** and **y**, and set the panel size using **width** and **height**. These attributes collectively define the display form of the panel. |
<!--DelEnd-->

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [PanelType](arkts-basicservices-selectioninput-selectionpanel-paneltype-e-sys.md) | Enumerates the word selection panel types, which defines the two-level architecture of the panel: menu panel (level 1) and main panel (level 2). |
<!--DelEnd-->

