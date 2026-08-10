# invokeFunction（系统接口）

## 导入模块

```TypeScript
import { functionManager } from 'kits/@kit.AbilityKit';
```

## invokeFunction

```TypeScript
function invokeFunction(functionNamespace: string, functionName: string,
    args: Record<string, Object>, options?: InvokeOptions): Promise<InvokeResult>
```

Invoke a function by functionNamespace and functionName.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**需要权限：** ohos.permission.ACCESS_FUNCTION

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-functionManager-function invokeFunction(functionNamespace: string, functionName: string,    args: Record<string, Object>, options?: InvokeOptions): Promise<InvokeResult>--><!--Device-functionManager-function invokeFunction(functionNamespace: string, functionName: string,    args: Record<string, Object>, options?: InvokeOptions): Promise<InvokeResult>-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| functionNamespace | string | 是 | The namespace of the target function. |
| functionName | string | 是 | The name of the target function. |
| args | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Object&gt; | 是 | The input arguments for the function. |
| options | [InvokeOptions](arkts-ability-functionmanager-invokeoptions-i-sys.md) | 否 | The options for this invocation. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;InvokeResult&gt; | The promise used to return the result of function invocation. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 35600062 | The function execute timeout. |
| 35600061 | The function execute failed. |
| 35600060 | The function does not exist. |
| 201 | Permission denied. |
| 202 | Not system application. |
| 35600050 | System Error. 1. Connect to system service failed; 2.System service failed to communicate with dependency module. |

