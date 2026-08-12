# @ohos.selectionInput.SelectionPanel(划词面板)

划词面板是用户选中文本后弹出的操作面板，适用于需要为选中文本提供翻译、搜索等快捷操作功能的场景，帮助开发者快速集成划词操作能力，提升用户交互体验。面板采用两级架构设计：菜单面板（MENU_PANEL）为一级面板，展示当前应用可提供的功
 能入口（如翻译、搜索等）；主面板（MAIN_PANEL）为二级面板，在用户点击菜单面板中的功能按钮后弹出，展示具体的功能结果。本模块提供划词面板的属性信息和类型，开发者可通过[PanelInfo](arkts-basicservices-selectioninput-selectionpanel-panelinfo-i.md#PanelInfo)设定
 面板的位置和尺寸，通过[PanelType](arkts-basicservices-selectioninput-selectionpanel-paneltype-e.md#PanelType)指定面板类型。划词面板的创建与显示接口请参见
 [createPanel](arkts-basicservices-selectionmanager-createpanel-f.md#createPanel)、
 [show](arkts-basicservices-selectionmanager-panel-i.md#show)。
 > **说明：**
 >
 > - 本模块仅支持PC/2in1设备。开发者可通过canIUse('SystemCapability.SelectionInput.Selection')判断当前设备是否支持该功能。


## 汇总

### 接口

| 名称 |
| --- |
| [PanelInfo](arkts-basicservices-selectioninput-selectionpanel-panelinfo-i.md) |

### 枚举

| 名称 |
| --- |
| [PanelType](arkts-basicservices-selectioninput-selectionpanel-paneltype-e.md) |
