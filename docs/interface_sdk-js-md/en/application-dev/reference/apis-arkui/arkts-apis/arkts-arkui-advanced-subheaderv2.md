# @ohos.arkui.advanced.SubHeaderV2

## Modules to Import

```TypeScript
import { SubHeaderV2IconType } from 'SubHeaderV2IconType';
import { SubHeaderV2Title } from 'SubHeaderV2Title';
import { SubHeaderV2Select } from 'SubHeaderV2Select';
import { SubHeaderV2 } from 'SubHeaderV2';
import { SubHeaderV2OperationType } from 'SubHeaderV2OperationType';
import { SubHeaderV2OperationItem } from 'SubHeaderV2OperationItem';
import { SubHeaderV2OperationItemType } from 'SubHeaderV2OperationItemType';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [SubHeaderV2OperationItem](arkts-arkui-arkui-advanced-subheaderv2-subheaderv2operationitem-c.md) | Represents an item in the operation area. |
| [SubHeaderV2Select](arkts-arkui-arkui-advanced-subheaderv2-subheaderv2select-c.md) | Defines the content and events for selection. |
| [SubHeaderV2Title](arkts-arkui-arkui-advanced-subheaderv2-subheaderv2title-c.md) | Defines the title settings for the subheader. |

### Structs

| Name | Description |
| --- | --- |
| [SubHeaderV2](arkts-arkui-arkui-advanced-subheaderv2-subheaderv2-s.md) | The component is positioned at the top of list items or content sections, organizing lists or content into distinct groups. The subheader text summarizes the content within each respective section. This component is implemented based on [state management V2](../../../ui/state-management/arkts-state-management-overview.md#state-management-v2). Compared with [state management V1](../../../ui/state-management/arkts-state-management-overview.md#state-management-v1), V2 offers a higher level of observation and management over data objects beyond the component level. You can now more easily manage subheader data and states with greater flexibility, leading to faster UI updates. > **NOTE：**> > - This component can be used only in the stage model. > > - If the **SubHeaderV2** component has universal attributes and > universal events configured, the compiler toolchain automatically > generates an additional **__Common__** node and mounts the universal attributes and universal events on this node > rather than the **SubHeaderV2** component itself. As a result, the configured universal attributes and universal > events may fail to take effect or behave as intended. For this reason, avoid using universal attributes and events > with the **SubHeaderV2** component. |

### Interfaces

| Name | Description |
| --- | --- |
| [SubHeaderV2OperationItemOptions](arkts-arkui-arkui-advanced-subheaderv2-subheaderv2operationitemoptions-i.md) | Defines the options for initializing a **SubHeaderV2OperationItem** object. |
| [SubHeaderV2SelectOptions](arkts-arkui-arkui-advanced-subheaderv2-subheaderv2selectoptions-i.md) | Defines the options for initializing a **SubHeaderV2Select** object. |
| [SubHeaderV2TitleOptions](arkts-arkui-arkui-advanced-subheaderv2-subheaderv2titleoptions-i.md) | Defines the options for initializing a **SubHeaderV2Title** object. |

### Enums

| Name | Description |
| --- | --- |
| [SubHeaderV2OperationType](arkts-arkui-arkui-advanced-subheaderv2-subheaderv2operationtype-e.md) | Defines the style of elements in the operation area. |

### Types

| Name | Description |
| --- | --- |
| [SubHeaderV2IconType](arkts-arkui-subheaderv2icontype-t.md) | SubHeaderV2IconType |
| [SubHeaderV2OperationItemAction](arkts-arkui-subheaderv2operationitemaction-t.md) | Defines the callback for items in the operation area. |
| [SubHeaderV2OperationItemType](arkts-arkui-subheaderv2operationitemtype-t.md) | SubHeaderV2OperationItemType |
| [SubHeaderV2SelectOnSelect](arkts-arkui-subheaderv2selectonselect-t.md) | Defines the callback invoked when an item in the drop-down list box is selected. |
| [SubHeaderV2TitleBuilder](arkts-arkui-subheaderv2titlebuilder-t.md) | Defines the callback used to customize the content of the title area. |

