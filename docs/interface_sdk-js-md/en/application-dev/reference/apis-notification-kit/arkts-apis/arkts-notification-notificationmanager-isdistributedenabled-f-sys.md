# isDistributedEnabled (System API)

## Modules to Import

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## isDistributedEnabled

```TypeScript
function isDistributedEnabled(deviceType: string): Promise<boolean>
```

Checks whether a device enables cross-device notification. This API uses a promise to return the result.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function isDistributedEnabled(deviceType: string): Promise<boolean>--><!--Device-notificationManager-function isDistributedEnabled(deviceType: string): Promise<boolean>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceType | string | Yes | Device type. The options are as follows:&lt;br&gt;- **headset**: wearable audio device&lt;br&gt; - **liteWearable**: lite wearable&lt;br&gt;- **wearable**: wearable&lt;br&gt;- **current**: current device&lt;br&gt;- **2in1**: PC&lt;br&gt;- **tablet**: tablet |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result. The value **true** indicates that the cross-device notification is enabled, and the value **false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application to call the interface. |

## Examples

```TypeScript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
  }

  onForeground(): void {
    try {
      let deviceType: string = "wearable";
      notificationManager.isDistributedEnabled(deviceType).then((data: boolean) => {
        console.info('isDistributedEnabled succeeded, result = ' + data);
      }).catch((err: BusinessError) => {
        console.error(`isDistributedEnabled failed. Code is ${err.code}, message is ${err.message}`);
      });
    } catch (err) {
      console.error(`isDistributedEnabled failed. Code is ${err.code}, message is ${err.message}`);
    }
  }
}
```

