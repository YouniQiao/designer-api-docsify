# getWantAgent

## Modules to Import

```TypeScript
```

## getWantAgent

```TypeScript
function getWantAgent(info: WantAgentInfo, callback: AsyncCallback<WantAgent>): void
```

Obtains a WantAgent object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getWantAgent](arkts-ability-wantagent-getwantagent-f.md)

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| info | [WantAgentInfo](arkts-ability-wantagentinfo-wantagentinfo-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[WantAgent](arkts-ability-wantagent-depr-t.md)&gt; | Yes |


## getWantAgent

```TypeScript
function getWantAgent(info: WantAgentInfo): Promise<WantAgent>
```

Obtains a WantAgent object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getWantAgent](arkts-ability-wantagent-getwantagent-f.md)

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| info | [WantAgentInfo](arkts-ability-wantagentinfo-wantagentinfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[WantAgent](arkts-ability-wantagent-depr-t.md)&gt; |
