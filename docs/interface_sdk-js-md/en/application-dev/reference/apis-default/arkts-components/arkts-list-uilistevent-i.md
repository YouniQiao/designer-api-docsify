# UIListEvent

Defines a UIListEvent which is used to set different common event to target component.

**Inheritance/Implementation:** UIListEvent extends UIScrollableCommonEvent

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export declare interface UIListEvent--><!--Device-unnamed-export declare interface UIListEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setOnDidScroll

```TypeScript
setOnDidScroll(callback: OnScrollCallback | undefined): void
```

Set or reset the callback which is triggered when List view did scroll.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIListEvent-setOnDidScroll(callback: OnScrollCallback | undefined): void--><!--Device-UIListEvent-setOnDidScroll(callback: OnScrollCallback | undefined): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnScrollCallback](../../apis-arkui/arkts-components/arkts-arkui-onscrollcallback-t.md) \| undefined | Yes | callback function, triggered when the List view did scroll. Passing undefined will unregister the callback. |

## setOnScrollIndex

```TypeScript
setOnScrollIndex(callback: OnListScrollIndexCallback | undefined): void
```

Set or reset the callback which is triggered when the start, end, or center positions of the display change.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIListEvent-setOnScrollIndex(callback: OnListScrollIndexCallback | undefined): void--><!--Device-UIListEvent-setOnScrollIndex(callback: OnListScrollIndexCallback | undefined): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnListScrollIndexCallback](arkts-onlistscrollindexcallback-t.md) \| undefined | Yes | callback function, triggered when the start, end, or center positions of the display change. Passing undefined will unregister the callback. |

## setOnScrollVisibleContentChange

```TypeScript
setOnScrollVisibleContentChange(callback: OnScrollVisibleContentChangeCallback | undefined): void
```

Set or reset the callback which is triggered when the list visible content changes.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIListEvent-setOnScrollVisibleContentChange(callback: OnScrollVisibleContentChangeCallback | undefined): void--><!--Device-UIListEvent-setOnScrollVisibleContentChange(callback: OnScrollVisibleContentChangeCallback | undefined): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnScrollVisibleContentChangeCallback](arkts-onscrollvisiblecontentchangecallback-t.md) \| undefined | Yes | callback function, triggered when the list visible content changes. Passing undefined will unregister the callback. |

## setOnWillScroll

```TypeScript
setOnWillScroll(callback: OnWillScrollCallback | undefined): void
```

Set or reset the callback which is triggered when the List will scroll.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIListEvent-setOnWillScroll(callback: OnWillScrollCallback | undefined): void--><!--Device-UIListEvent-setOnWillScroll(callback: OnWillScrollCallback | undefined): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnWillScrollCallback](../../apis-arkui/arkts-components/arkts-arkui-onwillscrollcallback-t.md) \| undefined | Yes | The callback will be triggered when the List will scroll. Passing undefined will unregister the callback. |

