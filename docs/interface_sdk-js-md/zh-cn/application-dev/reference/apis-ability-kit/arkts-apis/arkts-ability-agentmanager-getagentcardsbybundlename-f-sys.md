# getAgentCardsByBundleName（系统接口）

## 导入模块

```TypeScript
import { agentManager } from 'kits/@kit.AbilityKit';
```

## getAgentCardsByBundleName

```TypeScript
function getAgentCardsByBundleName(bundleName: string): Promise<Array<AgentCard>>
```

Gets all AgentCards within specified bundleName.

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**需要权限：** ohos.permission.GET_AGENT_CARD

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-agentManager-function getAgentCardsByBundleName(bundleName: string): Promise<Array<AgentCard>>--><!--Device-agentManager-function getAgentCardsByBundleName(bundleName: string): Promise<Array<AgentCard>>-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | The bundle name the AgentCard belongs to. |

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
| 18500001 | The bundle does not exist or no patch has been applied. |

