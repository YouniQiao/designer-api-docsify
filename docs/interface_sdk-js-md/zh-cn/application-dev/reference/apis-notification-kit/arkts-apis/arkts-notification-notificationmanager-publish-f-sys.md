# publish（系统接口）

## 导入模块

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## publish

```TypeScript
function publish(request: NotificationRequest, userId: number, callback: AsyncCallback<void>): void
```

发布通知给指定的用户。使用callback异步回调。

**起始版本：** 9

**需要权限：** 
- API版本18+：ohos.permission.NOTIFICATION_CONTROLLER or ohos.permission.SEND_NOTIFICATION_CROSS_USER
- API版本9 - 17：ohos.permission.NOTIFICATION_CONTROLLER

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| request | [NotificationRequest](arkts-notification-notificationmanager-notificationrequest-t.md) | 是 |
| userId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |
| [1600004](../errorcode-notification.md#1600004-通知开关关闭) |
| [1600005](../errorcode-notification.md#1600005-通知渠道关闭) |
| [1600007](../errorcode-notification.md#1600007-通知不存在) |
| [1600008](../errorcode-notification.md#1600008-用户不存在) |
| [1600009](../errorcode-notification.md#1600009-通知发布频度超过限制) |
| [1600012](../errorcode-notification.md#1600012-内存空间不足) |
| [1600014](../errorcode-notification.md#1600014-没有相关权限) |
| [1600015](../errorcode-notification.md#1600015-当前通知状态不支持重复配置) |
| [1600016](../errorcode-notification.md#1600016-本次更新的通知版本太低) |
| [1600020](../errorcode-notification.md#1600020-不允许权限管控名单中的应用发布通知) |
| [1600025](../errorcode-notification.md#1600025-地理围栏开关关闭) |
| [1600026](../errorcode-notification.md#1600026-位置功能开关关闭) |
| [1600027](../errorcode-notification.md#1600027-位置系统服务的感知与提醒开关关闭) |
| [1600029](../errorcode-notification.md#1600029-系统无法找到实况窗卡片自定义扩展区的extensionability) |
| [2300007](../../apis-network-kit/errorcode-net-http.md#2300007-无法连接到服务器) |


## publish

```TypeScript
function publish(request: NotificationRequest, userId: number): Promise<void>
```

发布通知给指定的用户。使用Promise异步回调。

**起始版本：** 9

**需要权限：** 
- API版本18+：ohos.permission.NOTIFICATION_CONTROLLER or ohos.permission.SEND_NOTIFICATION_CROSS_USER
- API版本9 - 17：ohos.permission.NOTIFICATION_CONTROLLER

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| request | [NotificationRequest](arkts-notification-notificationmanager-notificationrequest-t.md) | 是 |
| userId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |
| [1600004](../errorcode-notification.md#1600004-通知开关关闭) |
| [1600005](../errorcode-notification.md#1600005-通知渠道关闭) |
| [1600007](../errorcode-notification.md#1600007-通知不存在) |
| [1600008](../errorcode-notification.md#1600008-用户不存在) |
| [1600009](../errorcode-notification.md#1600009-通知发布频度超过限制) |
| [1600012](../errorcode-notification.md#1600012-内存空间不足) |
| [1600014](../errorcode-notification.md#1600014-没有相关权限) |
| [1600015](../errorcode-notification.md#1600015-当前通知状态不支持重复配置) |
| [1600016](../errorcode-notification.md#1600016-本次更新的通知版本太低) |
| [1600020](../errorcode-notification.md#1600020-不允许权限管控名单中的应用发布通知) |
| [1600025](../errorcode-notification.md#1600025-地理围栏开关关闭) |
| [1600026](../errorcode-notification.md#1600026-位置功能开关关闭) |
| [1600027](../errorcode-notification.md#1600027-位置系统服务的感知与提醒开关关闭) |
| [1600029](../errorcode-notification.md#1600029-系统无法找到实况窗卡片自定义扩展区的extensionability) |
| [2300007](../../apis-network-kit/errorcode-net-http.md#2300007-无法连接到服务器) |
