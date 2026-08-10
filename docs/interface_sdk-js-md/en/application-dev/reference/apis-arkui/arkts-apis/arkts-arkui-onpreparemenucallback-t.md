# OnPrepareMenuCallback

```TypeScript
type OnPrepareMenuCallback = (menuItems: Array<TextMenuItem>) => Array<TextMenuItem>
```

当文本选择区域变化后显示菜单之前触发该回调，可在该回调中进行菜单数据设置。入参和返回值只包含一级菜单项，不包含二级菜单项。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-unnamed-type OnPrepareMenuCallback = (menuItems: Array<TextMenuItem>) => Array<TextMenuItem>--><!--Device-unnamed-type OnPrepareMenuCallback = (menuItems: Array<TextMenuItem>) => Array<TextMenuItem>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| menuItems | Array&lt;TextMenuItem&gt; | Yes | 将要显示的菜单项。 <br>**说明：** <br>对默认菜单项的名称、图标、快捷键提示修改不生效。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;TextMenuItem&gt; | 处理后的菜单项。 |

