# EntryIntentInfo (System API)

Describes the parameters supported by the @InsightIntentForm decorator, such as the widget name. It also describes the widget information bound to the [intent developed using a configuration file](../../../application-models/insight-intent-config-development.md).

**Since:** 23

<!--Device-insightIntentDriver-interface EntryIntentInfo--><!--Device-insightIntentDriver-interface EntryIntentInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { insightIntentDriver } from 'insightIntentDriver';
```

## abilityName

```TypeScript
readonly abilityName: string
```

Ability name.

**Type:** string

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-EntryIntentInfo-readonly abilityName: string--><!--Device-EntryIntentInfo-readonly abilityName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## executeMode

```TypeScript
readonly executeMode: insightIntent.ExecuteMode[]
```

Intent execution mode. that is, execution mode supported when the bound ability is started.

**Type:** insightIntent.ExecuteMode[]

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-EntryIntentInfo-readonly executeMode: insightIntent.ExecuteMode[]--><!--Device-EntryIntentInfo-readonly executeMode: insightIntent.ExecuteMode[]-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

