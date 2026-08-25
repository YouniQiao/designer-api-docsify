# publishAsUser（系统接口）

## 导入模块

```TypeScript
import { commonEventManager } from 'kits/@kit.BasicServicesKit';
```

## publishAsUser

```TypeScript
function publishAsUser(event: string, userId: number, callback: AsyncCallback<void>): void
```

向指定用户发布公共事件。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Notification.CommonEvent

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | string | 是 |
| userId | number | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1500003](../errorcode-CommonEventService.md#1500003-公共事件发送频率过高) |
| [1500006](../errorcode-CommonEventService.md#1500006-无效userid) |
| [1500007](../errorcode-CommonEventService.md#1500007-ipc请求发送失败) |
| [1500008](../errorcode-CommonEventService.md#1500008-公共事件服务端初始化失败) |
| [1500009](../errorcode-CommonEventService.md#1500009-获取系统参数失败) |


## publishAsUser

```TypeScript
function publishAsUser(
    event: string,
    userId: number,
    options: CommonEventPublishData,
    callback: AsyncCallback<void>
  ): void
```

向指定用户发布公共事件并指定发布信息。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.Notification.CommonEvent

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | string | 是 |
| userId | number | 是 |
| options | [CommonEventPublishData](arkts-basicservices-commoneventpublishdata-commoneventpublishdata-i.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1500003](../errorcode-CommonEventService.md#1500003-公共事件发送频率过高) |
| [1500006](../errorcode-CommonEventService.md#1500006-无效userid) |
| [1500007](../errorcode-CommonEventService.md#1500007-ipc请求发送失败) |
| [1500008](../errorcode-CommonEventService.md#1500008-公共事件服务端初始化失败) |
| [1500009](../errorcode-CommonEventService.md#1500009-获取系统参数失败) |
