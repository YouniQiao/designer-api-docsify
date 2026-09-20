# @ohos.app.function.functionManager

The module provides the capability to manage and invoke functions in the system.

@namespace functionManager

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { functionManager, FunctionHook, InvokeFunctionParam, FunctionResultWrap } from '@kit.AbilityKit';
```

## Summary

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [invokeFunction](arkts-ability-functionmanager-invokefunction-f-sys.md) | Invoke a function by functionNamespace and functionName. |
| [queryFunctions](arkts-ability-functionmanager-queryfunctions-f-sys.md) | Query all available functions. |
| [registerFunctionHook](arkts-ability-functionmanager-registerfunctionhook-f-sys.md) | Register a function hook for intercepting function invocation. Only one function hook can be registered at a time; registering again while one is already active will fail. This API is only available in developer mode. To update a registered hook, call unregisterFunctionHook first, then register again. The hook object must implement at least one of the optional methods in FunctionHook. |
| [unregisterFunctionHook](arkts-ability-functionmanager-unregisterfunctionhook-f-sys.md) | Unregister the previously registered function hook. The hook object must be the same as the one passed to registerFunctionHook. If no hook is registered, the call will fail with an error. |
<!--DelEnd-->

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [InvokeOptions](arkts-ability-functionmanager-invokeoptions-i-sys.md) | Invoke options for function execution. |
| [InvokeResult](arkts-ability-functionmanager-invokeresult-i-sys.md) | Encapsulates the success or failure status of function invocation. |
<!--DelEnd-->
