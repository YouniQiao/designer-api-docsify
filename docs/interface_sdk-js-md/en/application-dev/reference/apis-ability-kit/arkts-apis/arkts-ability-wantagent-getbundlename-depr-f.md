# getBundleName

## Modules to Import

```TypeScript
```

## getBundleName

```TypeScript
function getBundleName(agent: WantAgent, callback: AsyncCallback<string>): void
```

Obtains the bundle name of a WantAgent.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getBundleName](arkts-ability-wantagent-getbundlename-f.md)

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [agent](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-request-agent-n.md) | [WantAgent](arkts-ability-wantagent-depr-t.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |


## getBundleName

```TypeScript
function getBundleName(agent: WantAgent): Promise<string>
```

Obtains the bundle name of a WantAgent.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [getBundleName](arkts-ability-wantagent-getbundlename-f.md)

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [agent](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-request-agent-n.md) | [WantAgent](arkts-ability-wantagent-depr-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |
