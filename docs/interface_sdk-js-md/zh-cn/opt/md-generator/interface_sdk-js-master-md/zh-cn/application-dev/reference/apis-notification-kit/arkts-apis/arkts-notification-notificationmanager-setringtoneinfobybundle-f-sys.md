# setRingtoneInfoByBundle（系统接口）

## 导入模块

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## setRingtoneInfoByBundle

```TypeScript
function setRingtoneInfoByBundle(bundle: BundleOption, ringtoneInfo: RingtoneInfo): Promise<void>
```

设置应用自定义铃声信息。使用Promise异步回调。

**起始版本：** 21

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function setRingtoneInfoByBundle(bundle: BundleOption, ringtoneInfo: RingtoneInfo): Promise<void>--><!--Device-notificationManager-function setRingtoneInfoByBundle(bundle: BundleOption, ringtoneInfo: RingtoneInfo): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundle | [BundleOption](arkts-notification-notificationcommondef-bundleoption-i.md) | 是 |
| ringtoneInfo | [RingtoneInfo](arkts-notification-notificationmanager-ringtoneinfo-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [1600001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-内部错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [1600003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600003-连接通知服务失败) |
| [1600022](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600022-无效的包信息) |

## 示例

```TypeScript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
  }

  onForeground(): void {
    try {
      let bundle: notificationManager.BundleOption = {
        bundle: 'bundleName',
      };
      let ringtoneInfo: notificationManager.RingtoneInfo = {
        ringtoneType: notificationManager.RingtoneType.RINGTONE_TYPE_SYSTEM,
        ringtoneTitle: 'ringtoneName',
        ringtoneFileName: 'ringtonePath',
        ringtoneUri: 'ringtoneUri',
      }
      notificationManager.setRingtoneInfoByBundle(bundle, ringtoneInfo).then(() => {
        console.info(`setRingtoneInfoByBundle bundle: ${JSON.stringify(bundle)}', ringtoneInfoJSON：' ${JSON.stringify(ringtoneInfo)}`);
      }).catch((err: BusinessError) => {
         console.error(`setRingtoneInfoByBundle failed, code is ${err.code}, message is ${err.message}`);
      });
    } catch (err) {
      console.error(`setRingtoneInfoByBundle failed, code is ${err.code}, message is ${err.message}`);
    }
  }
}
```
