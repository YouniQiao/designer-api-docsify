# AppIntentEntity

Define AppIntentEntity.

**Inheritance/Implementation:** AppIntentEntity implements [IntentEntity](arkts-ability-insightintent-intententity-i.md#intententity)

**Since:** 26.0.0

<!--Device-insightIntent-abstract class AppIntentEntity--><!--Device-insightIntent-abstract class AppIntentEntity-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
```

## onQueryEntity

```TypeScript
abstract onQueryEntity(params: QueryEntityParam): Promise<Array<T>>
```

Called when query entity execute.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AppIntentEntity-abstract onQueryEntity(params: QueryEntityParam): Promise<Array<T>>--><!--Device-AppIntentEntity-abstract onQueryEntity(params: QueryEntityParam): Promise<Array<T>>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| params | [QueryEntityParam](arkts-ability-insightintent-queryentityparam-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;T & gt; & gt; |

## displayName

```TypeScript
displayName: string
```

The display name of entity.

**Type:** string

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AppIntentEntity-displayName: string--><!--Device-AppIntentEntity-displayName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core
