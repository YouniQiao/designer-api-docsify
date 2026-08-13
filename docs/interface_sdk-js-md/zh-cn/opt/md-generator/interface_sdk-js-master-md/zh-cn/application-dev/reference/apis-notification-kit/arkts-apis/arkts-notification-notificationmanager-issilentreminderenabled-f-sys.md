# isSilentReminderEnabled（系统接口）

## 导入模块

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## isSilentReminderEnabled

```TypeScript
function isSilentReminderEnabled(bundle: BundleOption): Promise<SwitchState>
```

查询静默提醒的开关状态。使用Promise进行异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function isSilentReminderEnabled(bundle: BundleOption): Promise<SwitchState>--><!--Device-notificationManager-function isSilentReminderEnabled(bundle: BundleOption): Promise<SwitchState>-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundle | [BundleOption](arkts-notification-notificationcommondef-bundleoption-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[SwitchState](arkts-notification-notificationmanager-switchstate-e-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [1600012](../errorcode-notification.md#1600012-内存空间不足) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1600002](../errorcode-notification.md#1600002-序列化或反序列化错误) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |
| [17700001](../../apis-ability-kit/errorcode-bundle.md#17700001-指定的bundlename不存在) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundle: notificationManager.BundleOption = {
    bundle: 'bundleName1',
};
notificationManager.isSilentReminderEnabled(bundle).then((data: notificationManager.SwitchState) => {
    hilog.info(0x0000, 'testTag', '%{public}s', `isSilentReminderEnabled success, switchState:  ${JSON.stringify(data)}.`);
}).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', '%{public}s', `isSilentReminderEnabled failed, code is ${err.code}, message is ${err.message}`);
});
```
