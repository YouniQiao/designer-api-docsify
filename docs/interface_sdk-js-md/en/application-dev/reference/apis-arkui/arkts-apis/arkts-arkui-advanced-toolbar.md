# @ohos.arkui.advanced.ToolBar

## Modules to Import

```TypeScript
import { ToolBarOption, ItemState, ToolBar, ToolBarOptions, ToolBarModifier } from '@kit.ArkUI';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [ToolBarModifier](arkts-arkui-arkui-advanced-toolbar-toolbarmodifier-c.md) | Provides APIs for setting the height (**height**), background color (**backgroundColor**), left and right padding (**padding**, which only takes effect when there are fewer than five items) of the toolbar, and whether to display the pressed state effect (**stateEffect**). |
| [ToolBarOption](arkts-arkui-arkui-advanced-toolbar-toolbaroption-c.md) | Defines the content and attributes of a toolbar. |
| [ToolBarOptions](arkts-arkui-arkui-advanced-toolbar-toolbaroptions-c.md) | Inherits from Array&lt;[ToolBarOption](arkts-arkui-arkui-advanced-toolbar-toolbaroption-c.md)&gt;. |

### Structs

| Name | Description |
| --- | --- |
| [ToolBar](arkts-arkui-arkui-advanced-toolbar-toolbar-s.md) | The **Toolbar** component is designed to present a set of action options related to the current screen, displayed at the bottom of the screen. It can display up to five child components. If there are six or more child components, the first four are shown directly, and the additional ones are grouped under a **More** item on the rightmost side of the toolbar. @internal/component/ets/common} and  > [universal events](../../apis-arkui/arkts-components/arkts-arkui-common-attribute.md) configured, the compiler toolchain automatically  > generates an additional **__Common__** node and mounts the universal attributes and universal events on this node  > rather than the **ToolBar** component itself. As a result, the configured universal attributes and universal events  > may fail to take effect or behave as intended. For this reason, avoid using universal attributes and events with  > the **ToolBar** component. |

### Interfaces

| Name | Description |
| --- | --- |
| [ToolBarSymbolGlyphOptions](arkts-arkui-arkui-advanced-toolbar-toolbarsymbolglyphoptions-i.md) | Defines the icon symbol options. |

### Enums

| Name | Description |
| --- | --- |
| [ItemState](arkts-arkui-arkui-advanced-toolbar-itemstate-e.md) | Enumerates toolbar item states. |

