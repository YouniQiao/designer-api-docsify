# clearSession（系统接口）

## 导入模块

```TypeScript
import { cliManager } from 'kits/@kit.AbilityKit';
```

## clearSession

```TypeScript
function clearSession(sessionId: string): Promise<void>
```

Close session and force kill tool process.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**需要权限：** ohos.permission.EXEC_CLI_TOOL

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-cliManager-function clearSession(sessionId: string): Promise<void>--><!--Device-cliManager-function clearSession(sessionId: string): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sessionId | string | 是 | The session id of target tool process. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied, interface caller does not have permission "ohos.permission.EXEC_CLI_TOOL". |
| 202 | Not system application. Interface caller is not a system app. |
| 35600050 | System Error. 1. Connect to system service failed; 2.System service failed to communicate with dependency module. |
| 35600032 | The session does not exist. |

