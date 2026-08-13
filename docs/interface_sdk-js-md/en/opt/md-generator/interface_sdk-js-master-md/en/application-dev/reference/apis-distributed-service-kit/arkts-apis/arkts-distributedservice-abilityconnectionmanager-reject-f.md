# reject

## Modules to Import

```TypeScript
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
```

## reject

```TypeScript
function reject(token: string, reason: string): void
```

Rejects a connection request in a cross-device collaboration session. After a connection request sent from the peer application is rejected, a rejection reason is returned.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-abilityConnectionManager-function reject(token: string, reason: string): void--><!--Device-abilityConnectionManager-function reject(token: string, reason: string): void-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| token | string | Yes |
| reason | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## Examples

```TypeScript
import { AbilityConstant, UIAbility, Want} from '@kit.AbilityKit';
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class EntryAbility extends UIAbility {
    onCollaborate(wantParam: Record<string, Object>): AbilityConstant.CollaborateResult {
      hilog.info(0x0000, 'testTag', '%{public}s', 'on collaborate');
      let collabParam = wantParam["ohos.extra.param.key.supportCollaborateIndex"] as Record<string, Object>;
      const collabToken = collabParam["ohos.dms.collabToken"] as string;
      const reason = "test";
      hilog.info(0x0000, 'testTag', 'reject begin');
      abilityConnectionManager.reject(collabToken, reason);
      return AbilityConstant.CollaborateResult.REJECT;
    }
}
```
