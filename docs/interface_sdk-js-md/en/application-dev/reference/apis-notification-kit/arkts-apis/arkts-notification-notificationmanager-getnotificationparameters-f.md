# getNotificationParameters

## Modules to Import

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## getNotificationParameters

```TypeScript
function getNotificationParameters(id: number, label?: string): Promise<NotificationParameters>
```

获取通知[NotificationRequest](arkts-notification-notificationmanager-notificationrequest-t.md)中wantAgent字段的部分信息。使用Promise异步回调。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-notificationManager-function getNotificationParameters(id: number, label?: string): Promise<NotificationParameters>--><!--Device-notificationManager-function getNotificationParameters(id: number, label?: string): Promise<NotificationParameters>-End-->

**System capability:** SystemCapability.Notification.Notification

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | number | Yes | 通知ID，用于标识目标通知。该值由发布通知时NotificationRequest的id字段指定。 |
| label | string | No | 通知标签，默认为空。该值由发布通知时NotificationRequest的label字段指定。 - 若标签为空，则获取与指定通知ID匹配，标签为空的已发布通知的部分信息。 - 若标签不为空，则获取与指定通知ID和标签同时匹配的已发布通知的部分信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;NotificationParameters&gt; | Promise对象，返回wantAgent的部分信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600007 | The notification does not exist. |

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


## getNotificationParameters

```TypeScript
function getNotificationParameters(id: int, label?: string): Promise<NotificationParameters | null>
```

获取通知[NotificationRequest](arkts-notification-notificationmanager-notificationrequest-t.md)中wantAgent字段的部分信息。使用Promise异步回调。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-notificationManager-function getNotificationParameters(id: int, label?: string): Promise<NotificationParameters | null>--><!--Device-notificationManager-function getNotificationParameters(id: int, label?: string): Promise<NotificationParameters | null>-End-->

**System capability:** SystemCapability.Notification.Notification

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | int | Yes | 通知ID，用于标识目标通知。该值由发布通知时NotificationRequest的id字段指定。 |
| label | string | No | 通知标签，默认为空。该值由发布通知时NotificationRequest的label字段指定。 - 若标签为空，则获取与指定通知ID匹配，标签为空的已发布通知的部分信息。 - 若标签不为空，则获取与指定通知ID和标签同时匹配的已发布通知的部分信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;NotificationParameters \| null&gt; | Promise对象，返回wantAgent的部分信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 1600001 | Internal error. |
| 1600002 | Marshalling or unmarshalling error. |
| 1600003 | Failed to connect to the service. |
| 1600007 | The notification does not exist. |

