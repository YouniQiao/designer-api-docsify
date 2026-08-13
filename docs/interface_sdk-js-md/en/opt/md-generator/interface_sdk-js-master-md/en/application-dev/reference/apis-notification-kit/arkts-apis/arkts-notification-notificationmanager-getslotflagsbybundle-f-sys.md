# getSlotFlagsByBundle (System API)

## Modules to Import

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## getSlotFlagsByBundle

```TypeScript
function getSlotFlagsByBundle(bundle: BundleOption): Promise<number>
```

Obtains the notification slot flag of a specified application. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function getSlotFlagsByBundle(bundle: BundleOption): Promise<long>--><!--Device-notificationManager-function getSlotFlagsByBundle(bundle: BundleOption): Promise<long>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundle | [BundleOption](arkts-notification-notificationextensionsubscription-bundleoption-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1600002](../errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |
| [17700001](../../apis-ability-kit/errorcode-bundle.md#17700001-bundle-name-does-not-exist) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let bundle: notificationManager.BundleOption = {
    bundle: "bundleName1",
};
notificationManager.getSlotFlagsByBundle(bundle).then((data : number) => {
    console.info(`getSlotFlagsByBundle success, data: ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getSlotFlagsByBundle failed, code is ${err.code}, message is ${err.message}`);
});
```
