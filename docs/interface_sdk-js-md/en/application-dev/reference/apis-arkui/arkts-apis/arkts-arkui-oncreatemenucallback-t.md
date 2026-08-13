# OnCreateMenuCallback

```TypeScript
type OnCreateMenuCallback = (menuItems: Array<TextMenuItem>) => Array<TextMenuItem>
```

Callback function when the selection menu create.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-unnamed-type OnCreateMenuCallback = (menuItems: Array<TextMenuItem>) => Array<TextMenuItem>--><!--Device-unnamed-type OnCreateMenuCallback = (menuItems: Array<TextMenuItem>) => Array<TextMenuItem>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| menuItems | Array&lt;[TextMenuItem](arkts-arkui-textmenuitem-i.md)&gt; | Yes | currently displayed menu items. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[TextMenuItem](arkts-arkui-textmenuitem-i.md)&gt; | Return the menu items will displayed after operations. |

