# @ohos.app.ability.insightIntentProvider(Intent Provider Management)

Insight intent Provider. @namespace insightIntentProvider

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace insightIntentProvider--><!--Device-unnamed-declare namespace insightIntentProvider-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { insightIntentProvider } from '@kit.AbilityKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [sendExecuteResult](arkts-ability-insightintentprovider-sendexecuteresult-f.md) | If an intent provider needs to proactively send the execution result of an intent at a specific point in the service process, it can first set the [return mode](arkts-ability-insightintent-returnmode-e.md) of the intent execution result to FUNCTION through [setReturnModeForUIAbilityForeground](arkts-ability-app-ability-insightintentcontext-insightintentcontext-c.md#setreturnmodeforuiabilityforeground) or [setReturnModeForUIExtensionAbility](arkts-ability-app-ability-insightintentcontext-insightintentcontext-c.md#setreturnmodeforuiextensionability), and then call this API to send the intent execution result. This API applies to [configuration-type intents](../../../application-models/insight-intent-config-development.md). This API uses a promise to return the result asynchronously. |
| [sendIntentResult](arkts-ability-insightintentprovider-sendintentresult-f.md) | If an intent provider needs to proactively send the execution result of an intent at a specific point in the service process, it can first set the [return mode](arkts-ability-insightintent-returnmode-e.md) of the intent execution result to FUNCTION through [setReturnModeForUIAbilityForeground](arkts-ability-app-ability-insightintentcontext-insightintentcontext-c.md#setreturnmodeforuiabilityforeground) or [setReturnModeForUIExtensionAbility](arkts-ability-app-ability-insightintentcontext-insightintentcontext-c.md#setreturnmodeforuiextensionability), and then call this API to send the intent execution result. This API applies to [decorator-type intents](../../../application-models/insight-intent-decorator-development.md) decorated by [@InsightIntentEntry](arkts-ability-app-ability-insightintentdecorator-insightintententry-d.md#insightintententry). This API uses a promise to return the result asynchronously. |
