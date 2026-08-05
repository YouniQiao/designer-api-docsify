# ReturnMode

Enumerates the modes that define how the execution result of an intent is returned to the intent initiator.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-insightIntent-enum ReturnMode--><!--Device-insightIntent-enum ReturnMode-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## CALLBACK

```TypeScript
CALLBACK = 0
```

The intent execution result is returned through the [onExecuteInUIAbilityForegroundMode]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ or [onExecuteInUIExtensionAbility]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ API in the [intent execution base class]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ReturnMode-CALLBACK = 0--><!--Device-ReturnMode-CALLBACK = 0-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## FUNCTION

```TypeScript
FUNCTION = 1
```

The intent execution result is returned after the [sendExecuteResult]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ or [sendIntentResult]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ API in [intent provider management]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ is called.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ReturnMode-FUNCTION = 1--><!--Device-ReturnMode-FUNCTION = 1-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

