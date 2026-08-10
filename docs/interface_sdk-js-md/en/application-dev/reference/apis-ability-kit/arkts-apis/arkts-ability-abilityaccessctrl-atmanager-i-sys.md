# AtManager

程序访问控制管理类，提供权限校验、运行时权限弹窗申请、设置页授权引导、全局开关请求和权限状态监听等能力。通过[createAtManager](arkts-ability-abilityaccessctrl-createatmanager-f.md#createatmanager)获取实例。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-abilityAccessCtrl-interface AtManager--><!--Device-abilityAccessCtrl-interface AtManager-End-->

**System capability:** SystemCapability.Security.AccessToken

## Modules to Import

```TypeScript
import { Context, Permissions, PermissionRequestResult } from 'kits/@kit.AbilityKit';
```

## generateCliAuthResult

```TypeScript
generateCliAuthResult(
      hostTokenID: int,
      agentID: string,
      authInfoList: Array<CliAuthInfo>): Promise<ToolAuthResult>
```

根据CLI授权信息生成授权结果。使用Promise异步回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.MANAGE_TOOL_RUNTIME_PERMISSIONS

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtManager-generateCliAuthResult(      hostTokenID: int,      agentID: string,      authInfoList: Array<CliAuthInfo>): Promise<ToolAuthResult>--><!--Device-AtManager-generateCliAuthResult(      hostTokenID: int,      agentID: string,      authInfoList: Array<CliAuthInfo>): Promise<ToolAuthResult>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| hostTokenID | int | Yes | 访问CLI指令的应用的tokenID。可通过应用BundleInfo中的ApplicationInfo中的[accessTokenId](arkts-ability-applicationinfo-i.md#accesstokenid)字段获取。传入无效值时返回错误码12100001。 &lt;br&gt;取值限定为整数。取值约束：该参数必须为大于0的整数。 &lt;br&gt;BundleInfo获取可参考：[bundleManager.getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md#getbundleinfosync)。 |
| agentID | string | Yes | 用于标识发起CLI相关操作的智能体体标识。传入无效值时返回错误码12100001。 &lt;br&gt;取值约束：长度不能超过48个字符。 |
| authInfoList | Array&lt;CliAuthInfo&gt; | Yes | CLI授权信息列表，每项包含CLI信息（主命令和子命令名称）、待授权的权限名称列表和对应的授权结果列表。传入无效值时返回错误码12100001。 &lt;br&gt;最大长度为99且不能为空。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ToolAuthResult&gt; | Promise对象，返回生成的授权结果，包含授权结果字符串列表，可用于传递给CLI工具执行命令。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12100009 | Common internal error. The account is not logged in, network is not connected or an internal error occurs when generating authorization results. |
| 201 | Permission denied. Interface caller does not have permission "ohos.permission.MANAGE_TOOL_RUNTIME_PERMISSIONS". |
| 12100001 | Invalid parameter. The hostTokenID is 0, the agentID exceeds 48 characters, authInfoList is empty or contains more than 99 items, the cliName in cliInfo of an item in authInfoList is empty or exceeds 256 characters, the subCliName in cliInfo of an item in authInfoList exceeds 256 characters, a permission name in permissionNames of an item in authInfoList is empty or exceeds 256 characters, or the number of permissionNames does not equal the number of authorizationResults in an item in authInfoList. |
| 202 | Not system application. Interface caller is not a system application. |
| 12100002 | The specified tokenID does not exist. |
| 12100003 | A permission name in permissionNames of an item in authInfoList does not exist. |
| 12100007 | Service exception. |

## Examples

```TypeScript
import { abilityAccessCtrl, Permissions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let hostTokenID: number = 0; // For details about how to obtain it, see the description in the AtManager section.
let agentID: string = 'agent.demo';
let authInfoList: Array<abilityAccessCtrl.CliAuthInfo> = [{
  cliInfo: {
    cliName: 'ohos-example',
    subCliName: 'run'
  },
  permissionNames: ['ohos.permission.ACCESS_SYSTEM_SETTINGS' as Permissions],
  authorizationResults: [true]
}];
atManager.generateCliAuthResult(hostTokenID, agentID, authInfoList).then((data: abilityAccessCtrl.ToolAuthResult) => {
  console.info('generateCliAuthResult success, data: ' + JSON.stringify(data));
}).catch((err: BusinessError): void => {
  console.error(`generateCliAuthResult fail, code: ${err.code}, message: ${err.message}`);
});
```

## getCliPermissionRequestInfo

```TypeScript
getCliPermissionRequestInfo(agentID: string, cliInfoList: Array<CliInfo>): Promise<PermissionDialogResult>
```

查询CLI（Command Line Interface，命令行界面）命令是否需要权限弹窗，调用成功后，返回每条命令对应的权限弹窗判定结果。使用Promise异步回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.QUERY_TOOL_PERMISSIONS

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtManager-getCliPermissionRequestInfo(agentID: string, cliInfoList: Array<CliInfo>): Promise<PermissionDialogResult>--><!--Device-AtManager-getCliPermissionRequestInfo(agentID: string, cliInfoList: Array<CliInfo>): Promise<PermissionDialogResult>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| agentID | string | Yes | 用于标识发起CLI相关操作的智能体标识。传入无效值时返回错误码12100001。 &lt;br&gt;取值约束：长度不能超过48个字符。 |
| cliInfoList | Array&lt;CliInfo&gt; | Yes | 待查询的CLI信息列表。每项包含一条命令及其子命令信息；建议按实际即将执行的命令集合传入，避免无关命令扩大判定范围。传入无效值时返回错误码12100001。 &lt;br&gt;最大长度为99且不能为空。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PermissionDialogResult&gt; | Promise对象，返回每条CLI命令的权限弹窗判定结果，包含是否需要弹窗、未满足的权限列表及决策状态等信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12100009 | Common inner error. The account is not logged in, network is not connected or an internal error occurs when querying CLI permissions or generating auth results. |
| 201 | Permission denied. Interface caller does not have permission "ohos.permission.QUERY_TOOL_PERMISSIONS". |
| 12100001 | Invalid parameter. The agentID exceeds 48 characters, cliInfoList is empty or exceeds 99 items, the cliName of an item in cliInfoList is empty or exceeds 256 characters, the subCliName of an item in cliInfoList exceeds 256 characters, or the CLI command does not exist. |
| 202 | Not system application. Interface caller is not a system application. |
| 12100007 | Service exception. |

## Examples

```TypeScript
import { abilityAccessCtrl } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let agentID: string = 'agent.demo';
let cliInfoList: Array<abilityAccessCtrl.CliInfo> = [{
  cliName: 'ohos-example',
  subCliName: 'run'
}];
atManager.getCliPermissionRequestInfo(agentID, cliInfoList).then((data: abilityAccessCtrl.PermissionDialogResult) => {
  console.info('getCliPermissionRequestInfo success, data: ' + JSON.stringify(data));
}).catch((err: BusinessError): void => {
  console.error(`getCliPermissionRequestInfo fail, code: ${err.code}, message: ${err.message}`);
});
```

## getCliPermissions

```TypeScript
getCliPermissions(
      hostTokenID: int,
      agentID: string,
      cliInfoList: Array<CliInfo>): Promise<CliPermissionsResult>
```

查询指定应用使用的CLI命令依赖的CLI权限及映射的运行时权限。调用成功后返回每条命令的CLI权限决策状态和运行时权限映射列表。使用Promise异步回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.MANAGE_TOOL_RUNTIME_PERMISSIONS

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtManager-getCliPermissions(      hostTokenID: int,      agentID: string,      cliInfoList: Array<CliInfo>): Promise<CliPermissionsResult>--><!--Device-AtManager-getCliPermissions(      hostTokenID: int,      agentID: string,      cliInfoList: Array<CliInfo>): Promise<CliPermissionsResult>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| hostTokenID | int | Yes | 访问CLI指令的应用的tokenID。可通过应用BundleInfo中的ApplicationInfo中的[accessTokenId](arkts-ability-applicationinfo-i.md#accesstokenid)字段获取。传入无效值时返回错误码12100001。 &lt;br&gt;取值限定为整数。取值约束：该参数必须为大于0的整数。 &lt;br&gt;BundleInfo获取可参考：[bundleManager.getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md#getbundleinfosync)。 |
| agentID | string | Yes | 用于标识发起CLI相关操作的智能体标识。传入无效值时返回错误码12100001。 &lt;br&gt;取值约束：长度不能超过48个字符。 |
| cliInfoList | Array&lt;CliInfo&gt; | Yes | 待查询的CLI信息列表。每项包含一条命令及其子命令信息。传入无效值时返回错误码12100001。 &lt;br&gt;最大长度为99且不能为空。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;CliPermissionsResult&gt; | Promise对象，返回每条CLI命令依赖的CLI权限及其对应的运行时权限映射信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12100009 | Common internal error. An internal error occurs when querying CLI permissions or runtime permission information. |
| 201 | Permission denied. Interface caller does not have permission "ohos.permission.MANAGE_TOOL_RUNTIME_PERMISSIONS". |
| 12100001 | Invalid parameter. The hostTokenID is 0, the agentID exceeds 48 characters, cliInfoList is empty or contains more than 99 items, the cliName of an item in cliInfoList is empty or exceeds 256 characters, the subCliName of an item in cliInfoList exceeds 256 characters, or the CLI command does not exist. |
| 202 | Not system application. Interface caller is not a system application. |
| 12100002 | The specified tokenID does not exist. |
| 12100007 | Service exception. |

## Examples

```TypeScript
import { abilityAccessCtrl } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let hostTokenID: number = 0; // For details about how to obtain the token ID, see the description of the AtManager section.
let agentID: string = 'agent.demo';
let cliInfoList: Array<abilityAccessCtrl.CliInfo> = [{
  cliName: 'ohos-example',
  subCliName: 'run'
}];
atManager.getCliPermissions(hostTokenID, agentID, cliInfoList).then((data: abilityAccessCtrl.CliPermissionsResult) => {
  console.info('getCliPermissions success, data: ' + JSON.stringify(data));
}).catch((err: BusinessError): void => {
  console.error(`getCliPermissions fail, code: ${err.code}, message: ${err.message}`);
});
```

## getPermissionFlags

ArkTS-Dyn:
```TypeScript
getPermissionFlags(tokenID: number, permissionName: Permissions): Promise<number>
```

ArkTS-Sta:
```TypeScript
getPermissionFlags(tokenID: int, permissionName: Permissions): Promise<int>
```

获取指定应用的指定权限的标志。使用Promise异步回调。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.GET_SENSITIVE_PERMISSIONS or ohos.permission.GRANT_SENSITIVE_PERMISSIONS or ohos.permission.REVOKE_SENSITIVE_PERMISSIONS

<!--Device-AtManager-getPermissionFlags(tokenID: int, permissionName: Permissions): Promise<int>--><!--Device-AtManager-getPermissionFlags(tokenID: int, permissionName: Permissions): Promise<int>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tokenID | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 目标应用的身份标识。可通过应用BundleInfo中的ApplicationInfo中的[accessTokenId](arkts-ability-applicationinfo-i.md#accesstokenid)字段获取。传入无效值时返回错误码12100001。 &lt;br&gt;取值限定为整数。取值约束：该参数必须为大于0的整数。 &lt;br&gt;BundleInfo获取可参考：[bundleManager.getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md#getbundleinfosync)。 |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes | 查询的权限名称。传入无效值时返回错误码12100001。 &lt;br&gt;取值约束：权限名长度不能超过256个字符。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;int&gt; | Promise对象，返回查询到的权限标记值。标记值的含义请参见 [PermissionStatusInfo]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 201 | Permission denied. Interface caller does not have permission specified below. |
| 12100001 | Invalid parameter. The tokenID is 0, or the permissionName exceeds 256 characters. |
| 202 | Not System App. Interface caller is not a system app. |
| 12100002 | The specified tokenID does not exist. |
| 12100003 | The specified permission does not exist or is not declared in the module.json file. |
| 12100006 | The operation is not allowed. Either the application is a sandbox or the tokenID is from a remote device. |
| 12100007 | Service exception. |

## Examples

```TypeScript
import { abilityAccessCtrl } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let tokenID: number = 0; // For details about how to obtain the tokenID, see the description in the AtManager section.
atManager.getPermissionFlags(tokenID, 'ohos.permission.GRANT_SENSITIVE_PERMISSIONS').then((data: number) => {
  console.info(`getPermissionFlags success, result: ${data}`);
}).catch((err: BusinessError): void => {
  console.error(`getPermissionFlags fail, code: ${err.code}, message: ${err.message}`);
});
```

## getPermissionRequestToggleStatus

```TypeScript
getPermissionRequestToggleStatus(permissionName: Permissions): Promise<PermissionRequestToggleStatus>
```

获取当前用户指定权限的弹窗开关状态。使用Promise异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.GET_SENSITIVE_PERMISSIONS

<!--Device-AtManager-getPermissionRequestToggleStatus(permissionName: Permissions): Promise<PermissionRequestToggleStatus>--><!--Device-AtManager-getPermissionRequestToggleStatus(permissionName: Permissions): Promise<PermissionRequestToggleStatus>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes | 待查询弹窗开关状态的权限名称。传入无效值时返回错误码12100001。 &lt;br&gt;取值约束：权限名长度不能超过256个字符。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PermissionRequestToggleStatus&gt; | Promise对象，返回指定权限的弹窗开关状态值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 201 | Permission denied. Interface caller does not have permission specified below. |
| 12100001 | Invalid parameter. The permissionName exceeds 256 characters, or the specified permission is not a user_grant permission. |
| 202 | Not System App. Interface caller is not a system app. |
| 12100003 | The specified permission does not exist. |
| 12100004 | This API must be used together with [setPermissionRequestToggleStatus](arkts-ability-abilityaccessctrl-atmanager-i-sys.md#setpermissionrequesttogglestatus).<br>**Applicable version:** 26.1.0 and later |
| 12100007 | Service exception. |

## Examples

```TypeScript
import { abilityAccessCtrl, Permissions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let permission: Permissions = 'ohos.permission.CAMERA';

atManager.getPermissionRequestToggleStatus(permission).then((res: abilityAccessCtrl.PermissionRequestToggleStatus) => {
  if (res == abilityAccessCtrl.PermissionRequestToggleStatus.CLOSED) {
    console.info('getPermissionRequestToggleStatus: The toggle status is close');
  } else {
    console.info('getPermissionRequestToggleStatus: The toggle status is open');
  }
}).catch((err: BusinessError): void => {
  console.error(`getPermissionRequestToggleStatus fail, code: ${err.code}, message: ${err.message}`);
});
```

## getPermissionRequestToggleStatus

```TypeScript
getPermissionRequestToggleStatus(
      permissionName: Permissions,
      subProfileId: int): Promise<PermissionRequestToggleStatus>
```

获取指定子身份资料下指定权限的弹窗开关状态。使用Promise异步回调。

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Required permissions:** ohos.permission.GET_SENSITIVE_PERMISSIONS

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtManager-getPermissionRequestToggleStatus(      permissionName: Permissions,      subProfileId: int): Promise<PermissionRequestToggleStatus>--><!--Device-AtManager-getPermissionRequestToggleStatus(      permissionName: Permissions,      subProfileId: int): Promise<PermissionRequestToggleStatus>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes | 待查询弹窗开关状态的权限名称。传入无效值时返回错误码12100001。 &lt;br&gt;取值约束：权限名长度不能超过256个字。 |
| subProfileId | int | Yes | 子身份资料的标识符。可以通过[OsAccountSubProfile.id](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-osaccountsubprofile-i-sys.md/arkts-basicservices-osaccount-osaccountsubprofile-i-sys.md#id)获取。 &lt;br&gt;取值限定为整数。取值约束：该参数必须为大于0的整数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PermissionRequestToggleStatus&gt; | Promise对象，返回指定权限的弹窗开关状态值 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 12100009 | Common inner error. A database error occurs. |
| 201 | Permission denied. Interface caller does not have permission specified below. |
| 12100001 | Invalid parameter. The permissionName exceeds 256 characters, the specified permission is not a user_grant permission, or the specified subProfileId does not exist for the current user. |
| 202 | Not System App. Interface caller is not a system app. |
| 12100003 | The specified permission does not exist. |
| 12100007 | Service exception. |

## getPermissionsStatus

ArkTS-Dyn:
```TypeScript
getPermissionsStatus(tokenID: number, permissionList: Array<Permissions>): Promise<Array<PermissionStatus>>
```

ArkTS-Sta:
```TypeScript
getPermissionsStatus(tokenID: int, permissionList: Array<Permissions>): Promise<Array<PermissionStatus>>
```

获取指定应用权限状态列表。使用Promise异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.GET_SENSITIVE_PERMISSIONS

<!--Device-AtManager-getPermissionsStatus(tokenID: int, permissionList: Array<Permissions>): Promise<Array<PermissionStatus>>--><!--Device-AtManager-getPermissionsStatus(tokenID: int, permissionList: Array<Permissions>): Promise<Array<PermissionStatus>>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tokenID | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 目标应用的身份标识。可通过应用BundleInfo中的ApplicationInfo中的[accessTokenId](arkts-ability-applicationinfo-i.md#accesstokenid)字段获取。传入无效值时返回错误码12100001。 &lt;br&gt;取值限定为整数。取值约束：该参数必须为大于0的整数。 &lt;br&gt;BundleInfo获取可参考：[bundleManager.getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md#getbundleinfosync)。 |
| permissionList | Array&lt;[Permissions](arkts-ability-permissions-t.md)&gt; | Yes | 待获取权限状态的权限名列表。传入无效值时返回错误码12100001。 &lt;br&gt;最大长度为1024且不能为空。取值约束：权限名长度不能超过256个字符。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;PermissionStatus&gt;&gt; | Promise对象，返回查询到的权限状态列表。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 201 | Permission denied. Interface caller does not have permission "ohos.permission.GET_SENSITIVE_PERMISSIONS". |
| 12100001 | Invalid parameter. The tokenID is 0 or the permissionList is empty or exceeds the size limit. |
| 202 | Not System App. Interface caller is not a system app. |
| 12100002 | The specified tokenID does not exist. |
| 12100007 | Service exception. |

## Examples

```TypeScript
import { abilityAccessCtrl } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let tokenID: number = 0; // For details about how to obtain the tokenID, see the description in the AtManager section.
atManager.getPermissionsStatus(tokenID, ['ohos.permission.CAMERA']).then((data: Array<abilityAccessCtrl.PermissionStatus>) => {
  console.info(`getPermissionsStatus success, result: ${data}`);
}).catch((err: BusinessError): void => {
  console.error(`getPermissionsStatus fail, code: ${err.code}, message: ${err.message}`);
});
```

## getVersion

ArkTS-Dyn:
```TypeScript
getVersion(): Promise<number>
```

ArkTS-Sta:
```TypeScript
getVersion(): Promise<int>
```

获取当前权限管理的数据版本号。使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AtManager-getVersion(): Promise<int>--><!--Device-AtManager-getVersion(): Promise<int>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;int&gt; | Promise对象，返回查询到的版本号。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | Not System App. Interface caller is not a system app. |

## Examples

```TypeScript
import { abilityAccessCtrl } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let promise = atManager.getVersion();
promise.then((data: number) => {
  console.info(`getVersion promise: data->${data}`);
}).catch((err: BusinessError): void => {
  console.error(`getVersion fail, code: ${err.code}, message: ${err.message}`);
});
```

## grantPermission

ArkTS-Dyn:
```TypeScript
grantPermission(tokenID: number, permissionName: Permissions, permissionFlags: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
grantPermission(tokenID: int, permissionName: Permissions, permissionFlags: int): Promise<void>
```

授予应用权限。调用成功后，指定应用获得该权限，可以访问相应的受保护资源。与  
[grantUserGrantedPermission](arkts-ability-abilityaccessctrl-atmanager-i-sys.md#grantusergrantedpermission)仅支持user_grant类型权限不同,该接口同时支持user_grant和manual_settings类型的权限授予。使用Promise异步回调。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.GRANT_SENSITIVE_PERMISSIONS

<!--Device-AtManager-grantPermission(tokenID: int, permissionName: Permissions, permissionFlags: int): Promise<void>--><!--Device-AtManager-grantPermission(tokenID: int, permissionName: Permissions, permissionFlags: int): Promise<void>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tokenID | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 目标应用的身份标识。可通过应用BundleInfo中的ApplicationInfo中的[accessTokenId](arkts-ability-applicationinfo-i.md#accesstokenid)字段获取。传入无效值时返回错误码12100001。 &lt;br&gt;取值限定为整数。取值约束：该参数必须为大于0的整数。 &lt;br&gt;BundleInfo获取可参考：[bundleManager.getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md#getbundleinfosync)。 |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes | 被授予的权限名称。权限名长度不能超过256个字符，超过限制时返回错误码12100001。 |
| permissionFlags | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 授权选项。 &lt;br&gt;取值限定为整数。 &lt;br&gt;- 1表示当次用户若选择禁止该权限，下次权限弹窗仍可以弹出申请用户授权。 &lt;br&gt;- 2表示当次用户若选择禁止该权限，下次不会再弹出权限弹窗，用户需要在系统设置的权限管理中进行授权。 &lt;br&gt;- 64表示当次用户若选择仅本次允许，权限仅本次授权。应用切换后台状态或退出后取消授权。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12100014 | Unexpected permission. The specified permission is not a user_grant or manual_settings permission. |
| 201 | Permission denied. Interface caller does not have permission "ohos.permission.GRANT_SENSITIVE_PERMISSIONS". |
| 12100001 | Invalid parameter. The tokenID is 0, the permissionName exceeds 256 characters or is not declared in the module.json file, or the flags value is invalid. |
| 202 | Not System App. Interface caller is not a system app. |
| 12100002 | The specified tokenID does not exist. |
| 12100003 | The specified permission does not exist. |
| 12100006 | The application specified by the tokenID is not allowed to be granted with the specified permission. Either the application is a sandbox or the tokenID is from a remote device. |
| 12100007 | Service exception. |

## Examples

```TypeScript
import { abilityAccessCtrl } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let tokenID: number = 0; // For details about how to obtain the tokenID, see the description in the AtManager section.
let permissionFlags: number = 2;
atManager.grantPermission(tokenID, 'ohos.permission.READ_AUDIO', permissionFlags).then(() => {
  console.info('grantPermission success');
}).catch((err: BusinessError): void => {
  console.error(`grantPermission fail, code: ${err.code}, message: ${err.message}`);
});
```

## grantUserGrantedPermission

ArkTS-Dyn:
```TypeScript
grantUserGrantedPermission(tokenID: number, permissionName: Permissions, permissionFlags: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
grantUserGrantedPermission(tokenID: int, permissionName: Permissions, permissionFlags: int): Promise<void>
```

授予应用user_grant权限。调用成功后，应用获得该user_grant权限，可以访问相应的受保护资源。使用Promise异步回调。

本接口仅支持授予user_grant类型的权限。若需要授予user_grant或manual_settings类型权限，建议使用  
[grantPermission](arkts-ability-abilityaccessctrl-atmanager-i-sys.md#grantpermission)。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.GRANT_SENSITIVE_PERMISSIONS

<!--Device-AtManager-grantUserGrantedPermission(tokenID: int, permissionName: Permissions, permissionFlags: int): Promise<void>--><!--Device-AtManager-grantUserGrantedPermission(tokenID: int, permissionName: Permissions, permissionFlags: int): Promise<void>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tokenID | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 目标应用的身份标识。可通过应用BundleInfo中的ApplicationInfo中的[accessTokenId](arkts-ability-applicationinfo-i.md#accesstokenid)字段获取。传入无效值时返回错误码12100001。 &lt;br&gt;取值限定为整数。取值约束：该参数必须为大于0的整数。 &lt;br&gt;BundleInfo获取可参考：[bundleManager.getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md#getbundleinfosync)。 |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes | 被授予的权限名称。超过限制时返回错误码12100001。 &lt;br&gt;取值约束：权限名长度不能超过256个字符。 |
| permissionFlags | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 授权选项。 &lt;br&gt;取值限定为整数。 &lt;br&gt;- 1表示当次用户若选择禁止该权限，下次权限弹窗仍可以弹出申请用户授权。 &lt;br&gt;- 2表示当次用户若选择禁止该权限，下次不会再弹出权限弹窗，用户需要在系统设置的权限管理中进行授权。 &lt;br&gt;- 64表示当次用户若选择仅本次允许，权限仅本次授权。应用切换后台状态或退出后取消授权。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 201 | Permission denied. Interface caller does not have permission "ohos.permission.GRANT_SENSITIVE_PERMISSIONS". |
| 12100001 | Invalid parameter. The tokenID is 0, the permissionName exceeds 256 characters or is not declared in the module.json file, or the flags value is invalid. |
| 202 | Not System App. Interface caller is not a system app. |
| 12100002 | The specified tokenID does not exist. |
| 12100003 | The specified permission does not exist or is not a user_grant permission. |
| 12100006 | The application specified by the tokenID is not allowed to be granted with the specified permission. Either the application is a sandbox or the tokenID is from a remote device. |
| 12100007 | Service exception. |

## Examples

```TypeScript
import { abilityAccessCtrl } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let tokenID: number = 0; // For details about how to obtain the tokenID, see the description in the AtManager section.
let permissionFlags: number = 1;
atManager.grantUserGrantedPermission(tokenID, 'ohos.permission.READ_AUDIO', permissionFlags).then(() => {
  console.info('grantUserGrantedPermission success');
}).catch((err: BusinessError): void => {
  console.error(`grantUserGrantedPermission fail, code: ${err.code}, message: ${err.message}`);
});
```

## grantUserGrantedPermission

ArkTS-Dyn:
```TypeScript
grantUserGrantedPermission(
        tokenID: number,
        permissionName: Permissions,
        permissionFlags: number,
        callback: AsyncCallback<void>
    ): void
```

ArkTS-Sta:
```TypeScript
grantUserGrantedPermission(
        tokenID: int,
        permissionName: Permissions,
        permissionFlags: int,
        callback: AsyncCallback<void>
    ): void
```

授予应用user_grant权限。使用callback异步回调。调用成功后，应用获得该user_grant权限，可以访问相应的受保护资源。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.GRANT_SENSITIVE_PERMISSIONS

<!--Device-AtManager-grantUserGrantedPermission(        tokenID: int,        permissionName: Permissions,        permissionFlags: int,        callback: AsyncCallback<void>    ): void--><!--Device-AtManager-grantUserGrantedPermission(        tokenID: int,        permissionName: Permissions,        permissionFlags: int,        callback: AsyncCallback<void>    ): void-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tokenID | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 目标应用的身份标识。可通过应用BundleInfo中的ApplicationInfo中的[accessTokenId](arkts-ability-applicationinfo-i.md#accesstokenid)字段获取。传入无效值时返回错误码12100001。 &lt;br&gt;取值限定为整数。取值约束：该参数必须为大于0的整数。 &lt;br&gt;BundleInfo获取可参考：[bundleManager.getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md#getbundleinfosync)。 |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes | 被授予的权限名称。传入无效值时返回错误码12100001。 &lt;br&gt;取值约束：权限名长度不能超过256个字符。 |
| permissionFlags | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 授权选项。 &lt;br&gt;取值限定为整数。 &lt;br&gt;- 1表示当次用户若选择禁止该权限，下次权限弹窗仍可以弹出申请用户授权。 &lt;br&gt;- 2表示当次用户若选择禁止该权限，下次不会再弹出权限弹窗，用户需要在系统设置的权限管理中进行授权。 &lt;br&gt;- 64表示当次用户若选择仅本次允许，权限仅本次授权。应用切换后台状态或退出后取消授权。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当授予权限成功时，err为undefined，否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 201 | Permission denied. Interface caller does not have permission "ohos.permission.GRANT_SENSITIVE_PERMISSIONS". |
| 12100001 | Invalid parameter. The tokenID is 0, the permissionName exceeds 256 characters or is not declared in the module.json file, or the flags value is invalid. |
| 202 | Not System App. Interface caller is not a system app. |
| 12100002 | The specified tokenID does not exist. |
| 12100003 | The specified permission does not exist or is not a user_grant permission. |
| 12100006 | The application specified by the tokenID is not allowed to be granted with the specified permission. Either the application is a sandbox or the tokenID is from a remote device. |
| 12100007 | Service exception. |

## Examples

```TypeScript
import { abilityAccessCtrl } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let tokenID: number = 0; // For details about how to obtain the tokenID, see the description in the AtManager section.
let permissionFlags: number = 1;
atManager.grantUserGrantedPermission(tokenID, 'ohos.permission.READ_AUDIO', permissionFlags, (err: BusinessError, data: void) => {
  if (err) {
    console.error(`grantUserGrantedPermission fail, code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('grantUserGrantedPermission success');
  }
});
```

## off('permissionStateChange')

```TypeScript
off(
      type: 'permissionStateChange',
      tokenIDList: Array<int>,
      permissionList: Array<Permissions>,
      callback?: Callback<PermissionStateChangeInfo>
    ): void
```

取消订阅指定tokenID列表与权限列表的权限状态变更事件。使用callback异步回调。

取消订阅时，若不传入callback，则批量取消与tokenIDList和permissionList完全匹配的所有监听回调。

> **说明：**
> 该接口通常与[on](abilityAccessCtrl.AtManager.on)配套使用，用于取消通过on创建的监听关系。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Required permissions:** ohos.permission.GET_SENSITIVE_PERMISSIONS

<!--Device-AtManager-off(      type: 'permissionStateChange',      tokenIDList: Array<int>,      permissionList: Array<Permissions>,      callback?: Callback<PermissionStateChangeInfo>    ): void--><!--Device-AtManager-off(      type: 'permissionStateChange',      tokenIDList: Array<int>,      permissionList: Array<Permissions>,      callback?: Callback<PermissionStateChangeInfo>    ): void-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'permissionStateChange' | Yes | 订阅事件类型，固定为'permissionStateChange'，权限状态变更事件。 |
| tokenIDList | Array&lt;int&gt; | Yes | 取消订阅的tokenID列表，为空时表示取消订阅所有的应用的权限状态变化，必须与on的输入一致。应用的身份标识可通过应用BundleInfo中的ApplicationInfo中的[accessTokenId](arkts-ability-applicationinfo-i.md#accesstokenid)字段获取。传入无效值时返回错误码12100001。 &lt;br&gt;最大长度为1024。取值约束：列表中的tokenID必须为大于0的整数。 &lt;br&gt;BundleInfo获取可参考：[bundleManager.getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md#getbundleinfosync)。 |
| permissionList | Array&lt;[Permissions](arkts-ability-permissions-t.md)&gt; | Yes | 取消订阅的权限名列表，为空时表示取消订阅所有的权限状态变化，必须与on的输入一致。传入无效值时返回错误码12100001。 &lt;br&gt;最大长度为1024。取值约束：列表中的权限名需为有效权限名，权限名长度不能超过256个字符。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;PermissionStateChangeInfo&gt; | No | 回调函数。返回取消订阅指定tokenID与指定权限名状态变更事件的对象，需与 on注册时的callback一致。不传入此参数时，将取消与tokenIDList和permissionList完全匹配的所有监听回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 201 | Permission denied. Interface caller does not have permission "ohos.permission.GET_SENSITIVE_PERMISSIONS". |
| 12100001 | Invalid parameter. The tokenIDList or permissionList is not in the listening list. |
| 202 | Not System App. Interface caller is not a system app. |
| 12100007 | Service exception. |

## Examples

```TypeScript
import { abilityAccessCtrl, Permissions, bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
  let bundleInfo: bundleManager.BundleInfo = bundleManager.getBundleInfoForSelfSync(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION);
  let tokenIDList: Array<number> = [bundleInfo.appInfo.accessTokenId];
  let permissionList: Array<Permissions> = ['ohos.permission.DISTRIBUTED_DATASYNC'];
  atManager.off('permissionStateChange', tokenIDList, permissionList);
} catch (err) {
  let error = err as BusinessError;
  console.error(`catch errcode: ${error.code}, message: ${error.message}`);
}
```

## offPermissionStateChange

```TypeScript
offPermissionStateChange(
      tokenIDList: Array<int>,
      permissionList: Array<Permissions>,
      callback?: Callback<PermissionStateChangeInfo>
    ): void
```

取消订阅指定tokenID列表与权限列表的权限状态变更事件。使用callback异步回调。

取消订阅时，若不传入callback，则批量取消与tokenIDList和permissionList完全匹配的所有监听回调。

> **说明：**
> 该接口通常与[onPermissionStateChange](abilityAccessCtrl.AtManager.onPermissionStateChange)
> 配套使用，用于取消通过onPermissionStateChange创建的监听关系。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.GET_SENSITIVE_PERMISSIONS

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtManager-offPermissionStateChange(      tokenIDList: Array<int>,      permissionList: Array<Permissions>,      callback?: Callback<PermissionStateChangeInfo>    ): void--><!--Device-AtManager-offPermissionStateChange(      tokenIDList: Array<int>,      permissionList: Array<Permissions>,      callback?: Callback<PermissionStateChangeInfo>    ): void-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tokenIDList | Array&lt;int&gt; | Yes | 取消订阅的tokenID列表，为空时表示取消订阅所有的应用的权限状态变化，必须与on的输入一致。应用的身份标识可通过应用BundleInfo中的ApplicationInfo中的[accessTokenId](arkts-ability-applicationinfo-i.md#accesstokenid)字段获取。传入无效值时返回错误码12100001。 &lt;br&gt;最大长度为1024。取值约束：列表中的tokenID必须为大于0的整数。 &lt;br&gt;BundleInfo获取可参考：[bundleManager.getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md#getbundleinfosync)。 |
| permissionList | Array&lt;[Permissions](arkts-ability-permissions-t.md)&gt; | Yes | 取消订阅的权限名列表，为空时表示取消订阅所有的权限状态变化，必须与on的输入一致。传入无效值时返回错误码12100001。 &lt;br&gt;最大长度为1024。取值约束：列表中的权限名需为有效权限名，权限名长度不能超过256个字符。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;PermissionStateChangeInfo&gt; | No | 回调函数。返回取消订阅指定tokenID与指定权限名状态变更事件的对象，需与 onPermissionStateChange注册时的callback一致。不传入此参数时，将取消与tokenIDList和permissionList完全匹配的所有监听回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission denied. Interface caller does not have permission "ohos.permission.GET_SENSITIVE_PERMISSIONS". |
| 12100001 | Invalid parameter. The tokenIDList or permissionList is not in the listening list. |
| 202 | Not System App. Interface caller is not a system app. |
| 12100007 | Service exception. |

## on('permissionStateChange')

```TypeScript
on(
      type: 'permissionStateChange',
      tokenIDList: Array<int>,
      permissionList: Array<Permissions>,
      callback: Callback<PermissionStateChangeInfo>
    ): void
```

订阅指定tokenID列表与权限列表的权限状态变更事件。使用callback异步回调。

允许指定tokenID列表与权限列表订阅多个callback。

> **说明：**
> 若新的订阅与已有订阅在tokenID列表和权限列表上存在交集，不允许使用相同的callback进行订阅。
> 该接口通常与[off](abilityAccessCtrl.AtManager.of)配套使用，当不再需要监听时应调用off取消订阅。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Required permissions:** ohos.permission.GET_SENSITIVE_PERMISSIONS

<!--Device-AtManager-on(      type: 'permissionStateChange',      tokenIDList: Array<int>,      permissionList: Array<Permissions>,      callback: Callback<PermissionStateChangeInfo>    ): void--><!--Device-AtManager-on(      type: 'permissionStateChange',      tokenIDList: Array<int>,      permissionList: Array<Permissions>,      callback: Callback<PermissionStateChangeInfo>    ): void-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'permissionStateChange' | Yes | 订阅事件类型，固定为'permissionStateChange'，权限状态变更事件。 |
| tokenIDList | Array&lt;int&gt; | Yes | 订阅的tokenID列表，为空时表示订阅所有的应用的权限状态变化。应用的身份标识可通过应用BundleInfo中的ApplicationInfo中的[accessTokenId](arkts-ability-applicationinfo-i.md#accesstokenid)字段获取。传入无效值时返回错误码12100001。 &lt;br&gt;最大长度为1024。取值约束：列表中的tokenID必须为大于0的整数。 &lt;br&gt;BundleInfo获取可参考：[bundleManager.getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md#getbundleinfosync)。 |
| permissionList | Array&lt;[Permissions](arkts-ability-permissions-t.md)&gt; | Yes | 订阅的权限名列表，为空时表示订阅所有的权限状态变化。传入无效值时返回错误码12100001。 &lt;br&gt;最大长度为1024且不能为空。取值约束：列表中的权限名需为有效权限名，权限名长度不能超过256个字符。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;PermissionStateChangeInfo&gt; | Yes | 回调函数。订阅指定tokenID与指定权限名状态变更事件的回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12100008 | Out of memory. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 201 | Permission denied. Interface caller does not have permission "ohos.permission.GET_SENSITIVE_PERMISSIONS". |
| 12100001 | Invalid parameter. Possible causes: 1. The tokenIDList or permissionList exceeds the size limit; 2. The tokenIDs or permissionNames in the list are all invalid. |
| 202 | Not System App. Interface caller is not a system app. |
| 12100005 | The registration time has exceeded the limit. |
| 12100007 | Service exception. |

## Examples

```TypeScript
import { abilityAccessCtrl, Permissions, bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
  let bundleInfo: bundleManager.BundleInfo = bundleManager.getBundleInfoForSelfSync(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION);
  let tokenIDList: Array<number> = [bundleInfo.appInfo.accessTokenId];
  let permissionList: Array<Permissions> = ['ohos.permission.DISTRIBUTED_DATASYNC'];

  atManager.on('permissionStateChange', tokenIDList, permissionList, (data: abilityAccessCtrl.PermissionStateChangeInfo) => {
    console.info('receive permission state change');
    console.info(`data change: ${data.change}, tokenID: ${data.tokenID}, permission name: ${data.permissionName}`);
    });
} catch (err) {
  let error = err as BusinessError;
  console.error(`catch errcode: ${error.code}, message: ${error.message}`);
}
```

## onPermissionStateChange

```TypeScript
onPermissionStateChange(
      tokenIDList: Array<int>,
      permissionList: Array<Permissions>,
      callback: Callback<PermissionStateChangeInfo>
    ): void
```

订阅指定tokenID列表与权限列表的权限状态变更事件。使用callback异步回调。

允许指定tokenID列表与权限列表订阅多个callback。

若新的订阅与已有订阅在tokenID列表和权限列表上存在交集，不允许使用相同的callback进行订阅。

该接口通常与[offPermissionStateChange](abilityAccessCtrl.AtManager.offPermissionStateChange)配套使用，当不再需要监听时应调用offPermissionStateChange取消订阅。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.GET_SENSITIVE_PERMISSIONS

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtManager-onPermissionStateChange(      tokenIDList: Array<int>,      permissionList: Array<Permissions>,      callback: Callback<PermissionStateChangeInfo>    ): void--><!--Device-AtManager-onPermissionStateChange(      tokenIDList: Array<int>,      permissionList: Array<Permissions>,      callback: Callback<PermissionStateChangeInfo>    ): void-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tokenIDList | Array&lt;int&gt; | Yes | 订阅的tokenID列表，为空时表示订阅所有的应用的权限状态变化。应用的身份标识可通过应用BundleInfo中的ApplicationInfo中的[accessTokenId](arkts-ability-applicationinfo-i.md#accesstokenid)字段获取。传入无效值时返回错误码12100001。 &lt;br&gt;最大长度为1024。取值约束：列表中的tokenID必须为大于0的整数。 &lt;br&gt;BundleInfo获取可参考：[bundleManager.getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md#getbundleinfosync)。 |
| permissionList | Array&lt;[Permissions](arkts-ability-permissions-t.md)&gt; | Yes | 订阅的权限名列表，为空时表示订阅所有的权限状态变化。传入无效值时返回错误码12100001。 &lt;br&gt;最大长度为1024。取值约束：列表中的权限名需为有效权限名，权限名长度不能超过256个字符。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;PermissionStateChangeInfo&gt; | Yes | 回调函数。订阅指定tokenID与指定权限名状态变更事件的回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12100008 | Out of memory. |
| 201 | Permission denied. Interface caller does not have permission "ohos.permission.GET_SENSITIVE_PERMISSIONS". |
| 12100001 | Invalid parameter. Possible causes: 1. The tokenIDList or permissionList exceeds the size limit; 2. The tokenIDs or permissionNames in the list are all invalid. |
| 202 | Not System App. Interface caller is not a system app. |
| 12100005 | The registration time has exceeded the limit. |
| 12100007 | Service exception. |

## queryStatusByPermission

```TypeScript
queryStatusByPermission(
      permissionList: Array<Permissions>): Promise<Array<PermissionStatusInfo>>
```

根据权限列表查询所有已请求过该权限的应用及其权限状态。使用Promise异步回调。当查询的数据结果的大小超过50000条时，接口会直接返回12100015错误码。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.GET_SENSITIVE_PERMISSIONS

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtManager-queryStatusByPermission(      permissionList: Array<Permissions>): Promise<Array<PermissionStatusInfo>>--><!--Device-AtManager-queryStatusByPermission(      permissionList: Array<Permissions>): Promise<Array<PermissionStatusInfo>>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| permissionList | Array&lt;[Permissions](arkts-ability-permissions-t.md)&gt; | Yes | 待查询的权限名称列表。传入无效值时返回错误码12100001。 &lt;br&gt;最大长度为1024且不能为空。取值约束：权限名长度不能超过256个字符。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;PermissionStatusInfo&gt;&gt; | Promise对象，返回查询到的权限状态信息列表。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12100015 | The queried data exceeds the upper limit. |
| 201 | Permission denied. Interface caller does not have permission "ohos.permission.GET_SENSITIVE_PERMISSIONS". |
| 12100001 | Invalid parameter. The permissionList is empty or exceeds the size limit. |
| 202 | Not system application. Interface caller is not a system application. |
| 12100003 | The specified permission does not exist. |
| 12100007 | Service exception. |

## Examples

```TypeScript
import { abilityAccessCtrl, Permissions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let permissionList: Array<Permissions> = ['ohos.permission.CAMERA'];
atManager.queryStatusByPermission(permissionList).then((data: Array<abilityAccessCtrl.PermissionStatusInfo>) => {
  console.info('queryStatusByPermission success, data: ' + JSON.stringify(data));
}).catch((err: BusinessError): void => {
  console.error(`queryStatusByPermission fail, code: ${err.code}, message: ${err.message}`);
});
```

## queryStatusByTokenID

ArkTS-Dyn:
```TypeScript
queryStatusByTokenID(tokenIDList: Array<number>): Promise<Array<PermissionStatusInfo>>
```

ArkTS-Sta:
```TypeScript
queryStatusByTokenID(tokenIDList: Array<int>): Promise<Array<PermissionStatusInfo>>
```

根据应用tokenID列表查询其所有的权限状态。使用Promise异步回调。当查询的数据结果的大小超过50000条时，接口会直接返回12100015错误码。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.GET_SENSITIVE_PERMISSIONS

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtManager-queryStatusByTokenID(tokenIDList: Array<int>): Promise<Array<PermissionStatusInfo>>--><!--Device-AtManager-queryStatusByTokenID(tokenIDList: Array<int>): Promise<Array<PermissionStatusInfo>>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tokenIDList | ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt; | Yes | 待查询的应用tokenID列表。应用的身份标识可通过应用BundleInfo中的ApplicationInfo中的[accessTokenId](arkts-ability-applicationinfo-i.md#accesstokenid)字段获取。传入无效值时返回错误码12100001。 &lt;br&gt;最大长度为1024且不能为空。取值约束：列表中的tokenID必须为大于0的整数。 &lt;br&gt;BundleInfo获取可参考：[bundleManager.getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md#getbundleinfosync)。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;PermissionStatusInfo&gt;&gt; | Promise对象，返回查询到的权限状态信息列表。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12100015 | The queried data exceeds the upper limit. |
| 201 | Permission denied. Interface caller does not have permission "ohos.permission.GET_SENSITIVE_PERMISSIONS". |
| 12100001 | Invalid parameter. The tokenIDList is empty or exceeds the size limit. |
| 202 | Not system application. Interface caller is not a system application. |
| 12100002 | The specified tokenID does not exist. |
| 12100007 | Service exception. |

## Examples

```TypeScript
import { abilityAccessCtrl } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let tokenID: number = 0; // For details about how to obtain the token ID, see the description in the AtManager section.
let tokenIDList: Array<number> = [tokenID];
atManager.queryStatusByTokenID(tokenIDList).then((data: Array<abilityAccessCtrl.PermissionStatusInfo>) => {
  console.info('queryStatusByTokenID success, data: ' + JSON.stringify(data));
}).catch((err: BusinessError): void => {
  console.error(`queryStatusByTokenID fail, code: ${err.code}, message: ${err.message}`);
});
```

## requestPermissionOnApplicationSetting

ArkTS-Dyn:
```TypeScript
requestPermissionOnApplicationSetting(tokenID: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
requestPermissionOnApplicationSetting(tokenID: int): Promise<void>
```

拉起应用权限设置页面。使用Promise异步回调。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtManager-requestPermissionOnApplicationSetting(tokenID: int): Promise<void>--><!--Device-AtManager-requestPermissionOnApplicationSetting(tokenID: int): Promise<void>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tokenID | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 目标应用的身份标识。可通过应用BundleInfo中的ApplicationInfo中的[accessTokenId](arkts-ability-applicationinfo-i.md#accesstokenid)字段获取。传入无效值时返回错误码12100001。 &lt;br&gt;取值限定为整数。取值约束：该参数必须为大于0的整数。 &lt;br&gt;BundleInfo获取可参考：[bundleManager.getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md#getbundleinfosync)。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12100001 | Invalid parameter. The tokenID is 0. |
| 202 | Not System App. Interface caller is not a system app. |
| 12100002 | The specified tokenID does not exist. |
| 12100007 | Service exception. |

## Examples

```TypeScript
import { abilityAccessCtrl } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let tokenID: number = 0; // For details about how to obtain the tokenID, see the description in the AtManager section.
atManager.requestPermissionOnApplicationSetting(tokenID).then(() => {
  console.info('requestPermissionOnApplicationSetting success');
}).catch((err: BusinessError): void => {
  console.error(`requestPermissionOnApplicationSetting fail, code: ${err.code}, message: ${err.message}`);
});
```

## requestPermissionsFromUserWithWindowId

ArkTS-Dyn:
```TypeScript
requestPermissionsFromUserWithWindowId(
        context: Context,
        windowId: number,
        permissionList: Array<Permissions>) : Promise<PermissionRequestResult>
```

ArkTS-Sta:
```TypeScript
requestPermissionsFromUserWithWindowId(
        context: Context,
        windowId: int,
        permissionList: Array<Permissions>) : Promise<PermissionRequestResult>
```

基于窗口ID弹出弹窗请求用户授权，调用成功后，返回本次权限申请结果对象，开发者可根据权限申请结果继续窗口级授权后的业务流程。使用Promise异步回调。

适用于系统应用需要将权限申请弹窗明确附着到指定窗口的场景。

如果用户拒绝授权，将无法再次拉起弹窗，可通过以下方式重新获取权限：1. 在系统设置界面中手动授权；2. 调用  
[requestPermissionOnSetting](arkts-ability-abilityaccessctrl-atmanager-i.md#requestpermissiononsetting)，拉起权限设置弹窗引导用户授权。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtManager-requestPermissionsFromUserWithWindowId(        context: Context,        windowId: int,        permissionList: Array<Permissions>) : Promise<PermissionRequestResult>--><!--Device-AtManager-requestPermissionsFromUserWithWindowId(        context: Context,        windowId: int,        permissionList: Array<Permissions>) : Promise<PermissionRequestResult>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes | 请求权限的UIAbility/UIExtensionAbility的Context。若传入其他应用、无效页面或非Stage模型的Context，接口可能报错或无法拉起弹窗。 |
| windowId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 应用窗口的ID。可通过[window.findWindow](../../apis-arkui/arkts-apis/arkts-arkui-window-findwindow-f.md/arkts-arkui-window-findwindow-f.md#findwindow)(窗口名). [getWindowProperties()](../../apis-arkui/arkts-apis/arkts-arkui-window-window-i.md/arkts-arkui-window-window-i.md#getwindowproperties).id获取。该参数必须对应当前有效窗口，传入已销毁、不可见或无效 窗口ID时将返回12100001。 &lt;br&gt;取值限定为整数。 |
| permissionList | Array&lt;[Permissions](arkts-ability-permissions-t.md)&gt; | Yes | 权限名列表。建议仅传入当前窗口场景下真正需要的敏感权限。 &lt;br&gt;最小长度为1。取值约束：权限名长度不能超过256个字符。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;PermissionRequestResult&gt; | Promise对象，返回本次权限申请结果，包含权限数组、授权结果、是否展示弹窗以及失败原因等信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12100009 | Common inner error. An error occurs when creating the popup window or obtaining the user operation result. |
| 12100001 | Invalid parameter. windowId is invalid. |

## Examples

For details about the process and example of applying for user authorization, see [Requesting User Authorization](../../security/AccessToken/request-user-authorization.md).

```TypeScript
import { abilityAccessCtrl, Context, PermissionRequestResult } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
// Obtain the context within the component.
let context: Context = this.getUIContext().getHostContext() as Context;
let windowId = 0; // Obtain the window ID: let windowId = window.findWindow(window name).getWindowProperties().id;
// Request user authorization for a specified permission based on the window ID
atManager.requestPermissionsFromUserWithWindowId(context, windowId, ['ohos.permission.CAMERA']).then((data: PermissionRequestResult) => {
  console.info(`requestPermissionsFromUserWithWindowId success, result: ${data}`);
  console.info('requestPermissionsFromUserWithWindowId data permissions:' + data.permissions);
  console.info('requestPermissionsFromUserWithWindowId data authResults:' + data.authResults);
  console.info('requestPermissionsFromUserWithWindowId data dialogShownResults:' + data.dialogShownResults);
  console.info('requestPermissionsFromUserWithWindowId data errorReasons:' + data.errorReasons);
}).catch((err: BusinessError): void => {
  console.error(`requestPermissionsFromUserWithWindowId fail, code: ${err.code}, message: ${err.message}`);
});
```

## revokePermission

ArkTS-Dyn:
```TypeScript
revokePermission(
      tokenID: number,
      permissionName: Permissions,
      permissionFlags: number,
      killProcess?: boolean): Promise<void>
```

ArkTS-Sta:
```TypeScript
revokePermission(
      tokenID: int,
      permissionName: Permissions,
      permissionFlags: int,
      killProcess?: boolean): Promise<void>
```

撤销应用权限。调用成功后，应用失去该权限，无法访问相应的受保护资源。根据killProcess参数的值决定是否终止应用进程。使用Promise异步回调。

当killProcess参数为true且权限状态从“已授权”变为“未授权”时，应用进程会被终止。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.REVOKE_SENSITIVE_PERMISSIONS

<!--Device-AtManager-revokePermission(      tokenID: int,      permissionName: Permissions,      permissionFlags: int,      killProcess?: boolean): Promise<void>--><!--Device-AtManager-revokePermission(      tokenID: int,      permissionName: Permissions,      permissionFlags: int,      killProcess?: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tokenID | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 目标应用的身份标识。可通过应用BundleInfo中的ApplicationInfo中的[accessTokenId](arkts-ability-applicationinfo-i.md#accesstokenid)字段获取。传入无效值时返回错误码12100001。 &lt;br&gt;取值限定为整数。取值约束：该参数必须为大于0的整数。 &lt;br&gt;BundleInfo获取可参考：[bundleManager.getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md#getbundleinfosync)。 |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes | 被撤销的权限名称。传入无效值时返回错误码12100001。 &lt;br&gt;取值约束：权限名长度不能超过256个字符。 |
| permissionFlags | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 授权选项。 &lt;br&gt;取值限定为整数。 &lt;br&gt;- 1表示当次用户若选择禁止该权限，下次权限弹窗仍可以弹出申请用户授权。 &lt;br&gt;- 2表示当次用户若选择禁止该权限，下次不会再弹出权限弹窗，用户需要在系统设置的权限管理中进行授权。 &lt;br&gt;- 64表示当次用户若选择仅本次允许，权限仅本次授权。应用切换后台状态或退出后取消授权。 |
| killProcess | boolean | No | 是否终止应用进程。 &lt;br&gt;- true表示终止应用进程。 &lt;br&gt;- false表示不终止应用进程。 &lt;br&gt;- 默认值为true。 &lt;br&gt;<br>**Since:** 26.0.0 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12100014 | Unexpected permission. The specified permission is not a user_grant or manual_settings permission. |
| 201 | Permission denied. The interface invoker does not have permission "ohos.permission.REVOKE_SENSITIVE_PERMISSIONS". |
| 12100001 | Invalid parameter. The token ID is 0, the permission name exceeds 256 characters or is not declared in the module.json file, or the value of flags is invalid. |
| 202 | Not a system application. The interface invoker is not a system application. |
| 12100002 | The specified tokenID does not exist. |
| 12100003 | The specified permission does not exist. |
| 12100006 | The specified permission is not allowed to be revoked from the application specified by the tokenID. Either the application is a sandbox or the tokenID is from a remote device. |
| 12100007 | Service exception. |

## Examples

```TypeScript
import { abilityAccessCtrl } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let tokenID: number = 0; // For details about how to obtain the tokenID, see the description in the AtManager section.
let permissionFlags: number = 2;
// Do not terminate the application process.
atManager.revokePermission(tokenID, 'ohos.permission.READ_AUDIO', permissionFlags, false).then(() => {
  console.info('revokePermission success, process not killed');
}).catch((err: BusinessError): void => {
  console.error(`revokePermission fail, code: ${err.code}, message: ${err.message}`);
});
// Terminate the application process (default behavior).
atManager.revokePermission(tokenID, 'ohos.permission.READ_AUDIO', permissionFlags).then(() => {
  console.info('revokePermission success');
}).catch((err: BusinessError): void => {
  console.error(`revokePermission fail, code: ${err.code}, message: ${err.message}`);
});
```

## revokeUserGrantedPermission

ArkTS-Dyn:
```TypeScript
revokeUserGrantedPermission(tokenID: number, permissionName: Permissions, permissionFlags: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
revokeUserGrantedPermission(tokenID: int, permissionName: Permissions, permissionFlags: int): Promise<void>
```

撤销应用user_grant权限。调用成功后，应用失去该user_grant权限，无法访问相应的受保护资源。使用Promise异步回调。

本接口仅支持撤销user_grant类型的权限，且不支持控制是否终止应用进程。若需要撤销user_grant或manual_settings类型权限，或需要控制撤销权限后是否终止应用进程，建议使用  
[revokePermission](arkts-ability-abilityaccessctrl-atmanager-i-sys.md#revokepermission)。

当权限状态从“已授权”变为“未授权”时，应用进程会被终止。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.REVOKE_SENSITIVE_PERMISSIONS

<!--Device-AtManager-revokeUserGrantedPermission(tokenID: int, permissionName: Permissions, permissionFlags: int): Promise<void>--><!--Device-AtManager-revokeUserGrantedPermission(tokenID: int, permissionName: Permissions, permissionFlags: int): Promise<void>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tokenID | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 目标应用的身份标识。可通过应用BundleInfo中的ApplicationInfo中的[accessTokenId](arkts-ability-applicationinfo-i.md#accesstokenid)字段获取。传入无效值时返回错误码12100001。 &lt;br&gt;取值限定为整数。取值约束：该参数必须为大于0的整数。 &lt;br&gt;BundleInfo获取可参考：[bundleManager.getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md#getbundleinfosync)。 |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes | 被撤销的权限名称。传入无效值时返回错误码12100001。 &lt;br&gt;取值约束：权限名长度不能超过256个字符。 |
| permissionFlags | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 授权选项。 &lt;br&gt;取值限定为整数。 &lt;br&gt;- 1表示当次用户若选择禁止该权限，下次权限弹窗仍可以弹出申请用户授权。 &lt;br&gt;- 2表示当次用户若选择禁止该权限，下次不会再弹出权限弹窗，用户需要在系统设置的权限管理中进行授权。 &lt;br&gt;- 64表示当次用户若选择仅本次允许，权限仅本次授权。应用切换后台状态或退出后取消授权。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 201 | Permission denied. Interface caller does not have permission "ohos.permission.REVOKE_SENSITIVE_PERMISSIONS". |
| 12100001 | Invalid parameter. The tokenID is 0, the permissionName exceeds 256 characters or is not declared in the module.json file, or the flags value is invalid. |
| 202 | Not System App. Interface caller is not a system app. |
| 12100002 | The specified tokenID does not exist. |
| 12100003 | The specified permission does not exist or is not a user_grant permission. |
| 12100006 | The application specified by the tokenID is not allowed to be revoked with the specified permission. Either the application is a sandbox or the tokenID is from a remote device. |
| 12100007 | Service exception. |

## Examples

```TypeScript
import { abilityAccessCtrl } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let tokenID: number = 0; // For details about how to obtain the tokenID, see the description in the AtManager section.
let permissionFlags: number = 1;
atManager.revokeUserGrantedPermission(tokenID, 'ohos.permission.READ_AUDIO', permissionFlags).then(() => {
  console.info('revokeUserGrantedPermission success');
}).catch((err: BusinessError): void => {
  console.error(`revokeUserGrantedPermission fail, code: ${err.code}, message: ${err.message}`);
});
```

## revokeUserGrantedPermission

ArkTS-Dyn:
```TypeScript
revokeUserGrantedPermission(
        tokenID: number,
        permissionName: Permissions,
        permissionFlags: number,
        callback: AsyncCallback<void>
    ): void
```

ArkTS-Sta:
```TypeScript
revokeUserGrantedPermission(
        tokenID: int,
        permissionName: Permissions,
        permissionFlags: int,
        callback: AsyncCallback<void>
    ): void
```

撤销应用user_grant权限。使用callback异步回调。调用成功后，应用失去该user_grant权限，无法访问相应的受保护资源。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.REVOKE_SENSITIVE_PERMISSIONS

<!--Device-AtManager-revokeUserGrantedPermission(        tokenID: int,        permissionName: Permissions,        permissionFlags: int,        callback: AsyncCallback<void>    ): void--><!--Device-AtManager-revokeUserGrantedPermission(        tokenID: int,        permissionName: Permissions,        permissionFlags: int,        callback: AsyncCallback<void>    ): void-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tokenID | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 目标应用的身份标识。可通过应用BundleInfo中的ApplicationInfo中的[accessTokenId](arkts-ability-applicationinfo-i.md#accesstokenid)字段获取。传入无效值时返回错误码12100001。 &lt;br&gt;取值限定为整数。取值约束：该参数必须为大于0的整数。 &lt;br&gt;BundleInfo获取可参考：[bundleManager.getBundleInfoSync](arkts-ability-bundlemanager-getbundleinfosync-f.md#getbundleinfosync)。 |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes | 被撤销的权限名称。传入无效值时返回错误码12100001。 &lt;br&gt;取值约束：权限名长度不能超过256个字符。 |
| permissionFlags | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 授权选项。 &lt;br&gt;取值限定为整数。 &lt;br&gt;- 1表示当次用户若选择禁止该权限，下次权限弹窗仍可以弹出申请用户授权。 &lt;br&gt;- 2表示当次用户若选择禁止该权限，下次不会再弹出权限弹窗，用户需要在系统设置的权限管理中进行授权。 &lt;br&gt;- 64表示当次用户若选择仅本次允许，权限仅本次授权。应用切换后台状态或退出后取消授权。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。当撤销权限成功时，err为undefined，否则为错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 201 | Permission denied. Interface caller does not have permission "ohos.permission.REVOKE_SENSITIVE_PERMISSIONS". |
| 12100001 | Invalid parameter. The tokenID is 0, the permissionName exceeds 256 characters or is not declared in the module.json file, or the flags value is invalid. |
| 202 | Not System App. Interface caller is not a system app. |
| 12100002 | The specified tokenID does not exist. |
| 12100003 | The specified permission does not exist or is not a user_grant permission. |
| 12100006 | The application specified by the tokenID is not allowed to be revoked with the specified permission. Either the application is a sandbox or the tokenID is from a remote device. |
| 12100007 | Service exception. |

## Examples

```TypeScript
import { abilityAccessCtrl } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let tokenID: number = 0; // For details about how to obtain the tokenID, see the description in the AtManager section.
let permissionFlags: number = 1;
atManager.revokeUserGrantedPermission(tokenID, 'ohos.permission.READ_AUDIO', permissionFlags, (err: BusinessError, data: void) => {
  if (err) {
    console.error(`revokeUserGrantedPermission fail, code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('revokeUserGrantedPermission success');
  }
});
```

## setPermissionRequestToggleStatus

```TypeScript
setPermissionRequestToggleStatus(permissionName: Permissions, status: PermissionRequestToggleStatus): Promise<void>
```

设置当前用户指定权限的弹窗开关状态。调用成功后，该权限的弹窗开关状态将被设置为指定值。当状态为CLOSED时，应用请求该权限时不会弹出权限弹窗；当状态为OPEN时，应用请求该权限时会正常弹出权限弹窗。使用Promise异步回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.DISABLE_PERMISSION_DIALOG

<!--Device-AtManager-setPermissionRequestToggleStatus(permissionName: Permissions, status: PermissionRequestToggleStatus): Promise<void>--><!--Device-AtManager-setPermissionRequestToggleStatus(permissionName: Permissions, status: PermissionRequestToggleStatus): Promise<void>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes | 待设置弹窗开关状态的权限名称。传入无效值时返回错误码12100001。 &lt;br&gt;取值约束：权限名长度不能超过256个字符。 |
| status | [PermissionRequestToggleStatus](arkts-ability-abilityaccessctrl-permissionrequesttogglestatus-e-sys.md) | Yes | 指定权限的弹窗开关状态值。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12100009 | Common inner error. A database error occurs. |
| 201 | Permission denied. Interface caller does not have permission specified below. |
| 12100001 | Invalid parameter. The permissionName exceeds 256 characters, the specified permission is not a user_grant permission, or the status value is invalid. |
| 202 | Not System App. Interface caller is not a system app. |
| 12100003 | The specified permission does not exist. |
| 12100006 | Operation not allowed. The toggle status of the specified permission has already been set by [setPermissionRequestToggleStatus](arkts-ability-abilityaccessctrl-atmanager-i-sys.md#setpermissionrequesttogglestatus).<br>**Applicable version:** 26.1.0 and later |
| 12100007 | Service exception. |

## Examples

```TypeScript
import { abilityAccessCtrl, Permissions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
let permission: Permissions = 'ohos.permission.CAMERA';

atManager.setPermissionRequestToggleStatus(permission, abilityAccessCtrl.PermissionRequestToggleStatus.CLOSED).then(() => {
  console.info('setPermissionRequestToggleStatus: set closed successful');
}).catch((err: BusinessError): void => {
  console.error(`setPermissionRequestToggleStatus fail, code: ${err.code}, message: ${err.message}`);
});
```

## setPermissionRequestToggleStatus

```TypeScript
setPermissionRequestToggleStatus(
      permissionName: Permissions,
      status: PermissionRequestToggleStatus,
      subProfileId: int): Promise<void>
```

设置指定子身份资料下指定权限的弹窗开关状态。调用成功后，该权限的弹窗开关状态将被设置为指定值。当状态为CLOSED时，应用请求该权限时不会弹出权限弹窗；当状态为OPEN时，应用请求该权限时会正常弹出权限弹窗。使用Promise异步回调。

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.1.0.

**Required permissions:** ohos.permission.DISABLE_PERMISSION_DIALOG

**Model restriction:** This API can be used only in the stage model.

<!--Device-AtManager-setPermissionRequestToggleStatus(      permissionName: Permissions,      status: PermissionRequestToggleStatus,      subProfileId: int): Promise<void>--><!--Device-AtManager-setPermissionRequestToggleStatus(      permissionName: Permissions,      status: PermissionRequestToggleStatus,      subProfileId: int): Promise<void>-End-->

**System capability:** SystemCapability.Security.AccessToken

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| permissionName | [Permissions](arkts-ability-permissions-t.md) | Yes | 待设置弹窗开关状态的权限名称。传入无效值时返回错误码12100001。 &lt;br&gt;取值约束：权限名长度不能超过256个字符。 |
| status | [PermissionRequestToggleStatus](arkts-ability-abilityaccessctrl-permissionrequesttogglestatus-e-sys.md) | Yes | 指定权限的弹窗开关状态值。 |
| subProfileId | int | Yes | 子身份资料的标识符。可以通过[OsAccountSubProfile.id](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-osaccountsubprofile-i-sys.md/arkts-basicservices-osaccount-osaccountsubprofile-i-sys.md#id)获取。 &lt;br&gt;取值限定为整数。取值约束：该参数必须为大于0的整数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. |
| 12100009 | Common inner error. A database error occurs. |
| 201 | Permission denied. Interface caller does not have permission specified below. |
| 12100001 | Invalid parameter. The permissionName exceeds 256 characters, the specified permission is not a user_grant permission, the status value is invalid, or the specified subProfileId does not exist for the current user. |
| 202 | Not System App. Interface caller is not a system app. |
| 12100003 | The specified permission does not exist. |
| 12100006 | Operation not allowed. The toggle status of the specified permission has already been set by [setPermissionRequestToggleStatus](arkts-ability-abilityaccessctrl-atmanager-i-sys.md#setpermissionrequesttogglestatus). |
| 12100007 | Service exception. |

