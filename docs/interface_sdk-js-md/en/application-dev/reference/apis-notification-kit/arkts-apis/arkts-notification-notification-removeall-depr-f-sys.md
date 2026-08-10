# removeAll (System API)

## removeAll

```TypeScript
function removeAll(bundle: BundleOption, callback: AsyncCallback<void>): void
```

删除指定应用的所有通知（Callback形式）。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.notificationSubscribe/notificationSubscribe#removeAll

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function removeAll(bundle: BundleOption, callback: AsyncCallback<void>): void--><!--Device-notification-function removeAll(bundle: BundleOption, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundle | [BundleOption](arkts-notification-notificationextensionsubscription-bundleoption-t.md) | Yes | 指定应用的包信息。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 删除指定应用的所有通知回调函数。 |


## removeAll

```TypeScript
function removeAll(callback: AsyncCallback<void>): void
```

删除所有通知（Callback形式）。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.notificationSubscribe/notificationSubscribe#removeAll

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function removeAll(callback: AsyncCallback<void>): void--><!--Device-notification-function removeAll(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 删除所有通知回调函数。 |


## removeAll

```TypeScript
function removeAll(userId: number, callback: AsyncCallback<void>): void
```

删除指定用户下的所有通知（callback形式）。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.notificationSubscribe/notificationSubscribe#removeAll

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function removeAll(userId: number, callback: AsyncCallback<void>): void--><!--Device-notification-function removeAll(userId: number, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| userId | number | Yes | 用户ID。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 删除指定用户所有通知回调函数。 |


## removeAll

```TypeScript
function removeAll(userId: number): Promise<void>
```

删除指定用户下的所有通知（Promise形式）。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** ohos.notificationSubscribe/notificationSubscribe#removeAll

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function removeAll(userId: number): Promise<void>--><!--Device-notification-function removeAll(userId: number): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| userId | number | Yes | 用户ID。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |


## removeAll

```TypeScript
function removeAll(bundle?: BundleOption): Promise<void>
```

删除指定应用的所有通知（Promise形式）。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.notificationSubscribe/notificationSubscribe#removeAll

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notification-function removeAll(bundle?: BundleOption): Promise<void>--><!--Device-notification-function removeAll(bundle?: BundleOption): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundle | [BundleOption](arkts-notification-notificationextensionsubscription-bundleoption-t.md) | No | 指定应用的包信息。默认为空，表示删除所有通知。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

