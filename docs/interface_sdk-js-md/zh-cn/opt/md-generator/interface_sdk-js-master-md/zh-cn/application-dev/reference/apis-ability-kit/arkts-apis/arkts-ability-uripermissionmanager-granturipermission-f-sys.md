# grantUriPermission（系统接口）

## 导入模块

```TypeScript
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

授权URI给指定应用，授权成功后目标应用将获得该URI的文件访问权限，目标应用退出后权限将被回收。目标应用使用该URI的方法可以参考 [应用文件分享](../../../file-management/share-app-file.md)。使用callback异步回调。 该接口仅在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备可以调用但是不生效。 > **说明：** > > - 当应用拥有ohos.permission.PROXY_AUTHORIZATION_URI权限时, 可以授权不属于自身但具有访问权限的URI。如果不具备该权限，则仅支持授权属于自身的URI。 > > - 因URI处理涉及编解码，传入的URI需要使用[getUriFromPath](../../apis-core-file-kit/arkts-apis/arkts-corefile-fileuri-geturifrompath-f.md#geturifrompath)接口获取。对于应用自行拼接的URI，系统无法保证 > 其功能。

**起始版本：** 10

**需要权限：** ohos.permission.PROXY_AUTHORIZATION_URI

<!--Device-uriPermissionManager-function grantUriPermission(    uri: string,    flag: wantConstant.Flags,    targetBundleName: string,    callback: AsyncCallback<number>  ): void--><!--Device-uriPermissionManager-function grantUriPermission(    uri: string,    flag: wantConstant.Flags,    targetBundleName: string,    callback: AsyncCallback<number>  ): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| flag | wantConstant.Flags | 是 |
| targetBundleName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000060](../errorcode-ability.md#16000060-不支持沙箱应用授权uri) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16000058](../errorcode-ability.md#16000058-指定的uri-flag无效) |
| [16000059](../errorcode-ability.md#16000059-指定的uri类型无效) |

**示例**

```TypeScript
import { uriPermissionManager, wantConstant } from '@kit.AbilityKit';
import { fileIo, fileUri } from '@kit.CoreFileKit';

let targetBundleName = 'com.example.test_case1';
let path = 'file://com.example.test_case1/data/storage/el2/base/haps/entry_test/files/newDir';
// 创建目录
fileIo.mkdir(path, (err) => {
  if (err) {
    console.error(`mkdir failed, err code: ${err.code}, err msg: ${err.message}.`);
    return;
  }
  console.info(`mkdir success.`);
  let uri = fileUri.getUriFromPath(path);
  // 授权URI给指定应用
  uriPermissionManager.grantUriPermission(uri, wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION, targetBundleName,
    (error) => {
      if (error && error.code !== 0) {
        console.error(`grantUriPermission failed, err code: ${error.code}, err msg: ${error.message}.`);
        return;
      }
      console.info(`grantUriPermission success.`);
    });
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

授权URI给指定应用，授权成功后目标应用将获得该URI的文件访问权限，目标应用退出后权限将被回收。目标应用使用该URI的方法可以参考 [应用文件分享](../../../file-management/share-app-file.md)。使用callback异步回调。 该接口仅在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备可以调用但是不生效。 > **说明：** > > - 当应用拥有ohos.permission.PROXY_AUTHORIZATION_URI权限时, 可以授权不属于自身但具有访问权限的URI。如果不具备该权限，则仅支持授权属于自身的URI。 > > - 因URI处理涉及编解码，传入的URI需要使用[getUriFromPath](../../apis-core-file-kit/arkts-apis/arkts-corefile-fileuri-geturifrompath-f.md#geturifrompath)接口获取。对于应用自行拼接的URI，系统无法保证 > 其功能。

**起始版本：** 23

**需要权限：** ohos.permission.PROXY_AUTHORIZATION_URI

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-uriPermissionManager-function grantUriPermission(    uri: string,    flag: wantConstant.Flags,    targetBundleName: string,    callback: AsyncCallback<void>  ): void--><!--Device-uriPermissionManager-function grantUriPermission(    uri: string,    flag: wantConstant.Flags,    targetBundleName: string,    callback: AsyncCallback<void>  ): void-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| flag | wantConstant.Flags | 是 |
| targetBundleName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000060](../errorcode-ability.md#16000060-不支持沙箱应用授权uri) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16000058](../errorcode-ability.md#16000058-指定的uri-flag无效) |
| [16000059](../errorcode-ability.md#16000059-指定的uri类型无效) |


## grantUriPermission

```TypeScript
function grantUriPermission(uri: string, flag: wantConstant.Flags, targetBundleName: string): Promise<number>
```

授权URI给指定应用，授权成功后目标应用将获得该URI的文件访问权限，目标应用退出后权限将被回收。目标应用使用该URI的方法可以参考 [应用文件分享](../../../file-management/share-app-file.md)。使用Promise异步回调。 该接口仅在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备可以调用但是不生效。 > **说明：** > > - 当应用拥有ohos.permission.PROXY_AUTHORIZATION_URI权限时, 可以授权不属于自身但具有访问权限的URI。如果不具备该权限，则仅支持授权属于自身的URI。 > > - 因URI处理涉及编解码，传入的URI需要使用[getUriFromPath](../../apis-core-file-kit/arkts-apis/arkts-corefile-fileuri-geturifrompath-f.md#geturifrompath)接口获取。对于应用自行拼接的URI，系统无法保证 > 其功能。

**起始版本：** 10

**需要权限：** ohos.permission.PROXY_AUTHORIZATION_URI

<!--Device-uriPermissionManager-function grantUriPermission(uri: string, flag: wantConstant.Flags, targetBundleName: string): Promise<number>--><!--Device-uriPermissionManager-function grantUriPermission(uri: string, flag: wantConstant.Flags, targetBundleName: string): Promise<number>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| flag | wantConstant.Flags | 是 |
| targetBundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000060](../errorcode-ability.md#16000060-不支持沙箱应用授权uri) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16000058](../errorcode-ability.md#16000058-指定的uri-flag无效) |
| [16000059](../errorcode-ability.md#16000059-指定的uri类型无效) |

**示例**

```TypeScript
import { uriPermissionManager, wantConstant } from '@kit.AbilityKit';
import { fileIo, fileUri } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

let targetBundleName = 'com.example.test_case1'
let path = 'file://com.example.test_case1/data/storage/el2/base/haps/entry_test/files/newDir';

// 创建目录
fileIo.mkdir(path, (err) => {
  if (err) {
    console.error(`mkdir failed, err code: ${err.code}, err msg: ${err.message}.`);
    return;
  }
  console.info(`mkdir success.`);
  let uri = fileUri.getUriFromPath(path);
  // 授权URI给指定应用
  uriPermissionManager.grantUriPermission(uri, wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION, targetBundleName)
    .then((data) => {
      console.info(`grantUriPermission succeeded, data: ${JSON.stringify(data)}.`);
    }).catch((err: BusinessError) => {
    console.error(`grantUriPermission failed, err code: ${err.code}, err msg: ${err.message}.`);
  });
});
```


## grantUriPermission

```TypeScript
function grantUriPermission(uri: string, flag: wantConstant.Flags, targetBundleName: string): Promise<void>
```

Grant URI to another application

**起始版本：** 23

**需要权限：** ohos.permission.PROXY_AUTHORIZATION_URI

<!--Device-uriPermissionManager-function grantUriPermission(uri: string, flag: wantConstant.Flags, targetBundleName: string): Promise<void>--><!--Device-uriPermissionManager-function grantUriPermission(uri: string, flag: wantConstant.Flags, targetBundleName: string): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| flag | wantConstant.Flags | 是 |
| targetBundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000060](../errorcode-ability.md#16000060-不支持沙箱应用授权uri) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16000058](../errorcode-ability.md#16000058-指定的uri-flag无效) |
| [16000059](../errorcode-ability.md#16000059-指定的uri类型无效) |


## grantUriPermission

```TypeScript
function grantUriPermission(uri: string, flag: wantConstant.Flags, targetBundleName: string, appCloneIndex: number): Promise<void>
```

授权URI给指定应用，授权成功后目标应用将获得该URI的文件访问权限，目标应用退出后权限将被回收。目标应用使用该URI的方法可以参考 [应用文件分享](../../../file-management/share-app-file.md)。使用Promise异步回调。 该接口仅在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备可以调用但是不生效。 > **说明：** > > - 当应用拥有ohos.permission.PROXY_AUTHORIZATION_URI权限时, 可以授权不属于自身但具有访问权限的URI。如果不具备该权限，则仅支持授权属于自身的URI。 > > - 该接口支持给分身应用授权，需要指定目标应用的应用包名和分身索引。 > > - 因URI处理涉及编解码，传入的URI需要使用[getUriFromPath](../../apis-core-file-kit/arkts-apis/arkts-corefile-fileuri-geturifrompath-f.md#geturifrompath)接口获取。对于应用自行拼接的URI，系统无法保证 > 其功能。

**起始版本：** 23

**需要权限：** ohos.permission.PROXY_AUTHORIZATION_URI

<!--Device-uriPermissionManager-function grantUriPermission(uri: string, flag: wantConstant.Flags, targetBundleName: string, appCloneIndex: int): Promise<void>--><!--Device-uriPermissionManager-function grantUriPermission(uri: string, flag: wantConstant.Flags, targetBundleName: string, appCloneIndex: int): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| flag | wantConstant.Flags | 是 |
| targetBundleName | string | 是 |
| appCloneIndex | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [16000081](../errorcode-ability.md#16000081-获取目标应用信息失败) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000060](../errorcode-ability.md#16000060-不支持沙箱应用授权uri) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16000058](../errorcode-ability.md#16000058-指定的uri-flag无效) |
| [16000059](../errorcode-ability.md#16000059-指定的uri类型无效) |

**示例**

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
    // 授予主应用URI权限
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

    // 授予分身应用URI权限
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
