# @ohos.app.ability.InsightIntentDecorator

The InsightIntentDecorator module provides several types of intent decorators for decorating classes or methods. You
 can [use these decorators to develop intents](../../../application-models/insight-intent-decorator-development.md),
 define application functionalities as intents, and integrate them into AI entry points such as intelligent Q&A,
 intelligent search, and intelligent recommendation systems.
 -
 [@InsightIntentLink](../../../reference/apis-ability-kit/js-apis-app-ability-InsightIntentDecorator.md#insightintentlink)
 : decorates a URI in your application as an intent, enabling AI systems to quickly jump to your application via this
 intent. For details on the parameters supported by this decorator, see
 [LinkIntentDecoratorInfo](arkts-ability-app-ability-insightintentdecorator-linkintentdecoratorinfo-i.md).
 -
 [@InsightIntentPage](../../../reference/apis-ability-kit/js-apis-app-ability-InsightIntentDecorator.md#insightintentpage)
 : decorates a page in your application as an intent, enabling AI systems to swiftly navigate to that page. For
 details on the parameters supported by this decorator, see [PageIntentDecoratorInfo](arkts-ability-app-ability-insightintentdecorator-pageintentdecoratorinfo-i.md).
 -
 [@InsightIntentFunction](../../../reference/apis-ability-kit/js-apis-app-ability-InsightIntentDecorator.md#insightintentfunction)
 and
 [@InsightIntentFunctionMethod](../../../reference/apis-ability-kit/js-apis-app-ability-InsightIntentDecorator.md#insightintentfunctionmethod)
 : The two decorators must be used together.
 [@InsightIntentFunction](../../../reference/apis-ability-kit/js-apis-app-ability-InsightIntentDecorator.md#insightintentfunction)
 is used to decorate a class, and
 [@InsightIntentFunctionMethod](../../../reference/apis-ability-kit/js-apis-app-ability-InsightIntentDecorator.md#insightintentfunctionmethod)
 is used to decorate a static function in that class. This setup defines the static function as an intent, enabling
 AI systems to execute it rapidly.
 -
 [@InsightIntentEntry](../../../reference/apis-ability-kit/js-apis-app-ability-InsightIntentDecorator.md#insightintententry)
 : decorates a class that inherits from
 [InsightIntentEntryExecutor](arkts-ability-app-ability-insightintententryexecutor-insightintententryexecutor-c.md) to
 implement intent operations and configure the ability on which the intent depends. This helps the AI entry point to
 easily invoke the associated ability and perform the intended action. For details on the parameters supported by this
 decorator, see [EntryIntentDecoratorInfo](arkts-ability-app-ability-insightintentdecorator-entryintentdecoratorinfo-i.md).
 -
 [@InsightIntentForm](../../../reference/apis-ability-kit/js-apis-app-ability-InsightIntentDecorator.md#insightintentform)
 : decorates a [FormExtensionAbility](../../apis-form-kit/arkts-apis/arkts-form-app-form-formextensionability-formextensionability-c.md) to specify the name of the widget
 bound to the FormExtensionAbility. This enables the AI entry point to add the widget via intent calls. For details on
 the parameters supported by this decorator, see [FormIntentDecoratorInfo](arkts-ability-app-ability-insightintentdecorator-formintentdecoratorinfo-i.md).
 -
 [@InsightIntentEntity](../../../reference/apis-ability-kit/js-apis-app-ability-InsightIntentDecorator.md#insightintententity)
 : decorates a class that inherits from
 [IntentEntity](arkts-ability-insightintent-intententity-i.md) to define the class as an intent
 entity, which can pass parameters required for intent calls. For details on the parameters supported by this
 decorator, see [IntentEntityDecoratorInfo](arkts-ability-app-ability-insightintentdecorator-intententitydecoratorinfo-i.md).


## Modules to Import

```TypeScript
import { InsightIntentLink, InsightIntentPage, InsightIntentFunctionMethod, InsightIntentFunction, InsightIntentEntry, LinkParamCategory, InsightIntentForm, InsightIntentEntity } from 'kits/@kit.AbilityKit';
import { InsightIntentLink, InsightIntentPage, InsightIntentFunctionMethod, InsightIntentFunction, InsightIntentEntry, LinkParamCategory, LinkIntentParamMapping, InsightIntentEntity, InsightIntentForm } from 'kits/@kit.AbilityKit';
```

## Summary

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [EntryIntentDecoratorInfo](arkts-ability-app-ability-insightintentdecorator-entryintentdecoratorinfo-i.md) |
| [FormIntentDecoratorInfo](arkts-ability-app-ability-insightintentdecorator-formintentdecoratorinfo-i.md) |
| [FunctionIntentDecoratorInfo](arkts-ability-app-ability-insightintentdecorator-functionintentdecoratorinfo-i.md) |
| [IntentDecoratorInfo](arkts-ability-app-ability-insightintentdecorator-intentdecoratorinfo-i.md) |
| [IntentEntityDecoratorInfo](arkts-ability-app-ability-insightintentdecorator-intententitydecoratorinfo-i.md) |
| [LinkIntentDecoratorInfo](arkts-ability-app-ability-insightintentdecorator-linkintentdecoratorinfo-i.md) |
| [LinkIntentParamMapping](arkts-ability-app-ability-insightintentdecorator-linkintentparammapping-i.md) |
| [PageIntentDecoratorInfo](arkts-ability-app-ability-insightintentdecorator-pageintentdecoratorinfo-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [LinkParamCategory](arkts-ability-app-ability-insightintentdecorator-linkparamcategory-e.md) |
