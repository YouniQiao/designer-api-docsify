# @ohos.app.ability.insightIntent

本模块提供[意图框架](../../../application-models/insight-intent-overview.md)基础定义。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace insightIntent--><!--Device-unnamed-declare namespace insightIntent-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { insightIntent } from 'kits/@kit.AbilityKit';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [AppIntentEntity](arkts-ability-insightintent-appintententity-c.md) | 定义AppIntentEntity。 |

### Interfaces

| Name | Description |
| --- | --- |
| [ExecuteResult](arkts-ability-insightintent-executeresult-i.md) | 意图执行的返回结果。 |
| [IntentEntity](arkts-ability-insightintent-intententity-i.md) | 意图实体结构体定义，用于定义意图执行过程中涉及的关键信息对象，包括意图参数和意图执行结果等。  开发者通过继承该类来定义意图实体，继承类需使用  [@InsightIntentEntity](../../../reference/apis-ability-kit/js-apis-app-ability-InsightIntentDecorator.md#insightintententity)装饰。 |
| [IntentResult](arkts-ability-insightintent-intentresult-i.md) | 意图执行的返回结果，支持[泛型类型](../../../quick-start/introduction-to-arkts.md#泛型类和接口)。 |
| [QueryEntityParam](arkts-ability-insightintent-queryentityparam-i.md) | 查询实体的参数。 |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [ExecuteResult](arkts-ability-insightintent-executeresult-i-sys.md) | 意图执行的返回结果。 |
| [IntentResult](arkts-ability-insightintent-intentresult-i-sys.md) | 意图执行的返回结果，支持[泛型类型](../../../quick-start/introduction-to-arkts.md#泛型类和接口)。 |
| [InteractionInfo](arkts-ability-insightintent-interactioninfo-i-sys.md) | 定义当前意图执行完成后返回的交互信息，包括下一个要触发的意图和要显示的交互界面。 |
| [InteractionModalUIExtension](arkts-ability-insightintent-interactionmodaluiextension-i-sys.md) | 定义当意图执行完成时模态UIExtension要显示为交互界面的信息，不支持分布式。 |
| [InteractionUI](arkts-ability-insightintent-interactionui-i-sys.md) | 定义当前意图执行完成后需要展示的交互界面的信息。 |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [ExecuteMode](arkts-ability-insightintent-executemode-e.md) | 意图执行模式。表示系统入口触发意图执行时传递的执行模式，每个意图支持的执行模式在意图开发时定义。 |
| [QueryType](arkts-ability-insightintent-querytype-e.md) | 查询实体模式的枚举。 |
| [ReturnMode](arkts-ability-insightintent-returnmode-e.md) | 意图执行结果返回给意图拉起方的返回形式。 |

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [ExecuteMode](arkts-ability-insightintent-executemode-e-sys.md) | 意图执行模式。表示系统入口触发意图执行时传递的执行模式，每个意图支持的执行模式在意图开发时定义。 |
<!--DelEnd-->

