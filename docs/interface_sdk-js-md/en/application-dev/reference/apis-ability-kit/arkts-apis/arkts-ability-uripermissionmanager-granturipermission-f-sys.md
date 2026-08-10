# grantUriPermission (System API)

## Modules to Import

```TypeScript
import { uriPermissionManager } from 'kits/@kit.AbilityKit';
```

## grantUriPermission

```TypeScript
function grantUriPermission(
    uri: string,
    flag: wantConstant.Flags,
    targetBundleName: string,
    callback: AsyncCallback<number>
  ): void
```

授权URI给指定应用，授权成功后目标应用将获得该URI的文件访问权限，目标应用退出后权限将被回收。目标应用使用该URI的方法可以参考  
[应用文件分享](../../../file-management/share-app-file.md)。使用callback异步回调。该接口仅在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备可以调用但是不生效。

> **说明：**
> 
> - 当应用拥有ohos.permission.PROXY_AUTHORIZATION_URI权限时, 可以授权不属于自身但具有访问权限的URI。如果不具备该权限，则仅支持授权属于自身的URI。
> 
> - 因URI处理涉及编解码，传入的URI需要使用[getUriFromPath](../../apis-core-file-kit/arkts-apis/arkts-corefile-fileuri-geturifrompath-f.md/arkts-corefile-fileuri-geturifrompath-f.md#geturifrompath)接口获取。对于应用自行拼接的URI，系统无法保证
> 其功能。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Required permissions:** ohos.permission.PROXY_AUTHORIZATION_URI

<!--Device-uriPermissionManager-function grantUriPermission(    uri: string,    flag: wantConstant.Flags,    targetBundleName: string,    callback: AsyncCallback<number>  ): void--><!--Device-uriPermissionManager-function grantUriPermission(    uri: string,    flag: wantConstant.Flags,    targetBundleName: string,    callback: AsyncCallback<number>  ): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | 指向文件的URI，scheme固定为"file"，参考[FileUri](../../apis-core-file-kit/arkts-apis/arkts-corefile-fileuri-fileuri-c.md/arkts-corefile-fileuri-fileuri-c.md#constructor)。 |
| flag | wantConstant.Flags | Yes | URI的读权限或写权限。 |
| targetBundleName | string | Yes | 被授权URI的应用包名。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes | 回调函数。返回0表示有权限，返回-1表示无权限。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported.<br>**Applicable version:** 19 and later |
| 16000050 | Internal error. |
| 16000060 | A sandbox application cannot grant URI permission. |
| 201 | Permission denied. |
| 202 | Not System App. Interface caller is not a system app. |
| 16000058 | Invalid URI flag. |
| 16000059 | Invalid URI type. |

## Examples

```TypeScript
import { uriPermissionManager, wantConstant } from '@kit.AbilityKit';
import { fileIo, fileUri } from '@kit.CoreFileKit';

let targetBundleName = 'com.example.test_case1'
let path = 'file://com.example.test_case1/data/storage/el2/base/haps/entry_test/files/newDir';
fileIo.mkdir(path, (err) => {
  if (err) {
    console.error(`mkdir failed, err code: ${err.code}, err msg: ${err.message}.`);
  } else {
    console.info(`mkdir success.`);
  }
});
let uri = fileUri.getUriFromPath(path);
uriPermissionManager.grantUriPermission(uri, wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION, targetBundleName,
  (error) => {
    if (error && error.code !== 0) {
      console.error(`grantUriPermission failed, err code: ${error.code}, err msg: ${error.message}.`);
      return;
    }
    console.info(`grantUriPermission success.`);
  });
```


## grantUriPermission

```TypeScript
function grantUriPermission(
    uri: string,
    flag: wantConstant.Flags,
    targetBundleName: string,
    callback: AsyncCallback<void>
  ): void
```

授权URI给指定应用，授权成功后目标应用将获得该URI的文件访问权限，目标应用退出后权限将被回收。目标应用使用该URI的方法可以参考  
[应用文件分享](../../../file-management/share-app-file.md)。使用callback异步回调。该接口仅在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备可以调用但是不生效。

> **说明：**
> 
> - 当应用拥有ohos.permission.PROXY_AUTHORIZATION_URI权限时, 可以授权不属于自身但具有访问权限的URI。如果不具备该权限，则仅支持授权属于自身的URI。
> 
> - 因URI处理涉及编解码，传入的URI需要使用[getUriFromPath](../../apis-core-file-kit/arkts-apis/arkts-corefile-fileuri-geturifrompath-f.md/arkts-corefile-fileuri-geturifrompath-f.md#geturifrompath)接口获取。对于应用自行拼接的URI，系统无法保证
> 其功能。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.PROXY_AUTHORIZATION_URI

**Model restriction:** This API can be used only in the stage model.

<!--Device-uriPermissionManager-function grantUriPermission(    uri: string,    flag: wantConstant.Flags,    targetBundleName: string,    callback: AsyncCallback<void>  ): void--><!--Device-uriPermissionManager-function grantUriPermission(    uri: string,    flag: wantConstant.Flags,    targetBundleName: string,    callback: AsyncCallback<void>  ): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | 指向文件的URI，scheme固定为"file"，参考[FileUri](../../apis-core-file-kit/arkts-apis/arkts-corefile-fileuri-fileuri-c.md/arkts-corefile-fileuri-fileuri-c.md#constructor)。 |
| flag | wantConstant.Flags | Yes | URI的读权限或写权限。 |
| targetBundleName | string | Yes | 被授权URI的应用包名。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。返回0表示有权限，返回-1表示无权限。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 16000050 | Connect to system server failed. |
| 16000060 | A sandbox application cannot grant URI permission. |
| 201 | Permission denied. |
| 202 | Not System App. Interface caller is not a system app. |
| 16000058 | Invalid URI flag. |
| 16000059 | Invalid URI type. |


## grantUriPermission

```TypeScript
function grantUriPermission(uri: string, flag: wantConstant.Flags, targetBundleName: string): Promise<number>
```

授权URI给指定应用，授权成功后目标应用将获得该URI的文件访问权限，目标应用退出后权限将被回收。目标应用使用该URI的方法可以参考  
[应用文件分享](../../../file-management/share-app-file.md)。使用Promise异步回调。该接口仅在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备可以调用但是不生效。

> **说明：**
> 
> - 当应用拥有ohos.permission.PROXY_AUTHORIZATION_URI权限时, 可以授权不属于自身但具有访问权限的URI。如果不具备该权限，则仅支持授权属于自身的URI。
> 
> - 因URI处理涉及编解码，传入的URI需要使用[getUriFromPath](../../apis-core-file-kit/arkts-apis/arkts-corefile-fileuri-geturifrompath-f.md/arkts-corefile-fileuri-geturifrompath-f.md#geturifrompath)接口获取。对于应用自行拼接的URI，系统无法保证
> 其功能。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Required permissions:** ohos.permission.PROXY_AUTHORIZATION_URI

<!--Device-uriPermissionManager-function grantUriPermission(uri: string, flag: wantConstant.Flags, targetBundleName: string): Promise<number>--><!--Device-uriPermissionManager-function grantUriPermission(uri: string, flag: wantConstant.Flags, targetBundleName: string): Promise<number>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | 指向文件的URI，scheme固定为"file"，参考[FileUri](../../apis-core-file-kit/arkts-apis/arkts-corefile-fileuri-fileuri-c.md/arkts-corefile-fileuri-fileuri-c.md#constructor)。 |
| flag | wantConstant.Flags | Yes | URI的读权限或写权限。 |
| targetBundleName | string | Yes | 被授权URI的应用包名。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | Promise对象。返回0表示有权限，返回-1表示无权限。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported.<br>**Applicable version:** 19 and later |
| 16000050 | Internal error. |
| 16000060 | A sandbox application cannot grant URI permission. |
| 201 | Permission denied. |
| 202 | Not System App. Interface caller is not a system app. |
| 16000058 | Invalid URI flag. |
| 16000059 | Invalid URI type. |

## Examples

```TypeScript
import { uriPermissionManager, wantConstant } from '@kit.AbilityKit';
import { fileIo, fileUri } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

let targetBundleName = 'com.example.test_case1'
let path = 'file://com.example.test_case1/data/storage/el2/base/haps/entry_test/files/newDir';

fileIo.mkdir(path, (err) => {
  if (err) {
    console.error(`mkdir failed, err code: ${err.code}, err msg: ${err.message}.`);
  } else {
    console.info(`mkdir succeed.`);
  }
});
let uri = fileUri.getUriFromPath(path);
uriPermissionManager.grantUriPermission(uri, wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION, targetBundleName)
  .then((data) => {
    console.info(`Verification succeeded, data: ${JSON.stringify(data)}.`);
  }).catch((err: BusinessError) => {
  console.error(`Verification failed, err code: ${err.code}, err msg: ${err.message}.`);
});
```


## grantUriPermission

```TypeScript
function grantUriPermission(uri: string, flag: wantConstant.Flags, targetBundleName: string): Promise<void>
```

Grant URI to another application

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.PROXY_AUTHORIZATION_URI

<!--Device-uriPermissionManager-function grantUriPermission(uri: string, flag: wantConstant.Flags, targetBundleName: string): Promise<void>--><!--Device-uriPermissionManager-function grantUriPermission(uri: string, flag: wantConstant.Flags, targetBundleName: string): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | File URI. |
| flag | wantConstant.Flags | Yes | wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION, wantConstant.Flags.FLAG_AUTH_WRITE_URI_PERMISSION or wantConstant.Flags.FLAG_AUTH_PERSISTABLE_URI_PERMISSION. |
| targetBundleName | string | Yes | Indicates the bundle name of authorization target. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 16000050 | Connect to system server failed. |
| 16000060 | A sandbox application cannot grant URI permission. |
| 201 | Permission denied. |
| 202 | Not System App. Interface caller is not a system app. |
| 16000058 | Invalid URI flag. |
| 16000059 | Invalid URI type. |


## grantUriPermission

```TypeScript
function grantUriPermission(uri: string, flag: wantConstant.Flags, targetBundleName: string, appCloneIndex: int): Promise<void>
```

授权URI给指定应用，授权成功后目标应用将获得该URI的文件访问权限，目标应用退出后权限将被回收。目标应用使用该URI的方法可以参考  
[应用文件分享](../../../file-management/share-app-file.md)。使用Promise异步回调。该接口仅在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备可以调用但是不生效。

> **说明：**
> 
> - 当应用拥有ohos.permission.PROXY_AUTHORIZATION_URI权限时, 可以授权不属于自身但具有访问权限的URI。如果不具备该权限，则仅支持授权属于自身的URI。
> 
> - 该接口支持给分身应用授权，需要指定目标应用的应用包名和分身索引。
> 
> - 因URI处理涉及编解码，传入的URI需要使用[getUriFromPath](../../apis-core-file-kit/arkts-apis/arkts-corefile-fileuri-geturifrompath-f.md/arkts-corefile-fileuri-geturifrompath-f.md#geturifrompath)接口获取。对于应用自行拼接的URI，系统无法保证
> 其功能。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.PROXY_AUTHORIZATION_URI

<!--Device-uriPermissionManager-function grantUriPermission(uri: string, flag: wantConstant.Flags, targetBundleName: string, appCloneIndex: int): Promise<void>--><!--Device-uriPermissionManager-function grantUriPermission(uri: string, flag: wantConstant.Flags, targetBundleName: string, appCloneIndex: int): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | 指向文件的URI，scheme固定为"file"，参考[FileUri](../../apis-core-file-kit/arkts-apis/arkts-corefile-fileuri-fileuri-c.md/arkts-corefile-fileuri-fileuri-c.md#constructor)。 |
| flag | wantConstant.Flags | Yes | URI的读权限或写权限。 |
| targetBundleName | string | Yes | 被授权应用的应用包名。 |
| appCloneIndex | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 被授权应用的分身索引，有效范围为[0, 1000], 取值为0时表示主应用。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象。无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported.<br>**Applicable version:** 19 and later |
| 16000081 | Failed to obtain the target application information. |
| 16000050 | Internal error. |
| 16000060 | A sandbox application cannot grant URI permission. |
| 201 | Permission denied. |
| 202 | Not System App. Interface caller is not a system app. |
| 16000058 | Invalid URI flag. |
| 16000059 | Invalid URI type. |

## Examples

```TypeScript
import { AbilityConstant, UIAbility, Want, wantConstant, uriPermissionManager } from '@kit.AbilityKit';
import { fileUri } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
  }

  onForeground(): void {
    let targetBundleName: string = 'com.example.demo1';
    let filePath: string = this.context.filesDir + "/test.txt";
    let uri: string = fileUri.getUriFromPath(filePath);
    // grant uri permission to main application
    try {
      let appCloneIndex: number = 0;
      uriPermissionManager.grantUriPermission(uri, wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION, targetBundleName,
        appCloneIndex)
        .then(() => {
          console.info('grantUriPermission succeeded.');
        }).catch((error: BusinessError) => {
        console.error(`grantUriPermission failed. error: ${JSON.stringify(error)}.`);
      });
    } catch (error) {
      console.error(`grantUriPermission failed. error: ${JSON.stringify(error)}.`);
    }

    // grant uri permission to clone application
    try {
      let appCloneIndex: number = 1;
      uriPermissionManager.grantUriPermission(uri, wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION, targetBundleName,
        appCloneIndex)
        .then(() => {
          console.info('grantUriPermission succeeded.');
        }).catch((error: BusinessError) => {
        console.error(`grantUriPermission failed. error: ${JSON.stringify(error)}.`);
      });
    } catch (error) {
      console.error(`grantUriPermission failed. error: ${JSON.stringify(error)}.`);
    }
  }
}
```

