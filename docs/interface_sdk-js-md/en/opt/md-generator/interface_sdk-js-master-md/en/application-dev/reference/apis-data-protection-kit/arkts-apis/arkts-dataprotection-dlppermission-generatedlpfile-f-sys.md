# generateDLPFile (System API)

## Modules to Import

```TypeScript
import { dlpPermission } from 'kits/@kit.DataProtectionKit';
```

## generateDLPFile

```TypeScript
function generateDLPFile(plaintextFd: number, ciphertextFd: number, property: DLPProperty): Promise<DLPFile>
```

Generates a **DLPFile** object, which is an encrypted file that can be accessed only by authorized users. The users can have the full control permission or read-only permission on the DLP file. This API uses a promise to return the result.

After calling **generateDLPFile** to return a **DLPFile** object, the system must call **closeDLPFile** to release resources after using the object.

**Since:** 10

**Required permissions:** ohos.permission.ACCESS_DLP_FILE

<!--Device-dlpPermission-function generateDLPFile(plaintextFd: number, ciphertextFd: number, property: DLPProperty): Promise<DLPFile>--><!--Device-dlpPermission-function generateDLPFile(plaintextFd: number, ciphertextFd: number, property: DLPProperty): Promise<DLPFile>-End-->

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
| Promise&lt;DLPFile&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [19100003](../errorcode-dlp.md#19100003-encryptiondecryption-timeout) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [19100002](../errorcode-dlp.md#19100002-encryption-and-decryption-error) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100005](../errorcode-dlp.md#19100005-credential-authentication-server-error) |
| [19100004](../errorcode-dlp.md#19100004-credential-service-error) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [19100009](../errorcode-dlp.md#19100009-failed-to-operate-the-dlp-file) |

## Examples

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
import { fileIo } from '@kit.CoreFileKit';

async function ExampleFunction() {
  let dlpUri = 'file://docs/storage/Users/currentUser/Desktop/test.txt.dlp';
  let uri = 'file://docs/storage/Users/currentUser/Desktop/test.txt';
  let file: number | undefined = undefined;
  let dlp: number | undefined = undefined;
  let dlpFile: dlpPermission.DLPFile | undefined = undefined;

  file = fileIo.openSync(uri).fd;
  dlp = fileIo.openSync(dlpUri).fd;
  let dlpProperty: dlpPermission.DLPProperty = {
    ownerAccount: 'zhangsan',
    ownerAccountType: dlpPermission.AccountType.DOMAIN_ACCOUNT,
    authUserList: [],
    contactAccount: 'zhangsan',
    offlineAccess: true,
    ownerAccountID: 'xxxxxxx',
    everyoneAccessList: []
  };
  dlpFile = await dlpPermission.generateDLPFile(file, dlp, dlpProperty); // Generate a DLP file.

  await dlpFile?.closeDLPFile(); // Close the DLP object.
  if (file) {
    fileIo.closeSync(file);
  }
  if (dlp) {
    fileIo.closeSync(dlp);
  }
}

ExampleFunction();
```


## generateDLPFile

```TypeScript
function generateDLPFile(plaintextFd: number, ciphertextFd: number, property: DLPProperty, callback: AsyncCallback<DLPFile>): void
```

Generates a DLP file, which is an encrypted file that can be accessed only by authorized users. The users can have the full control permission or read-only permission on the DLP file. Obtains a **DLPFile** object. This API uses an asynchronous callback to return the result. After using the **DLPFile** object, call **closeDLPFile** to close the object to prevent resource leakage.

After calling **generateDLPFile()** to return a **DLPFile** object, the system must call **closeDLPFile()** to release resources after using the object.

**Since:** 10

**Required permissions:** ohos.permission.ACCESS_DLP_FILE

<!--Device-dlpPermission-function generateDLPFile(plaintextFd: number, ciphertextFd: number, property: DLPProperty, callback: AsyncCallback<DLPFile>): void--><!--Device-dlpPermission-function generateDLPFile(plaintextFd: number, ciphertextFd: number, property: DLPProperty, callback: AsyncCallback<DLPFile>): void-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| plaintextFd | number | Yes |
| ciphertextFd | number | Yes |
| property | [DLPProperty](arkts-dataprotection-dlppermission-dlpproperty-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;DLPFile&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [19100003](../errorcode-dlp.md#19100003-encryptiondecryption-timeout) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [19100002](../errorcode-dlp.md#19100002-encryption-and-decryption-error) |
| [19100001](../errorcode-dlp.md#19100001-invalid-parameter) |
| [19100005](../errorcode-dlp.md#19100005-credential-authentication-server-error) |
| [19100004](../errorcode-dlp.md#19100004-credential-service-error) |
| [19100011](../errorcode-dlp.md#19100011-system-service-abnormal) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [19100009](../errorcode-dlp.md#19100009-failed-to-operate-the-dlp-file) |

## Examples

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
import { fileIo } from '@kit.CoreFileKit';

let dlpUri = 'file://docs/storage/Users/currentUser/Desktop/test.txt.dlp';
let uri = 'file://docs/storage/Users/currentUser/Desktop/test.txt';
let file: number | undefined = undefined;
let dlp: number | undefined = undefined;

file = fileIo.openSync(uri).fd;
dlp = fileIo.openSync(dlpUri).fd;
let dlpProperty: dlpPermission.DLPProperty = {
  ownerAccount: 'zhangsan',
  ownerAccountType: dlpPermission.AccountType.DOMAIN_ACCOUNT,
  authUserList: [],
  contactAccount: 'zhangsan',
  offlineAccess: true,
  ownerAccountID: 'xxxxxxx',
  everyoneAccessList: []
};
dlpPermission.generateDLPFile(file, dlp, dlpProperty, (err, res) => { // Generate a DLP file.
  if (err) {
    console.error('generateDLPFile error,', err.code, err.message);
  } else {
    console.info('res', JSON.stringify(res));
  }
  fileIo.closeSync(file);
  fileIo.closeSync(dlp);
});
```
