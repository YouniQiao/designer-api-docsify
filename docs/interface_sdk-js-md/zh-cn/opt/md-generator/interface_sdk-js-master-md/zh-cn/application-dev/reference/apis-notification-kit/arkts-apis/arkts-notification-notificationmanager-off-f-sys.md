# off（系统接口）

## 导入模块

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## off('checkNotification')

```TypeScript
function off(
    type: 'checkNotification',
    callback?: (checkInfo: NotificationCheckInfo) => NotificationCheckResult
  ): void
```

取消通知监听回调。

**起始版本：** 10

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER and ohos.permission.NOTIFICATION_AGENT_CONTROLLER

<!--Device-notificationManager-function off(    type: 'checkNotification',    callback?: (checkInfo: NotificationCheckInfo) => NotificationCheckResult  ): void--><!--Device-notificationManager-function off(    type: 'checkNotification',    callback?: (checkInfo: NotificationCheckInfo) => NotificationCheckResult  ): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'checkNotification' | 是 |
| callback | (checkInfo: NotificationCheckInfo) =&gt; NotificationCheckResult | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try{
    notificationManager.off('checkNotification');
} catch (err){
    console.error(`notificationManager.off failed, code is ${err.code}, message is ${err.message}`);
}
```
