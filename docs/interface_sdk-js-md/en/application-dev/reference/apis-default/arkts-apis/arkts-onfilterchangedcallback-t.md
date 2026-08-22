# OnFilterChangedCallback

```TypeScript
declare type OnFilterChangedCallback = (filterResults: Array<FilterResult>) => void
```

Callback method after a user clicks a filter item.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare type OnFilterChangedCallback = (filterResults: Array<FilterResult>) => void--><!--Device-unnamed-declare type OnFilterChangedCallback = (filterResults: Array<FilterResult>) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| filterResults | Array&lt;[FilterResult](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-filter-filterresult-c.md)&gt; | Yes | The result of filter. |

