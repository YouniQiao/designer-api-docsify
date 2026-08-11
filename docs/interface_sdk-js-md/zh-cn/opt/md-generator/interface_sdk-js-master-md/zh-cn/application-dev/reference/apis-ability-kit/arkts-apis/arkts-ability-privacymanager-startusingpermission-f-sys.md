# startUsingPermission（系统接口）

## startUsingPermission

```TypeScript
function startUsingPermission(tokenID: number, permissionName: Permissions): Promise<void>
```

系统应用调用此接口，能够向系统上报应用在前后台的权限使用状态。隐私服务将此状态通知所有该权限使用状态变更事件的订阅者（订阅方法参考[on](privacyManager.on)）。使用Promise异步回调。

开始使用权限后，需要在权限使用结束时调用[stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md#stopusingpermission)停止使用权限。

**起始版本：** 9

**需要权限：** ohos.permission.PERMISSION_USED_STATS

<!--Device-privacyManager-function startUsingPermission(tokenID: int, permissionName: Permissions): Promise<void>--><!--Device-privacyManager-function startUsingPermission(tokenID: int, permissionName: Permissions): Promise<void>-End-->

**系统能力：** SystemCapability.Security.AccessToken

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tokenID | number | 是 |
| permissionName | Permissions | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [12100008](../errorcode-access-token.md#12100008-内存申请失败) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12100001](../errorcode-access-token.md#12100001-入参错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12100002](../errorcode-access-token.md#12100002-tokenid不存在) |
| [12100003](../errorcode-access-token.md#12100003-权限名不存在) |
| [12100004](../errorcode-access-token.md#12100004-接口未配套使用) |
| [12100007](../errorcode-access-token.md#12100007-系统服务工作异常) |

## 示例

```TypeScript
import { privacyManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tokenID: number = 0; // 可以通过应用BundleInfo中的ApplicationInfo的accessTokenId字段获取。
// 开始使用指定权限
privacyManager.startUsingPermission(tokenID, 'ohos.permission.READ_AUDIO').then(() => {
  console.info('startUsingPermission success');
}).catch((err: BusinessError): void => {
  console.error(`startUsingPermission fail, code: ${err.code}, message: ${err.message}`);
});
```


## startUsingPermission

```TypeScript
function startUsingPermission(
    tokenID: number,
    permissionName: Permissions,
    pid?: number,
    usedType?: PermissionUsedType
  ): Promise<void>
```

系统应用调用此接口，能够向系统上报应用在前后台的权限使用状态。隐私服务将此状态通知所有该权限使用状态变更事件的订阅者（订阅方法参考  
[on](privacyManager.on(type: 'activeStateChange', permissionList: Array&lt;Permissions&gt;, callback: Callback&lt;ActiveChangeResponse&gt;))）。使用Promise异步回调。

开始使用权限后，需要在权限使用结束时调用  
[stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md#stopusingpermission)停止使用权限。

**起始版本：** 18

**需要权限：** ohos.permission.PERMISSION_USED_STATS

<!--Device-privacyManager-function startUsingPermission(    tokenID: int,    permissionName: Permissions,    pid?: int,    usedType?: PermissionUsedType  ): Promise<void>--><!--Device-privacyManager-function startUsingPermission(    tokenID: int,    permissionName: Permissions,    pid?: int,    usedType?: PermissionUsedType  ): Promise<void>-End-->

**系统能力：** SystemCapability.Security.AccessToken

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tokenID | number | 是 |
| permissionName | Permissions | 是 |
| pid | number | 否 |
| usedType | [PermissionUsedType](arkts-ability-privacymanager-permissionusedtype-e-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [12100008](../errorcode-access-token.md#12100008-内存申请失败) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12100001](../errorcode-access-token.md#12100001-入参错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12100003](../errorcode-access-token.md#12100003-权限名不存在) |
| [12100004](../errorcode-access-token.md#12100004-接口未配套使用) |
| [12100007](../errorcode-access-token.md#12100007-系统服务工作异常) |

## 示例

```TypeScript
import { privacyManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { rpc } from '@kit.IPCKit';

let tokenID: number = rpc.IPCSkeleton.getCallingTokenId(); // 也可以通过应用BundleInfo中的ApplicationInfo的accessTokenId字段获取。
let pid: number = rpc.IPCSkeleton.getCallingPid();
let usedType: privacyManager.PermissionUsedType = privacyManager.PermissionUsedType.PICKER_TYPE;

// 开始使用指定权限
privacyManager.startUsingPermission(tokenID, 'ohos.permission.READ_AUDIO').then(() => {
  console.info('startUsingPermission success');
}).catch((err: BusinessError): void => {
  console.error(`startUsingPermission fail, code: ${err.code}, message: ${err.message}`);
});
// with pid
privacyManager.startUsingPermission(tokenID, 'ohos.permission.READ_AUDIO', pid).then(() => {
  console.info('startUsingPermission success');
}).catch((err: BusinessError): void => {
  console.error(`startUsingPermission fail, code: ${err.code}, message: ${err.message}`);
});
// with usedType
privacyManager.startUsingPermission(tokenID, 'ohos.permission.READ_AUDIO', -1, usedType).then(() => {
  console.info('startUsingPermission success');
}).catch((err: BusinessError): void => {
  console.error(`startUsingPermission fail, code: ${err.code}, message: ${err.message}`);
});
// with pid and usedType
privacyManager.startUsingPermission(tokenID, 'ohos.permission.READ_AUDIO', pid, usedType).then(() => {
  console.info('startUsingPermission success');
}).catch((err: BusinessError): void => {
  console.error(`startUsingPermission fail, code: ${err.code}, message: ${err.message}`);
});
```


## startUsingPermission

```TypeScript
function startUsingPermission(
     tokenID: number,
     permissionName: Permissions,
     pid?: number,
     usedType?: PermissionUsedType,
     options?: PermissionUsingOptions
   ): Promise<void>
```

系统应用调用此接口，能够向系统上报应用在前后台的权限使用状态。隐私服务将此状态通知所有该权限使用状态变更事件的订阅者（订阅方法参考  
[on](privacyManager.on(type: 'activeStateChange', permissionList: Array&lt;Permissions&gt;, callback:Callback&lt;ActiveChangeResponse&gt;))）。使用Promise异步回调。

开始使用权限后，需要在权限使用结束时调用  
[stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md#stopusingpermission)停止使用权限。

当传入pid时，pid需要与  
[stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md#stopusingpermission)传入的pid相同，不满足配套关系返回错误码12100004。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.PERMISSION_USED_STATS

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-privacyManager-function startUsingPermission(     tokenID: int,     permissionName: Permissions,     pid?: int,     usedType?: PermissionUsedType,     options?: PermissionUsingOptions   ): Promise<void>--><!--Device-privacyManager-function startUsingPermission(     tokenID: int,     permissionName: Permissions,     pid?: int,     usedType?: PermissionUsedType,     options?: PermissionUsingOptions   ): Promise<void>-End-->

**系统能力：** SystemCapability.Security.AccessToken

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tokenID | number | 是 |
| permissionName | Permissions | 是 |
| pid | number | 否 |
| usedType | [PermissionUsedType](arkts-ability-privacymanager-permissionusedtype-e-sys.md) | 否 |
| options | [PermissionUsingOptions](arkts-ability-privacymanager-permissionusingoptions-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [12100008](../errorcode-access-token.md#12100008-内存申请失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12100001](../errorcode-access-token.md#12100001-入参错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12100003](../errorcode-access-token.md#12100003-权限名不存在) |
| [12100004](../errorcode-access-token.md#12100004-接口未配套使用) |
| [12100007](../errorcode-access-token.md#12100007-系统服务工作异常) |

## 示例

```TypeScript
import { privacyManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { rpc } from '@kit.IPCKit';

let tokenID: number = rpc.IPCSkeleton.getCallingTokenId(); // 也可以通过应用BundleInfo中的ApplicationInfo的accessTokenId字段获取。
let pid: number = rpc.IPCSkeleton.getCallingPid();
let usedType: privacyManager.PermissionUsedType = privacyManager.PermissionUsedType.PICKER_TYPE;

// 不带pid和usedType参数
privacyManager.startUsingPermission(tokenID, 'ohos.permission.READ_AUDIO').then(() => {
  console.info('startUsingPermission success.');
}).catch((err: BusinessError): void => {
  console.error(`startUsingPermission fail, code: ${err.code}, message: ${err.message}`);
});
// 带pid参数
privacyManager.startUsingPermission(tokenID, 'ohos.permission.READ_AUDIO', pid).then(() => {
  console.info('startUsingPermission success.');
}).catch((err: BusinessError): void => {
  console.error(`startUsingPermission fail, code: ${err.code}, message: ${err.message}`);
});
// 带usedType参数
privacyManager.startUsingPermission(tokenID, 'ohos.permission.READ_AUDIO', -1, usedType).then(() => {
  console.info('startUsingPermission success.');
}).catch((err: BusinessError): void => {
  console.error(`startUsingPermission fail, code: ${err.code}, message: ${err.message}`);
});
// 带pid和usedType参数
privacyManager.startUsingPermission(tokenID, 'ohos.permission.READ_AUDIO', pid, usedType).then(() => {
  console.info('startUsingPermission success.');
}).catch((err: BusinessError): void => {
  console.error(`startUsingPermission fail, code: ${err.code}, message: ${err.message}`);
});
// 带pid、usedType和enhancedIdentity
privacyManager.startUsingPermission(tokenID, 'ohos.permission.READ_AUDIO', pid, usedType, {enhancedIdentity: 'test'}).then(() => {
  console.info('startUsingPermission success.');
}).catch((err: BusinessError): void => {
  console.error(`startUsingPermission fail, code: ${err.code}, message: ${err.message}`);
});
```


## startUsingPermission

```TypeScript
function startUsingPermission(
    tokenID: number,
    permissionName: Permissions,
    callback: AsyncCallback<void>
  ): void
```

系统应用调用此接口，能够向系统上报应用在前后台的权限使用状态。隐私服务将此状态通知所有该权限使用状态变更事件的订阅者（订阅方法参考  
[on](privacyManager.on(type: 'activeStateChange', permissionList: Array&lt;Permissions&gt;, callback: Callback&lt;ActiveChangeResponse&gt;))）。使用callback异步回调。

开始使用权限后，需要在权限使用结束时调用  
[stopUsingPermission](arkts-ability-privacymanager-stopusingpermission-f-sys.md#stopusingpermission)停止使用权限。

**起始版本：** 9

**需要权限：** ohos.permission.PERMISSION_USED_STATS

<!--Device-privacyManager-function startUsingPermission(    tokenID: int,    permissionName: Permissions,    callback: AsyncCallback<void>  ): void--><!--Device-privacyManager-function startUsingPermission(    tokenID: int,    permissionName: Permissions,    callback: AsyncCallback<void>  ): void-End-->

**系统能力：** SystemCapability.Security.AccessToken

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tokenID | number | 是 |
| permissionName | Permissions | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [12100008](../errorcode-access-token.md#12100008-内存申请失败) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [12100001](../errorcode-access-token.md#12100001-入参错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [12100002](../errorcode-access-token.md#12100002-tokenid不存在) |
| [12100003](../errorcode-access-token.md#12100003-权限名不存在) |
| [12100004](../errorcode-access-token.md#12100004-接口未配套使用) |
| [12100007](../errorcode-access-token.md#12100007-系统服务工作异常) |

## 示例

```TypeScript
import { privacyManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let tokenID: number = 0; // 可以通过应用BundleInfo中的ApplicationInfo的accessTokenId字段获取。
// 开始使用指定权限
privacyManager.startUsingPermission(tokenID, 'ohos.permission.READ_AUDIO', (err: BusinessError, data: void) => {
  if (err) {
    console.error(`startUsingPermission fail, code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('startUsingPermission success');
  }
});
```
