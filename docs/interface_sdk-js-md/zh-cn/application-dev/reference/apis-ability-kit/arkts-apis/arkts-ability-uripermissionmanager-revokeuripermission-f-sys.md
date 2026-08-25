# revokeUriPermission（系统接口）

## 导入模块

```TypeScript
import { uriPermissionManager } from '@kit.AbilityKit';
```

## revokeUriPermission

```TypeScript
function revokeUriPermission(uri: string, targetBundleName: string, callback: AsyncCallback<number>): void
```

撤销授权指定应用的URI。使用callback异步回调。 该接口仅在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备可以调用但是不生效。

> **说明：**&gt;
> - 允许应用撤销自身获得的其他应用URI权限，或授权给其他应用的URI权限。&gt;
> - 因URI处理涉及编解码，传入的URI需要使用[getUriFromPath](../../apis-core-file-kit/arkts-apis/arkts-corefile-fileuri-geturifrompath-f.md)接口获取。对于应用自行拼接的URI，系统无法保证
> 其功能。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**需要权限：** 
- API版本10 - 11：ohos.permission.PROXY_AUTHORIZATION_URI

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| targetBundleName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000059](../errorcode-ability.md#16000059-指定的uri类型无效) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

**示例**

```TypeScript
import { uriPermissionManager } from '@kit.AbilityKit';

let targetBundleName = 'com.example.test_case2';
let uri = "file://com.example.test_case1/data/storage/el2/base/haps/entry_test/files/newDir";

// 撤销指定应用的URI权限
uriPermissionManager.revokeUriPermission(uri, targetBundleName, (error) => {
  if (error && error.code !== 0) {
    console.error(`revokeUriPermission failed. Code: ${error.code}, message: ${error.message}.`);
    return;
  }
  console.info('revokeUriPermission success');
});
```

ArkTS-Sta示例：

```TypeScript
'use static'
import { uriPermissionManager } from '@kit.AbilityKit';

let targetBundleName = 'com.example.test_case2';
let uri = "file://com.example.test_case1/data/storage/el2/base/haps/entry_test/files/newDir";

uriPermissionManager.revokeUriPermission(uri, targetBundleName, (error) => {
  if (error && error.code !== 0) {
    console.error("revokeUriPermission failed, error.code = " + error.code);
    return;
  }
  console.info("revokeUriPermission success");
});
```

```TypeScript
import { uriPermissionManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let targetBundleName = 'com.example.test_case2';
let uri = 'file://com.example.test_case1/data/storage/el2/base/haps/entry_test/files/newDir';

// 撤销指定应用的URI权限
uriPermissionManager.revokeUriPermission(uri, targetBundleName)
  .then((data) => {
    console.info(`Verification success, data: ${JSON.stringify(data)}.`);
  }).catch((error: BusinessError) => {
  console.error(`Verification failed, err code: ${error.code}, err msg: ${error.message}.`);
});
```

ArkTS-Sta示例：

```TypeScript
'use static'
import { uriPermissionManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let targetBundleName = 'com.example.test_case2';
let uri = 'file://com.example.test_case1/data/storage/el2/base/haps/entry_test/files/newDir';

uriPermissionManager.revokeUriPermission(uri, targetBundleName)
  .then((data) => {
    console.info(`Verification success, data: ${data}.`);
  }).catch((error: BusinessError<void>): void => {
  console.error(`Verification failed, err code: ${error.code}, err msg: ${error.message}.`);
});
```

ArkTS-Dyn示例：

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
    // 撤销主应用uri权限
    try {
      let appCloneIndex: number = 0;
      uriPermissionManager.revokeUriPermission(uri, targetBundleName, appCloneIndex)
        .then(() => {
          console.info('revokeUriPermission succeeded.');
        }).catch((error: BusinessError) => {
        console.error(`revokeUriPermission failed. error: ${JSON.stringify(error)}.`);
      });
    } catch (error) {
      console.error(`revokeUriPermission failed. error: ${JSON.stringify(error)}.`);
    }

    // 撤销分身应用uri权限
    try {
      let appCloneIndex: number = 1;
      uriPermissionManager.revokeUriPermission(uri, targetBundleName, appCloneIndex)
        .then(() => {
          console.info('revokeUriPermission succeeded.');
        }).catch((error: BusinessError) => {
        console.error(`revokeUriPermission failed. error: ${JSON.stringify(error)}.`);
      });
    } catch (error) {
      console.error(`revokeUriPermission failed. error: ${JSON.stringify(error)}.`);
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
'use static'
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
    // 撤销主应用uri权限
    try {
      let appCloneIndex: int = 0;
      uriPermissionManager.revokeUriPermission(uri, targetBundleName, appCloneIndex)
        .then(() => {
          console.info('revokeUriPermission succeeded.');
        }).catch((error: BusinessError<void>): void => {
        console.error(`revokeUriPermission failed. error: ${JSON.stringify(error)}.`);
      });
    } catch (error) {
      console.error(`revokeUriPermission failed. error: ${JSON.stringify(error)}.`);
    }

    // 撤销分身应用uri权限
    try {
      let appCloneIndex: int = 0;
      uriPermissionManager.revokeUriPermission(uri, targetBundleName, appCloneIndex)
        .then(() => {
          console.info('revokeUriPermission succeeded.');
        }).catch((error: BusinessError<void>): void => {
        console.error(`revokeUriPermission failed. error: ${JSON.stringify(error)}.`);
      });
    } catch (error) {
      console.error(`revokeUriPermission failed. error: ${JSON.stringify(error)}.`);
    }
  }
}
```


## revokeUriPermission

```TypeScript
function revokeUriPermission(uri: string, targetBundleName: string, callback: AsyncCallback<void>): void
```

撤销授权指定应用的URI。使用callback异步回调。

> **说明：**&gt;
> - 允许应用撤销自身获得的其他应用URI权限，或授权给其他应用的URI权限。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| targetBundleName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000059](../errorcode-ability.md#16000059-指定的uri类型无效) |

**示例**

参见 [revokeUriPermission](#revokeuripermission)


## revokeUriPermission

```TypeScript
function revokeUriPermission(uri: string, targetBundleName: string): Promise<number>
```

撤销授权指定应用的URI。使用Promise异步回调。 该接口仅在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备可以调用但是不生效。

> **说明：**&gt;
> - 允许应用撤销自身获得的其他应用URI权限，或授权给其他应用的URI权限。&gt;
> - 因URI处理涉及编解码，传入的URI需要使用[getUriFromPath](../../apis-core-file-kit/arkts-apis/arkts-corefile-fileuri-geturifrompath-f.md)接口获取。对于应用自行拼接的URI，系统无法保证
> 其功能。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**需要权限：** 
- API版本10 - 11：ohos.permission.PROXY_AUTHORIZATION_URI

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| targetBundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000059](../errorcode-ability.md#16000059-指定的uri类型无效) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

**示例**

参见 [revokeUriPermission](#revokeuripermission)


## revokeUriPermission

```TypeScript
function revokeUriPermission(uri: string, targetBundleName: string): Promise<void>
```

撤销授权指定应用的URI。使用Promise异步回调。

> **说明：**&gt;
> - 允许应用撤销自身获得的其他应用URI权限，或授权给其他应用的URI权限。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| targetBundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000059](../errorcode-ability.md#16000059-指定的uri类型无效) |

**示例**

参见 [revokeUriPermission](#revokeuripermission)


## revokeUriPermission

```TypeScript
function revokeUriPermission(uri: string, targetBundleName: string, appCloneIndex: int): Promise<void>
```

撤销授权指定应用的URI。使用Promise异步回调。 该接口仅在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备可以调用但是不生效。

> **说明：**&gt;
> - 允许应用撤销自身获得的其他应用URI权限，或授权给其他应用的URI权限。&gt;
> - 该接口支持撤销授权给分身应用的URI权限，需要指定目标应用的应用包名和分身索引。&gt;
> - 因URI处理涉及编解码，传入的URI需要使用[getUriFromPath](../../apis-core-file-kit/arkts-apis/arkts-corefile-fileuri-geturifrompath-f.md)接口获取。对于应用自行拼接的URI，系统无法保证
> 其功能。

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| targetBundleName | string | 是 |
| appCloneIndex | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000059](../errorcode-ability.md#16000059-指定的uri类型无效) |
| [16000081](../errorcode-ability.md#16000081-获取目标应用信息失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |

**示例**

参见 [revokeUriPermission](#revokeuripermission)
