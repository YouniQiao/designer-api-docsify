# destroyAbilityConnectionSession

## Modules to Import

```TypeScript
import { abilityConnectionManager } from 'kits/@kit.DistributedServiceKit';
```

## destroyAbilityConnectionSession

```TypeScript
function destroyAbilityConnectionSession(sessionId: int): void
```

Destroys a collaboration session between applications.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-abilityConnectionManager-function destroyAbilityConnectionSession(sessionId: int): void--><!--Device-abilityConnectionManager-function destroyAbilityConnectionSession(sessionId: int): void-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sessionId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Collaboration session ID. |

## Examples

```TypeScript
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

hilog.info(0x0000, 'testTag', 'destroyAbilityConnectionSession called');
let sessionId = 100;
abilityConnectionManager.destroyAbilityConnectionSession(sessionId);
```

