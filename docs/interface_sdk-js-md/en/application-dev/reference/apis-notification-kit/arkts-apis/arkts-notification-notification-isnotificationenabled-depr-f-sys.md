# isNotificationEnabled (System API)

## Modules to Import

```TypeScript
```

## isNotificationEnabled

```TypeScript
function isNotificationEnabled(bundle: BundleOption, callback: AsyncCallback<boolean>): void
```

Checks whether notification is enabled for a specified application. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f.md)

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundle | BundleOption | Yes | Bundle information of the application. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | Callback used to return the result. |

**Examples**

```TypeScript
import Base from '@ohos.base';

let isNotificationEnabledCallback = (err: Base.BusinessError, data: boolean) => {
  if (err) {
    console.error("isNotificationEnabled failed " + JSON.stringify(err));
  } else {
    console.info("isNotificationEnabled success");
  }
}
let bundle: Notification.BundleOption = {
  bundle: "bundleName1",
};
Notification.isNotificationEnabled(bundle, isNotificationEnabledCallback);
```


## isNotificationEnabled

```TypeScript
function isNotificationEnabled(bundle: BundleOption): Promise<boolean>
```

Checks whether notification is enabled for a specified application. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f.md)

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundle | BundleOption | Yes | Bundle information of the application. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result. |

**Examples**

```TypeScript
import Base from '@ohos.base';

let bundle: Notification.BundleOption = {
  bundle: "bundleName1",
};
Notification.isNotificationEnabled(bundle).then((data) => {
  console.info("isNotificationEnabled success, data: " + JSON.stringify(data));
}).catch((err: Base.BusinessError) => {
  console.error(`isNotificationEnabled failed, code is ${err}`);
});
```


## isNotificationEnabled

```TypeScript
function isNotificationEnabled(callback: AsyncCallback<boolean>): void
```

Checks whether notification is enabled for this application. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f.md)

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | Callback used to return the result. |

**Examples**

```TypeScript
import Base from '@ohos.base';

let isNotificationEnabledCallback = (err: Base.BusinessError, data: boolean) => {
  if (err) {
    console.error("isNotificationEnabled failed " + JSON.stringify(err));
  } else {
    console.info("isNotificationEnabled success");
  }
}

Notification.isNotificationEnabled(isNotificationEnabledCallback);
```


## isNotificationEnabled

```TypeScript
function isNotificationEnabled(): Promise<boolean>
```

Checks whether notification is enabled for this application. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f.md)

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result. |

**Examples**

```TypeScript
import Base from '@ohos.base';

Notification.isNotificationEnabled().then((data: boolean) => {
  console.info("isNotificationEnabled success, data: " + JSON.stringify(data));
}).catch((err: Base.BusinessError) => {
  console.error(`isNotificationEnabled failed, code is ${err}`);
});
```


## isNotificationEnabled

```TypeScript
function isNotificationEnabled(userId: number, callback: AsyncCallback<boolean>): void
```

Checks whether notification is enabled for a specified user. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f.md)

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| userId | number | Yes | User ID. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | Callback used to return the result. The value **true** means that the notification is enabled, and **false** means the opposite. |

**Examples**

```TypeScript
import Base from '@ohos.base';

let isNotificationEnabledCallback = (err: Base.BusinessError, data: boolean) => {
  if (err) {
    console.error("isNotificationEnabled failed " + JSON.stringify(err));
  } else {
    console.info("isNotificationEnabled success");
  }
}
let bundle: Notification.BundleOption = {
  bundle: "bundleName1",
};
Notification.isNotificationEnabled(bundle, isNotificationEnabledCallback);
```

```TypeScript
import Base from '@ohos.base';

let bundle: Notification.BundleOption = {
  bundle: "bundleName1",
};
Notification.isNotificationEnabled(bundle).then((data) => {
  console.info("isNotificationEnabled success, data: " + JSON.stringify(data));
}).catch((err: Base.BusinessError) => {
  console.error(`isNotificationEnabled failed, code is ${err}`);
});
```

```TypeScript
import Base from '@ohos.base';

let isNotificationEnabledCallback = (err: Base.BusinessError, data: boolean) => {
  if (err) {
    console.error("isNotificationEnabled failed " + JSON.stringify(err));
  } else {
    console.info("isNotificationEnabled success");
  }
}

Notification.isNotificationEnabled(isNotificationEnabledCallback);
```

```TypeScript
import Base from '@ohos.base';

Notification.isNotificationEnabled().then((data: boolean) => {
  console.info("isNotificationEnabled success, data: " + JSON.stringify(data));
}).catch((err: Base.BusinessError) => {
  console.error(`isNotificationEnabled failed, code is ${err}`);
});
```


## isNotificationEnabled

```TypeScript
function isNotificationEnabled(userId: number): Promise<boolean>
```

Checks whether notification is enabled for a specified user. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [isNotificationEnabled](arkts-notification-notificationmanager-isnotificationenabled-f.md)

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| userId | number | Yes | User ID. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result. The value **true** means that the notification is enabled, and **false** means the opposite. |

**Examples**

See [isNotificationEnabled](#isnotificationenabled)
