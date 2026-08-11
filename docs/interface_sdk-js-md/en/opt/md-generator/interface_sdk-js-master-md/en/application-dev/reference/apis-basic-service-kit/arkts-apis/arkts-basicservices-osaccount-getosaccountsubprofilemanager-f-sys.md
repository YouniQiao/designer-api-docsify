# getOsAccountSubProfileManager (System API)

## Modules to Import

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
```

## getOsAccountSubProfileManager

```TypeScript
function getOsAccountSubProfileManager(): OsAccountSubProfileManager
```

Obtains an OS account sub-profile manager instance.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-osAccount-function getOsAccountSubProfileManager(): OsAccountSubProfileManager--><!--Device-osAccount-function getOsAccountSubProfileManager(): OsAccountSubProfileManager-End-->

**System capability:** SystemCapability.Account.OsAccount

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [OsAccountSubProfileManager](arkts-basicservices-osaccount-osaccountsubprofilemanager-i-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
let subProfileManager: osAccount.OsAccountSubProfileManager = osAccount.getOsAccountSubProfileManager();
```
