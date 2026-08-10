# InteractionInfo (System API)

定义当前意图执行完成后返回的交互信息，包括下一个要触发的意图和要显示的交互界面。

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

当前意图执行完成后需要展示的交互界面信息。

**Type:** [InteractionUI](arkts-ability-insightintent-interactionui-i-sys.md)

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InteractionInfo-interactionUI?: InteractionUI--><!--Device-InteractionInfo-interactionUI?: InteractionUI-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

