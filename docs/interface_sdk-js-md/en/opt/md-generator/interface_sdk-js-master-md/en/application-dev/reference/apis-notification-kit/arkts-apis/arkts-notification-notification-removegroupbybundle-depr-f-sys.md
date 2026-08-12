# removeGroupByBundle (System API)

## removeGroupByBundle

```TypeScript
function removeGroupByBundle(bundle: BundleOption, groupName: string, callback: AsyncCallback<void>): void
```

Removes notifications under a notification group of a specified application.This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [removeGroupByBundle](ohos.notificationManager/notificationManager#removeGroupByBundle)

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function removeGroupByBundle(bundle: BundleOption, groupName: string, callback: AsyncCallback<void>): void--><!--Device-notification-function removeGroupByBundle(bundle: BundleOption, groupName: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundle | [BundleOption](arkts-notification-notificationextensionsubscription-bundleoption-t.md) | Yes |
| groupName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |


## removeGroupByBundle

```TypeScript
function removeGroupByBundle(bundle: BundleOption, groupName: string): Promise<void>
```

Removes notifications under a notification group of a specified application.This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [removeGroupByBundle](ohos.notificationManager/notificationManager#removeGroupByBundle)

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function removeGroupByBundle(bundle: BundleOption, groupName: string): Promise<void>--><!--Device-notification-function removeGroupByBundle(bundle: BundleOption, groupName: string): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundle | [BundleOption](arkts-notification-notificationextensionsubscription-bundleoption-t.md) | Yes |
| groupName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |
