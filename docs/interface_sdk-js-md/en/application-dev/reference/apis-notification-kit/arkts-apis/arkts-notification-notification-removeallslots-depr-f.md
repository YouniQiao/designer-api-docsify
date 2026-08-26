# removeAllSlots

## Modules to Import

```TypeScript
import notificationManager from '@kit.NotificationKitManager';
import notificationSubscribe from '@kit.NotificationKitSubscribe';
import notificationExtensionSubscription from '@kit.NotificationKitExtensionSubscription';
```

## removeAllSlots

```TypeScript
function removeAllSlots(callback: AsyncCallback<void>): void
```

Removes all notification slots. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [removeAllSlots](arkts-notification-notificationmanager-removeallslots-f.md)

**System capability:** SystemCapability.Notification.Notification

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. |

**Examples**

```TypeScript
import Base from '@ohos.base';

let removeAllCallBack = (err: Base.BusinessError) => {
  if (err) {
    console.error("removeAllSlots failed " + JSON.stringify(err));
  } else {
    console.info("removeAllSlots success");
  }
}
Notification.removeAllSlots(removeAllCallBack);
```


## removeAllSlots

```TypeScript
function removeAllSlots(): Promise<void>
```

Removes all notification slots. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [removeAllSlots](arkts-notification-notificationmanager-removeallslots-f.md)

**System capability:** SystemCapability.Notification.Notification

**Return value:**

| Type | Description |
| --- | --- |
| Promise & lt;void & gt; | Promise that returns no value. |

**Examples**

```TypeScript
import Base from '@ohos.base';

Notification.removeAllSlots().then(() => {
  console.info("removeAllSlots success");
}).catch((err: Base.BusinessError) => {
  console.error(`removeAllSlots failed, code is ${err}`);
});
```
