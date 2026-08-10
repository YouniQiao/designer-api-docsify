# setPolicyByUid (System API)

## Modules to Import

```TypeScript
import { policy } from 'kits/@kit.NetworkKit';
```

## setPolicyByUid

```TypeScript
function setPolicyByUid(uid: number, policy: NetUidPolicy, callback: AsyncCallback<void>): void
```

Set the policy for the specified UID.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Required permissions:** ohos.permission.MANAGE_NET_STRATEGY

<!--Device-policy-function setPolicyByUid(uid: number, policy: NetUidPolicy, callback: AsyncCallback<void>): void--><!--Device-policy-function setPolicyByUid(uid: number, policy: NetUidPolicy, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uid | number | Yes | the specified UID of application. |
| policy | [NetUidPolicy](arkts-network-policy-netuidpolicy-e-sys.md) | Yes | the policy of the current UID of application.For details, see {@link NetUidPolicy}. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | the callback of setPolicyByUid. |

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

policy.setPolicyByUid(11111, policy.NetUidPolicy.NET_POLICY_NONE, (error: BusinessError) => {
  console.error(JSON.stringify(error));
});
```


## setPolicyByUid

```TypeScript
function setPolicyByUid(uid: number, policy: NetUidPolicy): Promise<void>
```

Set the policy for the specified UID.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Required permissions:** ohos.permission.MANAGE_NET_STRATEGY

<!--Device-policy-function setPolicyByUid(uid: number, policy: NetUidPolicy): Promise<void>--><!--Device-policy-function setPolicyByUid(uid: number, policy: NetUidPolicy): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uid | number | Yes | the specified UID of application. |
| policy | [NetUidPolicy](arkts-network-policy-netuidpolicy-e-sys.md) | Yes | the policy of the current UID of application.For details, see {@link NetUidPolicy}. |

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
  .setPolicyByUid(11111, policy.NetUidPolicy.NET_POLICY_NONE)
  .then(() => {
    console.info('setPolicyByUid success');
  })
  .catch((error: BusinessError) => {
    console.error(JSON.stringify(error));
  });
```

