# InsightIntentEntity

Define InsightIntentEntity Annotation.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export @interface InsightIntentEntity--><!--Device-unnamed-export @interface InsightIntentEntity-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { InsightIntentFunction, InsightIntentForm, InsightIntentLink, InsightIntentEntity, LinkParamCategory, InsightIntentPage, InsightIntentEntry, InsightIntentFunctionMethod } from 'kits/@kit.AbilityKit';
```

## entityCategory

```TypeScript
entityCategory: string
```

The entity category.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InsightIntentEntity-entityCategory: string--><!--Device-InsightIntentEntity-entityCategory: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## parameters

```TypeScript
parameters: string = ""
```

The parameters of intent entity.The value is the name of a variable of type Record&lt;string, RecordData&gt;.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InsightIntentEntity-parameters: string = ""--><!--Device-InsightIntentEntity-parameters: string = ""-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## supportedQueryProperties

```TypeScript
supportedQueryProperties: string[] = []
```

Supported query properties.

**Type:** string[]

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InsightIntentEntity-supportedQueryProperties: string[] = []--><!--Device-InsightIntentEntity-supportedQueryProperties: string[] = []-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

