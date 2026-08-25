# createLocalWantAgent (System API)

## Modules to Import

```TypeScript
import { wantAgent, WantAgent } from 'kits/@kit.AbilityKit';
```

## createLocalWantAgent

```TypeScript
function createLocalWantAgent(info: LocalWantAgentInfo): WantAgent
```

Create a local WantAgent object. The WantAgent created by this interface stores data on the client side and is not managed by the WantAgent servcer. If this WantAgent object is passed across processes, its contained data will be serialized and transmitted to the target process.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| info | [LocalWantAgentInfo](arkts-ability-wantagent-localwantagentinfo-t-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [WantAgent](arkts-ability-wantagent-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
