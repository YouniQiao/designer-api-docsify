# sendExecuteResult

## Modules to Import

```TypeScript
import { insightIntentProvider } from 'kits/@kit.AbilityKit';
```

## sendExecuteResult

```TypeScript
function sendExecuteResult(instanceId: number, result: insightIntent.ExecuteResult): Promise<void>
```

Send execute result.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| instanceId | number | Yes |
| result | insightIntent.ExecuteResult | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000003](../errorcode-ability.md#16000003-id-does-not-exist) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
