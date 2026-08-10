# OnMenuItemClickWithTextCallback

```TypeScript
export type OnMenuItemClickWithTextCallback = (menuItem: TextMenuItem, value: string) => boolean
```

点击菜单项时触发，可拦截系统默认菜单项（如复制、粘贴菜单项）的执行行为。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnMenuItemClickWithTextCallback = (menuItem: TextMenuItem, value: string) => boolean--><!--Device-unnamed-export type OnMenuItemClickWithTextCallback = (menuItem: TextMenuItem, value: string) => boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| menuItem | [TextMenuItem](arkts-arkui-textmenuitem-i.md) | Yes | 当前点击的菜单项。 |
| value | string | Yes | 选中文本内容。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 菜单项点击事件的处理结果。返回true表示事件已处理，返回false表示未处理。 |

