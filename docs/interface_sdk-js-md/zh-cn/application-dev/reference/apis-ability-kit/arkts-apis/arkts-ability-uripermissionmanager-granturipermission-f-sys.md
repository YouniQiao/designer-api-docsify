# grantUriPermission（系统接口）

## 导入模块

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

授权URI给指定应用，授权成功后目标应用将获得该URI的文件访问权限，目标应用退出后权限将被回收。目标应用使用该URI的方法可以参考 [应用文件分享](../../../file-management/share-app-file.md)。使用callback异步回调。 该接口仅在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备可以调用但是不生效。

> **说明：**&gt;
> - 当应用拥有ohos.permission.PROXY_AUTHORIZATION_URI权限时, 可以授权不属于自身但具有访问权限的URI。如果不具备该权限，则仅支持授权属于自身的URI。&gt;
> - 因URI处理涉及编解码，传入的URI需要使用[getUriFromPath](../../apis-core-file-kit/arkts-apis/arkts-corefile-fileuri-geturifrompath-f.md)接口获取。对于应用自行拼接的URI，系统无法保证
> 其功能。

**起始版本：** 10

**需要权限：** ohos.permission.PROXY_AUTHORIZATION_URI

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| flag | wantConstant.Flags | 是 |
| targetBundleName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000058](../errorcode-ability.md#16000058-指定的uri-flag无效) |
| [16000059](../errorcode-ability.md#16000059-指定的uri类型无效) |
| [16000060](../errorcode-ability.md#16000060-不支持沙箱应用授权uri) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |


## grantUriPermission

```TypeScript
function grantUriPermission(uri: string, flag: wantConstant.Flags, targetBundleName: string): Promise<number>
```

授权URI给指定应用，授权成功后目标应用将获得该URI的文件访问权限，目标应用退出后权限将被回收。目标应用使用该URI的方法可以参考 [应用文件分享](../../../file-management/share-app-file.md)。使用Promise异步回调。 该接口仅在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备可以调用但是不生效。

> **说明：**&gt;
> - 当应用拥有ohos.permission.PROXY_AUTHORIZATION_URI权限时, 可以授权不属于自身但具有访问权限的URI。如果不具备该权限，则仅支持授权属于自身的URI。&gt;
> - 因URI处理涉及编解码，传入的URI需要使用[getUriFromPath](../../apis-core-file-kit/arkts-apis/arkts-corefile-fileuri-geturifrompath-f.md)接口获取。对于应用自行拼接的URI，系统无法保证
> 其功能。

**起始版本：** 10

**需要权限：** ohos.permission.PROXY_AUTHORIZATION_URI

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
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000058](../errorcode-ability.md#16000058-指定的uri-flag无效) |
| [16000059](../errorcode-ability.md#16000059-指定的uri类型无效) |
| [16000060](../errorcode-ability.md#16000060-不支持沙箱应用授权uri) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |


## grantUriPermission

```TypeScript
function grantUriPermission(uri: string, flag: wantConstant.Flags, targetBundleName: string, appCloneIndex: number): Promise<void>
```

授权URI给指定应用，授权成功后目标应用将获得该URI的文件访问权限，目标应用退出后权限将被回收。目标应用使用该URI的方法可以参考 [应用文件分享](../../../file-management/share-app-file.md)。使用Promise异步回调。 该接口仅在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备可以调用但是不生效。

> **说明：**&gt;
> - 当应用拥有ohos.permission.PROXY_AUTHORIZATION_URI权限时, 可以授权不属于自身但具有访问权限的URI。如果不具备该权限，则仅支持授权属于自身的URI。&gt;
> - 该接口支持给分身应用授权，需要指定目标应用的应用包名和分身索引。&gt;
> - 因URI处理涉及编解码，传入的URI需要使用[getUriFromPath](../../apis-core-file-kit/arkts-apis/arkts-corefile-fileuri-geturifrompath-f.md)接口获取。对于应用自行拼接的URI，系统无法保证
> 其功能。

**起始版本：** 14

**需要权限：** ohos.permission.PROXY_AUTHORIZATION_URI

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
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
| [16000058](../errorcode-ability.md#16000058-指定的uri-flag无效) |
| [16000059](../errorcode-ability.md#16000059-指定的uri类型无效) |
| [16000060](../errorcode-ability.md#16000060-不支持沙箱应用授权uri) |
| [16000081](../errorcode-ability.md#16000081-获取目标应用信息失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
