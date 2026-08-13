# getAccountManager

## Modules to Import

```TypeScript
import { osAccount } from '@kit.BasicServicesKit';
```

## getAccountManager

```TypeScript
function getAccountManager(): AccountManager
```

Obtains an **AccountManager** instance.

**Since:** 23

**Deprecated since:** -1

<!--Device-osAccount-function getAccountManager(): AccountManager--><!--Device-osAccount-function getAccountManager(): AccountManager-End-->

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AccountManager](arkts-basicservices-osaccount-accountmanager-i.md) |

## Examples

```TypeScript
let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
```
