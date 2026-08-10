# ToolBarItem

可以使用**ToolBarItem**组件，通过[toolbar](docroot://reference/apis-arkui/arkui-ts/ts-universal-attributes-toolbar.md#toolbar)通用属性向标题栏中添加toolbar item。

> **说明**
>
> 该组件通常与[toolbar](docroot://reference/apis-arkui/arkui-ts/ts-universal-attributes-toolbar.md#toolbar)通用属性一起使用。

## 子组件

该组件可以包含单个子组件。

## ToolBarItem

```TypeScript
ToolBarItem(options?: ToolBarItemOptions)
```

默认在标题栏对应分栏开头位置创建工具栏项，分栏位置由绑定该[toolbar](docroot://reference/apis-arkui/arkui-ts/ts-universal-attributes-toolbar.md#toolbar)属性的组件所在分栏位置而定。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ToolBarItemInterface-(options?: ToolBarItemOptions): ToolBarItemAttribute--><!--Device-ToolBarItemInterface-(options?: ToolBarItemOptions): ToolBarItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ToolBarItemOptions](arkts-arkui-toolbaritemoptions-i.md) | No | ToolBarItem**的可选参数，包括[ToolBarItemPlacement]{@link ToolBarItemPlacement}类型的**placement**参数。<br>默认值：**placement: ToolBarItemPlacement.TOP_BAR_LEADING |

## Summary

- [ToolBarItemOptions](arkts-arkui-toolbaritem-toolbaritemoptions-i.md)
- [ToolBarItemPlacement](arkts-arkui-toolbaritem-toolbaritemplacement-e.md)
