# getSlotsByBundle (System API)

## Modules to Import

```TypeScript
import notificationManager from '@kit.NotificationKitManager';
import notificationSubscribe from '@kit.NotificationKitSubscribe';
import notificationExtensionSubscription from '@kit.NotificationKitExtensionSubscription';
```

## getSlotsByBundle

```TypeScript
function getSlotsByBundle(bundle: BundleOption, callback: AsyncCallback<Array<NotificationSlot>>): void
```

Obtains the notification slots of a specified application. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getSlotsByBundle](arkts-notification-notificationmanager-getslotsbybundle-f-sys.md)

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundle | [BundleOption](arkts-notification-notificationcommondef-bundleoption-i.md) | Yes | Bundle information of the application. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[NotificationSlot](arkts-notification-notificationslot-notificationslot-i.md)&gt;&gt; | Yes | Callback used to return the result. |

**Examples**

```TypeScript
import Base from '@ohos.base';
import NotificationManager from '@ohos.notificationManager';

let getSlotsByBundleCallback = (err: Base.BusinessError, data: NotificationManager.NotificationSlot[]) => {
  if (err) {
    console.error("getSlotsByBundle failed " + JSON.stringify(err));
  } else {
    console.info("getSlotsByBundle success");
  }
}
let bundle: Notification.BundleOption = {
  bundle: "bundleName1",
};
Notification.getSlotsByBundle(bundle, getSlotsByBundleCallback);
```


## getSlotsByBundle

```TypeScript
function getSlotsByBundle(bundle: BundleOption): Promise<Array<NotificationSlot>>
```

Obtains the notification slots of a specified application. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getSlotsByBundle](arkts-notification-notificationmanager-getslotsbybundle-f-sys.md)

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundle | [BundleOption](arkts-notification-notificationcommondef-bundleoption-i.md) | Yes | Bundle information of the application. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[NotificationSlot](arkts-notification-notificationslot-notificationslot-i.md)&gt;&gt; | Promise used to return the result. |

**Examples**

```TypeScript
import Base from '@ohos.base';
import NotificationManager from '@ohos.notificationManager';

let bundle: Notification.BundleOption = {
  bundle: "bundleName1",
};
Notification.getSlotsByBundle(bundle).then((data: NotificationManager.NotificationSlot[]) => {
  console.info("getSlotsByBundle success, data: " + JSON.stringify(data));
}).catch((err: Base.BusinessError) => {
  console.error(`getSlotsByBundle failed, code is ${err}`);
});
```
