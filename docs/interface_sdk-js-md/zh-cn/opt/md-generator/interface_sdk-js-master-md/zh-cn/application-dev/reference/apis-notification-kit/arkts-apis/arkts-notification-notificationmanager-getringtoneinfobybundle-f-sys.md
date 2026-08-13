# getRingtoneInfoByBundle（系统接口）

## 导入模块

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## getRingtoneInfoByBundle

```TypeScript
function getRingtoneInfoByBundle(bundle: BundleOption): Promise<RingtoneInfo>
```

获取应用自定义铃声信息。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function getRingtoneInfoByBundle(bundle: BundleOption): Promise<RingtoneInfo>--><!--Device-notificationManager-function getRingtoneInfoByBundle(bundle: BundleOption): Promise<RingtoneInfo>-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundle | [BundleOption](arkts-notification-notificationcommondef-bundleoption-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[RingtoneInfo](arkts-notification-notificationmanager-ringtoneinfo-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [1600024](../errorcode-notification.md#1600024-未配置自定义铃声) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [1600001](../errorcode-notification.md#1600001-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1600003](../errorcode-notification.md#1600003-连接通知服务失败) |
| [1600022](../errorcode-notification.md#1600022-无效的包信息) |

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
      notificationManager.getRingtoneInfoByBundle(bundle)
        .then((ringtoneInfo: notificationManager.RingtoneInfo) => {
          console.info(`getRingtoneInfoByBundle success: ${JSON.stringify(ringtoneInfo)}`);
        }).catch((err: BusinessError) => {
        console.error(`getRingtoneInfoByBundle failed, code is ${err.code}, message is ${err.message}`);
      });
    } catch (err) {
      console.error(`getRingtoneInfoByBundle failed, code is ${err.code}, message is ${err.message}`);
    }
  }
}
```
