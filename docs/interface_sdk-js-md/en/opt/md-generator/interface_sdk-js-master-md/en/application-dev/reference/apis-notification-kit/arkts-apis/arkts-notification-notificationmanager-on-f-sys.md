# on (System API)

## Modules to Import

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## on('checkNotification')

```TypeScript
function on(type: 'checkNotification', callback: (checkInfo: NotificationCheckInfo) => NotificationCheckResult): void
```

Subscribes to notification events. The notification service sends the notification information in the callback to the verification program. The verification program returns the verification result to determine whether to publish the notification, for example, controlling the publication frequency of marketing notifications.

Each [SlotType](arkts-notification-notificationmanager-slottype-e.md#SlotType) in the system can have only one registrant.

This API can be properly called on devices other than wearables. If it is called on wearables, error code 801 is returned.

**Since:** 10

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER and ohos.permission.NOTIFICATION_AGENT_CONTROLLER

<!--Device-notificationManager-function on(type: 'checkNotification', callback: (checkInfo: NotificationCheckInfo) => NotificationCheckResult): void--><!--Device-notificationManager-function on(type: 'checkNotification', callback: (checkInfo: NotificationCheckInfo) => NotificationCheckResult): void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'checkNotification' | Yes |
| callback | (checkInfo: NotificationCheckInfo) = & gt; NotificationCheckResult | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [1600001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let onCheckNotification = (info : notificationManager.NotificationCheckInfo): notificationManager.NotificationCheckResult => {
    console.info(`====>OnCheckNotification info: ${JSON.stringify(info)}`);
    if(info.notificationId == 1){
        let result: notificationManager.NotificationCheckResult =  { code: 1, message: "testMsg1"};
        return result;
    } else {
        let result: notificationManager.NotificationCheckResult =   { code: 0, message: "testMsg0"};
        return result;
    }
}
try{
    notificationManager.on("checkNotification", onCheckNotification);
} catch (err){
    console.error(`notificationManager.on failed, code is ${err.code}, message is ${err.message}`);
}
```


## on('checkNotification')

```TypeScript
function on(type: 'checkNotification', checkRequest: NotificationCheckRequest,
    callback: (checkInfo: NotificationCheckInfo) => Promise<NotificationCheckResult>): void
```

Subscribes to notification events. The notification service sends the notification information in the callback to the verification program. The verification program returns the verification result to determine whether to publish the notification, for example, controlling the publication frequency of marketing notifications. This API uses a promise to return the result.

Each [SlotType](arkts-notification-notificationmanager-slottype-e.md#SlotType) in the system can have only one registrant.

This API can be properly called on devices other than wearables. If it is called on wearables, error code 801 is returned.

**Since:** 11

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER and ohos.permission.NOTIFICATION_AGENT_CONTROLLER

<!--Device-notificationManager-function on(type: 'checkNotification', checkRequest: NotificationCheckRequest,    callback: (checkInfo: NotificationCheckInfo) => Promise<NotificationCheckResult>): void--><!--Device-notificationManager-function on(type: 'checkNotification', checkRequest: NotificationCheckRequest,    callback: (checkInfo: NotificationCheckInfo) => Promise<NotificationCheckResult>): void-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'checkNotification' | Yes |
| checkRequest | [NotificationCheckRequest](arkts-notification-notificationrequest-notificationcheckrequest-i-sys.md) | Yes |
| callback | (checkInfo: NotificationCheckInfo) =&gt; Promise&lt;[NotificationCheckResult](arkts-notification-notificationmanager-notificationcheckresult-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [1600001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-internal-error) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1600002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try{
  notificationManager.on('checkNotification',{
    contentType: notificationManager.ContentType.NOTIFICATION_CONTENT_LIVE_VIEW,
    slotType: notificationManager.SlotType.LIVE_VIEW ,
    extraInfoKeys: ["event"],
  },
    async (checkInfo)=>{
      return { code: 1, message: "INVALID_PARAMETERS"};
  },);
} catch (err) {
  console.error(`notificationManager.on failed, code is ${err.code}, message is ${err.message}`);
}
```
