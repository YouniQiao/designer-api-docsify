# publish（系统接口）

## 导入模块

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## publish

```TypeScript
function publish(request: NotificationRequest, userId: int, callback: AsyncCallback<void>): void
```

发布通知给指定的用户。使用callback异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** 
- API版本18+：ohos.permission.NOTIFICATION_CONTROLLER or ohos.permission.SEND_NOTIFICATION_CROSS_USER
- API版本9 - 17：ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function publish(request: NotificationRequest, userId: int, callback: AsyncCallback<void>): void--><!--Device-notificationManager-function publish(request: NotificationRequest, userId: int, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [NotificationRequest](arkts-notification-notificationmanager-notificationrequest-t.md) | 是 | 用于设置要发布通知的内容和相关配置信息。 |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | 用户ID。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | 被指定的回调方法。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | The device does not support geofencing.<br>**适用版本：** 23+ |
| 1600025 | Geofencing disabled.<br>**适用版本：** 23+ |
| 1600026 | The location switch is off.<br>**适用版本：** 23+ |
| 1600027 | The "Awareness & suggestions" switch of the location-based service is off.<br>**适用版本：** 23+ |
| 2300007 | Network unreachable.<br>**适用版本：** 11+ |
| 1600029 | The system failed to find the ExtensionAbility instance for the custom Live View widget template.<br>**适用版本：** 26.0.0+ |
| 1600016 | The notification version for this update is too low.<br>**适用版本：** 11+ |
| 201 | Permission denied. |
| 202 | Not system application to call the interface. |
| 1600020 | The application is not allowed to send notifications due to permission settings.<br>**适用版本：** 18+ |
| 1600008 | The user does not exist. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 1600009 | The notification sending frequency reaches the upper limit. |
| 1600012 | No memory space. |
| 1600014 | No permission.<br>**适用版本：** 11+ |
| 1600015 | The current notification status does not support duplicate configurations.<br>**适用版本：** 11+ |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600004 | Notification disabled. |
| 1600005 | Notification slot disabled. |
| 1600007 | The notification does not exist.<br>**适用版本：** 11+ |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// publish回调
let publishCallback = (err: BusinessError): void => {
    if (err) {
        console.error(`publish failed, code is ${err.code}, message is ${err.message}`);
    } else {
        console.info('publish success');
    }
}
// 用户ID，使用时需替换为真实的userId。
let userId: number = 1;
// 通知Request对象
let notificationRequest: notificationManager.NotificationRequest = {
    id: 1,
    content: {
        notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
        normal: {
            title: 'test_title',
            text: 'test_text',
            additionalText: 'test_additionalText'
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

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** 
- API版本18+：ohos.permission.NOTIFICATION_CONTROLLER or ohos.permission.SEND_NOTIFICATION_CROSS_USER
- API版本9 - 17：ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationManager-function publish(request: NotificationRequest, userId: int): Promise<void>--><!--Device-notificationManager-function publish(request: NotificationRequest, userId: int): Promise<void>-End-->

**系统能力：** SystemCapability.Notification.Notification

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [NotificationRequest](arkts-notification-notificationmanager-notificationrequest-t.md) | 是 | 用于设置要发布通知的内容和相关配置信息。 |
| userId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | 用户ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | The device does not support geofencing.<br>**适用版本：** 23+ |
| 1600025 | Geofencing disabled.<br>**适用版本：** 23+ |
| 1600026 | The location switch is off.<br>**适用版本：** 23+ |
| 1600027 | The "Awareness & suggestions" switch of the location-based service is off.<br>**适用版本：** 23+ |
| 2300007 | Network unreachable.<br>**适用版本：** 11+ |
| 1600029 | The system failed to find the ExtensionAbility instance for the custom Live View widget template.<br>**适用版本：** 26.0.0+ |
| 1600016 | The notification version for this update is too low.<br>**适用版本：** 11+ |
| 201 | Permission denied. |
| 202 | Not system application to call the interface. |
| 1600020 | The application is not allowed to send notifications due to permission settings.<br>**适用版本：** 18+ |
| 1600008 | The user does not exist. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 1600009 | The notification sending frequency reaches the upper limit. |
| 1600012 | No memory space. |
| 1600014 | No permission.<br>**适用版本：** 11+ |
| 1600015 | The current notification status does not support duplicate configurations.<br>**适用版本：** 11+ |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600004 | Notification disabled. |
| 1600005 | Notification slot disabled. |
| 1600007 | The notification does not exist.<br>**适用版本：** 11+ |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let notificationRequest: notificationManager.NotificationRequest = {
    id: 1,
    content: {
        notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
        normal: {
            title: 'test_title',
            text: 'test_text',
            additionalText: 'test_additionalText'
        }
    }
};

// 用户ID，使用时需替换为真实的userId。
let userId: number = 1;

notificationManager.publish(notificationRequest, userId).then(() => {
    console.info('publish success');
}).catch((err: BusinessError) => {
    console.error(`publish failed, code is ${err.code}, message is ${err.message}`);
});
```

