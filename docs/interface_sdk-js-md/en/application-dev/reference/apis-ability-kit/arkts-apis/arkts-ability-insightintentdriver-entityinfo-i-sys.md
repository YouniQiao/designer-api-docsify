# EntityInfo (System API)

EntityInfo继承自[IntentEntityDecoratorInfo](arkts-ability-app-ability-insightintentdecorator-intententitydecoratorinfo-i.md)，用于描述  
[@InsightIntentEntity](../../../reference/apis-ability-kit/js-apis-app-ability-InsightIntentDecorator.md#insightintententity)装饰器定义的意图实体的信息。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-insightIntentDriver-interface EntityInfo--><!--Device-insightIntentDriver-interface EntityInfo-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { insightIntentDriver } from 'kits/@kit.AbilityKit';
```

## className

```TypeScript
readonly className: string
```

表示  
[@InsightIntentEntity](../../../reference/apis-ability-kit/js-apis-app-ability-InsightIntentDecorator.md#insightintententity)装饰器修饰的类名。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EntityInfo-readonly className: string--><!--Device-EntityInfo-readonly className: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## entityCategory

```TypeScript
readonly entityCategory: string
```

表示意图实体类别。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EntityInfo-readonly entityCategory: string--><!--Device-EntityInfo-readonly entityCategory: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## entityId

```TypeScript
readonly entityId: string
```

表示意图实体的ID。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EntityInfo-readonly entityId: string--><!--Device-EntityInfo-readonly entityId: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## isQueryable

```TypeScript
readonly isQueryable?: boolean
```

实体是可查询的。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EntityInfo-readonly isQueryable?: boolean--><!--Device-EntityInfo-readonly isQueryable?: boolean-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## parameters

```TypeScript
readonly parameters: Record<string, Object>
```

表示意图实体参数的数据格式声明，用于意图调用时定义实体参数的数据格式。

**Type:** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Object&gt;

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EntityInfo-readonly parameters: Record<string, Object>--><!--Device-EntityInfo-readonly parameters: Record<string, Object>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## parentClassName

```TypeScript
readonly parentClassName: string
```

表示  
[@InsightIntentEntity](../../../reference/apis-ability-kit/js-apis-app-ability-InsightIntentDecorator.md#insightintententity)装饰器修饰的类的父类名。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EntityInfo-readonly parentClassName: string--><!--Device-EntityInfo-readonly parentClassName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## supportedQueryProperties

```TypeScript
readonly supportedQueryProperties?: string[]
```

支持查询属性。

**Type:** string[]

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EntityInfo-readonly supportedQueryProperties?: string[]--><!--Device-EntityInfo-readonly supportedQueryProperties?: string[]-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

