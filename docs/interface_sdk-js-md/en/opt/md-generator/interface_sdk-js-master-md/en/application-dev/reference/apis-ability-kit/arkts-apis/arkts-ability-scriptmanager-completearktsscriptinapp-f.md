# completeArkTSScriptInApp

## Modules to Import

```TypeScript
import { scriptManager } from '@kit.AbilityKit';
```

## completeArkTSScriptInApp

```TypeScript
function completeArkTSScriptInApp(context: Context, requestCode: string, result: ExecuteResult): Promise<void>
```

complete arkTS script for in-app skills.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-scriptManager-function completeArkTSScriptInApp(context: Context, requestCode: string, result: ExecuteResult): Promise<void>--><!--Device-scriptManager-function completeArkTSScriptInApp(context: Context, requestCode: string, result: ExecuteResult): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](arkts-ability-context-c.md) | Yes |
| requestCode | string | Yes |
| result | [ExecuteResult](arkts-ability-scriptmanager-executeresult-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000020](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000020-context-is-not-an-abilitylevel-context) |
| [16000050](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-internal-error) |
| [16000003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000003-id-does-not-exist) |
