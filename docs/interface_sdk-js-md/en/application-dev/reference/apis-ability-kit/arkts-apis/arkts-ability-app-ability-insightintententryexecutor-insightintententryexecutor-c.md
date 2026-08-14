# InsightIntentEntryExecutor

The class of insight intent entry executor.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-declare class InsightIntentEntryExecutor--><!--Device-unnamed-declare class InsightIntentEntryExecutor-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { InsightIntentEntryExecutor } from 'InsightIntentEntryExecutor';
```

## onExecute

```TypeScript
onExecute(): Promise<insightIntent.IntentResult<T>>
```

Called when insight intent execute.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-InsightIntentEntryExecutor-onExecute(): Promise<insightIntent.IntentResult<T>>--><!--Device-InsightIntentEntryExecutor-onExecute(): Promise<insightIntent.IntentResult<T>>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;insightIntent.IntentResult&lt;T&gt;&gt; | The result of insight intent execution, support promise. |

## context

```TypeScript
context: InsightIntentContext
```

The insight intent context.

**Type:** [InsightIntentContext](arkts-ability-app-ability-insightintentcontext-insightintentcontext-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-InsightIntentEntryExecutor-context: InsightIntentContext--><!--Device-InsightIntentEntryExecutor-context: InsightIntentContext-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## executeMode

```TypeScript
executeMode: insightIntent.ExecuteMode
```

The insight intent execute mode.

**Type:** insightIntent.ExecuteMode

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-InsightIntentEntryExecutor-executeMode: insightIntent.ExecuteMode--><!--Device-InsightIntentEntryExecutor-executeMode: insightIntent.ExecuteMode-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## uiExtensionSession

```TypeScript
uiExtensionSession?: UIExtensionContentSession
```

The UIExtension content session.

**Type:** [UIExtensionContentSession](arkts-ability-app-ability-uiextensioncontentsession-uiextensioncontentsession-c.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-InsightIntentEntryExecutor-uiExtensionSession?: UIExtensionContentSession--><!--Device-InsightIntentEntryExecutor-uiExtensionSession?: UIExtensionContentSession-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## windowStage

```TypeScript
windowStage?: window.WindowStage
```

The window stage.

**Type:** window.WindowStage

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-InsightIntentEntryExecutor-windowStage?: window.WindowStage--><!--Device-InsightIntentEntryExecutor-windowStage?: window.WindowStage-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

