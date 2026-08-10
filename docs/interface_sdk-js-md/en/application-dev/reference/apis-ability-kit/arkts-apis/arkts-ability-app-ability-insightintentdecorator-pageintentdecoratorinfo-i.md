# PageIntentDecoratorInfo

PageIntentDecoratorInfo继承自[IntentDecoratorInfo](arkts-ability-app-ability-insightintentdecorator-intentdecoratorinfo-i.md)，用于描述  
[@InsightIntentPage](../../../reference/apis-ability-kit/js-apis-app-ability-InsightIntentDecorator.md#insightintentpage)装饰器支持的参数，例如目标页面的  
[NavDestination](../../../reference/apis-arkui/arkui-ts/ts-basic-components-navigation.md#navdestination10)名称。

**Inheritance/Implementation:** PageIntentDecoratorInfo extends [IntentDecoratorInfo](arkts-ability-app-ability-insightintentdecorator-intentdecoratorinfo-i.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-unnamed-declare interface PageIntentDecoratorInfo extends IntentDecoratorInfo--><!--Device-unnamed-declare interface PageIntentDecoratorInfo extends IntentDecoratorInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { InsightIntentFunction, InsightIntentForm, InsightIntentLink, InsightIntentEntity, LinkParamCategory, InsightIntentPage, InsightIntentEntry, InsightIntentFunctionMethod } from 'kits/@kit.AbilityKit';
```

## navDestinationName

```TypeScript
navDestinationName?: string
```

表示与意图绑定  
[NavDestination组件](../../../reference/apis-arkui/arkui-ts/ts-basic-components-navigation.md#navdestination10)的名称。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-PageIntentDecoratorInfo-navDestinationName?: string--><!--Device-PageIntentDecoratorInfo-navDestinationName?: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## navigationId

```TypeScript
navigationId?: string
```

表示与意图绑定的[Navigation组件](../../../reference/apis-arkui/arkui-ts/ts-basic-components-navigation.md#属性)的id属性。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-PageIntentDecoratorInfo-navigationId?: string--><!--Device-PageIntentDecoratorInfo-navigationId?: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## pagePath

```TypeScript
pagePath: string
```

表示与意图绑定的页面路径，该页面需要是一个实际存在的文件。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-PageIntentDecoratorInfo-pagePath: string--><!--Device-PageIntentDecoratorInfo-pagePath: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## uiAbility

```TypeScript
uiAbility?: string
```

表示与意图绑定的UIAbility名称。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-PageIntentDecoratorInfo-uiAbility?: string--><!--Device-PageIntentDecoratorInfo-uiAbility?: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

