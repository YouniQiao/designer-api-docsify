# createSubscriberSync

## 导入模块

```TypeScript
import { commonEventManager } from 'kits/@kit.BasicServicesKit';
```

## createSubscriberSync

```TypeScript
function createSubscriberSync(subscribeInfo: CommonEventSubscribeInfo): CommonEventSubscriber
```

同步创建订阅者的接口。

**起始版本：** 10

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| subscribeInfo | [CommonEventSubscribeInfo](arkts-basicservices-commoneventmanager-commoneventsubscribeinfo-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [CommonEventSubscriber](arkts-basicservices-commoneventsubscriber-commoneventsubscriber-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
