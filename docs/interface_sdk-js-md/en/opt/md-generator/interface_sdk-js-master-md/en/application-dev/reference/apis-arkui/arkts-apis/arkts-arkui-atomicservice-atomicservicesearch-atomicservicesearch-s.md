# AtomicServiceSearch

**AtomicServiceSearch** allows you to customize the default search area, customizable selection area, and function area (a maximum of two).

**Since:** 18

<!--Device-unnamed-export declare struct AtomicServiceSearch--><!--Device-unnamed-export declare struct AtomicServiceSearch-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## controller

```TypeScript
controller?: SearchController
```

Set the Search component controller.

**Type:** [SearchController](../arkts-components/arkts-arkui-searchcontroller-c.md)

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AtomicServiceSearch-controller?: SearchController--><!--Device-AtomicServiceSearch-controller?: SearchController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## operation

```TypeScript
operation?: OperationParams
```

Function settings in the selection area (right).

**Type:** [OperationParams](arkts-arkui-atomicservice-atomicservicesearch-operationparams-i.md)

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AtomicServiceSearch-operation?: OperationParams--><!--Device-AtomicServiceSearch-operation?: OperationParams-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## placeholder

```TypeScript
@Prop
  placeholder?: ResourceStr
```

Indicates default prompt text displayed in the search box. The default value is Search, which supports globalization.

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AtomicServiceSearch-@Prop  placeholder?: ResourceStr--><!--Device-AtomicServiceSearch-@Prop  placeholder?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## search

```TypeScript
@Prop
  search?: SearchParams
```

Events and styles supported by the search area.

**Type:** [SearchParams](arkts-arkui-atomicservice-atomicservicesearch-searchparams-i.md)

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AtomicServiceSearch-@Prop  search?: SearchParams--><!--Device-AtomicServiceSearch-@Prop  search?: SearchParams-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## select

```TypeScript
@Prop
  select?: SelectParams
```

Contents, events, and styles of the select area.

**Type:** [SelectParams](arkts-arkui-atomicservice-atomicservicesearch-selectparams-i.md)

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AtomicServiceSearch-@Prop  select?: SelectParams--><!--Device-AtomicServiceSearch-@Prop  select?: SelectParams-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
@Prop
  value?: ResourceStr
```

Sets the search text content that is currently displayed.

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md)

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AtomicServiceSearch-@Prop  value?: ResourceStr--><!--Device-AtomicServiceSearch-@Prop  value?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
