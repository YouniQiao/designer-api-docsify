# getRingtoneInfoByBundle (System API)

## Modules to Import

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## getRingtoneInfoByBundle

```TypeScript
function getRingtoneInfoByBundle(bundle: BundleOption): Promise<RingtoneInfo>
```

Obtains the custom ringtone information of an application. This API uses a promise to return the result.

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function getRingtoneInfoByBundle(bundle: BundleOption): Promise<RingtoneInfo>--><!--Device-notificationManager-function getRingtoneInfoByBundle(bundle: BundleOption): Promise<RingtoneInfo>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundle | BundleOption | Yes | Bundle information of the application. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[RingtoneInfo](arkts-notification-notificationmanager-ringtoneinfo-i-sys.md)&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1600024](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600024-custom-ringtones-not-configured) | The specified bundle has no custom ringtone information. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [1600001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-internal-error) | Internal error. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application to call the interface. |
| [1600003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) | Failed to connect to the service. |
| [1600022](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600022-invalid-bundle-information) | The specified bundle is invalid. |

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

