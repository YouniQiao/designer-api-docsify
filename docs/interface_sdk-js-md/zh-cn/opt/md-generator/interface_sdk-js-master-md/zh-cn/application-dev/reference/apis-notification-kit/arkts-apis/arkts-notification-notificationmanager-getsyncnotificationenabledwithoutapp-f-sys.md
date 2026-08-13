# getSyncNotificationEnabledWithoutApp（系统接口）

## 导入模块

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## getSyncNotificationEnabledWithoutApp

```TypeScript
function getSyncNotificationEnabledWithoutApp(userId: number, callback: AsyncCallback<boolean>): void
```

获取同步通知到未安装应用设备的开关是否开启(callback形式)。

**起始版本：** 23

**废弃版本：** 26.0.0

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function getSyncNotificationEnabledWithoutApp(userId: int, callback: AsyncCallback<boolean>): void--><!--Device-notificationManager-function getSyncNotificationEnabledWithoutApp(userId: int, callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1600008](../errorcode-notification.md#1600008-用户不存在) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 用户ID，使用时需替换为真实的userId。
let userId: number = 100;
let getSyncNotificationEnabledWithoutAppCallback = (err: BusinessError, data: boolean): void => {
    if (err) {
        console.error(`getSyncNotificationEnabledWithoutAppCallback failed, code is ${err.code}, message is ${err.message}`);
    } else {
        console.info(`getSyncNotificationEnabledWithoutAppCallback success, data: ${JSON.stringify(data)}`);
    }
}
notificationManager.getSyncNotificationEnabledWithoutApp(userId, getSyncNotificationEnabledWithoutAppCallback);
```


## getSyncNotificationEnabledWithoutApp

```TypeScript
function getSyncNotificationEnabledWithoutApp(userId: number): Promise<boolean>
```

获取同步通知到未安装应用设备的开关是否开启(Promise形式)。

**起始版本：** 23

**废弃版本：** 26.0.0

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function getSyncNotificationEnabledWithoutApp(userId: int): Promise<boolean>--><!--Device-notificationManager-function getSyncNotificationEnabledWithoutApp(userId: int): Promise<boolean>-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [1600008](../errorcode-notification.md#1600008-用户不存在) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 用户ID，使用时需替换为真实的userId。
let userId: number = 100;
notificationManager.getSyncNotificationEnabledWithoutApp(userId).then((data: boolean) => {
  console.info(`getSyncNotificationEnabledWithoutApp, data: ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getSyncNotificationEnabledWithoutApp failed, code is ${err.code}, message is ${err.message}`);
});
```
