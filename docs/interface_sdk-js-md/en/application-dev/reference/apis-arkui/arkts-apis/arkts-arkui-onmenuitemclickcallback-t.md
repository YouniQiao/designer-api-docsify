# OnMenuItemClickCallback

```TypeScript
export type OnMenuItemClickCallback = (menuItem: TextMenuItem, range: TextRange) => boolean
```

菜单项功能函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnMenuItemClickCallback = (menuItem: TextMenuItem, range: TextRange) => boolean--><!--Device-unnamed-export type OnMenuItemClickCallback = (menuItem: TextMenuItem, range: TextRange) => boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| menuItem | [TextMenuItem](arkts-arkui-textmenuitem-i.md) | Yes | 菜单项。<br/>**说明：** <br/>从API version 23开始，对于具备可展开二级菜单能力的一级菜单项，例如自动填充，仅执行系统默认逻辑，不会执行用 户自定义逻辑。 |
| range | [TextRange](arkts-arkui-textrange-i.md) | Yes | 选中的文本信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 菜单项的执行逻辑。<br/>返回为true，拦截系统默认逻辑，仅执行自定义逻辑。<br/>返回为false，先执行自定义逻辑，再执行系统逻辑。 |

