# @ohos.arkui.advanced.FoldSplitContainer(Defines FoldSplitContainer component.)

## Modules to Import

```TypeScript
import { ExtraRegionPosition, ExpandedRegionLayoutOptions, HoverModeRegionLayoutOptions, FoldedRegionLayoutOptions, PresetSplitRatio, FoldSplitContainer, HoverModeStatus, OnHoverStatusChangeHandler, } from '@kit.ArkUI';
```

## Summary

### Structs

| Name | Description |
| --- | --- |
| [FoldSplitContainer](arkts-arkui-arkui-advanced-foldsplitcontainer-foldsplitcontainer-s.md) | The **FoldSplitContainer** component implements split-screen layout, providing region control for two-panel and three -panel layouts on foldable screens in the expanded state (device fully unfolded), hover state (device half-folded), and folded state (device fully folded). It is suitable for responsive layout adaptation scenarios in foldable screen apps, helping developers implement intelligent split-panel layouts across multiple screen states and improving user experience. For details about fold status, see [display.FoldStatus](arkts-arkui-display-foldstatus-e.md). |

### Interfaces

| Name | Description |
| --- | --- |
| [ExpandedRegionLayoutOptions](arkts-arkui-arkui-advanced-foldsplitcontainer-expandedregionlayoutoptions-i.md) | Defines layout information for the expanded state. |
| [FoldedRegionLayoutOptions](arkts-arkui-arkui-advanced-foldsplitcontainer-foldedregionlayoutoptions-i.md) | Defines the layout information for the folded state. |
| [HoverModeRegionLayoutOptions](arkts-arkui-arkui-advanced-foldsplitcontainer-hovermoderegionlayoutoptions-i.md) | Defines layout information for the hover state. |
| [HoverModeStatus](arkts-arkui-arkui-advanced-foldsplitcontainer-hovermodestatus-i.md) | Provides device or application information covering fold status, hover mode, application rotation, and window status type. |

### Enums

| Name | Description |
| --- | --- |
| [ExtraRegionPosition](arkts-arkui-arkui-advanced-foldsplitcontainer-extraregionposition-e.md) | Provides the position information of the extra region. |
| [PresetSplitRatio](arkts-arkui-arkui-advanced-foldsplitcontainer-presetsplitratio-e.md) | Enumerates the split ratios. |

### Types

| Name | Description |
| --- | --- |
| [OnHoverStatusChangeHandler](arkts-arkui-onhoverstatuschangehandler-t.md) | Defines an event handler for hover state changes. |

## Examples

```TypeScript
### Example 1: Setting Up a Two-Panel Layout

This example demonstrates how to control the region for a two-panel layout on a foldable screen across different states: folded, expanded, and hover.
```

```TypeScript
### Example 2: Setting Up a Three-Panel Layout

This example demonstrates how to control the region for a three-panel layout on a foldable screen across different states: folded, expanded, and hover.
```

```TypeScript
### Example 3: Configuring the Folded, Hover, and Expanded States of FoldSplitContainer

This example configures the folded, hover, and expanded state layout information of the foldable screen through [ExpandedRegionLayoutOptions](arkts-arkui-arkui-advanced-foldsplitcontainer-expandedregionlayoutoptions-i.md), [HoverModeRegionLayoutOptions](arkts-arkui-arkui-advanced-foldsplitcontainer-hovermoderegionlayoutoptions-i.md), and [FoldedRegionLayoutOptions](arkts-arkui-arkui-advanced-foldsplitcontainer-foldedregionlayoutoptions-i.md), respectively. The example provides an interactive configuration page, allowing users to adjust layout parameters in real time in each region: the primary area (MajorRegion) is used to configure folded state parameters, the secondary area (MinorRegion) is used to configure hover state parameters, and the expanded area (ExtraRegion) is used to configure expanded state parameters. These regions are implemented using the encapsulated region component Region, where RadioOptions is an encapsulated radio button switch component and SwitchOption is an encapsulated toggle switch component. The schematic diagram shows various layout effects under different parameter configurations.
```
