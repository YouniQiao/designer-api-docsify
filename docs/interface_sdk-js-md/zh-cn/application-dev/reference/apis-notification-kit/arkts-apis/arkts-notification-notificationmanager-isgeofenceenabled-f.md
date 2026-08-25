# isGeofenceEnabled

## 导入模块

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## isGeofenceEnabled

```TypeScript
function isGeofenceEnabled(): Promise<boolean>
```

检查地理围栏功能是否已启用。使用Promise异步回调。

**起始版本：** 23

**系统能力：** SystemCapability.Notification.Notification

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |
| [1600012](../errorcode-notification.md#1600012-内存空间不足) |
