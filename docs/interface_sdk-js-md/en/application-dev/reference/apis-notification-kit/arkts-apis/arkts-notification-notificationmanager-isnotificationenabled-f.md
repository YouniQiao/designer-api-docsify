# isNotificationEnabled

## Modules to Import

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## isNotificationEnabled

```TypeScript
function isNotificationEnabled(callback: AsyncCallback<boolean>): void
```

查询当前应用通知授权状态。使用callback异步回调。

用于在发布通知前检查当前应用是否被允许发送通知，避免在通知授权关闭时发布导致失败。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** 
- API version 9 - 10: ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function isNotificationEnabled(callback: AsyncCallback<boolean>): void--><!--Device-notificationManager-function isNotificationEnabled(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | 回调函数。返回true，表示允许发布通知；返回false，表示禁止发布通知；调用失败返回错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1600008 | The user does not exist.<br>**Applicable version:** 11 and later |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 201 | Permission denied.<br>**Applicable version:** 9 - 10 |
| 1600001 | Internal error. |
| 202 | Not system application to call the interface.<br>**Applicable version:** 9 - 10 |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 17700001 | The specified bundle name was not found.<br>**Applicable version:** 11 and later |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let isNotificationEnabledCallback = (err: BusinessError, data: boolean): void => {
  if (err) {
    console.error(`isNotificationEnabled failed, code is ${err.code}, message is ${err.message}`);
  } else {
    console.info(`isNotificationEnabled success, data is ${JSON.stringify(data)}`);
  }
}

notificationManager.isNotificationEnabled(isNotificationEnabledCallback);
```


## isNotificationEnabled

```TypeScript
function isNotificationEnabled(): Promise<boolean>
```

查询当前应用通知授权状态。使用Promise异步回调。

用于在发布通知前检查当前应用是否被允许发送通知，避免在通知使能关闭时发布导致失败。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** 
- API version 9 - 10: ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function isNotificationEnabled(): Promise<boolean>--><!--Device-notificationManager-function isNotificationEnabled(): Promise<boolean>-End-->

**System capability:** SystemCapability.Notification.Notification

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。返回true，表示允许发布通知；返回false，表示禁止发布通知。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1600008 | The user does not exist.<br>**Applicable version:** 11 and later |
| 201 | Permission denied.<br>**Applicable version:** 9 - 10 |
| 1600001 | Internal error. |
| 202 | Not system application to call the interface.<br>**Applicable version:** 9 - 10 |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 17700001 | The specified bundle name was not found.<br>**Applicable version:** 11 and later |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

notificationManager.isNotificationEnabled().then((data: boolean) => {
  console.info(`isNotificationEnabled success, data: ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`isNotificationEnabled failed, code is ${err.code}, message is ${err.message}`);
});
```

