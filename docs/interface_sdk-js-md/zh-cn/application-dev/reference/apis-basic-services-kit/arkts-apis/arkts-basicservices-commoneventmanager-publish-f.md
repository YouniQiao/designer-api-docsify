# publish

## 导入模块

```TypeScript
import { commonEventManager } from 'kits/@kit.BasicServicesKit';
```

## publish

```TypeScript
function publish(event: string, callback: AsyncCallback<void>): void
```

发布公共事件。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | string | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1500003](../errorcode-CommonEventService.md#1500003-公共事件发送频率过高) |
| [1500007](../errorcode-CommonEventService.md#1500007-ipc请求发送失败) |
| [1500008](../errorcode-CommonEventService.md#1500008-公共事件服务端初始化失败) |
| [1500009](../errorcode-CommonEventService.md#1500009-获取系统参数失败) |


## publish

```TypeScript
function publish(event: string, options: CommonEventPublishData, callback: AsyncCallback<void>): void
```

发布公共事件。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | string | 是 |
| options | [CommonEventPublishData](arkts-basicservices-commoneventpublishdata-commoneventpublishdata-i.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1500003](../errorcode-CommonEventService.md#1500003-公共事件发送频率过高) |
| [1500007](../errorcode-CommonEventService.md#1500007-ipc请求发送失败) |
| [1500008](../errorcode-CommonEventService.md#1500008-公共事件服务端初始化失败) |
| [1500009](../errorcode-CommonEventService.md#1500009-获取系统参数失败) |
