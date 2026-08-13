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

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function setDistributedEnabled(enable: boolean, deviceType: string): Promise<void>--><!--Device-notificationManager-function setDistributedEnabled(enable: boolean, deviceType: string): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |
| deviceType | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

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
