# GridObjectSortComponent

**GridObjectSortComponent** is a grid object organizer that you can use to edit, drag to sort, add, and delete grid objects.

> **NOTE：**&gt;
> - If the **GridObjectSortComponent** component has universal attributes
> and universal events configured, the compiler toolchain automatically
> generates an additional **__Common__** node and mounts the universal attributes and universal events on this node
> rather than the **GridObjectSortComponent** component itself. As a result, the configured universal attributes and
> universal events may fail to take effect or behave as intended. For this reason, avoid using universal attributes
> and events with the **GridObjectSortComponent** component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Component

<!--Device-unnamed-export declare struct GridObjectSortComponent--><!--Device-unnamed-export declare struct GridObjectSortComponent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## build

```TypeScript
build(): void
```

Build function of GridObjectSortComponent.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-GridObjectSortComponent-@Builder  build(): void--><!--Device-GridObjectSortComponent-@Builder  build(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## dataList

```TypeScript
dataList: Array<GridObjectSortComponentItem>
```

Data to pass. The maximum data length is 50 characters. If it is exceeded, only the first 50 characters are used.

**Type:** Array&lt;[GridObjectSortComponentItem](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-gridobjectsortcomponent-gridobjectsortcomponentitem-i.md)&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GridObjectSortComponent-dataList: Array<GridObjectSortComponentItem>--><!--Device-GridObjectSortComponent-dataList: Array<GridObjectSortComponentItem>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onCancel

```TypeScript
onCancel: () => void
```

Callback invoked when changes are canceled.

**Type:** () =&gt; void

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GridObjectSortComponent-onCancel: () => void--><!--Device-GridObjectSortComponent-onCancel: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onSave

```TypeScript
onSave: (select: Array<GridObjectSortComponentItem>, unselect: Array<GridObjectSortComponentItem>) => void
```

Callback invoked when changes are saved. The data after the changes is returned.

**Type:** (select: Array&lt;[GridObjectSortComponentItem](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-gridobjectsortcomponent-gridobjectsortcomponentitem-i.md)&gt;, unselect: Array&lt;GridObjectSortComponentItem&gt;) =&gt; void

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GridObjectSortComponent-onSave: (select: Array<GridObjectSortComponentItem>, unselect: Array<GridObjectSortComponentItem>) => void--><!--Device-GridObjectSortComponent-onSave: (select: Array<GridObjectSortComponentItem>, unselect: Array<GridObjectSortComponentItem>) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## options

```TypeScript
options: GridObjectSortComponentOptions
```

Component configuration.

**Type:** [GridObjectSortComponentOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-gridobjectsortcomponent-gridobjectsortcomponentoptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @PropRef

**Model restriction:** This API can be used only in the stage model.

<!--Device-GridObjectSortComponent-@PropRef  options: GridObjectSortComponentOptions--><!--Device-GridObjectSortComponent-@PropRef  options: GridObjectSortComponentOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

