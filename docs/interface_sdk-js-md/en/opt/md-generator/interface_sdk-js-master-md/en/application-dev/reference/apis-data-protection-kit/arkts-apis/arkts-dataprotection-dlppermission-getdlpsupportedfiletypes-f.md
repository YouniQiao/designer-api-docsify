# getDLPSupportedFileTypes

## Modules to Import

```TypeScript
```

## getDLPSupportedFileTypes

```TypeScript
function getDLPSupportedFileTypes(): Promise<Array<string>>
```

Obtains the file name extension types that support DLP. After the API is successfully called, the list of supported file types is returned, indicating the types of files that can be used to generate DLP files. This API uses a promise to return the result. This API is used to obtain the types of files that can be used to generate DLP files. If the current file type is in the list, it can be encrypted.

**Since:** 10

<!--Device-dlpPermission-function getDLPSupportedFileTypes(): Promise<Array<string>>--><!--Device-dlpPermission-function getDLPSupportedFileTypes(): Promise<Array<string>>-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |

**Examples**

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

dlpPermission.getDLPSupportedFileTypes().then((fileTypes) => { // Obtain the file types that support DLP.
  console.info('fileTypes', JSON.stringify(fileTypes));
}).catch((error: BusinessError)=> {
  console.error(JSON.stringify(error));
});
```


## getDLPSupportedFileTypes

```TypeScript
function getDLPSupportedFileTypes(callback: AsyncCallback<Array<string>>): void
```

Obtains the file name extension types that support DLP. After the API is successfully called, the list of supported file types is returned, indicating the types of files that can be used to generate DLP files. This API uses an asynchronous callback to return the result. This API is used to obtain the types of files that can be used to generate DLP files. If the current file type is in the list, it can be encrypted.

**Since:** 10

<!--Device-dlpPermission-function getDLPSupportedFileTypes(callback: AsyncCallback<Array<string>>): void--><!--Device-dlpPermission-function getDLPSupportedFileTypes(callback: AsyncCallback<Array<string>>): void-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |

**Examples**

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';

dlpPermission.getDLPSupportedFileTypes((err, fileTypes) => {
  if (err) {
    console.error(`Failed to get DLP supported file types. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('fileTypes', JSON.stringify(fileTypes));
  }
}); // Obtain the file types that support DLP.
```
