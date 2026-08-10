# MenuItem

用来展示菜单中具体的菜单选项。

> **说明：**

> - 该组件从API版本26.0.0开始支持[WithTheme]{@link with_theme}。

## 子组件

无

## MenuItem

```TypeScript
MenuItem(value?: MenuItemOptions | CustomBuilder)
```

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-MenuItemInterface-(value?: MenuItemOptions | CustomBuilder): MenuItemAttribute--><!--Device-MenuItemInterface-(value?: MenuItemOptions | CustomBuilder): MenuItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [MenuItemOptions](../arkts-apis/arkts-arkui-menuitem-menuitemoptions-i.md) \| CustomBuilder | No | 包含设置MenuItem的各项信息。需要使用标准菜单项配置（如起始图标、内容、标签等）时选择MenuItemOptions；需要自定义菜单项的显示内容和布局时选择CustomBuilder。如果不传该参数，则创建空的MenuItem对象。 |

## Summary

- [MenuItemOptions](arkts-arkui-menuitem-menuitemoptions-i.md)
