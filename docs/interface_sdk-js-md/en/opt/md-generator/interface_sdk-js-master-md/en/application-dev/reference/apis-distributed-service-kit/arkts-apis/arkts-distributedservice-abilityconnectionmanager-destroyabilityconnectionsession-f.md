# destroyAbilityConnectionSession

## Modules to Import

```TypeScript
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
```

## destroyAbilityConnectionSession

```TypeScript
function destroyAbilityConnectionSession(sessionId: number): void
```

Destroys a collaboration session between applications.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-abilityConnectionManager-function destroyAbilityConnectionSession(sessionId: int): void--><!--Device-abilityConnectionManager-function destroyAbilityConnectionSession(sessionId: int): void-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sessionId | number | Yes |

## Examples

```TypeScript
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

hilog.info(0x0000, 'testTag', 'destroyAbilityConnectionSession called');
let sessionId = 100;
abilityConnectionManager.destroyAbilityConnectionSession(sessionId);
```
