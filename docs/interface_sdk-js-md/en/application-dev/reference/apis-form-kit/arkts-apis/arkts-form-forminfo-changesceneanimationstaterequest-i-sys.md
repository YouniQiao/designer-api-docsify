# ChangeSceneAnimationStateRequest (System API)

ChangeSceneAnimationStateRequest

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-formInfo-interface ChangeSceneAnimationStateRequest--><!--Device-formInfo-interface ChangeSceneAnimationStateRequest-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { formInfo } from '@kit.FormKit';
```

## formId

```TypeScript
formId: string
```

The form id about request change scene animation state

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ChangeSceneAnimationStateRequest-formId: string--><!--Device-ChangeSceneAnimationStateRequest-formId: string-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

## state

```TypeScript
state: int
```

The state of scene animation. 0 means deactivate, 1 means activate The value must be an integer within [0,1].

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ChangeSceneAnimationStateRequest-state: int--><!--Device-ChangeSceneAnimationStateRequest-state: int-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

