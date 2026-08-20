# onScrollEvent

## Modules to Import

```TypeScript
```

## onScrollEvent

```TypeScript
export function onScrollEvent(options: ObserverOptions, callback: Callback<ScrollEventInfo>): void
```

Registers a callback function to be called when the scroll event starts or stops.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiObserver-export function onScrollEvent(options: ObserverOptions, callback: Callback<ScrollEventInfo>): void--><!--Device-uiObserver-export function onScrollEvent(options: ObserverOptions, callback: Callback<ScrollEventInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | ObserverOptions | Yes | The options object. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[ScrollEventInfo](../../apis-arkui/arkts-apis/arkts-arkui-uiobserver-scrolleventinfo-i.md)&gt; | Yes | The callback function to be called when the scroll event start or stop. |


## onScrollEvent

```TypeScript
export function onScrollEvent(callback: Callback<ScrollEventInfo>): void
```

Registers a callback function to be called when the scroll event starts or stops.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiObserver-export function onScrollEvent(callback: Callback<ScrollEventInfo>): void--><!--Device-uiObserver-export function onScrollEvent(callback: Callback<ScrollEventInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[ScrollEventInfo](../../apis-arkui/arkts-apis/arkts-arkui-uiobserver-scrolleventinfo-i.md)&gt; | Yes | The callback function to be called when the scroll event start or stop. |

