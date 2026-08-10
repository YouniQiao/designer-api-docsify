# AtomicServiceSearch

AtomicServiceSearch为开发者提供满足定制化需求的功能，内容包括默认显示的搜索区、可自定义的选择区和功能区（最多两个）。

> **说明：**
> 
> 该组件从API version 18开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Decorator:** @Component

<!--Device-unnamed-export declare struct AtomicServiceSearch--><!--Device-unnamed-export declare struct AtomicServiceSearch-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { SearchParams, AtomicServiceSearch, SearchButtonParams, OperationParams, SelectParams, InputFilterParams, MenuAlignParams } from 'kits/@kit.ArkUI';
```

## controller

```TypeScript
controller?: SearchController
```

Search组件控制器，用于设置输入光标的位置、退出编辑态等操作。默认值为undefined。

**Type:** [SearchController](../arkts-components/arkts-arkui-searchcontroller-c.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AtomicServiceSearch-controller?: SearchController--><!--Device-AtomicServiceSearch-controller?: SearchController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## operation

```TypeScript
operation?: OperationParams
```

功能区（右侧）的功能设置项。默认值为undefined。

**Type:** [OperationParams](arkts-arkui-atomicservice-atomicservicesearch-operationparams-i.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AtomicServiceSearch-operation?: OperationParams--><!--Device-AtomicServiceSearch-operation?: OperationParams-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## placeholder

```TypeScript
placeholder?: ResourceStr
```

搜索框内默认显示的提示文本。默认值为Search。

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Decorator:** @Prop

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AtomicServiceSearch-placeholder?: ResourceStr--><!--Device-AtomicServiceSearch-placeholder?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## search

```TypeScript
search?: SearchParams
```

search搜索区可支持的事件及样式。默认值为undefined。

**Type:** [SearchParams](arkts-arkui-atomicservice-atomicservicesearch-searchparams-i.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Decorator:** @Prop

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AtomicServiceSearch-search?: SearchParams--><!--Device-AtomicServiceSearch-search?: SearchParams-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## select

```TypeScript
select?: SelectParams
```

select选择区的内容、事件及样式。默认值为undefined。

**Type:** [SelectParams](arkts-arkui-atomicservice-atomicservicesearch-selectparams-i.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Decorator:** @Prop

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AtomicServiceSearch-select?: SelectParams--><!--Device-AtomicServiceSearch-select?: SelectParams-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
value?: ResourceStr
```

设置当前显示的搜索文本内容。默认值为空字符串。

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Decorator:** @Prop

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AtomicServiceSearch-value?: ResourceStr--><!--Device-AtomicServiceSearch-value?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

