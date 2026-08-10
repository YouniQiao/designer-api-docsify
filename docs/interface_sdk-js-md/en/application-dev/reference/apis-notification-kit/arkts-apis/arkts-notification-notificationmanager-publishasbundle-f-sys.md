# publishAsBundle (System API)

## Modules to Import

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## publishAsBundle

```TypeScript
function publishAsBundle(
    request: NotificationRequest,
    representativeBundle: string,
    userId: int,
    callback: AsyncCallback<void>
  ): void
```

发布代理通知。使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER and ohos.permission.NOTIFICATION_AGENT_CONTROLLER

<!--Device-notificationManager-function publishAsBundle(    request: NotificationRequest,    representativeBundle: string,    userId: int,    callback: AsyncCallback<void>  ): void--><!--Device-notificationManager-function publishAsBundle(    request: NotificationRequest,    representativeBundle: string,    userId: int,    callback: AsyncCallback<void>  ): void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| request | [NotificationRequest](arkts-notification-notificationmanager-notificationrequest-t.md) | Yes | 用于设置要发布通知的内容和相关配置信息。 |
| representativeBundle | string | Yes | 被代理应用的包名。 |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 用户ID。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 发布代理通知的回调方法。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | The device does not support geofencing.<br>**Applicable version:** 23 and later |
| 1600025 | Geofencing disabled.<br>**Applicable version:** 23 and later |
| 1600026 | The location switch is off.<br>**Applicable version:** 23 and later |
| 1600027 | The "Awareness & suggestions" switch of the location-based service is off.<br>**Applicable version:** 23 and later |
| 2300007 | Network unreachable. |
| 1600029 | The system failed to find the ExtensionAbility instance for the custom Live View widget template.<br>**Applicable version:** 26.0.0 and later |
| 1600016 | The notification version for this update is too low. |
| 201 | Permission denied. |
| 202 | Not system application to call the interface. |
| 1600020 | The application is not allowed to send notifications due to permission settings. |
| 1600008 | The user does not exist. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 1600009 | The notification sending frequency reaches the upper limit. |
| 1600012 | No memory space. |
| 1600014 | The right of liveView is not enabled.<br>**Applicable version:** 26.0.0 and later |
| 1600015 | The current notification status does not support duplicate configurations. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600004 | Notification disabled. |
| 1600005 | Notification slot disabled. |
| 1600007 | The notification does not exist. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// publishAsBundle callback
let callback = (err: BusinessError): void => {
    if (err) {
        console.error(`publishAsBundle failed, code is ${err.code}, message is ${err.message}`);
    } else {
        console.info("publishAsBundle success");
    }
}
// Bundle name of the application whose notification function is taken over by the reminder agent
let representativeBundle: string = "com.example.demo";
// Use the actual user ID when calling the API.
let userId: number = 100;
// NotificationRequest object
let request: notificationManager.NotificationRequest = {
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
notificationManager.publishAsBundle(request, representativeBundle, userId, callback);
```


## publishAsBundle

```TypeScript
function publishAsBundle(request: NotificationRequest, representativeBundle: string, userId: int): Promise<void>
```

发布代理通知。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER and ohos.permission.NOTIFICATION_AGENT_CONTROLLER

<!--Device-notificationManager-function publishAsBundle(request: NotificationRequest, representativeBundle: string, userId: int): Promise<void>--><!--Device-notificationManager-function publishAsBundle(request: NotificationRequest, representativeBundle: string, userId: int): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| request | [NotificationRequest](arkts-notification-notificationmanager-notificationrequest-t.md) | Yes | 用于设置要发布通知的内容和相关配置信息。 |
| representativeBundle | string | Yes | 被代理应用的包名。 |
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
| 2300007 | Network unreachable. |
| 1600029 | The system failed to find the ExtensionAbility instance for the custom Live View widget template.<br>**Applicable version:** 26.0.0 and later |
| 1600016 | The notification version for this update is too low. |
| 201 | Permission denied. |
| 202 | Not system application to call the interface. |
| 1600020 | The application is not allowed to send notifications due to permission settings. |
| 1600008 | The user does not exist. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 1600009 | The notification sending frequency reaches the upper limit. |
| 1600012 | No memory space. |
| 1600014 | The right of liveView is not enabled.<br>**Applicable version:** 26.0.0 and later |
| 1600015 | The current notification status does not support duplicate configurations. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600004 | Notification disabled. |
| 1600005 | Notification slot disabled. |
| 1600007 | The notification does not exist. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Bundle name of the application whose notification function is taken over by the reminder agent
let representativeBundle: string = "com.example.demo";
// Use the actual user ID when calling the API.
let userId: number = 100;
// NotificationRequest object
let request: notificationManager.NotificationRequest = {
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
notificationManager.publishAsBundle(request, representativeBundle, userId).then(() => {
    console.info("publishAsBundle success");
}).catch((err: BusinessError) => {
    console.error(`publishAsBundle failed, code is ${err.code}, message is ${err.message}`);
});
```


## publishAsBundle

```TypeScript
function publishAsBundle(representativeBundle: BundleOption, request: NotificationRequest): Promise<void>
```

发布代理通知。使用Promise异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER and ohos.permission.NOTIFICATION_AGENT_CONTROLLER

<!--Device-notificationManager-function publishAsBundle(representativeBundle: BundleOption, request: NotificationRequest): Promise<void>--><!--Device-notificationManager-function publishAsBundle(representativeBundle: BundleOption, request: NotificationRequest): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| representativeBundle | [BundleOption](arkts-notification-notificationextensionsubscription-bundleoption-t.md) | Yes | 被代理应用的包信息。 |
| request | [NotificationRequest](arkts-notification-notificationmanager-notificationrequest-t.md) | Yes | 用于设置要发布通知的内容和相关配置信息。 |

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
| 2300007 | Network unreachable. |
| 1600029 | The system failed to find the ExtensionAbility instance for the custom Live View widget template.<br>**Applicable version:** 26.0.0 and later |
| 1600016 | The notification version for this update is too low. |
| 201 | Permission denied. |
| 202 | Not system application to call the interface. |
| 1600020 | The application is not allowed to send notifications due to permission settings. |
| 1600008 | The user does not exist. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 1600009 | The notification sending frequency reaches the upper limit. |
| 1600012 | No memory space. |
| 1600014 | The right of liveView is not enabled.<br>**Applicable version:** 26.0.0 and later |
| 1600015 | The current notification status does not support duplicate configurations. |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600004 | Notification disabled. |
| 1600005 | Notification slot disabled. |
| 1600007 | The notification does not exist. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Bundle information of the application whose notification function is taken over by the reminder agent.
let representativeBundle: notificationManager.BundleOption = {
  bundle: "bundleName1",
};
// NotificationRequest object
let request: notificationManager.NotificationRequest = {
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
notificationManager.publishAsBundle(representativeBundle, request).then(() => {
    console.info("publishAsBundle success");
}).catch((err: BusinessError) => {
    console.error(`publishAsBundle failed, code is ${err.code}, message is ${err.message}`);
});
```

