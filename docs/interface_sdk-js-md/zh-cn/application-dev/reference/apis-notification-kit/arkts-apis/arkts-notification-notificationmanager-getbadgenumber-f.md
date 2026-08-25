# getBadgeNumber

## 导入模块

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## getBadgeNumber

```TypeScript
function getBadgeNumber(): Promise<number>
```

获取当前应用角标数量。使用Promise异步回调。用于查询当前应用桌面图标上显示的角标数字。

**起始版本：** 22

**系统能力：** SystemCapability.Notification.Notification

**参见：**

setBadgeNumber 设定角标个数。

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |
