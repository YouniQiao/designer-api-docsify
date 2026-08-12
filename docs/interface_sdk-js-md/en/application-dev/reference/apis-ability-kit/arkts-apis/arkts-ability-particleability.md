# @ohos.ability.particleAbility

The particleAbility module provides APIs for operating a DataAbility and ServiceAbility. You can use the APIs to start and terminate a ParticleAbility, obtain a dataAbilityHelper object, and connect to or disconnect from a ServiceAbility.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Model restriction:** This API can be used only in the FA model.

<!--Device-unnamed-declare namespace particleAbility--><!--Device-unnamed-declare namespace particleAbility-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

## Modules to Import

```TypeScript
import { particleAbility } from '@kit.AbilityKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [acquireDataAbilityHelper](arkts-ability-particleability-acquiredataabilityhelper-f.md#acquiredataabilityhelper) | Obtains a dataAbilityHelper object.  > **NOTE：** >  > For details about the startup rules for the components in the FA model, see > [Component Startup Rules (FA Model)](../../../application-models/component-startup-rules-fa.md). > To access a DataAbility of another application, the target application must be configured with associated > startup (**AssociateWakeUp** set to **true**). |
| [cancelBackgroundRunning](arkts-ability-particleability-cancelbackgroundrunning-f.md#cancelbackgroundrunning) | Requests to cancel a continuous task from the system. This API uses an asynchronous callback to return the result. |
| [cancelBackgroundRunning](arkts-ability-particleability-cancelbackgroundrunning-f.md#cancelbackgroundrunning-1) | Requests to cancel a continuous task from the system. This API uses a promise to return the result. |
| [connectAbility](arkts-ability-particleability-connectability-f.md#connectability) | Connects this ability to a ServiceAbility.  > **NOTE：** >  > For details about the startup rules for the components in the FA model, see > [Component Startup Rules (FA Model)](../../../application-models/component-startup-rules-fa.md). > > To connect to a ServiceAbility of another application, the target application must be configured with > associated startup (**AssociateWakeUp** set to **true**). |
| [disconnectAbility](arkts-ability-particleability-disconnectability-f.md#disconnectability) | Disconnects this ability from a specific ServiceAbility. This API uses an asynchronous callback to return the result. |
| [disconnectAbility](arkts-ability-particleability-disconnectability-f.md#disconnectability-1) | Disconnects this ability from a specific ServiceAbility. This API uses a promise to return the result. |
| [startAbility](arkts-ability-particleability-startability-f.md#startability) | Starts a ParticleAbility. This API uses an asynchronous callback to return the result.  > **NOTE：** >  > For details about the startup rules for the components in the FA model, see > [Component Startup Rules (FA Model)](../../../application-models/component-startup-rules-fa.md). |
| [startAbility](arkts-ability-particleability-startability-f.md#startability-1) | Starts a ParticleAbility. This API uses a promise to return the result.  > **NOTE：** >  > For details about the startup rules for the components in the FA model, see > [Component Startup Rules (FA Model)](../../../application-models/component-startup-rules-fa.md). |
| [startBackgroundRunning](arkts-ability-particleability-startbackgroundrunning-f.md#startbackgroundrunning) | Requests a continuous task from the system. This API uses an asynchronous callback to return the result. |
| [startBackgroundRunning](arkts-ability-particleability-startbackgroundrunning-f.md#startbackgroundrunning-1) | Requests a continuous task from the system. This API uses a promise to return the result. |
| [terminateSelf](arkts-ability-particleability-terminateself-f.md#terminateself) | Terminates this ParticleAbility. This API uses an asynchronous callback to return the result. |
| [terminateSelf](arkts-ability-particleability-terminateself-f.md#terminateself-1) | Terminates this ParticleAbility. This API uses a promise to return the result. |

### Enums

| Name | Description |
| --- | --- |
| [ErrorCode](arkts-ability-particleability-errorcode-e.md) | Enumerates the error codes that may be returned when an ability is started. |

