# getChildProcessInfos

## Modules to Import

```TypeScript
import { childProcessManager } from 'kits/@kit.AbilityKit';
```

## getChildProcessInfos

```TypeScript
function getChildProcessInfos(): Promise<Array<ChildProcessInformation>>
```

Obtains the information about the child processes of the current application. This API uses a promise to return the result. The returned child processes include those created through [startChildProcess](arkts-ability-childprocessmanager-startchildprocess-f.md) (in APP_SPAWN_FORK mode), [startArkChildProcess](arkts-ability-childprocessmanager-startarkchildprocess-f.md), and [startNativeChildProcess](arkts-ability-childprocessmanager-startnativechildprocess-f.md). [OH_Ability_CreateNativeChildProcess] [OH_Ability_CreateNativeChildProcessWithConfigs] [OH_Ability_StartNativeChildProcess] [OH_Ability_StartNativeChildProcessWithConfigs]

> **NOTE：**&gt;
> The child process started in SELF_FORK mode is not included in the returned list.
> If no child processes exist, an empty array is returned.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;ChildProcessInformation & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
