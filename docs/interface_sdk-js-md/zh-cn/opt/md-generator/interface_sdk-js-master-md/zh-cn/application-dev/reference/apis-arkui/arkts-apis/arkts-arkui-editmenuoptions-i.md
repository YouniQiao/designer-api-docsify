# EditMenuOptions

编辑菜单选项

**起始版本：** 12

<!--Device-unnamed-declare interface EditMenuOptions--><!--Device-unnamed-declare interface EditMenuOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onCreateMenu

```TypeScript
onCreateMenu(menuItems: Array<TextMenuItem>): Array<TextMenuItem>
```

在菜单创建时触发该回调，可在该回调中进行菜单数据设置。入参和返回值只包含一级菜单项，不包含二级菜单项。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-EditMenuOptions-onCreateMenu(menuItems: Array<TextMenuItem>): Array<TextMenuItem>--><!--Device-EditMenuOptions-onCreateMenu(menuItems: Array<TextMenuItem>): Array<TextMenuItem>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| menuItems | Array&lt;TextMenuItem&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;TextMenuItem&gt; |

## onMenuItemClick

```TypeScript
onMenuItemClick(menuItem: TextMenuItem, range: TextRange): boolean
```

在菜单项被点击时触发该回调，用于处理菜单项的点击行为。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-EditMenuOptions-onMenuItemClick(menuItem: TextMenuItem, range: TextRange): boolean--><!--Device-EditMenuOptions-onMenuItemClick(menuItem: TextMenuItem, range: TextRange): boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| menuItem | [TextMenuItem](arkts-arkui-textmenuitem-i.md) | 是 |
| range | [TextRange](arkts-arkui-textrange-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## onPrepareMenu

```TypeScript
onPrepareMenu?: OnPrepareMenuCallback
```

当文本选择区域变化后显示菜单之前触发该回调，可在该回调中进行菜单数据设置。

与[onCreateMenu](arkts-arkui-editmenuoptions-i.md#oncreatemenu)功能相似但触发时机不同：onCreateMenu在菜单创建时触发，适用于初始化菜单项；本接口在每次选择区域变化后、菜单显示前触发，适用于根据选择内容动态调整菜单。两者可同时使用。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-EditMenuOptions-onPrepareMenu?: OnPrepareMenuCallback--><!--Device-EditMenuOptions-onPrepareMenu?: OnPrepareMenuCallback-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
