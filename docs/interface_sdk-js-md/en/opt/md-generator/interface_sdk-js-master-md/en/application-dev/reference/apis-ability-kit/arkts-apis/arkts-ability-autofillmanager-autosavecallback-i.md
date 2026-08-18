# AutoSaveCallback

Implements callbacks triggered when auto-save is complete.

**Since:** 23

<!--Device-autoFillManager-export interface AutoSaveCallback--><!--Device-autoFillManager-export interface AutoSaveCallback-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## Modules to Import

```TypeScript
```

## onFailure

```TypeScript
onFailure(): void
```

Called when auto save request is failed to be handled.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AutoSaveCallback-onFailure(): void--><!--Device-AutoSaveCallback-onFailure(): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onSuccess

```TypeScript
onSuccess(): void
```

Called when auto save request is successfully handled.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AutoSaveCallback-onSuccess(): void--><!--Device-AutoSaveCallback-onSuccess(): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onFailure

```TypeScript
onFailure: OnFailureFn
```

Called when auto-save fails. **NOTE：**Starting from API version 23, the original **onFailure()** API is changed to a property, but its usage remains unchanged.

**Type:** [OnFailureFn](arkts-ability-autofillmanager-onfailurefn-t.md)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AutoSaveCallback-onFailure: OnFailureFn--><!--Device-AutoSaveCallback-onFailure: OnFailureFn-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## onSuccess

```TypeScript
onSuccess: OnSuccessFn
```

Called when auto-save is successful. **NOTE：**Starting from API version 23, the original **onSuccess()** API is changed to a property, but its usage remains unchanged.

**Type:** [OnSuccessFn](arkts-ability-autofillmanager-onsuccessfn-t.md)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AutoSaveCallback-onSuccess: OnSuccessFn--><!--Device-AutoSaveCallback-onSuccess: OnSuccessFn-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore
