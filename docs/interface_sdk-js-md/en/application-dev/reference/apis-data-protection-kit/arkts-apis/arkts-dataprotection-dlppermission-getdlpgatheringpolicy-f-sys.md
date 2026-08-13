# getDLPGatheringPolicy (System API)

## Modules to Import

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
```

## getDLPGatheringPolicy

```TypeScript
function getDLPGatheringPolicy(): Promise<GatheringPolicyType>
```

Obtains the DLP sandbox gathering policy. This API uses a promise to return the result. This API is used to obtain the DLP sandbox gathering policy of the current system.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_DLP_FILE

<!--Device-dlpPermission-function getDLPGatheringPolicy(): Promise<GatheringPolicyType>--><!--Device-dlpPermission-function getDLPGatheringPolicy(): Promise<GatheringPolicyType>-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[GatheringPolicyType](arkts-dataprotection-dlppermission-gatheringpolicytype-e-sys.md)&gt; | Promise used to return the DLP sandbox gathering policy obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported because car not support DLP feature.<br>**Applicable version:** 26.1.0 and later |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) | Invalid parameter value. |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) | The system ability works abnormally. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |

## Examples

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function ExampleFunction() {
  try {
    let res: dlpPermission.GatheringPolicyType = await dlpPermission.getDLPGatheringPolicy(); // Obtain the sandbox gathering policy.
    console.info('res', JSON.stringify(res));
  } catch (err) {
    console.error('error', (err as BusinessError).code, (err as BusinessError).message); // Throw an error if the operation fails.
  }
}
```


## getDLPGatheringPolicy

```TypeScript
function getDLPGatheringPolicy(callback: AsyncCallback<GatheringPolicyType>): void
```

Obtains the DLP sandbox gathering policy. This API uses an asynchronous callback to return the result. This API is used to obtain the DLP sandbox gathering policy of the current system.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_DLP_FILE

<!--Device-dlpPermission-function getDLPGatheringPolicy(callback: AsyncCallback<GatheringPolicyType>): void--><!--Device-dlpPermission-function getDLPGatheringPolicy(callback: AsyncCallback<GatheringPolicyType>): void-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[GatheringPolicyType](arkts-dataprotection-dlppermission-gatheringpolicytype-e-sys.md)&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Incorrect parameter types. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported because car not support DLP feature.<br>**Applicable version:** 26.1.0 and later |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) | Invalid parameter value. |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) | The system ability works abnormally. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |

## Examples

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  dlpPermission.getDLPGatheringPolicy((err, res) => {
    if (err !== undefined) {
      console.error('getDLPGatheringPolicy error,', err.code, err.message);
    } else {
      console.info('res', JSON.stringify(res));
    }
  }); // Obtain the sandbox gathering policy.
} catch (err) {
  console.error('getDLPGatheringPolicy error,', (err as BusinessError).code, (err as BusinessError).message);
}
```

