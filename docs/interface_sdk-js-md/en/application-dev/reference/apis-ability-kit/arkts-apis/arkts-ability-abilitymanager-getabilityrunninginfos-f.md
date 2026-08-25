# getAbilityRunningInfos

## Modules to Import

```TypeScript
import { abilityManager } from 'kits/@kit.AbilityKit';
```

## getAbilityRunningInfos

```TypeScript
function getAbilityRunningInfos(): Promise<Array<AbilityRunningInfo>>
```

Obtains the UIAbility running information. This API uses a promise to return the result.

> **NOTE：**&gt;
> If the application has requested the ohos.permission.GET_RUNNING_INFO permission, it can obtain the UIAbility
> running information of all applications; otherwise, it can obtain the UIAbility running information of the
> current application.

**Since:** 14

**Required permissions:** ohos.permission.GET_RUNNING_INFO

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;AbilityRunningInfo & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
