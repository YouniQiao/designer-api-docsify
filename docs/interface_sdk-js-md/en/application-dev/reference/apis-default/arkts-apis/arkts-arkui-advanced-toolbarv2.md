# @ohos.arkui.advanced.ToolBarV2

## Modules to Import

```TypeScript
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [ToolBarV2Item](arkts-arkui-advanced-toolbarv2-toolbarv2item-c.md) | Defines an item in the toolbar. |
| [ToolBarV2ItemImage](arkts-arkui-advanced-toolbarv2-toolbarv2itemimage-c.md) | Defines the icon content of a toolbar item. |
| [ToolBarV2ItemText](arkts-arkui-advanced-toolbarv2-toolbarv2itemtext-c.md) | Defines the text of a toolbar item. |
| [ToolBarV2Modifier](arkts-arkui-advanced-toolbarv2-toolbarv2modifier-c.md) | Provides APIs for setting the height (**height**), background color (**backgroundColor**), left and right padding (**padding**, which only takes effect when there are fewer than five items) of the toolbar, and whether to display the pressed state effect (**stateEffect**). |
| [ToolBarV2SymbolGlyph](arkts-arkui-advanced-toolbarv2-toolbarv2symbolglyph-c.md) | Defines the icon symbol options. |

### Structs

| Name | Description |
| --- | --- |
| [ToolBarV2](arkts-arkui-advanced-toolbarv2-toolbarv2-s.md) | The **Toolbar** component is designed to present a set of action options related to the current screen, displayed at the bottom of the screen. It can display up to five child components. If there are six or more child components, the first four are shown directly, and the additional ones are grouped under a **More** item on the rightmost side of the toolbar.This component is implemented based on [state management V2](../../../ui/state-management/arkts-state-management-overview.md#state-management-v2). Compared with [state management V1](../../../ui/state-management/arkts-state-management-overview.md#state-management-v1), V2 offers a higher level of observation and management over data objects beyond the component level. You can now more easily manage toolbar data and states with greater flexibility, leading to faster UI updates. |

### Interfaces

| Name | Description |
| --- | --- |
| [ToolBarV2ItemImageOptions](arkts-arkui-advanced-toolbarv2-toolbarv2itemimageoptions-i.md) | Defines the options for initializing a **ToolBarV2ItemImage** object. |
| [ToolBarV2ItemOptions](arkts-arkui-advanced-toolbarv2-toolbarv2itemoptions-i.md) | Defines the options for initializing a **ToolBarV2Item** object. |
| [ToolBarV2ItemTextOptions](arkts-arkui-advanced-toolbarv2-toolbarv2itemtextoptions-i.md) | Defines the options for initializing a **ToolBarV2ItemText** object. |
| [ToolBarV2SymbolGlyphOptions](arkts-arkui-advanced-toolbarv2-toolbarv2symbolglyphoptions-i.md) | Defines the options for initializing a **ToolBarV2SymbolGlyph** object. |

### Enums

| Name | Description |
| --- | --- |
| [ToolBarV2ItemState](arkts-arkui-advanced-toolbarv2-toolbarv2itemstate-e.md) | Enumerates the states of the toolbar item.  \| Name \| Value\| Description \| \| -------- \| - \| --------------- \| \| ENABLE \| 1 \| The toolbar item is enabled. \| \| DISABLE \| 2 \| The toolbar item is disabled. \| \| ACTIVATE \| 3 \| The toolbar item is activated.\| |

### Types

| Name | Description |
| --- | --- |
| [ToolBarV2ItemAction](arkts-toolbarv2itemaction-t.md) | Defines the callback for the click event of a toolbar item. |
| [ToolBarV2ItemIconType](arkts-toolbarv2itemicontype-t.md) | Defines the icon type of ToolBarV2 item. |

