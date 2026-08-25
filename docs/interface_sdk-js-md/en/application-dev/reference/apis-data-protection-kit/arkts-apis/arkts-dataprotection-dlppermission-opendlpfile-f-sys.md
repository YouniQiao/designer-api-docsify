# openDLPFile (System API)

## Modules to Import

```TypeScript
import { dlpPermission } from 'kits/@kit.DataProtectionKit';
```

## openDLPFile

```TypeScript
function openDLPFile(ciphertextFd: number, appId: string): Promise<DLPFile>
```

Opens a DLP file. After the API is successfully called, the **DLPFile** object is returned, which can be used to manage the permissions on the DLP file and perform related operations. This API uses a promise to return the result.After calling **openDLPFile()** to return a **DLPFile** object, the system must call [closeDLPFile](arkts-dataprotection-dlppermission-dlpfile-i-sys.md#closedlpfile) to release resources after using the object.When a DLP management application or an authorized application needs to access a DLP file, it must first open the file to obtain the managed object.

**Since:** 11

**Required permissions:** ohos.permission.ACCESS_DLP_FILE

**System capability:** SystemCapability.Security.DataLossPrevention

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ciphertextFd | number | Yes |
| appId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[DLPFile](arkts-dataprotection-dlppermission-dlpfile-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100002](../errorcode-dlp.md#19100002-encryption-and-decryption-error) |
| [19100003](../errorcode-dlp.md#19100003-encryptiondecryption-timeout) |
| [19100004](../errorcode-dlp.md#19100004-credential-service-error) |
| [19100005](../errorcode-dlp.md#19100005-credential-authentication-server-error) |
| [19100008](../errorcode-dlp.md#19100008-non-dlp-file) |
| [19100009](../errorcode-dlp.md#19100009-failed-to-operate-the-dlp-file) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |
| [19100018](../errorcode-dlp.md#19100018-application-unauthorized) |
| [19100019](../errorcode-dlp.md#19100019-dlp-file-has-expired) |
| [19100020](../errorcode-dlp.md#19100020-network-disconnected) |


## openDLPFile

```TypeScript
function openDLPFile(ciphertextFd: number, appId: string, callback: AsyncCallback<DLPFile>): void
```

Opens a DLP file. This API uses an asynchronous callback to return the result. After the API is successfully called, the **DLPFile** object is returned, which can be used to manage the permissions on the DLP file and perform related operations. After using the **DLPFile** object, call **closeDLPFile** to close the object to prevent resource leakage.

**Since:** 11

**Required permissions:** ohos.permission.ACCESS_DLP_FILE

**System capability:** SystemCapability.Security.DataLossPrevention

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| ciphertextFd | number | Yes |
| appId | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[DLPFile](arkts-dataprotection-dlppermission-dlpfile-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100002](../errorcode-dlp.md#19100002-encryption-and-decryption-error) |
| [19100003](../errorcode-dlp.md#19100003-encryptiondecryption-timeout) |
| [19100004](../errorcode-dlp.md#19100004-credential-service-error) |
| [19100005](../errorcode-dlp.md#19100005-credential-authentication-server-error) |
| [19100008](../errorcode-dlp.md#19100008-non-dlp-file) |
| [19100009](../errorcode-dlp.md#19100009-failed-to-operate-the-dlp-file) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |
| [19100018](../errorcode-dlp.md#19100018-application-unauthorized) |
| [19100019](../errorcode-dlp.md#19100019-dlp-file-has-expired) |
| [19100020](../errorcode-dlp.md#19100020-network-disconnected) |
