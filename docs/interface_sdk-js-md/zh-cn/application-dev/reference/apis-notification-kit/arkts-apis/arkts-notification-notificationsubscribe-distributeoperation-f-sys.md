# distributeOperation（系统接口）

## 导入模块

```TypeScript
import { notificationSubscribe } from 'kits/@kit.NotificationKit';
```

## distributeOperation

```TypeScript
function distributeOperation(hashcode: string, operationInfo?: OperationInfo): Promise<void>
```

触发指定通知的跨设备协同操作（例如通知跨设备点击跳转、通知跨设备快捷回复等）。使用Promise异步回调。

**起始版本：** 18

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hashcode | string | 是 |
| [operationInfo](../../apis-ability-kit/arkts-apis/arkts-ability-abilitytoolaccessctrl-permissionquery-i-sys.md) | [OperationInfo](arkts-notification-notificationsubscribe-operationinfo-i-sys.md) | 否 |

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
| [1600010](../errorcode-notification.md#1600010-分布式操作失败) |
| [1600021](../errorcode-notification.md#1600021-跨设备通信超时) |
