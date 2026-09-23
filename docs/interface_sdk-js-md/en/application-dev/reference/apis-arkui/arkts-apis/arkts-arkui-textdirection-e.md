# TextDirection

```TypeScript
declare enum TextDirection
```

Enumerates the text layout directions.

**Since:** 22

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## LTR

```TypeScript
LTR = 0
```

Text layout direction is from left to right.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## RTL

```TypeScript
RTL = 1
```

Text layout direction is from right to left.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## DEFAULT

```TypeScript
DEFAULT = 2
```

The text layout direction follows the component layout direction.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## AUTO

```TypeScript
AUTO = 3
```

The layout direction follows the actual text content. If the text is in an RTL (Right-to-Left) language (such as Tibetan or Uyghur), the text layout direction is from right to left. If the text is in an LTR (Left-to-Right) language (such as Chinese or English), the text layout direction is from left to right.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
