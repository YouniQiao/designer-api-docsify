# getWant (System API)

## Modules to Import

```TypeScript
import { WantAgent } from '@kit.AbilityKit';
```

## getWant

```TypeScript
function getWant(agent: WantAgent, callback: AsyncCallback<Want>): void
```

Obtains the Want in a WantAgent object. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-wantAgent-function getWant(agent: WantAgent, callback: AsyncCallback<Want>): void--><!--Device-wantAgent-function getWant(agent: WantAgent, callback: AsyncCallback<Want>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [agent](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-request-agent-n.md) | [WantAgent](arkts-ability-wantagent-t.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Want](arkts-ability-app-ability-want-want-c.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000007](../errorcode-ability.md#16000007-service-unresponsive) |
| [16000151](../errorcode-ability.md#16000151-invalid-wantagent-object) |
| [16000015](../errorcode-ability.md#16000015-service-timeout) |


## getWant

```TypeScript
function getWant(agent: WantAgent): Promise<Want>
```

Obtains the Want in a WantAgent object. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-wantAgent-function getWant(agent: WantAgent): Promise<Want>--><!--Device-wantAgent-function getWant(agent: WantAgent): Promise<Want>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [agent](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-request-agent-n.md) | [WantAgent](arkts-ability-wantagent-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Want](arkts-ability-app-ability-want-want-c.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000007](../errorcode-ability.md#16000007-service-unresponsive) |
| [16000151](../errorcode-ability.md#16000151-invalid-wantagent-object) |
| [16000015](../errorcode-ability.md#16000015-service-timeout) |
