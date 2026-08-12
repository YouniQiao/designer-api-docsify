# InsightIntentPage

Define InsightIntentPage Annotation.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export @interface InsightIntentPage--><!--Device-unnamed-export @interface InsightIntentPage-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { InsightIntentFunction, InsightIntentForm, InsightIntentLink, InsightIntentEntity, LinkParamCategory, InsightIntentPage, InsightIntentEntry, InsightIntentFunctionMethod } from '@kit.AbilityKit';
```

## displayDescription

```TypeScript
displayDescription: string = ''
```

The display description of intent.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InsightIntentPage-displayDescription: string = ''--><!--Device-InsightIntentPage-displayDescription: string = ''-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## displayName

```TypeScript
displayName: string
```

The display name of intent.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InsightIntentPage-displayName: string--><!--Device-InsightIntentPage-displayName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## domain

```TypeScript
domain: string
```

The intent domain.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InsightIntentPage-domain: string--><!--Device-InsightIntentPage-domain: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## icon

```TypeScript
icon: string = ''
```

The icon of intent, the string type indicates an online resource or a local resource.For example, "\$r('app.media.startIcon')".The value of Resource type must be a literal.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InsightIntentPage-icon: string = ''--><!--Device-InsightIntentPage-icon: string = ''-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## intentName

```TypeScript
intentName: string
```

The intent name.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InsightIntentPage-intentName: string--><!--Device-InsightIntentPage-intentName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## intentVersion

```TypeScript
intentVersion: string
```

The intent version.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InsightIntentPage-intentVersion: string--><!--Device-InsightIntentPage-intentVersion: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## keywords

```TypeScript
keywords: string[] = []
```

The search keywords of intent.

**Type:** string[]

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InsightIntentPage-keywords: string[] = []--><!--Device-InsightIntentPage-keywords: string[] = []-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## llmDescription

```TypeScript
llmDescription: string = ''
```

The large language model description of intent.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InsightIntentPage-llmDescription: string = ''--><!--Device-InsightIntentPage-llmDescription: string = ''-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## navDestinationName

```TypeScript
navDestinationName: string = ''
```

The navigation destination name bound to the intent.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InsightIntentPage-navDestinationName: string = ''--><!--Device-InsightIntentPage-navDestinationName: string = ''-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## navigationId

```TypeScript
navigationId: string = ''
```

The navigation Id bound to the intent.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InsightIntentPage-navigationId: string = ''--><!--Device-InsightIntentPage-navigationId: string = ''-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## pagePath

```TypeScript
pagePath: string
```

The page path bound to the intent.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InsightIntentPage-pagePath: string--><!--Device-InsightIntentPage-pagePath: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## parameters

```TypeScript
parameters: string = ''
```

The parameters of intent.The value is the name of a variable of type Record&lt;string, RecordData&gt;.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InsightIntentPage-parameters: string = ''--><!--Device-InsightIntentPage-parameters: string = ''-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## result

```TypeScript
result: string = ''
```

The type definition of the result returned by intent call.The value is the name of a variable of type Record&lt;string, RecordData&gt;.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InsightIntentPage-result: string = ''--><!--Device-InsightIntentPage-result: string = ''-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## schema

```TypeScript
schema: string = ''
```

The schema of intent, indicates a standard intent.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InsightIntentPage-schema: string = ''--><!--Device-InsightIntentPage-schema: string = ''-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## uiAbility

```TypeScript
uiAbility: string = ''
```

The uiAbility name bound to the intent.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InsightIntentPage-uiAbility: string = ''--><!--Device-InsightIntentPage-uiAbility: string = ''-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

