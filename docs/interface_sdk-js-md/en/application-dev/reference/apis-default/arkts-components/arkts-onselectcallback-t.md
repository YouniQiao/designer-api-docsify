# OnSelectCallback

```TypeScript
export type OnSelectCallback = (index: int, selectStr: string) => void
```

Callback of selecting an item from the select event.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnSelectCallback = (index: int, selectStr: string) => void--><!--Device-unnamed-export type OnSelectCallback = (index: int, selectStr: string) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | The index of the selected item. |
| selectStr | string | Yes | The value of the selected item. |

