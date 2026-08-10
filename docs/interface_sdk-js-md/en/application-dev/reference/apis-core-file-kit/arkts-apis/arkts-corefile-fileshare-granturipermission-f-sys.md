# grantUriPermission (System API)

## Modules to Import

```TypeScript
import { fileShare } from 'kits/@kit.CoreFileKit';
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

为应用授予公共目录文件URI的临时访问权限，使用Callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.WRITE_MEDIA

<!--Device-fileShare-function grantUriPermission(    uri: string,    bundleName: string,    flag: wantConstant.Flags,    callback: AsyncCallback<void>  ): void--><!--Device-fileShare-function grantUriPermission(    uri: string,    bundleName: string,    flag: wantConstant.Flags,    callback: AsyncCallback<void>  ): void-End-->

**System capability:** SystemCapability.FileManagement.AppFileService

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | 公共目录文件URI。 |
| bundleName | string | Yes | 分享目标的包名。 |
| flag | wantConstant.Flags | Yes | 授权的权限，可取wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION或 wantConstant.Flags.FLAG_AUTH_WRITE_URI_PERMISSION。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 异步授权之后的回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | The input parameter is invalid.Possible causes:1.Mandatory parameters are left unspecified; &lt;br&gt;2.Incorrect parameter types. |
| 201 | Permission verification failed |
| 202 | The caller is not a system application |
| 14300001 | IPC error |

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

为应用授予公共目录文件URI的临时访问权限，使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.WRITE_MEDIA

<!--Device-fileShare-function grantUriPermission(uri: string, bundleName: string, flag: wantConstant.Flags): Promise<void>--><!--Device-fileShare-function grantUriPermission(uri: string, bundleName: string, flag: wantConstant.Flags): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.AppFileService

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | 公共目录文件URI。 |
| bundleName | string | Yes | 分享目标的包名。 |
| flag | wantConstant.Flags | Yes | 授权的权限，可取wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION或 wantConstant.Flags.FLAG_AUTH_WRITE_URI_PERMISSION。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | The input parameter is invalid.Possible causes:1.Mandatory parameters are left unspecified; &lt;br&gt;2.Incorrect parameter types. |
| 201 | Permission verification failed |
| 202 | The caller is not a system application |
| 14300001 | IPC error |

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
function grantUriPermission(policies: Array<PolicyInfo>, targetBundleName: string, appCloneIndex: int): Promise<void>
```

给应用授予目标文件临时权限，使用Promise异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.FILE_ACCESS_MANAGER

<!--Device-fileShare-function grantUriPermission(policies: Array<PolicyInfo>, targetBundleName: string, appCloneIndex: int): Promise<void>--><!--Device-fileShare-function grantUriPermission(policies: Array<PolicyInfo>, targetBundleName: string, appCloneIndex: int): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.AppFileService.FolderAuthorization

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| policies | Array&lt;PolicyInfo&gt; | Yes | 需要授权URI的策略信息数组。 |
| targetBundleName | string | Yes | 被授权应用的应用包名。 |
| appCloneIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 被授权应用的分身索引，取值为0时表示主应用。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 13900001 | Operation not permitted. |
| 201 | Permission verification failed. |
| 202 | The caller is not a system application. |
| 13900011 | Out of memory. |

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

