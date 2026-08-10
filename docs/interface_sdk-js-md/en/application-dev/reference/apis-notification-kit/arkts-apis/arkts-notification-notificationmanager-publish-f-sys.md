# publish (System API)

## Modules to Import

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## publish

```TypeScript
function publish(request: NotificationRequest, userId: int, callback: AsyncCallback<void>): void
```

发布通知给指定的用户。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** 
- API version 18+: ohos.permission.NOTIFICATION_CONTROLLER or ohos.permission.SEND_NOTIFICATION_CROSS_USER
- API version 9 - 17: ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function publish(request: NotificationRequest, userId: int, callback: AsyncCallback<void>): void--><!--Device-notificationManager-function publish(request: NotificationRequest, userId: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| request | [NotificationRequest](arkts-notification-notificationmanager-notificationrequest-t.md) | Yes | 用于设置要发布通知的内容和相关配置信息。 |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 用户ID。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 被指定的回调方法。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | The device does not support geofencing.<br>**Applicable version:** 23 and later |
| 1600025 | Geofencing disabled.<br>**Applicable version:** 23 and later |
| 1600026 | The location switch is off.<br>**Applicable version:** 23 and later |
| 1600027 | The "Awareness & suggestions" switch of the location-based service is off.<br>**Applicable version:** 23 and later |
| 2300007 | Network unreachable.<br>**Applicable version:** 11 and later |
| 1600029 | The system failed to find the ExtensionAbility instance for the custom Live View widget template.<br>**Applicable version:** 26.0.0 and later |
| 1600016 | The notification version for this update is too low.<br>**Applicable version:** 11 and later |
| 201 | Permission denied. |
| 202 | Not system application to call the interface. |
| 1600020 | The application is not allowed to send notifications due to permission settings.<br>**Applicable version:** 18 and later |
| 1600008 | The user does not exist. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 1600009 | The notification sending frequency reaches the upper limit. |
| 1600012 | No memory space. |
| 1600014 | No permission.<br>**Applicable version:** 11 and later |
| 1600015 | The current notification status does not support duplicate configurations.<br>**Applicable version:** 11 and later |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600004 | Notification disabled. |
| 1600005 | Notification slot disabled. |
| 1600007 | The notification does not exist.<br>**Applicable version:** 11 and later |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// publish callback
let publishCallback = (err: BusinessError): void => {
    if (err) {
        console.error(`publish failed, code is ${err.code}, message is ${err.message}`);
    } else {
        console.info("publish success");
    }
}
// Use the actual user ID when calling the API.
let userId: number = 1;
// NotificationRequest object
let notificationRequest: notificationManager.NotificationRequest = {
    id: 1,
    content: {
        notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
        normal: {
            title: "test_title",
            text: "test_text",
            additionalText: "test_additionalText"
        }
    }
};
notificationManager.publish(notificationRequest, userId, publishCallback);
```


## publish

```TypeScript
function publish(request: NotificationRequest, userId: int): Promise<void>
```

发布通知给指定的用户。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** 
- API version 18+: ohos.permission.NOTIFICATION_CONTROLLER or ohos.permission.SEND_NOTIFICATION_CROSS_USER
- API version 9 - 17: ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function publish(request: NotificationRequest, userId: int): Promise<void>--><!--Device-notificationManager-function publish(request: NotificationRequest, userId: int): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| request | [NotificationRequest](arkts-notification-notificationmanager-notificationrequest-t.md) | Yes | 用于设置要发布通知的内容和相关配置信息。 |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 用户ID。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | The device does not support geofencing.<br>**Applicable version:** 23 and later |
| 1600025 | Geofencing disabled.<br>**Applicable version:** 23 and later |
| 1600026 | The location switch is off.<br>**Applicable version:** 23 and later |
| 1600027 | The "Awareness & suggestions" switch of the location-based service is off.<br>**Applicable version:** 23 and later |
| 2300007 | Network unreachable.<br>**Applicable version:** 11 and later |
| 1600029 | The system failed to find the ExtensionAbility instance for the custom Live View widget template.<br>**Applicable version:** 26.0.0 and later |
| 1600016 | The notification version for this update is too low.<br>**Applicable version:** 11 and later |
| 201 | Permission denied. |
| 202 | Not system application to call the interface. |
| 1600020 | The application is not allowed to send notifications due to permission settings.<br>**Applicable version:** 18 and later |
| 1600008 | The user does not exist. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 1600009 | The notification sending frequency reaches the upper limit. |
| 1600012 | No memory space. |
| 1600014 | No permission.<br>**Applicable version:** 11 and later |
| 1600015 | The current notification status does not support duplicate configurations.<br>**Applicable version:** 11 and later |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600004 | Notification disabled. |
| 1600005 | Notification slot disabled. |
| 1600007 | The notification does not exist.<br>**Applicable version:** 11 and later |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let notificationRequest: notificationManager.NotificationRequest = {
    id: 1,
    content: {
        notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
        normal: {
            title: "test_title",
            text: "test_text",
            additionalText: "test_additionalText"
        }
    }
};

// Use the actual user ID when calling the API.
let userId: number = 1;

notificationManager.publish(notificationRequest, userId).then(() => {
    console.info("publish success");
}).catch((err: BusinessError) => {
    console.error(`publish failed, code is ${err.code}, message is ${err.message}`);
});
```

