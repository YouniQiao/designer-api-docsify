# InteractionInfo (System API)

Defines the interaction information returned after the current intent execution completes, including the next intent to be triggered and the interaction UI to be displayed.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

<!--Device-insightIntent-interface InteractionInfo--><!--Device-insightIntent-interface InteractionInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { insightIntent } from 'kits/@kit.AbilityKit';
```

## interactionUI

```TypeScript
interactionUI?: InteractionUI
```

Information of the interaction UI to be displayed after the current intent execution completes.

**Type:** [InteractionUI](arkts-ability-insightintent-interactionui-i-sys.md)

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InteractionInfo-interactionUI?: InteractionUI--><!--Device-InteractionInfo-interactionUI?: InteractionUI-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

