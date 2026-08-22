# Filter

Declare Filter.The Filter is used in scenarios where multi-dimensional filtering is required. @struct { Filter }

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare struct Filter--><!--Device-unnamed-export declare struct Filter-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## build

```TypeScript
@Builder
    build(): void
```

The method to build component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Filter-@Builder    build(): void--><!--Device-Filter-@Builder    build(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## additionFilters

```TypeScript
@PropRef
    additionFilters?: FilterParams
```

FilterParams, Additional filter item parameter. The filter item name is displayed and can be deselected.

**Type:** [FilterParams](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-filter-filterparams-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Filter-@PropRef    additionFilters?: FilterParams--><!--Device-Filter-@PropRef    additionFilters?: FilterParams-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## container

```TypeScript
@BuilderParam
    container: () => void
```

Container in the user-defined filtering result display area.

**Type:** () =&gt; void

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Filter-@BuilderParam    container: () => void--><!--Device-Filter-@BuilderParam    container: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## filterType

```TypeScript
@PropRef
    filterType?: FilterType
```

FilterType, Filter display style type.

**Type:** [FilterType](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-filter-filtertype-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Filter-@PropRef    filterType?: FilterType--><!--Device-Filter-@PropRef    filterType?: FilterType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## multiFilters

```TypeScript
@PropRef
    multiFilters: Array<FilterParams>
```

Multi-dimensional filtering parameters.

**Type:** Array&lt;[FilterParams](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-filter-filterparams-c.md)&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Filter-@PropRef    multiFilters: Array<FilterParams>--><!--Device-Filter-@PropRef    multiFilters: Array<FilterParams>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onFilterChanged

```TypeScript
onFilterChanged: OnFilterChangedCallback
```

FilterParams, Callback method after a user clicks a filter item.

**Type:** [OnFilterChangedCallback](arkts-onfilterchangedcallback-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Filter-onFilterChanged: OnFilterChangedCallback--><!--Device-Filter-onFilterChanged: OnFilterChangedCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

