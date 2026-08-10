# OnCreateMenuCallback

```TypeScript
type OnCreateMenuCallback = (menuItems: Array<TextMenuItem>) => Array<TextMenuItem>
```

菜单创建时触发。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-unnamed-type OnCreateMenuCallback = (menuItems: Array<TextMenuItem>) => Array<TextMenuItem>--><!--Device-unnamed-type OnCreateMenuCallback = (menuItems: Array<TextMenuItem>) => Array<TextMenuItem>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| menuItems | Array&lt;TextMenuItem&gt; | Yes | 当前显示的菜单项。<br/>**说明：**<br/>对默认菜单项的名称、图标、快捷键提示修改不生效。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;TextMenuItem&gt; | 处理后的菜单项。 |

