# grantUriPermission (System API)

## Modules to Import

```TypeScript
import { fileShare } from '@kit.CoreFileKit';
```

## grantUriPermission

```TypeScript
function grantUriPermission(
    uri: string,
    bundleName: string,
    flag: wantConstant.Flags,
    callback: AsyncCallback<void>
  ): void
```

Provides grant uri permission for app

**Since:** 9

**Required permissions:** ohos.permission.WRITE_MEDIA

<!--Device-fileShare-function grantUriPermission(    uri: string,    bundleName: string,    flag: wantConstant.Flags,    callback: AsyncCallback<void>  ): void--><!--Device-fileShare-function grantUriPermission(    uri: string,    bundleName: string,    flag: wantConstant.Flags,    callback: AsyncCallback<void>  ): void-End-->

**System capability:** SystemCapability.FileManagement.AppFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| bundleName | string | Yes |
| flag | wantConstant.Flags | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14300001 |

## Examples

```TypeScript
import { wantConstant } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileShare } from '@kit.CoreFileKit';

let uri: string =
  'file://docs/storage/Users/currentUser/Document/1.txt'; // You are advised to use the system API fileUri.getUriFromPath('Sandbox path') to generate a URI.
let bundleName: string = 'com.demo.test';
try {
  fileShare.grantUriPermission(uri, bundleName, wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION |
    wantConstant.Flags.FLAG_AUTH_WRITE_URI_PERMISSION, (err: BusinessError) => {
    if (err) {
      console.error(`grantUriPermission failed with error: ${JSON.stringify(err)}`);
      return;
    }
    console.info('grantUriPermission success!');
  });
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error(`grantUriPermission failed with error: ${JSON.stringify(error)}`);
}
```


## grantUriPermission

```TypeScript
function grantUriPermission(uri: string, bundleName: string, flag: wantConstant.Flags): Promise<void>
```

Provides grant uri permission for app

**Since:** 9

**Required permissions:** ohos.permission.WRITE_MEDIA

<!--Device-fileShare-function grantUriPermission(uri: string, bundleName: string, flag: wantConstant.Flags): Promise<void>--><!--Device-fileShare-function grantUriPermission(uri: string, bundleName: string, flag: wantConstant.Flags): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.AppFileService

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| bundleName | string | Yes |
| flag | wantConstant.Flags | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 14300001 |

## Examples

```TypeScript
import { wantConstant } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileShare } from '@kit.CoreFileKit';

let uri: string =
  'file://docs/storage/Users/currentUser/Document/1.txt'; // You are advised to use the system API fileUri.getUriFromPath('Sandbox path') to generate a URI.
let bundleName: string = 'com.demo.test';
try {
  fileShare.grantUriPermission(uri, bundleName, wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION |
    wantConstant.Flags.FLAG_AUTH_WRITE_URI_PERMISSION).then(() => {
    console.info('grantUriPermission success!');
  }).catch((error: BusinessError) => {
    console.error(`grantUriPermission failed with error: ${JSON.stringify(error)}`);
  });
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error(`grantUriPermission failed with error: ${JSON.stringify(error)}`);
}
```


## grantUriPermission

```TypeScript
function grantUriPermission(policies: Array<PolicyInfo>, targetBundleName: string, appCloneIndex: number): Promise<void>
```

Grant URI permissions for an application.

**Since:** 20

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-fileShare-function grantUriPermission(policies: Array<PolicyInfo>, targetBundleName: string, appCloneIndex: int): Promise<void>--><!--Device-fileShare-function grantUriPermission(policies: Array<PolicyInfo>, targetBundleName: string, appCloneIndex: int): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| policies | Array&lt;[PolicyInfo](arkts-corefile-fileshare-policyinfo-i.md)&gt; | Yes |
| targetBundleName | string | Yes |
| appCloneIndex | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| 13900001 |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13900011 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileShare } from '@kit.CoreFileKit';

async function grantUriPermissionExample() {
  try {
    let uri = 'file://docs/storage/Users/currentUser/Documents/1.txt';
    let policyInfo: fileShare.PolicyInfo = {
      uri: uri,
      operationMode: fileShare.OperationMode.CREATE_MODE | fileShare.OperationMode.READ_MODE,
    };
    let policies: Array<fileShare.PolicyInfo> = [policyInfo];

    fileShare.grantUriPermission(policies, 'com.example.myapplicationtest', 0).then(() => {
    }).catch((err: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
      console.error(`grantUriPermission failed. Code: ${err.code}, message: ${err.message}`);
    });
  } catch (error) {
    console.info(`grantUriPermission error, Code: ${error.code}, message: ${error.message}`);
  }
}
```
