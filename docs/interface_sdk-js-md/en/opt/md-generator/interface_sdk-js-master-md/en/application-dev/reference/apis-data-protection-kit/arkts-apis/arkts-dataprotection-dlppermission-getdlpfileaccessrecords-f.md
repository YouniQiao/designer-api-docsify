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

**Deprecated since:** -1

<!--Device-dlpPermission-function getDLPFileAccessRecords(): Promise<Array<AccessedDLPFileInfo>>--><!--Device-dlpPermission-function getDLPFileAccessRecords(): Promise<Array<AccessedDLPFileInfo>>-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[AccessedDLPFileInfo](arkts-dataprotection-dlppermission-accesseddlpfileinfo-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100007](../errorcode-dlp.md#19100007-access-denied-for-a-dlp-sandbox-application) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |

## Examples

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

dlpPermission.getDLPFileAccessRecords().then((accessRecords) => { // Obtain the list of recently accessed DLP files.
  console.info('accessRecords', JSON.stringify(accessRecords));
}).catch((error: BusinessError)=> {
  console.error(JSON.stringify(error));
});
```


## getDLPFileAccessRecords

```TypeScript
function getDLPFileAccessRecords(callback: AsyncCallback<Array<AccessedDLPFileInfo>>): void
```

Obtains the list of DLP files that are accessed recently. After the API is successfully called, the file access records are returned, which can be used to track and manage the usage of DLP files. This API uses an asynchronous callback to return the result. This API is used to obtain the list of DLP files that are accessed recently, which can be used to track and manage file usage.

**Since:** 10

**Deprecated since:** -1

<!--Device-dlpPermission-function getDLPFileAccessRecords(callback: AsyncCallback<Array<AccessedDLPFileInfo>>): void--><!--Device-dlpPermission-function getDLPFileAccessRecords(callback: AsyncCallback<Array<AccessedDLPFileInfo>>): void-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[AccessedDLPFileInfo](arkts-dataprotection-dlppermission-accesseddlpfileinfo-i.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100007](../errorcode-dlp.md#19100007-access-denied-for-a-dlp-sandbox-application) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |

## Examples

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

dlpPermission.getDLPFileAccessRecords((err, accessRecords) => {
  if (err) {
    console.error(`Failed to get DLP file access records. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('accessRecords', JSON.stringify(accessRecords));
  }
}); // Obtain the list of recently accessed DLP files.
```
