# ISendable

是所有Sendable对象类型（除null和undefined）的父类型。实现该接口后，自定义类的实例将支持跨线程传递。自身不定义任何方法和属性。

ArkTS中，ISendable类型的对象是Object类型的实例，遵循Object类型的基本特征，同时支持跨线程传递。

ISendable主要用在开发者自定义Sendable数据结构的场景中。ArkTS语言标准库中的Sendable容器类型（如Array、Map、Set等）隐式地继承并实现了ISendable。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-lang-interface ISendable--><!--Device-lang-interface ISendable-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
import { Retention, RetentionPolicy } from 'kits/@kit.ArkTS';
```

