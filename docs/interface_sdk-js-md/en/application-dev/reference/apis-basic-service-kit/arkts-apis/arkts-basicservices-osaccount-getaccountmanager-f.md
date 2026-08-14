# getAccountManager

## Modules to Import

```TypeScript
import { osAccount } from 'osAccount';
```

## getAccountManager

```TypeScript
function getAccountManager(): AccountManager
```

Obtains an **AccountManager** instance.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-osAccount-function getAccountManager(): AccountManager--><!--Device-osAccount-function getAccountManager(): AccountManager-End-->

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| Type | Description |
| --- | --- |
| [AccountManager](arkts-basicservices-osaccount-accountmanager-i.md) | AccountManager** instance obtained. |

## Examples

```TypeScript
let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
```

