# LeadingMarginSpanDrawInfo

```TypeScript
declare interface LeadingMarginSpanDrawInfo
```

Provides the custom drawing information.

**Since:** 22

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## baseline

```TypeScript
baseline: number
```

Distance between the baseline of the current line and the top edge of the component. Unit: [px](../../../reference/apis-arkui/arkui-ts/ts-pixel-units.md#basic-pixel-units) Value range: greater than or equal to 0.

**Type:** number

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## bottom

```TypeScript
bottom: number
```

Distance between the bottom of the line and the top edge of the component. Unit: [px](../../../reference/apis-arkui/arkui-ts/ts-pixel-units.md#basic-pixel-units) Value range: greater than or equal to 0.

**Type:** number

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## direction

```TypeScript
direction: TextDirection
```

Direction of the text content.

**Type:** [TextDirection](arkts-arkui-textdirection-e.md)

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## end

```TypeScript
end: number
```

End index of the current line. Value range: greater than or equal to 0.

**Type:** number

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## first

```TypeScript
first: boolean
```

Whether the current line is the first line of the paragraph.

**true**: first line; **false**: not the first line.

**Type:** boolean

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## start

```TypeScript
start: number
```

Start index of the current line. Value range: greater than or equal to 0.

**Type:** number

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## top

```TypeScript
top: number
```

Distance between the top of the line and the top edge of the component. Unit: [px](../../../reference/apis-arkui/arkui-ts/ts-pixel-units.md#basic-pixel-units) Value range: greater than or equal to 0.

**Type:** number

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## x

```TypeScript
x: number
```

Horizontal offset of the current line relative to the component. When **direction** is RTL, the distance between the right side of the current line and the right edge of the component is returned. Unit: [px](../../../reference/apis-arkui/arkui-ts/ts-pixel-units.md#basic-pixel-units) Value range: greater than or equal to 0.

**Type:** number

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
