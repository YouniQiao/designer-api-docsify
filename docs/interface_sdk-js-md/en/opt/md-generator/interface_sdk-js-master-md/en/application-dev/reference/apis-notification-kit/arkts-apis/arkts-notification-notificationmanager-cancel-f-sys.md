# cancel (System API)

## Modules to Import

```TypeScript
import { notificationManager } from 'kits/@kit.NotificationKit';
```

## cancel

```TypeScript
function cancel(representativeBundle: BundleOption, id: number): Promise<void>
```

Cancels the notification of other applications of the user. This API uses a promise to return the result.

The current application must have a proxy relationship with another application, or the   
**ohos.permission.NOTIFICATION_AGENT_CONTROLLER** permission is granted to the current application.

**Since:** 12

<!--Device-notificationManager-function cancel(representativeBundle: BundleOption, id: int): Promise<void>--><!--Device-notificationManager-function cancel(representativeBundle: BundleOption, id: int): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| representativeBundle | [BundleOption](arkts-notification-notificationcommondef-bundleoption-i.md) | Yes |
| id | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [1600012](../errorcode-notification.md#1600012-insufficient-memory-space) |
| [1600001](../errorcode-notification.md#1600001-internal-error) |
| [1600017](../errorcode-notification.md#1600017-no-configured-proxy-relationship) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1600002](../errorcode-notification.md#1600002-marshalling-or-unmarshalling-error) |
| [1600003](../errorcode-notification.md#1600003-failed-to-connect-to-the-notification-service) |
| [1600007](../errorcode-notification.md#1600007-notification-not-found) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let bundle: notificationManager.BundleOption = {
  bundle: "bundleName"
};
let id: number = 1;
notificationManager.cancel(bundle, id).then(() => {
  console.info("cancel success");
}).catch((err: BusinessError) => {
  console.error(`cancel failed, code is ${err.code}, message is ${err.message}`);
});
```
