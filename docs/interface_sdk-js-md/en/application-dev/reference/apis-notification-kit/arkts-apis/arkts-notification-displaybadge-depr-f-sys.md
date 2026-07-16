# displayBadge (System API)

## displayBadge

```TypeScript
function displayBadge(bundle: BundleOption, enable: boolean, callback: AsyncCallback<void>): void
```

Sets whether to enable the notification badge for a specified application.This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** displayBadge

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function displayBadge(bundle: BundleOption, enable: boolean, callback: AsyncCallback<void>): void--><!--Device-notification-function displayBadge(bundle: BundleOption, enable: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundle | [BundleOption](arkts-notification-bundleoption-i.md) | Yes | Bundle information of the application. |
| enable | boolean | Yes | Whether to enable notification. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-i.md)<void> | Yes | Callback used to return the result. |


## displayBadge

```TypeScript
function displayBadge(bundle: BundleOption, enable: boolean): Promise<void>
```

Sets whether to enable the notification badge for a specified application.This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** displayBadge

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function displayBadge(bundle: BundleOption, enable: boolean): Promise<void>--><!--Device-notification-function displayBadge(bundle: BundleOption, enable: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundle | [BundleOption](arkts-notification-bundleoption-i.md) | Yes | Bundle information of the application. |
| enable | boolean | Yes | Whether to enable notification. |

**Return value:**

| Type | Description |
| --- | --- |
| [Promise](../../apis-na/arkts-apis/arkts-na-promise-i.md)<void> | Promise that returns no value. |

