# isLocalWantAgent (System API)

## Modules to Import

```TypeScript
import { wantAgent, WantAgent } from 'kits/@kit.AbilityKit';
```

## isLocalWantAgent

```TypeScript
function isLocalWantAgent(agent: WantAgent): boolean
```

Checks whether the specified WantAgent is local.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [agent](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-request-agent-n.md) | [WantAgent](arkts-ability-wantagent-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
