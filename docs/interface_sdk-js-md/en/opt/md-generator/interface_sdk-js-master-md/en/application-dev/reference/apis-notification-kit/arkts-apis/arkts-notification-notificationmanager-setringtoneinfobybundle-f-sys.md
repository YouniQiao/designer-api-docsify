# setRingtoneInfoByBundle (System API)

## Modules to Import

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## setRingtoneInfoByBundle

```TypeScript
function setRingtoneInfoByBundle(bundle: BundleOption, ringtoneInfo: RingtoneInfo): Promise<void>
```

Sets the custom ringtone information for an application. This API uses a promise to return the result.

**Since:** 21

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function setRingtoneInfoByBundle(bundle: BundleOption, ringtoneInfo: RingtoneInfo): Promise<void>--><!--Device-notificationManager-function setRingtoneInfoByBundle(bundle: BundleOption, ringtoneInfo: RingtoneInfo): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundle | [BundleOption](arkts-notification-notificationcommondef-bundleoption-i.md) | Yes |
| ringtoneInfo | [RingtoneInfo](arkts-notification-notificationmanager-ringtoneinfo-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |
| [1600022](../errorcode-notification.md#1600022-invalid-bundle-information) |

## Examples

```TypeScript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
  }

  onForeground(): void {
    try {
      let bundle: notificationManager.BundleOption = {
        bundle: "bundleName",
      };
      let ringtoneInfo: notificationManager.RingtoneInfo = {
        ringtoneType: notificationManager.RingtoneType.RINGTONE_TYPE_SYSTEM,
        ringtoneTitle: "ringtoneName",
        ringtoneFileName: "ringtonePath",
        ringtoneUri: "ringtoneUri",
      }
      notificationManager.setRingtoneInfoByBundle(bundle, ringtoneInfo).then(() => {
        console.info(`setRingtoneInfoByBundle bundle: ${JSON.stringify(bundle)}', ringtoneInfoJSON: ' ${JSON.stringify(ringtoneInfo)}`);
      }).catch((err: BusinessError) => {
         console.error(`setRingtoneInfoByBundle failed, code is ${err.code}, message is ${err.message}`);
      });
    } catch (err) {
      console.error(`setRingtoneInfoByBundle failed, code is ${err.code}, message is ${err.message}`);
    }
  }
}
```
