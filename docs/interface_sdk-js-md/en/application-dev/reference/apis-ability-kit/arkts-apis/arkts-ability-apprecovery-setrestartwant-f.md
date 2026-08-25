# setRestartWant

## Modules to Import

```TypeScript
import { appRecovery } from 'kits/@kit.AbilityKit';
```

## setRestartWant

```TypeScript
function setRestartWant(want: Want): void
```

Sets an ability that will be recovered. The ability must be a UIAbility in the current bundle.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |
