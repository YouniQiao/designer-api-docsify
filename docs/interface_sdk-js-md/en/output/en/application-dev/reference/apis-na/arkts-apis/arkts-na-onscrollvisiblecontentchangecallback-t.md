# OnScrollVisibleContentChangeCallback

```TypeScript
export type OnScrollVisibleContentChangeCallback = (start: VisibleListContentInfo, end: VisibleListContentInfo) => void
```

Called when a child component enters or leaves the list display area.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnScrollVisibleContentChangeCallback = (start: VisibleListContentInfo, end: VisibleListContentInfo) => void--><!--Device-unnamed-export type OnScrollVisibleContentChangeCallback = (start: VisibleListContentInfo, end: VisibleListContentInfo) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Information about the currently displayed first list item or list item group.  |
| end | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Information about the currently displayed last list item or list item group.  |

