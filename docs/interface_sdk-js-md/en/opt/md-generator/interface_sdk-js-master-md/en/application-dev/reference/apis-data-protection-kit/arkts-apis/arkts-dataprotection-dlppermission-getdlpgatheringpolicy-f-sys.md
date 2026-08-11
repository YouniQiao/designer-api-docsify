# getDLPGatheringPolicy (System API)

## Modules to Import

```TypeScript
import { dlpPermission } from 'kits/@kit.DataProtectionKit';
```

## getDLPGatheringPolicy

```TypeScript
function getDLPGatheringPolicy(): Promise<GatheringPolicyType>
```

Obtains the DLP sandbox gathering policy. This API uses a promise to return the result.

This API is used to obtain the DLP sandbox gathering policy of the current system.

**Since:** 10

**Required permissions:** ohos.permission.ACCESS_DLP_FILE

<!--Device-dlpPermission-function getDLPGatheringPolicy(): Promise<GatheringPolicyType>--><!--Device-dlpPermission-function getDLPGatheringPolicy(): Promise<GatheringPolicyType>-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;GatheringPolicyType&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

dlpPermission.getDLPGatheringPolicy().then((gatheringPolicy: dlpPermission.GatheringPolicyType) => {
  console.info('gatheringPolicy: ', JSON.stringify(gatheringPolicy));
}).catch((error: BusinessError)=> {
  console.error(error.message);
}); // Obtain the sandbox gathering policy.
```


## getDLPGatheringPolicy

```TypeScript
function getDLPGatheringPolicy(callback: AsyncCallback<GatheringPolicyType>): void
```

Obtains the DLP sandbox gathering policy. This API uses an asynchronous callback to return the result.

This API is used to obtain the DLP sandbox gathering policy of the current system.

**Since:** 10

**Required permissions:** ohos.permission.ACCESS_DLP_FILE

<!--Device-dlpPermission-function getDLPGatheringPolicy(callback: AsyncCallback<GatheringPolicyType>): void--><!--Device-dlpPermission-function getDLPGatheringPolicy(callback: AsyncCallback<GatheringPolicyType>): void-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;GatheringPolicyType&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

dlpPermission.getDLPGatheringPolicy((err, gatheringPolicy) => {
  if (err) {
    console.error('getDLPGatheringPolicy error,', err.code, err.message);
  } else {
    console.info('gatheringPolicy: ', JSON.stringify(gatheringPolicy));
  }
}); // Obtain the sandbox gathering policy.
```
