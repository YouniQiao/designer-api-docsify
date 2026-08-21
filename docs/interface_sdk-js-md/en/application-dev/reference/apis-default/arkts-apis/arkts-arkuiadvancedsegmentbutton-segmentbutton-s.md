# SegmentButton

Declare Component SegmentButton

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-declare struct SegmentButton--><!--Device-unnamed-declare struct SegmentButton-End-->

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

<!--Device-SegmentButton-@Builder  build(): void--><!--Device-SegmentButton-@Builder  build(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableStateAnimation

```TypeScript
@PropRef
  enableStateAnimation: boolean
```

Enable animation when selectedIndexes change.

**Type:** boolean

**Default:** false

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SegmentButton-@PropRef  enableStateAnimation: boolean--><!--Device-SegmentButton-@PropRef  enableStateAnimation: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maxFontScale

```TypeScript
@PropRef
  maxFontScale: double | Resource
```

The max font scale of the segmented button option text.

**Type:** double \| Resource

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SegmentButton-@PropRef  maxFontScale: double | Resource--><!--Device-SegmentButton-@PropRef  maxFontScale: double | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onItemClicked

```TypeScript
onItemClicked?: Callback<int>
```

The click event callback will be triggered when a option button of SegmentButton is clicked.

**Type:** [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;int&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SegmentButton-onItemClicked?: Callback<int>--><!--Device-SegmentButton-onItemClicked?: Callback<int>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## options

```TypeScript
@ObjectLink
  options: SegmentButtonOptions
```

The options of SegmentButton.

**Type:** [SegmentButtonOptions](arkts-arkuiadvancedsegmentbutton-segmentbuttonoptions-c.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SegmentButton-@ObjectLink  options: SegmentButtonOptions--><!--Device-SegmentButton-@ObjectLink  options: SegmentButtonOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedIndexes

```TypeScript
@Link
  selectedIndexes: int[]
```

The selectedIndex.

**Type:** int[]

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SegmentButton-@Link  selectedIndexes: int[]--><!--Device-SegmentButton-@Link  selectedIndexes: int[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

