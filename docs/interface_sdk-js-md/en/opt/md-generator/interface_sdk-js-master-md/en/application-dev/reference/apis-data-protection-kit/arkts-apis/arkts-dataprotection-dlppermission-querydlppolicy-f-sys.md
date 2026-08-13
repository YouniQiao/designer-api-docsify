# queryDlpPolicy (System API)

## Modules to Import

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
```

## queryDlpPolicy

```TypeScript
function queryDlpPolicy(dlpFd: number): Promise<string>
```

Parses the file header in a DLP file to obtain the DLP plaintext policy. The returned JSON string of the DLP policy contains the [DLPProperty](arkts-dataprotection-dlppermission-dlpproperty-i.md#DLPProperty-(System-API)) and [CustomProperty](arkts-dataprotection-dlppermission-customproperty-i.md#CustomProperty-(System-API)) information. This API uses a promise to return the result. This API obtains the policy information of a DLP file for analysis in scenarios such as viewing the DLP file permission configuration. > **NOTE：**> > This API can be called only by enterprise accounts.

**Since:** 20

**Deprecated since:** -1

**Required permissions:** ohos.permission.ENTERPRISE_ACCESS_DLP_FILE

<!--Device-dlpPermission-function queryDlpPolicy(dlpFd: number): Promise<string>--><!--Device-dlpPermission-function queryDlpPolicy(dlpFd: number): Promise<string>-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dlpFd | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [19100003](../errorcode-dlp.md#19100003-encryptiondecryption-timeout) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
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

let dlpFd : number | undefined = undefined; // FD of the DLP file to be queried.
let dlpFilePath: string = "file://docs/storage/Users/currentUser/Documents/test.txt.dlp"; // Specify the DLP file path.
dlpFd = fileIo.openSync(dlpFilePath, fileIo.OpenMode.READ_ONLY).fd; // Open the DLP file to obtain the descriptor.
dlpPermission.queryDlpPolicy(dlpFd).then((policy) => {
  console.info('DLP policy:' + policy);
}).catch((error: BusinessError)=> {
  console.error(JSON.stringify(error));
}).finally(()=>{
  if (dlpFd) {
    fileIo.closeSync(dlpFd);
  }
});
```
