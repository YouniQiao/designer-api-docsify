# enableAppRecovery

## Modules to Import

```TypeScript
import { appRecovery } from '@kit.AbilityKit';
```

## enableAppRecovery

```TypeScript
function enableAppRecovery(restart?: RestartFlag, saveOccasion?: SaveOccasionFlag, saveMode?: SaveModeFlag) : void
```

Enables application recovery. After this API is called, the first ability that is displayed when the application is started from the initiator can be restored.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-appRecovery-function enableAppRecovery(restart?: RestartFlag, saveOccasion?: SaveOccasionFlag, saveMode?: SaveModeFlag) : void--><!--Device-appRecovery-function enableAppRecovery(restart?: RestartFlag, saveOccasion?: SaveOccasionFlag, saveMode?: SaveModeFlag) : void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| restart | [RestartFlag](arkts-ability-apprecovery-restartflag-e.md) | No |
| saveOccasion | [SaveOccasionFlag](arkts-ability-apprecovery-saveoccasionflag-e.md) | No |
| saveMode | [SaveModeFlag](arkts-ability-apprecovery-savemodeflag-e.md) | No |
