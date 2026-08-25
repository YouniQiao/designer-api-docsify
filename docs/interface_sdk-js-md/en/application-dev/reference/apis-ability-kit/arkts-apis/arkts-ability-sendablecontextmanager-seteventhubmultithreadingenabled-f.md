# setEventHubMultithreadingEnabled

## Modules to Import

```TypeScript
import { sendableContextManager } from 'kits/@kit.AbilityKit';
```

## setEventHubMultithreadingEnabled

```TypeScript
function setEventHubMultithreadingEnabled(context: common.Context, enabled: boolean): void
```

Enables the cross-thread data transfer feature of [EventHub](arkts-ability-eventhub-c.md) in Context.

> **NOTE：**&gt;
> - When multiple Context objects communicate, you need to call this API to set each Context object to support
> EventHub cross-thread data transfer.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | common.Context | Yes |
| enabled | boolean | Yes |
