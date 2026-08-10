# getToolInfoByName（系统接口）

## 导入模块

```TypeScript
import { cliManager } from 'kits/@kit.AbilityKit';
```

## getToolInfoByName

```TypeScript
function getToolInfoByName(toolName: string): Promise<ToolInfo>
```

Get detailed information of a single tool by its name

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**需要权限：** ohos.permission.QUERY_CLI_TOOL

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-cliManager-function getToolInfoByName(toolName: string): Promise<ToolInfo>--><!--Device-cliManager-function getToolInfoByName(toolName: string): Promise<ToolInfo>-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| toolName | string | 是 | The name of target tool. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;[ToolInfo](arkts-ability-toolinfo-i-sys.md)&gt; | detailed information of tool. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 35600030 | No tool with the specified name exists. |
| 201 | Permission denied, interface caller does not have permission "ohos.permission.QUERY_CLI_TOOL". |
| 202 | Not system application. Interface caller is not a system app. |
| 35600050 | System Error. 1. Connect to system service failed; 2.System service failed to communicate with dependency module. |

