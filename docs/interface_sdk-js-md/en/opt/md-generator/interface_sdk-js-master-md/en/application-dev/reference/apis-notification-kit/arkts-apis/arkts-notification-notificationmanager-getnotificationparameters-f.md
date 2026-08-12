# getNotificationParameters

## Modules to Import

```TypeScript
import { notificationManager } from '@kit.NotificationKit';
```

## getNotificationParameters

```TypeScript
function getNotificationParameters(id: number, label?: string): Promise<NotificationParameters>
```

Obtains some information about the **wantAgent** field in   
[NotificationRequest](arkts-notification-notificationrequest-notificationrequest-i.md#NotificationRequest). This API uses a promise to return the result.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-notificationManager-function getNotificationParameters(id: number, label?: string): Promise<NotificationParameters>--><!--Device-notificationManager-function getNotificationParameters(id: number, label?: string): Promise<NotificationParameters>-End-->

**System capability:** SystemCapability.Notification.Notification

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | number | Yes |
| label | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;NotificationParameters & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [1600001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600001-internal-error) |
| [1600002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |
| [1600007](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600007-notification-not-found) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let id: number = 0;
let label: string = "";
notificationManager.getNotificationParameters(id, label).then((data: notificationManager.NotificationParameters) => {
  console.info(`Succeeded in getting notification parameters, data is ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get notification parameters. Code is ${err.code}, message is ${err.message}`);
});
```
