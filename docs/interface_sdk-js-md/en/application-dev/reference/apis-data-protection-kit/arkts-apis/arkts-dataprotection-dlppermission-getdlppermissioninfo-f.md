# getDLPPermissionInfo

## Modules to Import

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
```

## getDLPPermissionInfo

```TypeScript
function getDLPPermissionInfo(): Promise<DLPPermissionInfo>
```

Queries the permission information of the current DLP sandbox, including permissions on the file and operations that can be performed (such as viewing, editing, and copying). This API can be called only in DLP sandbox applications. This API uses a promise to return the result. When processing files in the DLP sandbox, the system determines the operations that can be performed for the current user to prevent calling unauthorized capabilities.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-dlpPermission-function getDLPPermissionInfo(): Promise<DLPPermissionInfo>--><!--Device-dlpPermission-function getDLPPermissionInfo(): Promise<DLPPermissionInfo>-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[DLPPermissionInfo](arkts-dataprotection-dlppermission-dlppermissioninfo-i.md)&gt; | Promise used to return the permission information about the DLP file. The operation is successful if no error is reported. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported because car not support DLP feature.<br>**Applicable version:** 26.1.0 and later |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) | Invalid parameter value. |
| [19100006](../errorcode-dlp.md#19100006-access-denied-for-a-nondlp-sandbox-application) | No permission to call this API, which is available only for DLP sandbox applications. |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) | The system ability works abnormally. |

## Examples

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function ExampleFunction() {
  try {
    dlpPermission.isInSandbox().then(async (inSandbox) => { // Check whether the application is running in a sandbox.
      if (inSandbox) {
        let res: dlpPermission.DLPPermissionInfo = await dlpPermission.getDLPPermissionInfo(); // Obtain the permission information.
        console.info('res', JSON.stringify(res));
      }
    });
  } catch (err) {
    console.error('error', (err as BusinessError).code, (err as BusinessError).message); // Throw an error if the operation fails.
  }
}
```


## getDLPPermissionInfo

```TypeScript
function getDLPPermissionInfo(callback: AsyncCallback<DLPPermissionInfo>): void
```

Obtains the permission information of this DLP file. The returned permission information includes permissions on the file and operations that can be performed (such as viewing, editing, and copying). This API uses an asynchronous callback to return the result. When processing files in the DLP sandbox, the system determines the operations that can be performed for the current user to prevent calling unauthorized capabilities.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-dlpPermission-function getDLPPermissionInfo(callback: AsyncCallback<DLPPermissionInfo>): void--><!--Device-dlpPermission-function getDLPPermissionInfo(callback: AsyncCallback<DLPPermissionInfo>): void-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[DLPPermissionInfo](arkts-dataprotection-dlppermission-dlppermissioninfo-i.md)&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Incorrect parameter types. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported because car not support DLP feature.<br>**Applicable version:** 26.1.0 and later |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) | Invalid parameter value. |
| [19100006](../errorcode-dlp.md#19100006-access-denied-for-a-nondlp-sandbox-application) | No permission to call this API, which is available only for DLP sandbox applications. |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) | The system ability works abnormally. |

## Examples

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  dlpPermission.isInSandbox().then((inSandbox) => { // Check whether the application is running in a sandbox.
    if (inSandbox) {
      dlpPermission.getDLPPermissionInfo((err, res) => {
        if (err != undefined) {
          console.error('getDLPPermissionInfo error', err.code, err.message);
        } else {
          console.info('res', JSON.stringify(res));
        }
      }); // Obtain the permission information.
    }
  });
} catch (err) {
  console.error('getDLPPermissionInfo error', (err as BusinessError).code, (err as BusinessError).message);
}
```

