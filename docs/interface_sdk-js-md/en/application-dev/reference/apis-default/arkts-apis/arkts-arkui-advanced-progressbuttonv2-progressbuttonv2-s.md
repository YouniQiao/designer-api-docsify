# ProgressButtonV2

Declare Component ProgressButtonV2 @struct { ProgressButtonV2 }

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare struct ProgressButtonV2--><!--Device-unnamed-export declare struct ProgressButtonV2-End-->

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

<!--Device-ProgressButtonV2-@Builder  build(): void--><!--Device-ProgressButtonV2-@Builder  build(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## colorOptions

```TypeScript
@Param
  colorOptions?: ProgressButtonV2Color
```

Set Color options of the ProgressButtonV2.

**Type:** [ProgressButtonV2Color](arkts-arkui-advanced-progressbuttonv2-progressbuttonv2color-c.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ProgressButtonV2-@Param  colorOptions?: ProgressButtonV2Color--><!--Device-ProgressButtonV2-@Param  colorOptions?: ProgressButtonV2Color-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## content

```TypeScript
@Require
  @Param
  readonly content: ResourceStr
```

Sets the ProgressButtonV2 content.

**Type:** ResourceStr

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ProgressButtonV2-@Require  @Param  readonly content: ResourceStr--><!--Device-ProgressButtonV2-@Require  @Param  readonly content: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isEnabled

```TypeScript
@Param
  readonly isEnabled: boolean
```

Sets the ProgressButtonV2 isEnabled state.

**Type:** boolean

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ProgressButtonV2-@Param  readonly isEnabled: boolean--><!--Device-ProgressButtonV2-@Param  readonly isEnabled: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onClicked

```TypeScript
@Param
  readonly onClicked: ClickCallback
```

Sets the ProgressButtonV2 onClicked.

**Type:** [ClickCallback](arkts-clickcallback-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ProgressButtonV2-@Param  readonly onClicked: ClickCallback--><!--Device-ProgressButtonV2-@Param  readonly onClicked: ClickCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## progress

```TypeScript
@Require
  @Param
  readonly progress: double
```

Sets the ProgressButtonV2 progress.

**Type:** double

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ProgressButtonV2-@Require  @Param  readonly progress: double--><!--Device-ProgressButtonV2-@Require  @Param  readonly progress: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## progressButtonRadius

```TypeScript
@Param
  progressButtonRadius?: LengthMetrics
```

Set border rounded corner radius of progress.

**Type:** [LengthMetrics](arkts-graphics-lengthmetrics-c.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ProgressButtonV2-@Param  progressButtonRadius?: LengthMetrics--><!--Device-ProgressButtonV2-@Param  progressButtonRadius?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## progressButtonWidth

```TypeScript
@Param
  @Once
  progressButtonWidth?: LengthMetrics
```

Sets the ProgressButtonV2 progressButtonWidth.

**Type:** [LengthMetrics](arkts-graphics-lengthmetrics-c.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ProgressButtonV2-@Param  @Once  progressButtonWidth?: LengthMetrics--><!--Device-ProgressButtonV2-@Param  @Once  progressButtonWidth?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

