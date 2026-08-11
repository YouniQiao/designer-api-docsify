# onTabContentUpdate

## Modules to Import

```TypeScript
import { uiObserver } from 'kits/@kit.ArkUI';
```

## onTabContentUpdate

```TypeScript
export function onTabContentUpdate(options: ObserverOptions, callback: Callback<TabContentInfo>): void
```

Registers a callback function to be called when the tabContent is showed or hidden.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiObserver-export function onTabContentUpdate(options: ObserverOptions, callback: Callback<TabContentInfo>): void--><!--Device-uiObserver-export function onTabContentUpdate(options: ObserverOptions, callback: Callback<TabContentInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ObserverOptions](../../apis-telephony-kit/arkts-apis/arkts-telephony-observer-observeroptions-i.md) | Yes | The options object. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;TabContentInfo&gt; | Yes | The callback function to be called when when the tabContent is showed or hidden. |


## onTabContentUpdate

```TypeScript
export function onTabContentUpdate(callback: Callback<TabContentInfo>): void
```

Registers a callback function to be called when the tabContent is showed or hidden.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiObserver-export function onTabContentUpdate(callback: Callback<TabContentInfo>): void--><!--Device-uiObserver-export function onTabContentUpdate(callback: Callback<TabContentInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;TabContentInfo&gt; | Yes | The callback function to be called when the tabContent is showed or hidden. |

