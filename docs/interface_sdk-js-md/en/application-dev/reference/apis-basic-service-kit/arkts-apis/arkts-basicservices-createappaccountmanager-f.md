# createAppAccountManager

## Modules to Import

```TypeScript
import { appAccount } from '@kit.BasicServicesKit';
```

## createAppAccountManager

```TypeScript
function createAppAccountManager(): AppAccountManager
```

Creates an **AppAccountManager** object.

**Since:** 7

**System capability:** SystemCapability.Account.AppAccount

**Return value:**

| Type | Description |
| --- | --- |
| AppAccountManager | **AppAccountManager** object created. |

**Example**

```TypeScript
let appAccountManager: appAccount.AppAccountManager = appAccount.createAppAccountManager();

```

