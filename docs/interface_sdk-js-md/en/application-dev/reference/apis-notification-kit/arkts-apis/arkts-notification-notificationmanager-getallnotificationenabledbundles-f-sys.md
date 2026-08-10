# getAllNotificationEnabledBundles (System API)

## Modules to Import

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## getAllNotificationEnabledBundles

```TypeScript
function getAllNotificationEnabledBundles(): Promise<Array<BundleOption>>
```

获取允许通知的应用列表。使用Promise异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function getAllNotificationEnabledBundles(): Promise<Array<BundleOption>>--><!--Device-notificationManager-function getAllNotificationEnabledBundles(): Promise<Array<BundleOption>>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;BundleOption&gt;&gt; | 返回允许通知的应用列表。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission denied. |
| 1600001 | Internal error. |
| 202 | Not system application to call the interface. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.getAllNotificationEnabledBundles().then((data: Array<notificationManager.BundleOption>) => {
    console.info(`Enable bundle data is ${JSON.stringify(data)}`);
    data.forEach(element => {
        console.info(`Enable uid is ${JSON.stringify(element.uid)}`);
        console.info(`Enable bundle is ${JSON.stringify(element.bundle)}`);
    });
}).catch((err: BusinessError) => {
    console.error(`getAllNotificationEnabledBundles failed, code is ${err.code}, message is ${err.message}`);
})
```


## getAllNotificationEnabledBundles

```TypeScript
function getAllNotificationEnabledBundles(userId: int): Promise<Array<BundleOption>>
```

获取指定用户下允许通知的应用列表。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function getAllNotificationEnabledBundles(userId: int): Promise<Array<BundleOption>>--><!--Device-notificationManager-function getAllNotificationEnabledBundles(userId: int): Promise<Array<BundleOption>>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 要获取允许通知的应用列表的用户。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;BundleOption&gt;&gt; | 返回允许通知的应用列表。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1600008 | The user does not exist. |
| 201 | Permission denied. |
| 1600001 | Internal error. |
| 202 | Not system application to call the interface. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let userId : number = 100;

notificationManager.getAllNotificationEnabledBundles(userId).then((data: Array<notificationManager.BundleOption>) => {
  console.info(`Enable bundle data is ${JSON.stringify(data)}`);
  data.forEach(element => {
    console.info(`Enable uid is ${JSON.stringify(element.uid)}`);
    console.info(`Enable bundle is ${JSON.stringify(element.bundle)}`);
  });
}).catch((err: BusinessError) => {
  console.error(`getAllNotificationEnabledBundles failed, code is ${err.code}, message is ${err.message}`);
});
```

