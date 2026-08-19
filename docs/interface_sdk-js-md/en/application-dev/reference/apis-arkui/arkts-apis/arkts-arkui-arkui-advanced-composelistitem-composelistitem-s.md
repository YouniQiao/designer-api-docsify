# ComposeListItem

The **ComposeListItem** component is a container that presents a series of items arranged in a column with the same width. You can use it to present data of the same type in a multiple and coherent row style, for example, images or text. &gt; **NOTE：**&gt; &gt; - This component can be used only in the stage model. &gt; &gt; - If the **ComposeListItem** component has universal attributes and &gt; universal events configured, the compiler toolchain automatically &gt; generates an additional **__Common__** node and mounts the universal attributes and universal events on this node &gt; rather than the **ComposeListItem** component itself. As a result, the configured universal attributes and &gt; universal events may fail to take effect or behave as intended. For this reason, avoid using universal attributes &gt; and events with the **ComposeListItem** component.

**Since:** 10

<!--Device-unnamed-export declare struct ComposeListItem--><!--Device-unnamed-export declare struct ComposeListItem-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { ComposeListItem, ContentItem, IconType, OperateButton, OperateCheck, OperateIcon, OperateItem } from '@kit.ArkUI';
import { ComposeListItemV2, ContentItemV2, ContentItemV2Options, IconTypeV2, OperateButtonV2, OperateButtonV2Options, OperateCheckV2, OperateCheckV2Options, OperateIconV2, OperateIconV2Options, OperateItemV2, OperateItemV2Options } from '@kit.ArkUI';
```

## contentItem

```TypeScript
@Prop
  contentItem?: ContentItem
```

Elements on the left and in the center.

**Type:** [ContentItem](arkts-arkui-arkui-advanced-composelistitem-contentitem-c.md)

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ComposeListItem-@Prop  contentItem?: ContentItem--><!--Device-ComposeListItem-@Prop  contentItem?: ContentItem-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## operateItem

```TypeScript
@Prop
  operateItem?: OperateItem
```

Element on the right.

**Type:** [OperateItem](arkts-arkui-arkui-advanced-composelistitem-operateitem-c.md)

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ComposeListItem-@Prop  operateItem?: OperateItem--><!--Device-ComposeListItem-@Prop  operateItem?: OperateItem-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

