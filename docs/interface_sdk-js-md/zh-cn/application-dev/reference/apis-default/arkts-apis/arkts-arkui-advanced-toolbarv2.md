# @ohos.arkui.advanced.ToolBarV2

## 导入模块

```TypeScript
```

## 汇总

### 类

| 名称 | 说明 |
| --- | --- |
| [ToolBarV2Item](arkts-arkui-advanced-toolbarv2-toolbarv2item-c.md) | 定义工具栏子项。 |
| [ToolBarV2ItemImage](arkts-arkui-advanced-toolbarv2-toolbarv2itemimage-c.md) | 定义工具栏子项的普通图标。 |
| [ToolBarV2ItemText](arkts-arkui-advanced-toolbarv2-toolbarv2itemtext-c.md) | 定义工具栏子项的文本。 |
| [ToolBarV2Modifier](arkts-arkui-advanced-toolbarv2-toolbarv2modifier-c.md) | ToolBarV2Modifier提供设置工具栏高度(height)、背景色(backgroundColor)、左右内边距（padding，仅在子项数量小于5个时生效）、是否显示按压态（stateEffect）的方法。 |
| [ToolBarV2SymbolGlyph](arkts-arkui-advanced-toolbarv2-toolbarv2symbolglyph-c.md) | ToolBarV2SymbolGlyph定义Symbol图标的属性。 |

### 结构体

| 名称 | 说明 |
| --- | --- |
| [ToolBarV2](arkts-arkui-advanced-toolbarv2-toolbarv2-s.md) | 工具栏用于展示针对当前界面内容的操作选项，在界面底部显示，适用于需要为用户提供快速操作入口的场景。底部最多显示5个入口，超过则收纳入“更多”子项中，在最右侧显示。适用于需要对当前页面内容进行快捷操作的场景，可帮助用户快速访问常用功能， 提升操作效率。该组件基于[状态管理（V2）](../../../ui/state-management/arkts-state-management-overview.md#状态管理v2)实现，相较于 [状态管理（V1）](../../../ui/state-management/arkts-state-management-overview.md#状态管理v1)，状态管理（V2）增强了对数据对象的深度观察与管理能力，不再局限于组 件层级。借助状态管理（V2），开发者可以通过该组件更灵活地控制工具栏的数据和状态，实现更高效的用户界面刷新。 |

### 接口

| 名称 | 说明 |
| --- | --- |
| [ToolBarV2ItemImageOptions](arkts-arkui-advanced-toolbarv2-toolbarv2itemimageoptions-i.md) | 用于构建ToolBarV2ItemImage对象。 |
| [ToolBarV2ItemOptions](arkts-arkui-advanced-toolbarv2-toolbarv2itemoptions-i.md) | 用于构建ToolBarV2Item对象。 |
| [ToolBarV2ItemTextOptions](arkts-arkui-advanced-toolbarv2-toolbarv2itemtextoptions-i.md) | 用于构建ToolBarV2ItemText对象。 |
| [ToolBarV2SymbolGlyphOptions](arkts-arkui-advanced-toolbarv2-toolbarv2symbolglyphoptions-i.md) | ToolBarV2SymbolGlyphOptions定义Symbol图标的属性。 |

### 枚举

| 名称 | 说明 |
| --- | --- |
| [ToolBarV2ItemState](arkts-arkui-advanced-toolbarv2-toolbarv2itemstate-e.md) | 工具栏子项状态枚举。  \| 名称 \| 值 \| 说明 \| \| -------- \| - \| --------------- \| \| ENABLE \| 1 \| 工具栏子项为正常可点击状态。 \| \| DISABLE \| 2 \| 工具栏子项为不可点击状态。 \| \| ACTIVATE \| 3 \| 工具栏子项为激活状态，可点击。 \| |

### 类型

| 名称 | 说明 |
| --- | --- |
| [ToolBarV2ItemAction](arkts-toolbarv2itemaction-t.md) | 定义ToolBarV2Item的动作回调结构体。 |
| [ToolBarV2ItemIconType](arkts-toolbarv2itemicontype-t.md) | Defines the icon type of ToolBarV2 item. |

