# offTabContentUpdate

## Modules to Import

```TypeScript
import { uiObserver } from 'kits/@kit.ArkUI';
```

## offTabContentUpdate

```TypeScript
export function offTabContentUpdate(options: ObserverOptions, callback?: Callback<TabContentInfo>): void
```

Removes a callback function that was previously registered with `on()`.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiObserver-export function offTabContentUpdate(options: ObserverOptions, callback?: Callback<TabContentInfo>): void--><!--Device-uiObserver-export function offTabContentUpdate(options: ObserverOptions, callback?: Callback<TabContentInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ObserverOptions](../../apis-telephony-kit/arkts-apis/arkts-telephony-observer-observeroptions-i.md) | Yes | The options object. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;TabContentInfo&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type and Tabs ID will be removed. |


## offTabContentUpdate

```TypeScript
export function offTabContentUpdate(callback?: Callback<TabContentInfo>): void
```

Removes a callback function that was previously registered with `on()`.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiObserver-export function offTabContentUpdate(callback?: Callback<TabContentInfo>): void--><!--Device-uiObserver-export function offTabContentUpdate(callback?: Callback<TabContentInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;TabContentInfo&gt; | No | The callback function to remove. If not provided, all callbacks for the given event type will be removed. |

