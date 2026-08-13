# @ohos.arkui.advanced.SegmentButton

## Modules to Import

```TypeScript
import { CommonSegmentButtonOptions, SegmentButtonItemOptionsConstructorOptions, SegmentButtonIconTextItem, SegmentButtonItemOptions, SegmentButtonTextItem, CapsuleSegmentButtonOptions, SegmentButtonOptions, CapsuleSegmentButtonConstructionOptions, SegmentButtonItemTuple, SegmentButton, SegmentButtonItemArray, SegmentButtonItemOptionsArray, SegmentButtonIconItem, BorderRadiusMode, TabSegmentButtonConstructionOptions, TabSegmentButtonOptions, ItemRestriction, DimensionNoPercentage } from '@kit.ArkUI';
```

## Summary

### Structs

| Name | Description |
| --- | --- |
| [SegmentButton](arkts-arkui-arkui-advanced-segmentbutton-segmentbutton-s.md) | **SegmentButton** is a versatile component that organizes related options into visually grouped buttons. It supports three variants: tab-style, capsule-style single-select, and capsule-style multi-select. >**NOTE：**> > - The **SegmentButton** component does not support [universal attributes](ts-component-general-attributes.md). The component occupies the maximum available width within its content area and distributes this width evenly among its items. It adapts its height automatically to the content (text and images), the minimum height being 28 vp. > > - Properties decorated with @Prop are optional. They are required during construction only when used together with the @Require decorator. |

### Enums

| Name | Description |
| --- | --- |
| [BorderRadiusMode](arkts-arkui-arkui-advanced-segmentbutton-borderradiusmode-e.md) | Enumerates the border radius modes for the **SegmentButton** component, which are used to control the border radius calculation method. |

### Types

| Name | Description |
| --- | --- |
| [DimensionNoPercentage](arkts-arkui-dimensionnopercentage-t.md) | The percentage length union type is not supported. |
| [ItemRestriction](arkts-arkui-itemrestriction-t.md) | Tuple type that stores button information. > **NOTE：**> > A **SegmentButton** component supports two to five buttons. |
| [SegmentButtonItemTuple](arkts-arkui-segmentbuttonitemtuple-t.md) | Represents the tuple union type used to store button information. |

