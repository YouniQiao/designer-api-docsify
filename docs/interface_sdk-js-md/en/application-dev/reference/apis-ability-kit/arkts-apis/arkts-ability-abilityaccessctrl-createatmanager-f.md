# createAtManager

## Modules to Import

```TypeScript
import { Context } from 'Context';
import { PermissionRequestResult } from 'PermissionRequestResult';
import { Permissions } from 'Permissions';
```

## createAtManager

```TypeScript
function createAtManager(): AtManager
```

Creates a program access control management instance for scenarios such as permission verification, runtime permission request, settings page authorization guidance, and permission status change monitoring. After the call is successful, an AtManager instance is returned, which can be used for subsequent permission management operations.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-abilityAccessCtrl-function createAtManager(): AtManager--><!--Device-abilityAccessCtrl-function createAtManager(): AtManager-End-->

**System capability:** SystemCapability.Security.AccessToken

**Return value:**

| Type | Description |
| --- | --- |
| [AtManager](arkts-ability-abilityaccessctrl-atmanager-i.md) | AtManager** instance obtained. |

**Examples**

```TypeScript
let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
```

