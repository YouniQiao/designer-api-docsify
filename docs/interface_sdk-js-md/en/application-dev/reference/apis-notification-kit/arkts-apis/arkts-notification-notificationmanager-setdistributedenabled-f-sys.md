# setDistributedEnabled (System API)

## Modules to Import

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## setDistributedEnabled

```TypeScript
function setDistributedEnabled(enable: boolean, deviceType: string): Promise<void>
```

Sets whether the device of a specified type enables cross-device notification. This API uses a promise to return the result.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function setDistributedEnabled(enable: boolean, deviceType: string): Promise<void>--><!--Device-notificationManager-function setDistributedEnabled(enable: boolean, deviceType: string): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | Whether the device of a specified type enables cross-device notification. The value **true** indicates that the cross-device notification is enabled, and the value **false** indicates the opposite. |
| deviceType | string | Yes | Device type. The options are as follows:&lt;br&gt;- **headset**: wearable audio device&lt;br&gt; - **liteWearable**: lite wearable&lt;br&gt;- **wearable**: wearable&lt;br&gt;- **current**: current device&lt;br&gt;- **2in1**: PC&lt;br&gt;- **tablet**: tablet |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no result. |

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
      let isEnable: boolean = true;
      let deviceType: string = "wearable";
      notificationManager.setDistributedEnabled(isEnable, deviceType).then(() => {
        console.info('setDistributedEnabled succeeded.');
      }).catch((err: BusinessError) => {
        console.error(`setDistributedEnabled failed. Code is ${err.code}, message is ${err.message}`);
      });
    } catch (err) {
      console.error(`setDistributedEnabled failed. Code is ${err.code}, message is ${err.message}`);
    }
  }
}
```

