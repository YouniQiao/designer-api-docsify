# getAccountManager

## Modules to Import

```TypeScript
import { osAccount } from 'kits/@kit.BasicServicesKit';
```

## getAccountManager

```TypeScript
function getAccountManager(): AccountManager
```

获取系统账号管理对象。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-osAccount-function getAccountManager(): AccountManager--><!--Device-osAccount-function getAccountManager(): AccountManager-End-->

**System capability:** SystemCapability.Account.OsAccount

**Return value:**

| Type | Description |
| --- | --- |
| [AccountManager](arkts-basicservices-osaccount-accountmanager-i.md) | 系统账号管理对象。 |

## Examples

```TypeScript
let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
```

