# getAuthorizationManager (System API)

## Modules to Import

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
```

## getAuthorizationManager

```TypeScript
function getAuthorizationManager(): AuthorizationManager
```

获取系统账号授权管理器。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-osAccount-function getAuthorizationManager(): AuthorizationManager--><!--Device-osAccount-function getAuthorizationManager(): AuthorizationManager-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| [AuthorizationManager](arkts-basicservices-osaccount-authorizationmanager-i-sys.md) | 返回系统账号授权管理的实例对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | Not system application. |

## Examples

```TypeScript
let authorizationManager: osAccount.AuthorizationManager = osAccount.getAuthorizationManager();
```

