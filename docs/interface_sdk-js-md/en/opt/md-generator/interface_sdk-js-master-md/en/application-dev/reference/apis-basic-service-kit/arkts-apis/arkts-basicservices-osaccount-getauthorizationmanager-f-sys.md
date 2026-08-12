# getAuthorizationManager (System API)

## Modules to Import

```TypeScript
import { osAccount } from '@kit.BasicServicesKit';
```

## getAuthorizationManager

```TypeScript
function getAuthorizationManager(): AuthorizationManager
```

Obtains this OS account authorization manager.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-osAccount-function getAuthorizationManager(): AuthorizationManager--><!--Device-osAccount-function getAuthorizationManager(): AuthorizationManager-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AuthorizationManager](arkts-basicservices-osaccount-authorizationmanager-i-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
let authorizationManager: osAccount.AuthorizationManager = osAccount.getAuthorizationManager();
```
