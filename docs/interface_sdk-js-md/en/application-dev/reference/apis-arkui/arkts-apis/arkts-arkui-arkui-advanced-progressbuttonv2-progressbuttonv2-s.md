# ProgressButtonV2

Declare Component ProgressButtonV2

**Since:** 18

**Decorator:** @ComponentV2

<!--Device-unnamed-export declare struct ProgressButtonV2--><!--Device-unnamed-export declare struct ProgressButtonV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { ProgressButtonV2, ProgressButtonV2Color, ProgressButtonV2ColorOptions } from '@kit.ArkUI';
```

## colorOptions

Set Color options of the ProgressButtonV2.

**Type:** [ProgressButtonV2Color](arkts-arkui-arkui-advanced-progressbuttonv2-progressbuttonv2color-c.md)

**Since:** 18

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ProgressButtonV2-@Param colorOptions?: ProgressButtonV2Color--><!--Device-ProgressButtonV2-@Param colorOptions?: ProgressButtonV2Color-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## content

Sets the ProgressButtonV2 content.

**Type:** ResourceStr

**Since:** 18

**Decorator:** @Require, @Param

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ProgressButtonV2-@Require  @Param readonly content: ResourceStr--><!--Device-ProgressButtonV2-@Require  @Param readonly content: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isEnabled

Sets the ProgressButtonV2 isEnabled state.

**Type:** boolean

**Since:** 18

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ProgressButtonV2-@Param readonly isEnabled: boolean--><!--Device-ProgressButtonV2-@Param readonly isEnabled: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onClicked

Sets the ProgressButtonV2 onClicked.

**Type:** [ClickCallback](arkts-arkui-clickcallback-t.md)

**Since:** 18

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ProgressButtonV2-@Param readonly onClicked: ClickCallback--><!--Device-ProgressButtonV2-@Param readonly onClicked: ClickCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## progress

Sets the ProgressButtonV2 progress.

**Type:** number

**Since:** 18

**Decorator:** @Require, @Param

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ProgressButtonV2-@Require  @Param readonly progress: number--><!--Device-ProgressButtonV2-@Require  @Param readonly progress: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## progressButtonRadius

Set border rounded corner radius of progress.

**Type:** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**Since:** 18

**Decorator:** @Param

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ProgressButtonV2-@Param progressButtonRadius?: LengthMetrics--><!--Device-ProgressButtonV2-@Param progressButtonRadius?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## progressButtonWidth

Sets the ProgressButtonV2 progressButtonWidth.

**Type:** [LengthMetrics](arkts-arkui-graphics-lengthmetrics-c.md)

**Since:** 18

**Decorator:** @Param, @Once

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-ProgressButtonV2-@Param @Once progressButtonWidth?: LengthMetrics--><!--Device-ProgressButtonV2-@Param @Once progressButtonWidth?: LengthMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

