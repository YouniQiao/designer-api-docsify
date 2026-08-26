# remove (System API)

## Modules to Import

```TypeScript
import notificationManager from '@kit.NotificationKitManager';
import notificationSubscribe from '@kit.NotificationKitSubscribe';
import notificationExtensionSubscription from '@kit.NotificationKitExtensionSubscription';
```

## remove

```TypeScript
function remove(
    bundle: BundleOption,
    notificationKey: NotificationKey,
    reason: RemoveReason,
    callback: AsyncCallback<void>
  ): void
```

Removes a notification for a specified bundle. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [remove](arkts-notification-notificationsubscribe-remove-f-sys.md)

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundle | [BundleOption](arkts-notification-notificationcommondef-bundleoption-i.md) | Yes | Bundle information of the application. |
| notificationKey | [NotificationKey](arkts-notification-notificationsubscribe-notificationkey-i-sys.md) | Yes | Notification key. |
| reason | [RemoveReason](arkts-notification-notificationsubscribe-removereason-e-sys.md) | Yes | Reason for deleting a notification. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. |

**Examples**

```TypeScript
import Base from '@ohos.base';

let removeCallback = (err: Base.BusinessError) => {
  if (err) {
    console.error("remove failed " + JSON.stringify(err));
  } else {
    console.info("remove success");
  }
}
let bundle: Notification.BundleOption = {
  bundle: "bundleName1",
};
let notificationKey: Notification.NotificationKey = {
  id: 0,
  label: "label",
};
let reason: Notification.RemoveReason = Notification.RemoveReason.CLICK_REASON_REMOVE;
Notification.remove(bundle, notificationKey, reason, removeCallback);
```


## remove

```TypeScript
function remove(bundle: BundleOption, notificationKey: NotificationKey, reason: RemoveReason): Promise<void>
```

Removes a notification for a specified bundle. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [remove](arkts-notification-notificationsubscribe-remove-f-sys.md)

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundle | [BundleOption](arkts-notification-notificationcommondef-bundleoption-i.md) | Yes | Bundle information of the application. |
| notificationKey | [NotificationKey](arkts-notification-notificationsubscribe-notificationkey-i-sys.md) | Yes | Notification key. |
| reason | [RemoveReason](arkts-notification-notificationsubscribe-removereason-e-sys.md) | Yes | Reason for deleting a notification. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise & lt;void & gt; | Promise that returns no value. |

**Examples**

```TypeScript
import Base from '@ohos.base';

let bundle: Notification.BundleOption = {
  bundle: "bundleName1",
};
let notificationKey: Notification.NotificationKey = {
  id: 0,
  label: "label",
};
let reason: Notification.RemoveReason = Notification.RemoveReason.CLICK_REASON_REMOVE;
Notification.remove(bundle, notificationKey, reason).then(() => {
  console.info("remove success");
}).catch((err: Base.BusinessError) => {
  console.error(`remove failed, code is ${err}`);
});
```


## remove

```TypeScript
function remove(hashCode: string, reason: RemoveReason, callback: AsyncCallback<void>): void
```

Removes a notification for a specified bundle. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [remove](arkts-notification-notificationsubscribe-remove-f-sys.md)

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| hashCode | string | Yes | Unique notification ID. It is the value of **hashCode** in the [NotificationRequest](arkts-notification-notificationrequest-notificationrequest-i.md) object of [SubscribeCallbackData](arkts-notification-notificationsubscriber-subscribecallbackdata-i-sys.md) used in the [onConsume](arkts-notification-notificationsubscriber-notificationsubscriber-i-sys.md#onconsume) callback. |
| reason | [RemoveReason](arkts-notification-notificationsubscribe-removereason-e-sys.md) | Yes | Reason for deleting a notification. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. |

**Examples**

```TypeScript
import Base from '@ohos.base';

let hashCode: string = 'hashCode';

let removeCallback = (err: Base.BusinessError) => {
  if (err) {
    console.error("remove failed " + JSON.stringify(err));
  } else {
    console.info("remove success");
  }
}
let reason: Notification.RemoveReason = Notification.RemoveReason.CANCEL_REASON_REMOVE;
Notification.remove(hashCode, reason, removeCallback);
```


## remove

```TypeScript
function remove(hashCode: string, reason: RemoveReason): Promise<void>
```

Removes a notification for a specified bundle. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [remove](arkts-notification-notificationsubscribe-remove-f-sys.md)

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| hashCode | string | Yes | Unique notification ID. |
| reason | [RemoveReason](arkts-notification-notificationsubscribe-removereason-e-sys.md) | Yes | Reason for deleting a notification. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise & lt;void & gt; | Promise that returns no value. |

**Examples**

```TypeScript
import Base from '@ohos.base';

let hashCode: string = 'hashCode';
let reason: Notification.RemoveReason = Notification.RemoveReason.CLICK_REASON_REMOVE;
Notification.remove(hashCode, reason).then(() => {
  console.info("remove success");
}).catch((err: Base.BusinessError) => {
  console.error(`remove failed, code is ${err}`);
});
```
