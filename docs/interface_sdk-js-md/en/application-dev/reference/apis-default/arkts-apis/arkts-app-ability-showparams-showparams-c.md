# ShowParams

```TypeScript
declare class ShowParams
```

ShowParams can be used as an input parameter for APIs used to show a UIAbility (for example, [showAbility()](../../apis-ability-kit/arkts-apis/arkts-ability-uiabilitycontext-c.md#showability-2)). It specifies the params for showing the target UIAbility, including but not limited to the window gains focus where the target UIAbility is started.

**Since:** 26.1.0

<!--Device-unnamed-declare class ShowParams--><!--Device-unnamed-declare class ShowParams-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { ShowParams } from '@ohos.app.ability.ShowParams';
```

## windowShowParams

```TypeScript
windowShowParams: window.WindowShowParams
```

Parameters for the window for the UIAbility upon startup.

**Type:** [window.WindowShowParams](../../apis-arkui/arkts-apis/arkts-arkui-window-windowshowparams-i.md)

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

<!--Device-ShowParams-windowShowParams: window.WindowShowParams--><!--Device-ShowParams-windowShowParams: window.WindowShowParams-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core
