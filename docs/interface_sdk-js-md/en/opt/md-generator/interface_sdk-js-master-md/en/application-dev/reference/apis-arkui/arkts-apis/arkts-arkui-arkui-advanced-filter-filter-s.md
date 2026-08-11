# Filter

Declare Filter.The Filter is used in scenarios where multi-dimensional filtering is required.

**Since:** 22

**Decorator:** @Component

<!--Device-unnamed-export declare struct Filter--><!--Device-unnamed-export declare struct Filter-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { FilterType, Filter, FilterParams, FilterResult } from 'kits/@kit.ArkUI';
```

## container

```TypeScript
container: () => void
```

Container in the user-defined filtering result display area.

**Since:** 22

**Decorator:** @BuilderParam

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Filter-container: () => void--><!--Device-Filter-container: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onFilterChanged

```TypeScript
onFilterChanged: (filterResults: Array<FilterResult>) => void
```

FilterParams, Callback method after a user clicks a filter item.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Filter-onFilterChanged: (filterResults: Array<FilterResult>) => void--><!--Device-Filter-onFilterChanged: (filterResults: Array<FilterResult>) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| filterResults | Array&lt;FilterResult&gt; | Yes |

## additionFilters

```TypeScript
additionFilters?: FilterParams
```

FilterParams, Additional filter item parameter. The filter item name is displayed and can be deselected.

**Type:** [FilterParams](arkts-arkui-arkui-advanced-filter-filterparams-c.md)

**Since:** 22

**Decorator:** @Prop

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Filter-additionFilters?: FilterParams--><!--Device-Filter-additionFilters?: FilterParams-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## filterType

```TypeScript
filterType?: FilterType
```

FilterType, Filter display style type.

**Type:** [FilterType](arkts-arkui-arkui-advanced-filter-filtertype-e.md)

**Since:** 22

**Decorator:** @Prop

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Filter-filterType?: FilterType--><!--Device-Filter-filterType?: FilterType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## multiFilters

```TypeScript
multiFilters: Array<FilterParams>
```

Multi-dimensional filtering parameters.

**Type:** Array&lt;FilterParams&gt;

**Since:** 22

**Decorator:** @Prop

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-Filter-multiFilters: Array<FilterParams>--><!--Device-Filter-multiFilters: Array<FilterParams>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
