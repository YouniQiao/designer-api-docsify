# setDeviceIdleTrustlist (System API)

## Modules to Import

```TypeScript
import { policy } from '@kit.NetworkKit';
```

## setDeviceIdleTrustlist

```TypeScript
function setDeviceIdleTrustlist(uids: Array<number>, isAllowed: boolean, callback: AsyncCallback<void>): void
```

Set the list of uids that are allowed to access the Internet in hibernation mode.

**Since:** 10

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_NET_STRATEGY

<!--Device-policy-function setDeviceIdleTrustlist(uids: Array<number>, isAllowed: boolean, callback: AsyncCallback<void>): void--><!--Device-policy-function setDeviceIdleTrustlist(uids: Array<number>, isAllowed: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uids | Array & lt;number & gt; | Yes |
| isAllowed | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

policy.setDeviceIdleTrustlist([11111, 22222], true, (error: BusinessError) => {
  console.error(JSON.stringify(error));
});
```


## setDeviceIdleTrustlist

```TypeScript
function setDeviceIdleTrustlist(uids: Array<number>, isAllowed: boolean): Promise<void>
```

Set the list of uids that are allowed to access the Internet in hibernation mode.

**Since:** 10

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_NET_STRATEGY

<!--Device-policy-function setDeviceIdleTrustlist(uids: Array<number>, isAllowed: boolean): Promise<void>--><!--Device-policy-function setDeviceIdleTrustlist(uids: Array<number>, isAllowed: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uids | Array & lt;number & gt; | Yes |
| isAllowed | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

policy
  .setDeviceIdleTrustlist([11111, 22222], true)
  .then(() => {
    console.info('setDeviceIdleTrustlist success');
  })
  .catch((error: BusinessError) => {
    console.error(JSON.stringify(error));
  });
```
