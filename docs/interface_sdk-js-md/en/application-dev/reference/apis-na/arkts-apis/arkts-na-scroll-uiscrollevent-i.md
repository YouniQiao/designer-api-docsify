# UIScrollEvent

Defines a UIScrollableCommonEvent which is used to set different common event to target component.

**Inheritance/Implementation:** UIScrollEvent extends UIScrollableCommonEvent

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export declare interface UIScrollEvent--><!--Device-unnamed-export declare interface UIScrollEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setOnDidScroll

```TypeScript
setOnDidScroll(callback: ScrollOnScrollCallback | undefined): void
```

Set or reset the callback which is triggered when the Scroll did scroll.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIScrollEvent-setOnDidScroll(callback: ScrollOnScrollCallback | undefined): void--><!--Device-UIScrollEvent-setOnDidScroll(callback: ScrollOnScrollCallback | undefined): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ScrollOnScrollCallback](arkts-na-scrollonscrollcallback-t.md) \| undefined | Yes | callback function, triggered when the Scroll did scroll. Passing undefined will unregister the callback. |

## setOnWillScroll

```TypeScript
setOnWillScroll(callback: ScrollOnWillScrollCallback | undefined): void
```

Set or reset the callback which is triggered when the Scroll will scroll.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIScrollEvent-setOnWillScroll(callback: ScrollOnWillScrollCallback | undefined): void--><!--Device-UIScrollEvent-setOnWillScroll(callback: ScrollOnWillScrollCallback | undefined): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ScrollOnWillScrollCallback](arkts-na-scrollonwillscrollcallback-t.md) \| undefined | Yes | callback function, triggered when the Scroll will scroll. Passing undefined will unregister the callback. |

