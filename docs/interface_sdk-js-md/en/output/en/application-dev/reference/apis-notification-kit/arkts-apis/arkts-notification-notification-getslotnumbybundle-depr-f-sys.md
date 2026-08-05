# getSlotNumByBundle (System API)

## getSlotNumByBundle

```TypeScript
function getSlotNumByBundle(bundle: BundleOption, callback: AsyncCallback<number>): void
```

Obtains the number of notification slots of a specified application. This API uses an asynchronous callback to return the result.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.notificationManager/notificationManager#getSlotNumByBundle

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function getSlotNumByBundle(bundle: BundleOption, callback: AsyncCallback<number>): void--><!--Device-notification-function getSlotNumByBundle(bundle: BundleOption, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundle | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Bundle information of the application. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;number&gt; | Yes | Callback used to return the result. |


## getSlotNumByBundle

```TypeScript
function getSlotNumByBundle(bundle: BundleOption): Promise<number>
```

Obtains the number of notification slots of a specified application. This API uses a promise to return the result.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.notificationManager/notificationManager#getSlotNumByBundle

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function getSlotNumByBundle(bundle: BundleOption): Promise<number>--><!--Device-notification-function getSlotNumByBundle(bundle: BundleOption): Promise<number>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundle | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Bundle information of the application. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | Promise used to return the result. |

