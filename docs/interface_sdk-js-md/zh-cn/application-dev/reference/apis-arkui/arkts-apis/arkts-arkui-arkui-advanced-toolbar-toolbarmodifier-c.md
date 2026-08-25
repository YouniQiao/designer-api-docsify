# ToolBarModifier

ToolBarModifier提供设置工具栏高度(height)、背景色(backgroundColor)、左右内边距（padding，仅在子项数量小于5个时生效）、是否显示按压态（stateEffect）的方法。

**起始版本：** 13

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { ItemState, ToolBar, ToolBarOption, ToolBarOptions, ToolBarModifier } from 'kits/@kit.ArkUI';
```

## backgroundColor

```TypeScript
backgroundColor(backgroundColor: ResourceColor): ToolBarModifier
```

设置工具栏背景色的接口。

**起始版本：** 13

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [backgroundColor](#backgroundcolor) | [ResourceColor](arkts-arkui-resourcecolor-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [ToolBarModifier](arkts-arkui-arkui-advanced-toolbar-toolbarmodifier-c.md) |

## height

```TypeScript
height(height: LengthMetrics): ToolBarModifier
```

设置工具栏高度的接口，此高度不包含分割线高度。

**起始版本：** 13

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [height](#height) | [LengthMetrics](arkts-arkui-lengthmetrics-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [ToolBarModifier](arkts-arkui-arkui-advanced-toolbar-toolbarmodifier-c.md) |

## padding

```TypeScript
padding(padding: LengthMetrics): ToolBarModifier
```

设置工具栏左右内边距的接口。

**起始版本：** 13

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [padding](#padding) | [LengthMetrics](arkts-arkui-lengthmetrics-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [ToolBarModifier](arkts-arkui-arkui-advanced-toolbar-toolbarmodifier-c.md) |

## stateEffect

```TypeScript
stateEffect(stateEffect: boolean): ToolBarModifier
```

设置是否显示按压态效果的接口。

**起始版本：** 13

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本13开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [stateEffect](#stateeffect) | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| [ToolBarModifier](arkts-arkui-arkui-advanced-toolbar-toolbarmodifier-c.md) |
