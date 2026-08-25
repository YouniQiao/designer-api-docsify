# CanvasTextBaseline

```TypeScript
export type CanvasTextBaseline = 'alphabetic' | 'bottom' | 'hanging' | 'ideographic' | 'middle' | 'top'
```

Text baseline, which supports the following configurations:'alphabetic': (Default) The text baseline is the standard letter baseline.'bottom': The text baseline is at the bottom of the text block. The difference between the ideographic baseline and the ideographic baseline is that the ideographic baseline does not need to consider downlink letters.'hanging': The text baseline is a hanging baseline.'ideographic': The text baseline is the ideographic baseline; If the character itself exceeds the alphabetic baseline, the ideographic baseline is at the bottom of the character itself.'middle': The text baseline is in the middle of the text block.'top': The text baseline is at the top of the text block.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| 'alphabetic' |
| 'bottom' |
| 'hanging' |
| 'ideographic' |
| 'middle' |
| 'top' |
