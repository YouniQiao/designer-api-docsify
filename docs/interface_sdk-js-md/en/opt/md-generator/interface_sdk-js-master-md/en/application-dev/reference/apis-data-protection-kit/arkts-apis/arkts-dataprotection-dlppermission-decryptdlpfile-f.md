# decryptDlpFile

## Modules to Import

```TypeScript
import { dlpPermission } from 'kits/@kit.DataProtectionKit';
```

## decryptDlpFile

```TypeScript
function decryptDlpFile(dlpFd: number, plaintextFd: number): Promise<void>
```

Decrypts a DLP file to generate a plaintext file. This API can be called only by enterprise accounts. This API uses a promise to return the result.

This API decrypts DLP files into plaintext files, which is applicable to exporting or migrating files by users with owner permissions.

> **NOTE：**
> 
> This API can be called only by enterprise accounts. Enterprises need to set up their own enterprise account
> servers. The enterprise server determines whether an account is authorized to decrypt DLP files.

**Since:** 21

**Required permissions:** ohos.permission.ENTERPRISE_ACCESS_DLP_FILE

<!--Device-dlpPermission-function decryptDlpFile(dlpFd: number, plaintextFd: number): Promise<void>--><!--Device-dlpPermission-function decryptDlpFile(dlpFd: number, plaintextFd: number): Promise<void>-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dlpFd | number | Yes |
| plaintextFd | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [19100003](../errorcode-dlp.md#19100003-encryptiondecryption-timeout) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [19100002](../errorcode-dlp.md#19100002-encryption-and-decryption-error) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100005](../errorcode-dlp.md#19100005-credential-authentication-server-error) |
| [19100004](../errorcode-dlp.md#19100004-credential-service-error) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [19100009](../errorcode-dlp.md#19100009-failed-to-operate-the-dlp-file) |
| [19100008](../errorcode-dlp.md#19100008-nondlp-file) |
| [19100013](../errorcode-dlp.md#19100013-user-access-denied) |

## Examples

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
import { fileIo } from '@kit.CoreFileKit';

let plaintextFd: number | undefined = undefined;
let dlpFd: number | undefined = undefined;
let plainFilePath: string = "file://docs/storage/Users/currentUser/Documents/test.txt";
let dlpFilePath: string = "file://docs/storage/Users/currentUser/Documents/test.txt.dlp";
plaintextFd = fileIo.openSync(plainFilePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE).fd; // Open the target plaintext file.
dlpFd = fileIo.openSync(dlpFilePath, fileIo.OpenMode.READ_ONLY).fd; // Open the DLP file to be decrypted.
dlpPermission.decryptDlpFile(dlpFd, plaintextFd).then((res) => {
  console.info('Successfully decrypt DLP file.');
}).catch((error: BusinessError)=> {
  console.error(JSON.stringify(error));
}).finally(()=>{
  if (dlpFd) {
    fileIo.closeSync(dlpFd);
  }
  if (plaintextFd) {
    fileIo.closeSync(plaintextFd);
  }
});
```
