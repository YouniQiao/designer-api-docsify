# disableNotificationFeature（系统接口）

## 导入模块

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## disableNotificationFeature

```TypeScript
function disableNotificationFeature(disabled:boolean, bundleList: Array<string>): Promise<void>
```

将应用包名添加到通知发布权限管控名单，以阻止应用发布通知。支持启用或关闭该功能。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER or ohos.permission.MANAGE_EDM_POLICY

<!--Device-notificationManager-function disableNotificationFeature(disabled:boolean, bundleList: Array<string>): Promise<void>--><!--Device-notificationManager-function disableNotificationFeature(disabled:boolean, bundleList: Array<string>): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| disabled | boolean | 是 |
| bundleList | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let disabled: boolean = true;
let bundleList: Array<string> = ['com.example.myapplication'];
try {
  notificationManager.disableNotificationFeature(disabled, bundleList).then(() => {
    hilog.info(0x0000, 'testTag', '%{public}s', `disableNotificationFeature success.`);
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', '%{public}s', `disableNotificationFeature failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (err) {
  hilog.error(0x0000, 'testTag', '%{public}s', `testTag failed, code is ${err.code}, message is ${err.message}`);
}
```


## disableNotificationFeature

```TypeScript
function disableNotificationFeature(disabled: boolean, bundleList: Array<string>, userId: number): Promise<void>
```

将应用包名添加到通知发布权限管控名单，以阻止应用发布通知。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER or ohos.permission.MANAGE_EDM_POLICY

<!--Device-notificationManager-function disableNotificationFeature(disabled: boolean, bundleList: Array<string>, userId: int): Promise<void>--><!--Device-notificationManager-function disableNotificationFeature(disabled: boolean, bundleList: Array<string>, userId: int): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| disabled | boolean | 是 |
| bundleList | Array & lt;string & gt; | 是 |
| userId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let disabled: boolean = true;
let bundleList: Array<string> = ['com.example.myapplication'];
let userId: number = 1;
try {
  notificationManager.disableNotificationFeature(disabled, bundleList, userId).then(() => {
    hilog.info(0x0000, 'testTag', '%{public}s', `disableNotificationFeature success.`);
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', '%{public}s', `disableNotificationFeature failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (err) {
  hilog.error(0x0000, 'testTag', '%{public}s', `testTag failed, code is ${err.code}, message is ${err.message}`);
}
```
