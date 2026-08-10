# onTabContentUpdate

## Modules to Import

```TypeScript
import { uiObserver } from 'kits/@kit.ArkUI';
```

## onTabContentUpdate

```TypeScript
export function onTabContentUpdate(options: ObserverOptions, callback: Callback<TabContentInfo>): void
```

监听TabContent页面的切换事件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiObserver-export function onTabContentUpdate(options: ObserverOptions, callback: Callback<TabContentInfo>): void--><!--Device-uiObserver-export function onTabContentUpdate(options: ObserverOptions, callback: Callback<TabContentInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ObserverOptions](../../apis-telephony-kit/arkts-apis/arkts-telephony-observer-observeroptions-i.md) | Yes | 指定监听的Tabs组件的id。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;TabContentInfo&gt; | Yes | 回调函数。携带TabContentInfo，返回TabContent页面切换事件的信息。 |


## onTabContentUpdate

```TypeScript
export function onTabContentUpdate(callback: Callback<TabContentInfo>): void
```

监听TabContent页面的切换事件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiObserver-export function onTabContentUpdate(callback: Callback<TabContentInfo>): void--><!--Device-uiObserver-export function onTabContentUpdate(callback: Callback<TabContentInfo>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;TabContentInfo&gt; | Yes | 回调函数。携带TabContentInfo，返回TabContent页面切换事件的信息。 |

