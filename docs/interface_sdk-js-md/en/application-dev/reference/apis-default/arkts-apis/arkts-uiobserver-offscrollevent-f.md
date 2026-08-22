# offScrollEvent

## Modules to Import

```TypeScript
```

## offScrollEvent

```TypeScript
export function offScrollEvent(options: ObserverOptions, callback?: Callback<ScrollEventInfo>): void
```

Removes a callback function that was previously registered with `onScrollEvent()`.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiObserver-export function offScrollEvent(options: ObserverOptions, callback?: Callback<ScrollEventInfo>): void--><!--Device-uiObserver-export function offScrollEvent(options: ObserverOptions, callback?: Callback<ScrollEventInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | ObserverOptions | Yes | The options object. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[ScrollEventInfo](arkts-uiobserver-scrolleventinfo-i.md)&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type and scroll ID will be removed. |


## offScrollEvent

```TypeScript
export function offScrollEvent(callback?: Callback<ScrollEventInfo>): void
```

Removes a callback function that was previously registered with `onScrollEvent()`.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiObserver-export function offScrollEvent(callback?: Callback<ScrollEventInfo>): void--><!--Device-uiObserver-export function offScrollEvent(callback?: Callback<ScrollEventInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[ScrollEventInfo](arkts-uiobserver-scrolleventinfo-i.md)&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

