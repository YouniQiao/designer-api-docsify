# on_scrollEvent

## Modules to Import

```TypeScript
import { uiObserver } from '@kit.ArkUI';
```

## on_scrollEvent('scrollEvent')

```TypeScript
export function on(type: 'scrollEvent', options: ObserverOptions, callback: Callback<ScrollEventInfo>): void
```

Registers a callback function to be called when the scroll event start or stop.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-uiObserver-export function on(type: 'scrollEvent', options: ObserverOptions, callback: Callback<ScrollEventInfo>): void--><!--Device-uiObserver-export function on(type: 'scrollEvent', options: ObserverOptions, callback: Callback<ScrollEventInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'scrollEvent' | Yes | The type of event to listen for. Must be 'scrollEvent'. |
| options | ObserverOptions | Yes | The options object. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[ScrollEventInfo](../../apis-na/arkts-apis/arkts-na-uiobserver-scrolleventinfo-i.md)&gt; | Yes | The callback function to be called when the scroll event start or stop. |


## on_scrollEvent('scrollEvent')

```TypeScript
export function on(type: 'scrollEvent', callback: Callback<ScrollEventInfo>): void
```

Registers a callback function to be called when the scroll event start or stop.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-uiObserver-export function on(type: 'scrollEvent', callback: Callback<ScrollEventInfo>): void--><!--Device-uiObserver-export function on(type: 'scrollEvent', callback: Callback<ScrollEventInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'scrollEvent' | Yes | The type of event to listen for. Must be 'scrollEvent'. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[ScrollEventInfo](../../apis-na/arkts-apis/arkts-na-uiobserver-scrolleventinfo-i.md)&gt; | Yes | The callback function to be called when the scroll event start or stop. |

