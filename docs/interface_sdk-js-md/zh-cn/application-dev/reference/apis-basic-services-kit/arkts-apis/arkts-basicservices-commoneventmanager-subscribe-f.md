# subscribe

## 导入模块

```TypeScript
import { commonEventManager } from 'kits/@kit.BasicServicesKit';
```

## subscribe

```TypeScript
function subscribe(subscriber: CommonEventSubscriber, callback: AsyncCallback<CommonEventData>): void
```

订阅公共事件。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| subscriber | [CommonEventSubscriber](arkts-basicservices-commoneventsubscriber-commoneventsubscriber-i.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;CommonEventData&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1500007](../errorcode-CommonEventService.md#1500007-ipc请求发送失败) |
| [1500008](../errorcode-CommonEventService.md#1500008-公共事件服务端初始化失败) |
| [1500010](../errorcode-CommonEventService.md#1500010-订阅者数量超限) |
