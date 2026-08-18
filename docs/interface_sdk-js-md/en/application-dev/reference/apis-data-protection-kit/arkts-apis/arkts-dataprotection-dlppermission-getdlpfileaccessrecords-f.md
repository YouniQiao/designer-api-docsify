# getDLPFileAccessRecords

## Modules to Import

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
```

## getDLPFileAccessRecords

```TypeScript
function getDLPFileAccessRecords(): Promise<Array<AccessedDLPFileInfo>>
```

Obtains the list of DLP files that are accessed recently. After the API is successfully called, the file access records are returned, which can be used to track and manage the usage of DLP files. This API can be called only in non-DLP sandbox applications. This API uses a promise to return the result. This API is used to obtain the list of DLP files that are accessed recently, which can be used to track and manage file usage.

**Since:** 10

<!--Device-dlpPermission-function getDLPFileAccessRecords(): Promise<Array<AccessedDLPFileInfo>>--><!--Device-dlpPermission-function getDLPFileAccessRecords(): Promise<Array<AccessedDLPFileInfo>>-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[AccessedDLPFileInfo](arkts-dataprotection-dlppermission-accesseddlpfileinfo-i.md)&gt;&gt; | Promise used to return the list of recently accessed DLP files obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported because car not support DLP feature.<br>**Applicable version:** 26.1.0 and later |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) | Invalid parameter value. |
| [19100007](../errorcode-dlp.md#19100007-access-denied-for-a-dlp-sandbox-application) | No permission to call this API, which is available only for non-DLP sandbox applications. |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) | The system ability works abnormally. |

**Examples**

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function ExampleFunction() {
  try {
    let res:Array<dlpPermission.AccessedDLPFileInfo> = await dlpPermission.getDLPFileAccessRecords(); // Obtain the list of recently accessed DLP files.
    console.info('res', JSON.stringify(res))
  } catch (err) {
    console.error('error', (err as BusinessError).code, (err as BusinessError).message); // Throw an error if the operation fails.
  }
}
```


## getDLPFileAccessRecords

```TypeScript
function getDLPFileAccessRecords(callback: AsyncCallback<Array<AccessedDLPFileInfo>>): void
```

Obtains the list of DLP files that are accessed recently. After the API is successfully called, the file access records are returned, which can be used to track and manage the usage of DLP files. This API uses an asynchronous callback to return the result. This API is used to obtain the list of DLP files that are accessed recently, which can be used to track and manage file usage.

**Since:** 10

<!--Device-dlpPermission-function getDLPFileAccessRecords(callback: AsyncCallback<Array<AccessedDLPFileInfo>>): void--><!--Device-dlpPermission-function getDLPFileAccessRecords(callback: AsyncCallback<Array<AccessedDLPFileInfo>>): void-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;Array&lt;[AccessedDLPFileInfo](arkts-dataprotection-dlppermission-accesseddlpfileinfo-i.md)&gt;&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Incorrect parameter types. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported because car not support DLP feature.<br>**Applicable version:** 26.1.0 and later |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) | Invalid parameter value. |
| [19100007](../errorcode-dlp.md#19100007-access-denied-for-a-dlp-sandbox-application) | No permission to call this API, which is available only for non-DLP sandbox applications. |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) | The system ability works abnormally. |

**Examples**

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  dlpPermission.getDLPFileAccessRecords((err, res) => {
    if (err != undefined) {
      console.error('getDLPFileAccessRecords error,', err.code, err.message);
    } else {
      console.info('res', JSON.stringify(res));
    }
  }); // Obtain the list of recently accessed DLP files.
} catch (err) {
  console.error('getDLPFileAccessRecords error,', (err as BusinessError).code, (err as BusinessError).message);
}
```

