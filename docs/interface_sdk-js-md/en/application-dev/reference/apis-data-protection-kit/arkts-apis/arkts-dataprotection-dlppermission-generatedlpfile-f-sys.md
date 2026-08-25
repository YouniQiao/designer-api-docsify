# generateDLPFile (System API)

## Modules to Import

```TypeScript
import { dlpPermission } from 'kits/@kit.DataProtectionKit';
```

## generateDLPFile

```TypeScript
function generateDLPFile(plaintextFd: number, ciphertextFd: number, property: DLPProperty): Promise<DLPFile>
```

Generates a **DLPFile** object, which is an encrypted file that can be accessed only by authorized users. The users can have the full control permission or read-only permission on the DLP file. This API uses a promise to return the result.After calling **generateDLPFile** to return a **DLPFile** object, the system must call **closeDLPFile** to release resources after using the object.

**Since:** 10

**Required permissions:** ohos.permission.ACCESS_DLP_FILE

**System capability:** SystemCapability.Security.DataLossPrevention

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| plaintextFd | number | Yes |
| ciphertextFd | number | Yes |
| property | [DLPProperty](arkts-dataprotection-dlppermission-dlpproperty-i.md) | Yes |

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
| [19100009](../errorcode-dlp.md#19100009-failed-to-operate-the-dlp-file) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |


## generateDLPFile

```TypeScript
function generateDLPFile(plaintextFd: number, ciphertextFd: number, property: DLPProperty, callback: AsyncCallback<DLPFile>): void
```

Generates a DLP file, which is an encrypted file that can be accessed only by authorized users. The users can have the full control permission or read-only permission on the DLP file. Obtains a **DLPFile** object. This API uses an asynchronous callback to return the result. After using the **DLPFile** object, call **closeDLPFile** to close the object to prevent resource leakage.After calling **generateDLPFile()** to return a **DLPFile** object, the system must call **closeDLPFile()** to release resources after using the object.

**Since:** 10

**Required permissions:** ohos.permission.ACCESS_DLP_FILE

**System capability:** SystemCapability.Security.DataLossPrevention

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| plaintextFd | number | Yes |
| ciphertextFd | number | Yes |
| property | [DLPProperty](arkts-dataprotection-dlppermission-dlpproperty-i.md) | Yes |
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
| [19100009](../errorcode-dlp.md#19100009-failed-to-operate-the-dlp-file) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |
