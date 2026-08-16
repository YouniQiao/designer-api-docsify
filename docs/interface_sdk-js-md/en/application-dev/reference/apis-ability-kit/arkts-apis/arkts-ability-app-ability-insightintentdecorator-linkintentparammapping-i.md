# LinkIntentParamMapping

LinkIntentParamMapping defines the mapping between intent parameters and URI information for the @InsightIntentLink decorator.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** -1

<!--Device-unnamed-declare interface LinkIntentParamMapping--><!--Device-unnamed-declare interface LinkIntentParamMapping-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { InsightIntentLink } from 'InsightIntentLink';
import { InsightIntentPage } from 'InsightIntentPage';
import { InsightIntentFunctionMethod } from 'InsightIntentFunctionMethod';
import { InsightIntentFunction } from 'InsightIntentFunction';
import { InsightIntentEntry } from 'InsightIntentEntry';
import { LinkParamCategory } from 'LinkParamCategory';
import { InsightIntentForm } from 'InsightIntentForm';
import { InsightIntentEntity } from 'InsightIntentEntity';
```

## paramCategory

```TypeScript
paramCategory?: LinkParamCategory
```

Category of the intent parameter. If an intent parameter is of the [LINK](../../apis-na/arkts-apis/arkts-na-app-ability-insightintentdecorator-linkparamcategory-e.md#LinkParamCategory) category, the system retrieves **paramMappingName** corresponding to **paramName** and appends it to the URI as a key-value pair (where **key** is the value of **paramMappingName**, and **value** is the intent parameter value). If an intent parameter is of the [WANT](../../apis-na/arkts-apis/arkts-na-app-ability-insightintentdecorator-linkparamcategory-e.md#LinkParamCategory) category, the system retrieves **paramMappingName** corresponding to **paramName** and passes the mapping name and value using the **parameters** field in [Want](arkts-ability-app-ability-want-want-c.md#Want).

**Type:** [LinkParamCategory](../../apis-na/arkts-apis/arkts-na-app-ability-insightintentdecorator-linkparamcategory-e.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-LinkIntentParamMapping-paramCategory?: LinkParamCategory--><!--Device-LinkIntentParamMapping-paramCategory?: LinkParamCategory-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## paramMappingName

```TypeScript
paramMappingName?: string
```

Mapping name of the intent parameter.

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-LinkIntentParamMapping-paramMappingName?: string--><!--Device-LinkIntentParamMapping-paramMappingName?: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## paramName

```TypeScript
paramName: string
```

Name of the intent parameter.

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-LinkIntentParamMapping-paramName: string--><!--Device-LinkIntentParamMapping-paramName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

