# getAllAgentCards (System API)

## Modules to Import

```TypeScript
import { agentManager } from '@kit.AbilityKit';
```

## getAllAgentCards

```TypeScript
function getAllAgentCards(): Promise<Array<AgentCard>>
```

Gets all AgentCards on the device.

**Since:** 24

**Required permissions:** ohos.permission.GET_AGENT_CARD

**Model restriction:** This API can be used only in the stage model.

<!--Device-agentManager-function getAllAgentCards(): Promise<Array<AgentCard>>--><!--Device-agentManager-function getAllAgentCards(): Promise<Array<AgentCard>>-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[AgentCard](arkts-ability-agentcard-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000050](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000050-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
