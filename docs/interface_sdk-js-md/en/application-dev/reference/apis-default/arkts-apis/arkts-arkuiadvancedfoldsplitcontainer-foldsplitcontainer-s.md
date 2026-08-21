# FoldSplitContainer

Defines FoldSplitContainer container.

@interface FoldSplitContainer

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare struct FoldSplitContainer--><!--Device-unnamed-export declare struct FoldSplitContainer-End-->

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

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FoldSplitContainer-@Builder    build(): void--><!--Device-FoldSplitContainer-@Builder    build(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## animationOptions

```TypeScript
@PropRef
    animationOptions?: AnimateParam
```

The animation options of layout

**Type:** [AnimateParam](arkts-common-animateparam-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FoldSplitContainer-@PropRef    animationOptions?: AnimateParam--><!--Device-FoldSplitContainer-@PropRef    animationOptions?: AnimateParam-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## expandedLayoutOptions

```TypeScript
@PropRef
    expandedLayoutOptions: ExpandedRegionLayoutOptions
```

The layout options for the container when the foldable screen is expanded.

**Type:** [ExpandedRegionLayoutOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkuiadvancedfoldsplitcontainer-expandedregionlayoutoptions-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FoldSplitContainer-@PropRef    expandedLayoutOptions: ExpandedRegionLayoutOptions--><!--Device-FoldSplitContainer-@PropRef    expandedLayoutOptions: ExpandedRegionLayoutOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## extra

```TypeScript
@BuilderParam
    extra?: RegionBuilder
```

The builder function which will be rendered in the extra region of container.

**Type:** [RegionBuilder](arkts-regionbuilder-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FoldSplitContainer-@BuilderParam    extra?: RegionBuilder--><!--Device-FoldSplitContainer-@BuilderParam    extra?: RegionBuilder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## foldedLayoutOptions

```TypeScript
@PropRef
    foldedLayoutOptions: FoldedRegionLayoutOptions
```

The layout options for the container when the foldable screen is folded.

**Type:** [FoldedRegionLayoutOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkuiadvancedfoldsplitcontainer-foldedregionlayoutoptions-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FoldSplitContainer-@PropRef    foldedLayoutOptions: FoldedRegionLayoutOptions--><!--Device-FoldSplitContainer-@PropRef    foldedLayoutOptions: FoldedRegionLayoutOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## hoverModeLayoutOptions

```TypeScript
@PropRef
    hoverModeLayoutOptions: HoverModeRegionLayoutOptions
```

The layout options for the container when the foldable screen is in hover mode.

**Type:** [HoverModeRegionLayoutOptions](../../apis-arkui/arkts-apis/arkts-arkui-arkuiadvancedfoldsplitcontainer-hovermoderegionlayoutoptions-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FoldSplitContainer-@PropRef    hoverModeLayoutOptions: HoverModeRegionLayoutOptions--><!--Device-FoldSplitContainer-@PropRef    hoverModeLayoutOptions: HoverModeRegionLayoutOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onHoverStatusChange

```TypeScript
onHoverStatusChange?: OnHoverStatusChangeHandler
```

The callback function that is triggered when the foldable screen enters or exits hover mode. In hover mode, the upper half of the screen is used for display, and the lower half is used for operation.

**Type:** [OnHoverStatusChangeHandler](../../apis-arkui/arkts-apis/arkts-arkui-onhoverstatuschangehandler-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FoldSplitContainer-onHoverStatusChange?: OnHoverStatusChangeHandler--><!--Device-FoldSplitContainer-onHoverStatusChange?: OnHoverStatusChangeHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## primary

```TypeScript
@BuilderParam
    primary: RegionBuilder
```

The builder function which will be rendered in the major region of container.

**Type:** [RegionBuilder](arkts-regionbuilder-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FoldSplitContainer-@BuilderParam    primary: RegionBuilder--><!--Device-FoldSplitContainer-@BuilderParam    primary: RegionBuilder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## secondary

```TypeScript
@BuilderParam
    secondary: RegionBuilder
```

The builder function which will be rendered in the minor region of container.

**Type:** [RegionBuilder](arkts-regionbuilder-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FoldSplitContainer-@BuilderParam    secondary: RegionBuilder--><!--Device-FoldSplitContainer-@BuilderParam    secondary: RegionBuilder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

