# Callee

Background communication object created by the system for the UIAbility, known as the Callee UIAbility (Callee), which is capable of receiving data sent from the Caller object.

**Since:** 9

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## Modules to Import

```TypeScript
import { UIAbility, Callee, CalleeCallback, Caller, OnReleaseCallback, OnRemoteStateChangeCallback } from 'kits/@kit.AbilityKit';
```

## off

```TypeScript
off(method: string): void
```

Unregisters a caller notification callback, which is invoked when the target UIAbility registers a function.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| method | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16200005](../errorcode-ability.md#16200005-method-not-registered) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |

## on

```TypeScript
on(method: string, callback: CalleeCallback): void
```

Registers a caller notification callback, which is invoked when the target UIAbility registers a function.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| method | string | Yes |
| callback | [CalleeCallback](arkts-ability-app-ability-uiability-calleecallback-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16200004](../errorcode-ability.md#16200004-method-registered) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
