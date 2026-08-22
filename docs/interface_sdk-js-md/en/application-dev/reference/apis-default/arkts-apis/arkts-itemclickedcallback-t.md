# ItemClickedCallback

```TypeScript
export type ItemClickedCallback = (itemInfo: ItemInfo, clickType: ClickType) => boolean
```

The callback of itemClicked event

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type ItemClickedCallback = (itemInfo: ItemInfo, clickType: ClickType) => boolean--><!--Device-unnamed-export type ItemClickedCallback = (itemInfo: ItemInfo, clickType: ClickType) => boolean-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| itemInfo | [ItemInfo](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-filephotopickercomponent-iteminfo-c.md) | Yes |  |
| clickType | [ClickType](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-filephotopickercomponent-clicktype-e.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | - |

