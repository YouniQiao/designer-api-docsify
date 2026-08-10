# setDeviceIdleTrustlist (System API)

## Modules to Import

```TypeScript
import { policy } from 'kits/@kit.NetworkKit';
```

## setDeviceIdleTrustlist

```TypeScript
function setDeviceIdleTrustlist(uids: Array<number>, isAllowed: boolean, callback: AsyncCallback<void>): void
```

Set the list of uids that are allowed to access the Internet in hibernation mode.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Required permissions:** ohos.permission.MANAGE_NET_STRATEGY

<!--Device-policy-function setDeviceIdleTrustlist(uids: Array<number>, isAllowed: boolean, callback: AsyncCallback<void>): void--><!--Device-policy-function setDeviceIdleTrustlist(uids: Array<number>, isAllowed: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uids | Array&lt;number&gt; | Yes | The specified uids of application. |
| isAllowed | boolean | Yes | Whether to allow Uids in the list to access the Internet. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | the callback of setDeviceIdleTrustlist. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 201 | Permission denied. |
| 202 | Non-system applications use system APIs. |

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

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Required permissions:** ohos.permission.MANAGE_NET_STRATEGY

<!--Device-policy-function setDeviceIdleTrustlist(uids: Array<number>, isAllowed: boolean): Promise<void>--><!--Device-policy-function setDeviceIdleTrustlist(uids: Array<number>, isAllowed: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uids | Array&lt;number&gt; | Yes | The specified uids of application. |
| isAllowed | boolean | Yes | Whether to allow Uids in the list to access the Internet. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 201 | Permission denied. |
| 202 | Non-system applications use system APIs. |

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

