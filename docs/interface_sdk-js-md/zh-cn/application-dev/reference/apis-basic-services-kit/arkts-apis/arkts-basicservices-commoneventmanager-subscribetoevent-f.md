# subscribeToEvent

## 导入模块

```TypeScript
import { commonEventManager } from 'kits/@kit.BasicServicesKit';
```

## subscribeToEvent

```TypeScript
function subscribeToEvent(subscriber: CommonEventSubscriber, callback: Callback<CommonEventData>): Promise<void>
```

订阅公共事件，并返回订阅成功或失败信息。使用Promise异步回调。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| subscriber | [CommonEventSubscriber](arkts-basicservices-commoneventsubscriber-commoneventsubscriber-i.md) | 是 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;CommonEventData&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1500007](../errorcode-CommonEventService.md#1500007-ipc请求发送失败) |
| [1500008](../errorcode-CommonEventService.md#1500008-公共事件服务端初始化失败) |
| [1500010](../errorcode-CommonEventService.md#1500010-订阅者数量超限) |
