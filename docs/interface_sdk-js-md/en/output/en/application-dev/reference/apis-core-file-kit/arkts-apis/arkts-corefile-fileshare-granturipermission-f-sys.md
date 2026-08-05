# grantUriPermission (System API)

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

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.WRITE_MEDIA

<!--Device-fileShare-function grantUriPermission(    uri: string,    bundleName: string,    flag: wantConstant.Flags,    callback: AsyncCallback<void>  ): void--><!--Device-fileShare-function grantUriPermission(    uri: string,    bundleName: string,    flag: wantConstant.Flags,    callback: AsyncCallback<void>  ): void-End-->

**System capability:** SystemCapability.FileManagement.AppFileService

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | uri |
| bundleName | string | Yes | bundleName |
| flag | wantConstant.Flags | Yes | wantConstant.Flags.FLAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_AUTH\_\_\_ESCAPED\_UNDERSCORE\_\_\_READ\_\_\_ESCAPED\_UNDERSCORE\_\_\_URI\_\_\_ESCAPED\_UNDERSCORE\_\_\_PERMISSION or wantConstant.Flags.FLAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_AUTH\_\_\_ESCAPED\_UNDERSCORE\_\_\_WRITE\_\_\_ESCAPED\_UNDERSCORE\_\_\_URI\_\_\_ESCAPED\_UNDERSCORE\_\_\_PERMISSION |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes |  |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The caller is not a system application |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | The input parameter is invalid.Possible causes:1.Mandatory parameters are left unspecified;\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_2.Incorrect parameter types. |
| 14300001 | IPC error |

**Example**

```TypeScript
import { wantConstant } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let uri: string =
  'file://docs/storage/Users/currentUser/Document/1.txt'; // You are advised to use the system API fileUri.getUriFromPath("Sandbox path") to generate a URI.;
let bundleName: string = 'com.demo.test';
try {
  fileShare.grantUriPermission(uri, bundleName, wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION |
    wantConstant.Flags.FLAG_AUTH_WRITE_URI_PERMISSION, (err: BusinessError) => {
    if (err) {
      console.error("grantUriPermission failed with error: " + JSON.stringify(err));
      return;
    }
    console.info("grantUriPermission success!");
  });
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error("grantUriPermission failed with error:" + JSON.stringify(error));
}
```


## grantUriPermission

```TypeScript
function grantUriPermission(uri: string, bundleName: string, flag: wantConstant.Flags): Promise<void>
```

Provides grant uri permission for app

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.WRITE_MEDIA

<!--Device-fileShare-function grantUriPermission(uri: string, bundleName: string, flag: wantConstant.Flags): Promise<void>--><!--Device-fileShare-function grantUriPermission(uri: string, bundleName: string, flag: wantConstant.Flags): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.AppFileService

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | uri |
| bundleName | string | Yes | bundleName |
| flag | wantConstant.Flags | Yes | wantConstant.Flags.FLAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_AUTH\_\_\_ESCAPED\_UNDERSCORE\_\_\_READ\_\_\_ESCAPED\_UNDERSCORE\_\_\_URI\_\_\_ESCAPED\_UNDERSCORE\_\_\_PERMISSION or wantConstant.Flags.FLAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_AUTH\_\_\_ESCAPED\_UNDERSCORE\_\_\_WRITE\_\_\_ESCAPED\_UNDERSCORE\_\_\_URI\_\_\_ESCAPED\_UNDERSCORE\_\_\_PERMISSION |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | no callback return Promise otherwise return void |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The caller is not a system application |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | The input parameter is invalid.Possible causes:1.Mandatory parameters are left unspecified;\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_2.Incorrect parameter types. |
| 14300001 | IPC error |

**Example**

```TypeScript
import { wantConstant } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let uri: string =
  'file://docs/storage/Users/currentUser/Document/1.txt'; // You are advised to use the system API fileUri.getUriFromPath("Sandbox path") to generate a URI.;
let bundleName: string = 'com.demo.test';
try {
  fileShare.grantUriPermission(uri, bundleName, wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION |
    wantConstant.Flags.FLAG_AUTH_WRITE_URI_PERMISSION).then(() => {
    console.info("grantUriPermission success!");
  }).catch((error: BusinessError) => {
    console.error("grantUriPermission failed with error:" + JSON.stringify(error));
  });
} catch (err) {
  let error: BusinessError = err as BusinessError;
  console.error("grantUriPermission failed with error:" + JSON.stringify(error));
}
```


## grantUriPermission

```TypeScript
function grantUriPermission(policies: Array<PolicyInfo>, targetBundleName: string, appCloneIndex: int): Promise<void>
```

Grant URI permissions for an application.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-fileShare-function grantUriPermission(policies: Array<PolicyInfo>, targetBundleName: string, appCloneIndex: int): Promise<void>--><!--Device-fileShare-function grantUriPermission(policies: Array<PolicyInfo>, targetBundleName: string, appCloneIndex: int): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| policies | Array&lt;PolicyInfo&gt; | Yes | Policy information for the user to grant permissions on URIs. |
| targetBundleName | string | Yes | Name of the target bundle to authorize. |
| appCloneIndex | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Clone index of the target application. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Returns void. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The caller is not a system application. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| 13900001 | Operation not permitted. |
| 13900011 | Out of memory. |

**Example**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileShare } from '@kit.CoreFileKit';

async function grantUriPermissionExample() {
  try {
    let uri = "file://docs/storage/Users/currentUser/Documents/1.txt";
    let policyInfo: fileShare.PolicyInfo = {
      uri: uri,
      operationMode: fileShare.OperationMode.CREATE_MODE | fileShare.OperationMode.READ_MODE,
    };
    let policies: Array<fileShare.PolicyInfo> = [policyInfo];

    fileShare.grantUriPermission(policies, "com.example.myapplicationtest", 0).then(() => {
    }).catch((err: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
      console.error("grantUriPermission failed. Code: " +
      err.code + ", message: " + err.message);
    });
  }
  catch (error) {
    console.info('grantUriPermission error, Code: ' + error.code + ', message: ' + error.message);
  }
}
```

