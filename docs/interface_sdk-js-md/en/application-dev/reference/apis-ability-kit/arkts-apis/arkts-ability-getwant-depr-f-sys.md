# getWant (System API)

## getWant

```TypeScript
function getWant(agent: WantAgent, callback: AsyncCallback<Want>): void
```

Obtains the {@link Want} of an {@link WantAgent}.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** getWant

<!--Device-wantAgent-function getWant(agent: WantAgent, callback: AsyncCallback<Want>): void--><!--Device-wantAgent-function getWant(agent: WantAgent, callback: AsyncCallback<Want>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| agent | [WantAgent](../../apis-background-tasks-kit/arkts-apis/arkts-backgroundtasks-wantagent-i.md) | Yes | Indicates the {@link WantAgent} whose UID is to be obtained. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-i.md)<Want> | Yes | Obtain the callback method for Want in WantAgent. |


## getWant

```TypeScript
function getWant(agent: WantAgent): Promise<Want>
```

Obtains the {@link Want} of an {@link WantAgent}.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** getWant

<!--Device-wantAgent-function getWant(agent: WantAgent): Promise<Want>--><!--Device-wantAgent-function getWant(agent: WantAgent): Promise<Want>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| agent | [WantAgent](../../apis-background-tasks-kit/arkts-apis/arkts-backgroundtasks-wantagent-i.md) | Yes | Indicates the {@link WantAgent} whose UID is to be obtained. |

**Return value:**

| Type | Description |
| --- | --- |
| [Promise](../../apis-na/arkts-apis/arkts-na-promise-i.md)<Want> | Returns the {@link Want} of the {@link WantAgent}. |

