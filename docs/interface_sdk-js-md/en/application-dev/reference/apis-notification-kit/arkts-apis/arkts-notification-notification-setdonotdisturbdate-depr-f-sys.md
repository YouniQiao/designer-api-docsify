# setDoNotDisturbDate (System API)

## setDoNotDisturbDate

```TypeScript
function setDoNotDisturbDate(date: DoNotDisturbDate, callback: AsyncCallback<void>): void
```

Sets the DND time. This API uses an asynchronous callback to return the result.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.notificationManager/notificationManager#setDoNotDisturbDate

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function setDoNotDisturbDate(date: DoNotDisturbDate, callback: AsyncCallback<void>): void--><!--Device-notification-function setDoNotDisturbDate(date: DoNotDisturbDate, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| date | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | DND time to set. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback used to return the result. |


## setDoNotDisturbDate

```TypeScript
function setDoNotDisturbDate(date: DoNotDisturbDate): Promise<void>
```

Sets the DND time. This API uses a promise to return the result.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.notificationManager/notificationManager#setDoNotDisturbDate

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function setDoNotDisturbDate(date: DoNotDisturbDate): Promise<void>--><!--Device-notification-function setDoNotDisturbDate(date: DoNotDisturbDate): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| date | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | DND time to set. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |


## setDoNotDisturbDate

```TypeScript
function setDoNotDisturbDate(date: DoNotDisturbDate, userId: number, callback: AsyncCallback<void>): void
```

Sets the DND time for a specified user. This API uses an asynchronous callback to return the result.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.notificationManager/notificationManager#setDoNotDisturbDate

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function setDoNotDisturbDate(date: DoNotDisturbDate, userId: number, callback: AsyncCallback<void>): void--><!--Device-notification-function setDoNotDisturbDate(date: DoNotDisturbDate, userId: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| date | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | DND time to set. |
| userId | number | Yes | ID of the user for whom you want to set the DND time. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | Callback used to return the result. |


## setDoNotDisturbDate

```TypeScript
function setDoNotDisturbDate(date: DoNotDisturbDate, userId: number): Promise<void>
```

Sets the DND time for a specified user. This API uses a promise to return the result.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.notificationManager/notificationManager#setDoNotDisturbDate

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function setDoNotDisturbDate(date: DoNotDisturbDate, userId: number): Promise<void>--><!--Device-notification-function setDoNotDisturbDate(date: DoNotDisturbDate, userId: number): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| date | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | DND time to set. |
| userId | number | Yes | ID of the user for whom you want to set the DND time. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

