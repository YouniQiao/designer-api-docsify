# restartSelfAtomicService

## Modules to Import

```TypeScript
import { abilityManager } from 'kits/@kit.AbilityKit';
```

## restartSelfAtomicService

```TypeScript
function restartSelfAtomicService(context: Context): void
```

Restarts the current atomic service.

> **NOTE：**&gt;
> - Currently, atomic services can be started only in an independent window.&gt;
> - If you call this API,
> ApplicationContext.restartApp(), or
> [UIAbilityContext.restartApp()](arkts-ability-uiabilitycontext-c.md#restartapp) within 3 seconds
> after a successful call to this API, the system returns error code 16000064.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](arkts-ability-context-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16000053](../errorcode-ability.md#16000053-ability-is-not-on-top-of-ui) |
| [16000064](../errorcode-ability.md#16000064-frequent-application-restart) |
| [16000086](../errorcode-ability.md#16000086-context-is-not-a-uiabilitycontext) |
| [16000090](../errorcode-ability.md#16000090-caller-is-not-an-atomic-service) |
