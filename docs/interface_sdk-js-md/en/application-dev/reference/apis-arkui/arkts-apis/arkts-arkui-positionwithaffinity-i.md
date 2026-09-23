# PositionWithAffinity

```TypeScript
interface PositionWithAffinity
```

Describes the position and affinity of a glyph.

**Since:** 12

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## affinity

```TypeScript
affinity: Affinity
```

Position affinity, which indicates the tendency of the caret position at glyph boundaries. For details about the values, see the Affinity enum.

**Type:** [Affinity](arkts-arkui-affinity-t.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## position

```TypeScript
position: number
```

Index of the glyph or character relative to the component. The value is an integer.

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
