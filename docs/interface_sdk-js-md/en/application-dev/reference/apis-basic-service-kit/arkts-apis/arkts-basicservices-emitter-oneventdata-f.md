# onEventData

## Modules to Import

```TypeScript
import { emitter } from 'kits/@kit.BasicServicesKit';
```

## onEventData

```TypeScript
function onEventData(eventId: string, callback: Callback<EventData>): void
```

持续订阅指定的事件，并在接收到该事件时，使用callback异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-emitter-function onEventData(eventId: string, callback: Callback<EventData>): void--><!--Device-emitter-function onEventData(eventId: string, callback: Callback<EventData>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | 持续订阅的事件。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;EventData&gt; | Yes | 接收到该事件时需要执行的回调处理函数。 |

