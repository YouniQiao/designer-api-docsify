# setDistributedEnabledBySlot（系统接口）

## 导入模块

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## setDistributedEnabledBySlot

```TypeScript
function setDistributedEnabledBySlot(slot: SlotType, deviceType: string, enabled: boolean): Promise<void>
```

设置指定渠道的通知是否支持通知跨设备协同至指定类型设备。使用Promise异步回调。

**起始版本：** 18

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [slot](arkts-notification-notificationsorting-notificationsorting-i-sys.md) | [SlotType](arkts-notification-notificationmanager-slottype-e.md) | 是 |
| deviceType | string | 是 |
| enabled | boolean | 是 |

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
