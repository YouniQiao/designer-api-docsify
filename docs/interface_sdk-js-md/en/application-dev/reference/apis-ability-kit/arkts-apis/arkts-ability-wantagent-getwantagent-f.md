# getWantAgent

## Modules to Import

```TypeScript
import { wantAgent, WantAgent } from 'kits/@kit.AbilityKit';
```

## getWantAgent

```TypeScript
function getWantAgent(info: WantAgentInfo, callback: AsyncCallback<WantAgent>): void
```

Obtains a WantAgent object. This API uses an asynchronous callback to return the result. If the creation fails, a null WantAgent object is returned.<p>**NOTE：**: Third-party applications can set only their own abilities. </p>

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| info | [WantAgentInfo](arkts-ability-wantagent-wantagentinfo-t.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[WantAgent](arkts-ability-wantagent-t.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000007](../errorcode-ability.md#16000007-service-unresponsive) |
| [16000151](../errorcode-ability.md#16000151-invalid-wantagent-object) |


## getWantAgent

```TypeScript
function getWantAgent(info: WantAgentInfo): Promise<WantAgent>
```

Obtains a WantAgent object. This API uses a promise to return the result. If the creation fails, a null WantAgent object is returned.<p>**NOTE：**: Third-party applications can set only their own abilities. </p>

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| info | [WantAgentInfo](arkts-ability-wantagent-wantagentinfo-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[WantAgent](arkts-ability-wantagent-t.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000007](../errorcode-ability.md#16000007-service-unresponsive) |
| [16000151](../errorcode-ability.md#16000151-invalid-wantagent-object) |
