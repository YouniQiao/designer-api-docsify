# OnMenuItemClickCallback

```TypeScript
export type OnMenuItemClickCallback = (menuItem: TextMenuItem, range: TextRange) => boolean
```

Invoke upon clicking an item, capable of intercepting the default system menu execution behavior.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnMenuItemClickCallback = (menuItem: TextMenuItem, range: TextRange) => boolean--><!--Device-unnamed-export type OnMenuItemClickCallback = (menuItem: TextMenuItem, range: TextRange) => boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| menuItem | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | current default menu.  |
| range | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | current selected range.  |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | - Return True, the event is consumed, false otherwise.  |

