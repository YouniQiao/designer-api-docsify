# publish

## Modules to Import

```TypeScript
import notificationManager from '@kit.NotificationKitManager';
import notificationSubscribe from '@kit.NotificationKitSubscribe';
import notificationExtensionSubscription from '@kit.NotificationKitExtensionSubscription';
```

## publish

```TypeScript
function publish(request: NotificationRequest, callback: AsyncCallback<void>): void
```

Publishes a notification. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [publish](arkts-notification-notificationmanager-publish-f.md)

**System capability:** SystemCapability.Notification.Notification

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| request | [NotificationRequest](arkts-notification-notificationrequest-notificationrequest-i.md) | Yes | Content and related configuration of the notification to publish. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback used to return the result. |

**Examples**

```TypeScript
import NotificationManager from '@ohos.notificationManager';
import Base from '@ohos.base';

// publish callback
let publishCallback = (err: Base.BusinessError) => {
  if (err) {
    console.error(`publish failed, code is ${err}`);
  } else {
    console.info("publish success");
  }
}
// NotificationRequest object
let notificationRequest: NotificationManager.NotificationRequest = {
  id: 1,
  content: {
    contentType: Notification.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
    normal: {
      title: "test_title",
      text: "test_text",
      additionalText: "test_additionalText"
    }
  }
};
Notification.publish(notificationRequest, publishCallback);
```


## publish

```TypeScript
function publish(request: NotificationRequest): Promise<void>
```

Publishes a notification. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [publish](arkts-notification-notificationmanager-publish-f.md)

**System capability:** SystemCapability.Notification.Notification

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| request | [NotificationRequest](arkts-notification-notificationrequest-notificationrequest-i.md) | Yes | Content and related configuration of the notification to publish. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise & lt;void & gt; | Promise that returns no value. |

**Examples**

```TypeScript
import NotificationManager from '@ohos.notificationManager';
import Base from '@ohos.base';

// NotificationRequest object
let notificationRequest: NotificationManager.NotificationRequest = {
  id: 1,
  content: {
    contentType: Notification.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
    normal: {
      title: "test_title",
      text: "test_text",
      additionalText: "test_additionalText"
    }
  }
};
Notification.publish(notificationRequest).then(() => {
  console.info("publish success");
}).catch((err: Base.BusinessError) => {
  console.error(`publish failed, code is ${err}`);
});
```
