# invokeFunction (System API)

## Modules to Import

```TypeScript
import { functionManager } from 'kits/@kit.AbilityKit';
```

## invokeFunction

```TypeScript
function invokeFunction(functionNamespace: string, functionName: string,
    args: Record<string, Object>, options?: InvokeOptions): Promise<InvokeResult>
```

Invoke a function by functionNamespace and functionName.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_FUNCTION

**Model restriction:** This API can be used only in the stage model.

<!--Device-functionManager-function invokeFunction(functionNamespace: string, functionName: string,    args: Record<string, Object>, options?: InvokeOptions): Promise<InvokeResult>--><!--Device-functionManager-function invokeFunction(functionNamespace: string, functionName: string,    args: Record<string, Object>, options?: InvokeOptions): Promise<InvokeResult>-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| functionNamespace | string | Yes |
| functionName | string | Yes |
| args | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Object&gt; | Yes |
| options | [InvokeOptions](arkts-ability-functionmanager-invokeoptions-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;InvokeResult&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 35600062 |
| 35600061 |
| 35600060 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 35600050 |
