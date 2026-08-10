# InsightIntentEntryExecutor

本模块提供  
[@InsightIntentEntry](../../../reference/apis-ability-kit/js-apis-app-ability-InsightIntentDecorator.md#insightintententry)装饰器的意图执行基类，必须与@InsightIntentEntry装饰器联合使用。开发者需要在继承该基类的子类中，实现[onExecute()](InsightIntentEntryExecutor.InsightIntentEntryExecutor#onExecute)意图执行回调，并使用@InsightIntentEntry装饰器来装饰子类。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-unnamed-export default class InsightIntentEntryExecutor<T>--><!--Device-unnamed-export default class InsightIntentEntryExecutor<T>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { InsightIntentEntryExecutor } from 'kits/@kit.AbilityKit';
```

