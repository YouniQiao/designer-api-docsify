# setBadgeNumber

## 导入模块

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## setBadgeNumber

```TypeScript
function setBadgeNumber(badgeNumber: number, callback: AsyncCallback<void>): void
```

设定角标个数，在应用的桌面图标上呈现。使用callback异步回调。角标是应用桌面图标右上角显示的数字标识，用于提示用户有未处理的通知数量。 设定后，桌面图标将显示对应角标数字。适用于需要在桌面图标上提示用户 待处理消息数量的场景，如未读消息数、待办事项数等。

**起始版本：** 10

**系统能力：** SystemCapability.Notification.Notification

**参见：**

getActiveNotificationCount 获取当前应用的通知数量。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| badgeNumber | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |
| [1600012](../errorcode-notification.md#1600012-内存空间不足) |


## setBadgeNumber

```TypeScript
function setBadgeNumber(badgeNumber: number): Promise<void>
```

设定角标个数，在应用的桌面图标上呈现。使用Promise异步回调。角标是应用桌面图标右上角显示的数字标识，用于提示用户有未处理的通知数量。 设定后，桌面图标将显示对应角标数字。适用于需要在桌面图标上提示用户 待处理消息数量的场景，如未读消息数、待办事项数等。

**起始版本：** 10

**系统能力：** SystemCapability.Notification.Notification

**参见：**

getActiveNotificationCount 获取当前应用的通知数量。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| badgeNumber | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |
| [1600012](../errorcode-notification.md#1600012-内存空间不足) |
