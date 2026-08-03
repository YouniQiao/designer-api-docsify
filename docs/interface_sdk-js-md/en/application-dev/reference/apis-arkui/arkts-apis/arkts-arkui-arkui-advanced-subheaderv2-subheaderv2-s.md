# SubHeaderV2

The component is positioned at the top of list items or content sections, organizing lists or content into distinct groups. The subheader text summarizes the content within each respective section.

This component is implemented based on [state management V2](../../../ui/state-management/arkts-state-management-overview.md#state-management-v2). Compared with [state management V1](../../../ui/state-management/arkts-state-management-overview.md#state-management-v1), V2offers a higher level of observation and management over data objects beyond the component level. You can now more easily manage subheader data and states with greater flexibility, leading to faster UI updates.
> **NOTE**  
>  
> - This component can be used only in the stage model.  
>  
> - If the **SubHeaderV2** component has [universal attributes](../../apis-arkui/arkts-components/arkts-arkui-common-attribute.md) and  
> [universal events](../../apis-arkui/arkts-components/arkts-arkui-common-attribute.md) configured, the compiler toolchain automatically  
> generates an additional **__Common__** node and mounts the universal attributes and universal events on this node  
> rather than the **SubHeaderV2** component itself. As a result, the configured universal attributes and universal  
> events may fail to take effect or behave as intended. For this reason, avoid using universal attributes and events  
> with the **SubHeaderV2** component.

**Since:** 18

**Decorator:** @ComponentV2

<!--Device-unnamed-export declare struct SubHeaderV2--><!--Device-unnamed-export declare struct SubHeaderV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { SubHeaderV2Select, SubHeaderV2, SubHeaderV2IconType, SubHeaderV2OperationItemType, SubHeaderV2OperationType, SubHeaderV2Title, SubHeaderV2OperationItem } from '@kit.ArkUI';
```

## icon

```TypeScript
readonly icon?: SubHeaderV2IconType
```

Icon.

Default value: **undefined**

**icon** takes effect only when **secondaryTitle** is used for **title**.

**Type:** SubHeaderV2IconType

**Since:** 18

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SubHeaderV2-readonly icon?: SubHeaderV2IconType--><!--Device-SubHeaderV2-readonly icon?: SubHeaderV2IconType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## operationItems

```TypeScript
readonly operationItems?: SubHeaderV2OperationItem[]
```

Items in the operation area.

Default value: **undefined**

**Type:** SubHeaderV2OperationItem[]

**Since:** 18

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SubHeaderV2-readonly operationItems?: SubHeaderV2OperationItem[]--><!--Device-SubHeaderV2-readonly operationItems?: SubHeaderV2OperationItem[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## operationType

```TypeScript
readonly operationType?: SubHeaderV2OperationType
```

Style of elements in the operation area.

Default value: **SubHeaderV2OperationType.BUTTON**

**Type:** SubHeaderV2OperationType

**Since:** 18

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SubHeaderV2-readonly operationType?: SubHeaderV2OperationType--><!--Device-SubHeaderV2-readonly operationType?: SubHeaderV2OperationType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## select

```TypeScript
readonly select?: SubHeaderV2Select
```

Content and events for selection.

Default value: **undefined**

**Type:** SubHeaderV2Select

**Since:** 18

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SubHeaderV2-readonly select?: SubHeaderV2Select--><!--Device-SubHeaderV2-readonly select?: SubHeaderV2Select-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## title

```TypeScript
readonly title?: SubHeaderV2Title
```

Title of the subheader.

Default value: **undefined**

**Type:** SubHeaderV2Title

**Since:** 18

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SubHeaderV2-readonly title?: SubHeaderV2Title--><!--Device-SubHeaderV2-readonly title?: SubHeaderV2Title-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## titleBuilder

```TypeScript
titleBuilder?: SubHeaderV2TitleBuilder
```

Custom content for the title area.

Default value: **() => void**

**Type:** SubHeaderV2TitleBuilder

**Since:** 18

**Decorator:** @BuilderParam

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SubHeaderV2-titleBuilder?: SubHeaderV2TitleBuilder--><!--Device-SubHeaderV2-titleBuilder?: SubHeaderV2TitleBuilder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

