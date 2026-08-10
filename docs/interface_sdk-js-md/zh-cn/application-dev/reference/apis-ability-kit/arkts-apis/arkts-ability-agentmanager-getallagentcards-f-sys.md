# getAllAgentCards（系统接口）

## 导入模块

```TypeScript
import { agentManager } from 'kits/@kit.AbilityKit';
```

## getAllAgentCards

```TypeScript
function getAllAgentCards(): Promise<Array<AgentCard>>
```

Gets all AgentCards on the device.

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**需要权限：** ohos.permission.GET_AGENT_CARD

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-agentManager-function getAllAgentCards(): Promise<Array<AgentCard>>--><!--Device-agentManager-function getAllAgentCards(): Promise<Array<AgentCard>>-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Array&lt;[AgentCard](arkts-ability-agentcard-i.md)&gt;&gt; | Returns the array of AgentCard. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 16000050 | Internal error. Possible causes: 1.Connect to system service failed. 2.System service failed to communicate with dependency module. |
| 201 | Permission denied. |
| 202 | Not system application. |

