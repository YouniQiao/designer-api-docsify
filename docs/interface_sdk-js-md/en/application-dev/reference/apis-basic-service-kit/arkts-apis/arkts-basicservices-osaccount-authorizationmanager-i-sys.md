# AuthorizationManager (System API)

系统账号授权管理类，用于管理系统账号授权。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

<!--Device-osAccount-interface AuthorizationManager--><!--Device-osAccount-interface AuthorizationManager-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
```

## acquireAuthorization

```TypeScript
acquireAuthorization(privilege: string, options?: AcquireAuthorizationOptions): Promise<AcquireAuthorizationResult>
```

为当前进程获取授权。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Required permissions:** ohos.permission.ACQUIRE_LOCAL_ACCOUNT_AUTHORIZATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-AuthorizationManager-acquireAuthorization(privilege: string, options?: AcquireAuthorizationOptions): Promise<AcquireAuthorizationResult>--><!--Device-AuthorizationManager-acquireAuthorization(privilege: string, options?: AcquireAuthorizationOptions): Promise<AcquireAuthorizationResult>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| privilege | string | Yes | 目标权限，详见 [配置文件](https://gitcode.com/openharmony/account_os_account/blob/master/services/accountmgr/authorization_manager/config/privileges.json) 。 |
| options | [AcquireAuthorizationOptions](arkts-basicservices-osaccount-acquireauthorizationoptions-i-sys.md) | No | 获取授权的选项，默认为空。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;AcquireAuthorizationResult&gt; | Promise对象，返回获取授权的结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission denied. |
| 12300002 | Invalid privilege or options. |
| 202 | Not system application. |
| 12300001 | The system service works abnormally. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let authorizationManager: osAccount.AuthorizationManager = osAccount.getAuthorizationManager();
let privilege: string = 'testPrivilege';
let options: osAccount.AcquireAuthorizationOptions = {
  challenge: new Uint8Array([1, 2, 3]),
  isReuseNeeded: true,
  isInteractionAllowed: true,
};
try {
  authorizationManager.acquireAuthorization(privilege, options).then((result: osAccount.AcquireAuthorizationResult) => {
    console.info(`acquireAuthorization successfully, resultCode: ${result.resultCode}`);
  }).catch((err: BusinessError) => {
    console.error(`acquireAuthorization failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`acquireAuthorization exception: code is ${err.code}, message is ${err.message}`);
}
```

## hasAuthorization

```TypeScript
hasAuthorization(privilege: string): Promise<boolean>
```

检查当前进程是否已获得指定特权的授权。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AuthorizationManager-hasAuthorization(privilege: string): Promise<boolean>--><!--Device-AuthorizationManager-hasAuthorization(privilege: string): Promise<boolean>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| privilege | string | Yes | 目标权限，详见 [配置文件](https://gitcode.com/openharmony/account_os_account/blob/master/services/accountmgr/authorization_manager/config/privileges.json) 。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象，返回true表示已获得指定特权的授权；返回false表示未获得指定特权的授权。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12300002 | Invalid privilege. |
| 202 | Not system application. |
| 12300001 | The system service works abnormally. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let authorizationManager: osAccount.AuthorizationManager = osAccount.getAuthorizationManager();
let privilege: string = 'testPrivilege';

try {
  authorizationManager.hasAuthorization(privilege).then((isAuthorized: boolean) => {
    console.info(`Privilege: ${privilege} has been authorized: ${isAuthorized}`);
  }).catch((e:Error) => {
    const err = e as BusinessError;
    console.error(`hasAuthorization failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`hasAuthorization exception: code is ${err.code}, message is ${err.message}`);
}
```

## releaseAuthorization

```TypeScript
releaseAuthorization(privilege: string): Promise<void>
```

为当前进程撤销指定特权的授权。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AuthorizationManager-releaseAuthorization(privilege: string): Promise<void>--><!--Device-AuthorizationManager-releaseAuthorization(privilege: string): Promise<void>-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| privilege | string | Yes | 目标权限，详见 [配置文件](https://gitcode.com/openharmony/account_os_account/blob/master/services/accountmgr/authorization_manager/config/privileges.json) 。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 12300002 | Invalid privilege. |
| 202 | Not system application. |
| 12300001 | The system service works abnormally. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let authorizationManager: osAccount.AuthorizationManager = osAccount.getAuthorizationManager();
let privilege: string = 'testPrivilege';

try {
  authorizationManager.releaseAuthorization(privilege).then(() => {
    console.info('releaseAuthorization success');
  }).catch((e:Error) => {
    const err = e as BusinessError;
    console.error(`releaseAuthorization failed, code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  const err = e as BusinessError;
  console.error(`releaseAuthorization exception: code is ${err.code}, message is ${err.message}`);
}
```

