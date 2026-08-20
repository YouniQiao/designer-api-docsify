# FoldSplitContainer

*FoldSplitContainer** is a layout container designed to manage regions for two-panel and three-panel arrangements on a foldable device across various states, including the expanded state, the semi-folded state, and the folded state.

> **NOTE：**
> 
> By default, a two-panel layout is used when the window width is less than or equal to 600 vp.
> When the window width exceeds 600 vp, an extended area is supported alongside the top-bottom split layout.
> A semi-folded state layout can be triggered when the window width is greater than 600 vp and the device &gt; is in a horizontal, half-folded posture. In the semi-folded layout, visual avoidance for the screen &gt; crease area is applied, and the extended area cannot span across the crease. The extended area can also &gt; be configured not to display in the semi-folded state.

**Since:** 12

<!--Device-unnamed-export declare struct FoldSplitContainer--><!--Device-unnamed-export declare struct FoldSplitContainer-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { ExtraRegionPosition, ExpandedRegionLayoutOptions, HoverModeRegionLayoutOptions, FoldedRegionLayoutOptions, PresetSplitRatio, FoldSplitContainer, HoverModeStatus, OnHoverStatusChangeHandler, } from '@kit.ArkUI';
```

## animationOptions

```TypeScript
@Prop
    animationOptions?: AnimateParam | null
```

Animation settings. The value **null** indicates that the animation is disabled.

**Type:** [AnimateParam](../../apis-default/arkts-apis/arkts-common-animateparam-i.md) \| null

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FoldSplitContainer-@Prop    animationOptions?: AnimateParam | null--><!--Device-FoldSplitContainer-@Prop    animationOptions?: AnimateParam | null-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## expandedLayoutOptions

```TypeScript
@Prop
    expandedLayoutOptions: ExpandedRegionLayoutOptions
```

Layout information for the expanded state.

**Type:** [ExpandedRegionLayoutOptions](../../apis-default/arkts-apis/arkts-arkui-advanced-foldsplitcontainer-expandedregionlayoutoptions-i.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FoldSplitContainer-@Prop    expandedLayoutOptions: ExpandedRegionLayoutOptions--><!--Device-FoldSplitContainer-@Prop    expandedLayoutOptions: ExpandedRegionLayoutOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## extra

```TypeScript
@BuilderParam
    extra?: Callback<void>
```

Callback function for the extra region. If this parameter is not provided, there is no corresponding region.

**Type:** [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;void&gt;

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FoldSplitContainer-@BuilderParam    extra?: Callback<void>--><!--Device-FoldSplitContainer-@BuilderParam    extra?: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## foldedLayoutOptions

```TypeScript
@Prop
    foldedLayoutOptions: FoldedRegionLayoutOptions
```

Layout information for the folded state.

**Type:** [FoldedRegionLayoutOptions](../../apis-default/arkts-apis/arkts-arkui-advanced-foldsplitcontainer-foldedregionlayoutoptions-i.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FoldSplitContainer-@Prop    foldedLayoutOptions: FoldedRegionLayoutOptions--><!--Device-FoldSplitContainer-@Prop    foldedLayoutOptions: FoldedRegionLayoutOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## hoverModeLayoutOptions

```TypeScript
@Prop
    hoverModeLayoutOptions: HoverModeRegionLayoutOptions
```

Layout information for the semi-folded state.

**Type:** [HoverModeRegionLayoutOptions](../../apis-default/arkts-apis/arkts-arkui-advanced-foldsplitcontainer-hovermoderegionlayoutoptions-i.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FoldSplitContainer-@Prop    hoverModeLayoutOptions: HoverModeRegionLayoutOptions--><!--Device-FoldSplitContainer-@Prop    hoverModeLayoutOptions: HoverModeRegionLayoutOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onHoverStatusChange

```TypeScript
onHoverStatusChange?: OnHoverStatusChangeHandler
```

Callback function triggered when the foldable device enters or exits the semi-folded state.

**Type:** [OnHoverStatusChangeHandler](../../apis-default/arkts-apis/arkts-onhoverstatuschangehandler-t.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FoldSplitContainer-onHoverStatusChange?: OnHoverStatusChangeHandler--><!--Device-FoldSplitContainer-onHoverStatusChange?: OnHoverStatusChangeHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## primary

```TypeScript
@BuilderParam
    primary: Callback<void>
```

Callback function for the primary region.

**Type:** [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;void&gt;

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FoldSplitContainer-@BuilderParam    primary: Callback<void>--><!--Device-FoldSplitContainer-@BuilderParam    primary: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## secondary

```TypeScript
@BuilderParam
    secondary: Callback<void>
```

Callback function for the extra region.

**Type:** [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;void&gt;

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FoldSplitContainer-@BuilderParam    secondary: Callback<void>--><!--Device-FoldSplitContainer-@BuilderParam    secondary: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

