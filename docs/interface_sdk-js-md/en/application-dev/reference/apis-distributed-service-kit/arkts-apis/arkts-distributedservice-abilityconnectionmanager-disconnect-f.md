# disconnect

## Modules to Import

```TypeScript
import { abilityConnectionManager } from 'kits/@kit.DistributedServiceKit';
```

## disconnect

```TypeScript
function disconnect(sessionId: int): void
```

Disconnects the UIAbility connection to end the collaboration session.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-abilityConnectionManager-function disconnect(sessionId: int): void--><!--Device-abilityConnectionManager-function disconnect(sessionId: int): void-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sessionId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | ID of the collaboration session. |

## Examples

```TypeScript
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

hilog.info(0x0000, 'testTag', 'disconnectRemoteAbility begin');
let sessionId = 100;
abilityConnectionManager.disconnect(sessionId);
```

