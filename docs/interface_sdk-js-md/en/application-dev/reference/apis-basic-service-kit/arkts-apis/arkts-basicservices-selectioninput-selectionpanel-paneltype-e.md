# PanelType

划词面板类型枚举，定义面板的两级架构：菜单面板（一级）和主面板（二级）。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

<!--Device-unnamed-export enum PanelType--><!--Device-unnamed-export enum PanelType-End-->

**System capability:** SystemCapability.SelectionInput.Selection

## MENU_PANEL

```TypeScript
MENU_PANEL = 1
```

菜单面板为一级面板，显示当前应用可以提供的功能，如翻译、搜索等。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanelType-MENU_PANEL = 1--><!--Device-PanelType-MENU_PANEL = 1-End-->

**System capability:** SystemCapability.SelectionInput.Selection

## MAIN_PANEL

```TypeScript
MAIN_PANEL = 2
```

主面板为二级面板，当用户点击菜单面板中的功能按钮时弹出，展示具体的翻译或搜索结果等内容。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanelType-MAIN_PANEL = 2--><!--Device-PanelType-MAIN_PANEL = 2-End-->

**System capability:** SystemCapability.SelectionInput.Selection

