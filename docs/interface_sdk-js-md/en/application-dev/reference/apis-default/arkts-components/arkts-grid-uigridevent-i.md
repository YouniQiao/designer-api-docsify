# UIGridEvent

Defines a UIGridEvent which is used to set event to target component.

**Inheritance/Implementation:** UIGridEvent extends UIScrollableCommonEvent

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export declare interface UIGridEvent--><!--Device-unnamed-export declare interface UIGridEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setOnDidScroll

```TypeScript
setOnDidScroll(callback: OnScrollCallback | undefined): void
```

Set or reset the callback which is triggered when the Grid did scroll.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIGridEvent-setOnDidScroll(callback: OnScrollCallback | undefined): void--><!--Device-UIGridEvent-setOnDidScroll(callback: OnScrollCallback | undefined): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnScrollCallback](../../apis-arkui/arkts-components/arkts-arkui-onscrollcallback-t.md) \| undefined | Yes | callback function, triggered when the Grid did scroll. Passing undefined will unregister the callback. |

## setOnScrollIndex

```TypeScript
setOnScrollIndex(callback: OnGridScrollIndexCallback | undefined): void
```

Set or reset the callback which is triggered when the start and end positions of the display change.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIGridEvent-setOnScrollIndex(callback: OnGridScrollIndexCallback | undefined): void--><!--Device-UIGridEvent-setOnScrollIndex(callback: OnGridScrollIndexCallback | undefined): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnGridScrollIndexCallback](arkts-ongridscrollindexcallback-t.md) \| undefined | Yes | callback function, triggered when start or end positions of the display change. Passing undefined will unregister the callback. |

## setOnWillScroll

```TypeScript
setOnWillScroll(callback: OnWillScrollCallback | undefined): void
```

Set or reset the callback which is triggered when the Grid will scroll.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIGridEvent-setOnWillScroll(callback: OnWillScrollCallback | undefined): void--><!--Device-UIGridEvent-setOnWillScroll(callback: OnWillScrollCallback | undefined): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnWillScrollCallback](../../apis-arkui/arkts-components/arkts-arkui-onwillscrollcallback-t.md) \| undefined | Yes | callback function, triggered when the Grid will scroll. Passing undefined will unregister the callback. |

