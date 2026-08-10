# getUidsByPolicy (System API)

## Modules to Import

```TypeScript
import { policy } from 'kits/@kit.NetworkKit';
```

## getUidsByPolicy

```TypeScript
function getUidsByPolicy(policy: NetUidPolicy, callback: AsyncCallback<Array<number>>): void
```

Query the application UIDs of the specified policy.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Required permissions:** ohos.permission.MANAGE_NET_STRATEGY

<!--Device-policy-function getUidsByPolicy(policy: NetUidPolicy, callback: AsyncCallback<Array<number>>): void--><!--Device-policy-function getUidsByPolicy(policy: NetUidPolicy, callback: AsyncCallback<Array<number>>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| policy | [NetUidPolicy](arkts-network-policy-netuidpolicy-e-sys.md) | Yes | the policy of the current UID of application.For details, see {@link NetUidPolicy}. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;number&gt;&gt; | Yes | the callback of getUidsByPolicy. |

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

policy.getUidsByPolicy(11111, (error: BusinessError, data: number[]) => {
  console.error(JSON.stringify(error));
  console.info(JSON.stringify(data));
});
```


## getUidsByPolicy

```TypeScript
function getUidsByPolicy(policy: NetUidPolicy): Promise<Array<number>>
```

Query the application UIDs of the specified policy.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Required permissions:** ohos.permission.MANAGE_NET_STRATEGY

<!--Device-policy-function getUidsByPolicy(policy: NetUidPolicy): Promise<Array<number>>--><!--Device-policy-function getUidsByPolicy(policy: NetUidPolicy): Promise<Array<number>>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| policy | [NetUidPolicy](arkts-network-policy-netuidpolicy-e-sys.md) | Yes | the policy of the current UID of application.For details, see {@link NetUidPolicy}. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;number&gt;&gt; | The promise returned by the function. |

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
  .getUidsByPolicy(11111)
  .then((data: object) => {
    console.info(JSON.stringify(data));
  })
  .catch((error: BusinessError) => {
    console.error(JSON.stringify(error));
  });
```

