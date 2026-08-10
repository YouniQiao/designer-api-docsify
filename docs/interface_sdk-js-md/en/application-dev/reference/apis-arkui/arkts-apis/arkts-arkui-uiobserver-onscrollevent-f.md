# onScrollEvent

## Modules to Import

```TypeScript
import { uiObserver } from 'kits/@kit.ArkUI';
```

## onScrollEvent

```TypeScript
export function onScrollEvent(options: ObserverOptions, callback: Callback<ScrollEventInfo>): void
```

Registers a callback function to be called when the scroll event starts or stops.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiObserver-export function onScrollEvent(options: ObserverOptions, callback: Callback<ScrollEventInfo>): void--><!--Device-uiObserver-export function onScrollEvent(options: ObserverOptions, callback: Callback<ScrollEventInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ObserverOptions](../../apis-telephony-kit/arkts-apis/arkts-telephony-observer-observeroptions-i.md) | Yes | The options object. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ScrollEventInfo&gt; | Yes | The callback function to be called when the scroll event start or stop. |


## onScrollEvent

```TypeScript
export function onScrollEvent(callback: Callback<ScrollEventInfo>): void
```

Registers a callback function to be called when the scroll event starts or stops.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiObserver-export function onScrollEvent(callback: Callback<ScrollEventInfo>): void--><!--Device-uiObserver-export function onScrollEvent(callback: Callback<ScrollEventInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ScrollEventInfo&gt; | Yes | The callback function to be called when the scroll event start or stop. |

