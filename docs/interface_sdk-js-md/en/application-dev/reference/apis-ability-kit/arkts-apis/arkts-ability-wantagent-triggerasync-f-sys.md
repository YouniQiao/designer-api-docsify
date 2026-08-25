# triggerAsync (System API)

## Modules to Import

```TypeScript
import { wantAgent, WantAgent } from 'kits/@kit.AbilityKit';
```

## triggerAsync

```TypeScript
function triggerAsync(agent: WantAgent, triggerInfo: TriggerInfo, context: Context): Promise<CompleteData>
```

Asynchronously triggers a predefined operation encration encapsulated in a Wantagent with specified trigger information. If the specified wantAgent is local, you need to apply for permission: ohos.permission.TRIGGER_LOCAL_WANTAGENT permission.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [agent](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-request-agent-n.md) | [WantAgent](arkts-ability-wantagent-t.md) | Yes |
| triggerInfo | [TriggerInfo](arkts-ability-wantagent-triggerinfo-t.md) | Yes |
| context | [Context](arkts-ability-context-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;CompleteData & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16000020](../errorcode-ability.md#16000020-context-is-not-an-ability-level-context) |
| [16000151](../errorcode-ability.md#16000151-invalid-wantagent-object) |
| [16000153](../errorcode-ability.md#16000153-wantagent-object-is-canceled) |
