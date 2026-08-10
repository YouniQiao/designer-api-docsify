# MenuItemGroup

该组件用于展示MenuItem的分组，支持设置分组的标题和尾部信息，用于组织和管理菜单项的分类结构。适用于需要在菜单中按类别组织多个菜单项的场景，通过分组清晰地展示菜单的层次结构，提升菜单的可读性和用户体验。

> **说明：**

> - 该组件从API版本26.0.0开始支持[WithTheme]{@link with_theme}。

## 子组件

包含[MenuItem]{@link menu_item}子组件。

## MenuItemGroup

```TypeScript
MenuItemGroup(value?: MenuItemGroupOptions)
```

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-MenuItemGroupInterface-(value?: MenuItemGroupOptions): MenuItemGroupAttribute--><!--Device-MenuItemGroupInterface-(value?: MenuItemGroupOptions): MenuItemGroupAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [MenuItemGroupOptions](arkts-arkui-menuitemgroupoptions-i.md) | No | 设置MenuItemGroup的标题和尾部信息。<br/> 未设置时，不显示标题和尾部信息。 |

## Summary

- [MenuItemGroupOptions](arkts-arkui-menuitemgroup-menuitemgroupoptions-i.md)
