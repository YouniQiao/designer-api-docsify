# trigger

## Modules to Import

```TypeScript
```

## trigger

```TypeScript
function trigger(agent: WantAgent, triggerInfo: TriggerInfo, callback?: Callback<CompleteData>): void
```

Triggers a WantAgent.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [trigger](arkts-ability-wantagent-trigger-f.md)

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [agent](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-request-agent-n.md) | [WantAgent](arkts-ability-wantagent-depr-t.md) | Yes |
| triggerInfo | [TriggerInfo](arkts-ability-triggerinfo-triggerinfo-i.md) | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;CompleteData&gt; | No |
