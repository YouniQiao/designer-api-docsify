# createAtManager

## Modules to Import

```TypeScript
import { Context, Permissions, PermissionRequestResult } from '@kit.AbilityKit';
```

## createAtManager

```TypeScript
function createAtManager(): AtManager
```

Creates a program access control management instance for scenarios such as permission verification, runtime permission request, settings page authorization guidance, and permission status change monitoring. After the call is successful, an AtManager instance is returned, which can be used for subsequent permission management operations.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-abilityAccessCtrl-function createAtManager(): AtManager--><!--Device-abilityAccessCtrl-function createAtManager(): AtManager-End-->

**System capability:** SystemCapability.Security.AccessToken

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AtManager](arkts-ability-abilityaccessctrl-atmanager-i.md) |

## Examples

```TypeScript
// Create a permission management instance
let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
```
