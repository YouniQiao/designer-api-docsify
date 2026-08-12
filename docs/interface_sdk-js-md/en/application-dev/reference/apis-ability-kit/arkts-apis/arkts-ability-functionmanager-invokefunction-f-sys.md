# invokeFunction (System API)

## Modules to Import

```TypeScript
import { functionManager } from '@kit.AbilityKit';
```

## invokeFunction

```TypeScript
function invokeFunction(functionNamespace: string, functionName: string,
    args: Record<string, Object>, options?: InvokeOptions): Promise<InvokeResult>
```

Invoke a function by functionNamespace and functionName.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.ACCESS_FUNCTION

**Model restriction:** This API can be used only in the stage model.

<!--Device-functionManager-function invokeFunction(functionNamespace: string, functionName: string,    args: Record<string, Object>, options?: InvokeOptions): Promise<InvokeResult>--><!--Device-functionManager-function invokeFunction(functionNamespace: string, functionName: string,    args: Record<string, Object>, options?: InvokeOptions): Promise<InvokeResult>-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| functionNamespace | string | Yes | The namespace of the target function. |
| functionName | string | Yes | The name of the target function. |
| args | Record&lt;string, Object&gt; | Yes | The input arguments for the function. |
| options | [InvokeOptions](arkts-ability-functionmanager-invokeoptions-i-sys.md) | No | The options for this invocation. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[InvokeResult](arkts-ability-functionmanager-invokeresult-i-sys.md)&gt; | The promise used to return the result of function invocation. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35600062 | The function execute timeout. |
| 35600061 | The function execute failed. |
| 35600060 | The function does not exist. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |
| 35600050 | System Error. 1. Connect to system service failed; 2.System service failed to communicate with dependency module. |

