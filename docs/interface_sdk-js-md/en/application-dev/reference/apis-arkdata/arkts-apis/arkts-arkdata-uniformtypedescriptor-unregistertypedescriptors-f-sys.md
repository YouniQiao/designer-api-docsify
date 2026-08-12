# unregisterTypeDescriptors (System API)

## Modules to Import

```TypeScript
import { uniformTypeDescriptor } from '@kit.ArkData';
```

## unregisterTypeDescriptors

```TypeScript
function unregisterTypeDescriptors(typeIds: Array<string>): Promise<void>
```

Unregister one or more type descriptors from the system by the given type IDs.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_DYNAMIC_UTD_TYPE

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-uniformTypeDescriptor-function unregisterTypeDescriptors(typeIds: Array<string>): Promise<void>--><!--Device-uniformTypeDescriptor-function unregisterTypeDescriptors(typeIds: Array<string>): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| typeIds | Array&lt;string&gt; | Yes | The list of type IDs to be unregistered. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [20400004](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-arkdata/errorcode-udmf.md#20400004-invalid-utd-ids) | One or more typeIds are invalid or do not exist. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied, non-system app called system api. |

