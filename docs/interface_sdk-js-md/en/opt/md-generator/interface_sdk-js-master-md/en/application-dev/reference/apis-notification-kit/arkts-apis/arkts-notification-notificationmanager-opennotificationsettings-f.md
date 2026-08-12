# openNotificationSettings

## Modules to Import

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## openNotificationSettings

```TypeScript
function openNotificationSettings(context: UIAbilityContext): Promise<void>
```

Opens the notification settings page of the application, which is displayed in semi-modal mode and can be used to set the notification enabling and notification mode. This API uses a promise to return the result.

This is suitable for scenarios where users need to manually modify notification settings, such as a secondary request after a user denies authorization, or when the notification reminder method(vibration, ringtone, etc.) needs to be modified. When the requestEnableNotification dialog box is denied by the user, you can call this API to guide the user to the notification settings page to manually enable it.

**Since:** 13

**Model restriction:** This API can be used only in the stage model.

<!--Device-notificationManager-function openNotificationSettings(context: UIAbilityContext): Promise<void>--><!--Device-notificationManager-function openNotificationSettings(context: UIAbilityContext): Promise<void>-End-->

**System capability:** SystemCapability.Notification.NotificationSettings

**See also:**

[requestEnableNotification](notificationManager.requestEnableNotification(context: UIAbilityContext): Promise<void>) requests notification

[isNotificationEnabled](notificationManager.isNotificationEnabled(): Promise<boolean>) checks whether notification is

[getNotificationSetting](notificationManager.getNotificationSetting(): Promise<NotificationSetting>) obtains the notification settings

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIAbilityContext](../../apis-ability-kit/arkts-apis/arkts-ability-uiabilitycontext-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [1600001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-internal-error) |
| [1600018](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600018-notification-settings-page-already-displayed) |
| [1600003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MyAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', `Failed to load the content. Cause: ${JSON.stringify(err) ?? ''}`);
        return;
      }
      hilog.info(0x0000, 'testTag', `Succeeded in loading the content. Data: ${JSON.stringify(data) ?? ''}`);
      notificationManager.openNotificationSettings(this.context).then(() => {
        hilog.info(0x0000, 'testTag', `[ANS] openNotificationSettings success`);
      }).catch((err: BusinessError) => {
        hilog.error(0x0000, 'testTag', `[ANS] openNotificationSettings failed, code is ${err.code}, message is ${err.message}`);
      });
    });
  }
}
```
