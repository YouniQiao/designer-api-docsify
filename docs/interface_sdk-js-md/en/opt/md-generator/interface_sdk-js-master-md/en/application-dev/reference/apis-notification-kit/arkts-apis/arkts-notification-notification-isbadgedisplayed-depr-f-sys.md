# isBadgeDisplayed (System API)

## isBadgeDisplayed

```TypeScript
function isBadgeDisplayed(bundle: BundleOption, callback: AsyncCallback<boolean>): void
```

Checks whether the notification badge is enabled for a specified application. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [isBadgeDisplayed](arkts-notification-notificationmanager-isbadgedisplayed-f-sys.md#isBadgeDisplayed-(System-API))

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function isBadgeDisplayed(bundle: BundleOption, callback: AsyncCallback<boolean>): void--><!--Device-notification-function isBadgeDisplayed(bundle: BundleOption, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundle | [BundleOption](arkts-notification-notificationextensionsubscription-bundleoption-t.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |


## isBadgeDisplayed

```TypeScript
function isBadgeDisplayed(bundle: BundleOption): Promise<boolean>
```

Checks whether the notification badge is enabled for a specified application. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [isBadgeDisplayed](arkts-notification-notificationmanager-isbadgedisplayed-f-sys.md#isBadgeDisplayed-(System-API))

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function isBadgeDisplayed(bundle: BundleOption): Promise<boolean>--><!--Device-notification-function isBadgeDisplayed(bundle: BundleOption): Promise<boolean>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundle | [BundleOption](arkts-notification-notificationextensionsubscription-bundleoption-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |
