# InsightIntentFunction

该注解与@InsightIntentFunctionMethod注解必须组合使用。 使用该注解来装饰类，同时使用@InsightIntentFunctionMethod注解来装饰类中的静态函数，可以将对应的静态函数定义为意图，便于AI入口能够快速执行此函数。 该注解仅支持ArkTS-Sta模式，对应ArkTS-Dyn模式接口见 @InsightIntentFunction。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## 导入模块

```TypeScript
import { InsightIntentLink, InsightIntentPage, InsightIntentFunctionMethod, InsightIntentFunction, InsightIntentEntry, LinkParamCategory, InsightIntentForm, InsightIntentEntity } from '@kit.AbilityKit';
import { InsightIntentLink, InsightIntentPage, InsightIntentFunctionMethod, InsightIntentFunction, InsightIntentEntry, LinkParamCategory, LinkIntentParamMapping, InsightIntentEntity, InsightIntentForm } from '@kit.AbilityKit';
```
