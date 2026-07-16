# AutoFillCallback

Auto fill callback.

**Since:** 26.0.0

<!--Device-autoFillManager-export interface AutoFillCallback--><!--Device-autoFillManager-export interface AutoFillCallback-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## Modules to Import

```TypeScript
import { autoFillManager } from '@kit.AbilityKit';
```

## onFailure

```TypeScript
onFailure: OnFillFailureFn
```

Called when auto fill request is failed to be handled.

**Type:** OnFillFailureFn

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AutoFillCallback-onFailure: OnFillFailureFn--><!--Device-AutoFillCallback-onFailure: OnFillFailureFn-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onSuccess

```TypeScript
onSuccess: OnFillSuccessFn
```

Called when auto fill request is successfully handled.

**Type:** OnFillSuccessFn

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AutoFillCallback-onSuccess: OnFillSuccessFn--><!--Device-AutoFillCallback-onSuccess: OnFillSuccessFn-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

