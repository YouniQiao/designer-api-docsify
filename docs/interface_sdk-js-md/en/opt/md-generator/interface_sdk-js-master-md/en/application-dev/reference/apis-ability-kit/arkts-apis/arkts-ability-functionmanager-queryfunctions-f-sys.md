# queryFunctions (System API)

## Modules to Import

```TypeScript
import { functionManager } from 'kits/@kit.AbilityKit';
```

## queryFunctions

```TypeScript
function queryFunctions(): Promise<Array<FunctionInfo>>
```

Query all available functions.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_FUNCTION

**Model restriction:** This API can be used only in the stage model.

<!--Device-functionManager-function queryFunctions(): Promise<Array<FunctionInfo>>--><!--Device-functionManager-function queryFunctions(): Promise<Array<FunctionInfo>>-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[FunctionInfo](arkts-ability-functioninfo-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 35600050 |
