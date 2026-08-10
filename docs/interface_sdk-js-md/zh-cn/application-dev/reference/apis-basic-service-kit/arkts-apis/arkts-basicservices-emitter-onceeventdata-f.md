# onceEventData

## 导入模块

```TypeScript
import { emitter } from 'kits/@kit.BasicServicesKit';
```

## onceEventData

```TypeScript
function onceEventData(eventId: string, callback: Callback<EventData>): void
```

单次订阅指定的事件，在接收到该事件且执行完对应的回调函数后，自动取消订阅。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-emitter-function onceEventData(eventId: string, callback: Callback<EventData>): void--><!--Device-emitter-function onceEventData(eventId: string, callback: Callback<EventData>): void-End-->

**系统能力：** SystemCapability.Notification.Emitter

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventId | string | 是 | 单次订阅的事件。取值为长度不超过10240字节的自定义字符串，且不可为空字符。 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;EventData&gt; | 是 | 接收到该事件时需要执行的回调处理函数。 |

