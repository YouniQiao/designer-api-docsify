# getSlotByBundle (System API)

## Modules to Import

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## getSlotByBundle

```TypeScript
function getSlotByBundle(bundle: BundleOption, slotType: SlotType): Promise<NotificationSlot>
```

Obtains a notification slot of a specified application. This API uses a promise to return the result.

Before obtaining the notification slot, create a slot through   
[addSlot](arkts-notification-notificationmanager-addslot-f.md#addSlot-2).

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function getSlotByBundle(bundle: BundleOption, slotType: SlotType): Promise<NotificationSlot>--><!--Device-notificationManager-function getSlotByBundle(bundle: BundleOption, slotType: SlotType): Promise<NotificationSlot>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundle | BundleOption | Yes | Bundle information of the application. |
| slotType | SlotType | Yes | Notification slot type. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;NotificationSlot&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported.<br>**Applicable version:** 18 and later |
| [1600012](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600012-insufficient-memory-space) | No memory space. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [1600001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-internal-error) | Internal error. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application to call the interface. |
| [1600002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) | Marshalling or unmarshalling error. |
| [1600003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) | Failed to connect to the service. |
| [17700001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-bundle.md#17700001-bundle-name-does-not-exist) | The specified bundle name was not found. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let bundle: notificationManager.BundleOption = {
    bundle: "bundleName1",
};

let slotType = notificationManager.SlotType.LIVE_VIEW;

notificationManager.getSlotByBundle(bundle, slotType).then((data: notificationManager.NotificationSlot) => {
    console.info(`getSlotByBundle success, data: ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getSlotByBundle failed, code is ${err.code}, message is ${err.message}`);
});
```


## getSlotByBundle

```TypeScript
function getSlotByBundle(bundle: BundleOption, slotType: SlotType): Promise<NotificationSlot|null>
```

Obtains a notification slot of a specified application. This API uses a promise to return the result.

Before obtaining the notification slot, create a slot through   
[addSlot](arkts-notification-notificationmanager-addslot-f.md#addSlot-2).

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function getSlotByBundle(bundle: BundleOption, slotType: SlotType): Promise<NotificationSlot|null>--><!--Device-notificationManager-function getSlotByBundle(bundle: BundleOption, slotType: SlotType): Promise<NotificationSlot|null>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundle | BundleOption | Yes | Bundle information of the application. |
| slotType | SlotType | Yes | Notification slot type. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;NotificationSlot \| null&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [1600012](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600012-insufficient-memory-space) | No memory space. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [1600001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-internal-error) | Internal error. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application to call the interface. |
| [1600002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) | Marshalling or unmarshalling error. |
| [1600003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) | Failed to connect to the service. |
| [17700001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-bundle.md#17700001-bundle-name-does-not-exist) | The specified bundle name was not found. |

