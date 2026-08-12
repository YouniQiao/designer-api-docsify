# distributeOperation (System API)

## Modules to Import

```TypeScript
import { notificationSubscribe } from '@kit.NotificationKit';
```

## distributeOperation

```TypeScript
function distributeOperation(hashcode: string, operationInfo?: OperationInfo): Promise<void>
```

Triggers a notification for cross-device operations, such as tap-to-redirect and quick reply. This API uses a promise to return the result.

**Since:** 18

**Required permissions:** ohos.permission.NOTIFICATION_CONTROLLER

<!--Device-notificationSubscribe-function distributeOperation(hashcode: string, operationInfo?: OperationInfo): Promise<void>--><!--Device-notificationSubscribe-function distributeOperation(hashcode: string, operationInfo?: OperationInfo): Promise<void>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| hashcode | string | Yes |
| [operationInfo](../../apis-ability-kit/arkts-apis/arkts-ability-abilitytoolaccessctrl-permissionquery-i-sys.md) | [OperationInfo](arkts-notification-notificationsubscribe-operationinfo-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [1600010](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600010-distributed-operation-failed) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [1600021](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-notification-kit/errorcode-notification.md#1600021-crossdevice-communication-timeout) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let hashcode: string = 'hashcode';
let operationInfo: notificationSubscribe.OperationInfo = {
  actionName: "actionName",
  userInput: "userInput",
  operationType: 1,
  buttonIndex: 1,
};
notificationSubscribe.distributeOperation(hashcode, operationInfo).then(() => {
  console.info("distributeOperation success");
}).catch((err: BusinessError) => {
  console.error(`distributeOperation fail, code is ${err.code}, message is ${err.message}`);
});
```
