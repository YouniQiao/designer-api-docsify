# isDistributedEnabledBySlot (System API)

## Modules to Import

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## isDistributedEnabledBySlot

```TypeScript
function isDistributedEnabledBySlot(slot: SlotType, deviceType: string): Promise<boolean>
```

Queries whether notifications of a specified slot can be sent to devices of a specified type. This API uses a promise to return the result.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function isDistributedEnabledBySlot(slot: SlotType, deviceType: string): Promise<boolean>--><!--Device-notificationManager-function isDistributedEnabledBySlot(slot: SlotType, deviceType: string): Promise<boolean>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| slot | [SlotType](arkts-notification-notificationmanager-slottype-e-sys.md) | Yes | Types of the notification slot. |
| deviceType | string | Yes | Device type.&lt;br&gt;Since API version 18, the following device types are supported:&lt;br&gt;- **headset**: wearable audio device&lt;br&gt;- **liteWearable**: lite wearable&lt;br&gt;- **wearable**: wearable&lt;br&gt;Since API version 20, the following device types are supported:&lt;br&gt;- **headset**: wearable audio device&lt;br&gt;- **liteWearable**: lite wearable&lt;br&gt;- **wearable**: wearable&lt;br&gt;- **current**: current device&lt;br&gt;- **2in1**: PC&lt; br&gt;- **tablet**: tablet |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result. The value **true** means that cross-device collaboration is supported, and **false** means the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application to call the interface. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let slot: notificationManager.SlotType = notificationManager.SlotType.SOCIAL_COMMUNICATION;
let deviceType: string = 'wearable';

notificationManager.isDistributedEnabledBySlot(slot, deviceType).then((data: boolean) => {
    hilog.info(0x0000, 'testTag', '%{public}s', `isDistributedEnabledBySlot success.`);
}).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', '%{public}s', `isDistributedEnabledBySlot failed, code is ${err.code}, message is ${err.message}`);
});
```

