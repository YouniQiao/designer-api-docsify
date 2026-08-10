# offEventData

## Modules to Import

```TypeScript
import { emitter } from 'kits/@kit.BasicServicesKit';
```

## offEventData

```TypeScript
function offEventData(eventId: string, callback: Callback<EventData>): void
```

取消事件ID为eventId且回调处理函数为callback的订阅。仅当已使用  
[onEventData](emitter.onEventData(eventId: string, callback: Callback&lt;EventData&gt;))或  
[onceEventData](emitter.onceEventData(eventId: string, callback: Callback&lt;EventData&gt;))接口订阅callback时，该接口才生效。

使用该接口取消某个事件订阅后，已通过[emit](emitter.emit(eventId: string))接口发布但尚未被执行的事件将被取消。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-emitter-function offEventData(eventId: string, callback: Callback<EventData>): void--><!--Device-emitter-function offEventData(eventId: string, callback: Callback<EventData>): void-End-->

**System capability:** SystemCapability.Notification.Emitter

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventId | string | Yes | 事件ID。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;EventData&gt; | Yes | 事件的回调处理函数。 |

