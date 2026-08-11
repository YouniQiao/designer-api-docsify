# setDistributedEnabledBySlot (System API)

## Modules to Import

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## setDistributedEnabledBySlot

```TypeScript
function setDistributedEnabledBySlot(slot: SlotType, deviceType: string, enabled: boolean): Promise<void>
```

Sets whether notifications of a specified slot can be sent to devices of a specified type through cross-device collaboration. This API uses a promise to return the result.

**Since:** 18

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function setDistributedEnabledBySlot(slot: SlotType, deviceType: string, enabled: boolean): Promise<void>--><!--Device-notificationManager-function setDistributedEnabledBySlot(slot: SlotType, deviceType: string, enabled: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| slot | [SlotType](arkts-notification-notificationmanager-slottype-e-sys.md) | Yes |
| deviceType | string | Yes |
| enabled | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let slot: notificationManager.SlotType = notificationManager.SlotType.SOCIAL_COMMUNICATION;
let deviceType: string = 'wearable';
let enabled: boolean = true;

notificationManager.setDistributedEnabledBySlot(slot, deviceType, enabled).then(() => {
    hilog.info(0x0000, 'testTag', '%{public}s', `setDistributedEnabledBySlot success.`);
}).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', '%{public}s', `setDistributedEnabledBySlot failed, code is ${err.code}, message is ${err.message}`);
});
```
