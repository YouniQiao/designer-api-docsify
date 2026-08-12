# UIScrollableCommonEvent

Defines a UIScrollableCommonEvent which is used to set event to target component.

**Inheritance/Implementation:** UIScrollableCommonEvent extends [UICommonEvent](arkts-arkui-common-uicommonevent-i.md#UICommonEvent)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare interface UIScrollableCommonEvent extends UICommonEvent--><!--Device-unnamed-export declare interface UIScrollableCommonEvent extends UICommonEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setOnReachEnd

```TypeScript
setOnReachEnd(callback: VoidCallback | undefined): void
```

Set or reset the callback which is triggered when the scrolling reaches the end position.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIScrollableCommonEvent-setOnReachEnd(callback: VoidCallback | undefined): void--><!--Device-UIScrollableCommonEvent-setOnReachEnd(callback: VoidCallback | undefined): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | Yes | callback function, triggered when the scrolling reaches the end position. &lt;br&gt;Passing undefined will unregister the callback. |

## setOnReachStart

```TypeScript
setOnReachStart(callback: VoidCallback | undefined): void
```

Set or reset the callback which is triggered when the scrolling reaches the start position.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIScrollableCommonEvent-setOnReachStart(callback: VoidCallback | undefined): void--><!--Device-UIScrollableCommonEvent-setOnReachStart(callback: VoidCallback | undefined): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | Yes | callback function, triggered when the scrolling reaches the start position. &lt;br&gt;Passing undefined will unregister the callback. |

## setOnScrollFrameBegin

```TypeScript
setOnScrollFrameBegin(callback: OnScrollFrameBeginCallback | undefined): void
```

Set or reset the callback which is triggered when scrolling begin each frame.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIScrollableCommonEvent-setOnScrollFrameBegin(callback: OnScrollFrameBeginCallback | undefined): void--><!--Device-UIScrollableCommonEvent-setOnScrollFrameBegin(callback: OnScrollFrameBeginCallback | undefined): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnScrollFrameBeginCallback](../arkts-components/arkts-arkui-onscrollframebegincallback-t.md) \| undefined | Yes | callback function, triggered when the scrolling begin each frame. &lt;br&gt;Passing undefined will unregister the callback. |

## setOnScrollStart

```TypeScript
setOnScrollStart(callback: VoidCallback | undefined): void
```

Set or reset the callback which is triggered when the scrolling started.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIScrollableCommonEvent-setOnScrollStart(callback: VoidCallback | undefined): void--><!--Device-UIScrollableCommonEvent-setOnScrollStart(callback: VoidCallback | undefined): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | Yes | callback function, triggered when the scrolling started. &lt;br&gt;Passing undefined will unregister the callback. |

## setOnScrollStop

```TypeScript
setOnScrollStop(callback: VoidCallback | undefined): void
```

Set or reset the callback which is triggered when the scrolling stopped.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UIScrollableCommonEvent-setOnScrollStop(callback: VoidCallback | undefined): void--><!--Device-UIScrollableCommonEvent-setOnScrollStop(callback: VoidCallback | undefined): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | Yes | callback function, triggered when the scrolling stopped. &lt;br&gt;Passing undefined will unregister the callback. |

