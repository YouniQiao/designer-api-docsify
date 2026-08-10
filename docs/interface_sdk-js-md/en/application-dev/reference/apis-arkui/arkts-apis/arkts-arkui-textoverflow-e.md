# TextOverflow

Declare how text overflows.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-unnamed-declare enum TextOverflow--><!--Device-unnamed-declare enum TextOverflow-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## None

```TypeScript
None = 0
```

When the text overflows its dimensions, the text will not be cropped.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-TextOverflow-None = 0--><!--Device-TextOverflow-None = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Clip

```TypeScript
Clip = 1
```

When the text overflows its dimensions, the text will be cropped and displayed.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-TextOverflow-Clip = 1--><!--Device-TextOverflow-Clip = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Ellipsis

```TypeScript
Ellipsis = 2
```

If the text overflows its dimensions, the text that cannot be displayed shall be replaced by ellipsis.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-TextOverflow-Ellipsis = 2--><!--Device-TextOverflow-Ellipsis = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## MARQUEE

```TypeScript
MARQUEE = 3
```

When the text overflows its dimensions, the text will scroll for displaying.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextOverflow-MARQUEE = 3--><!--Device-TextOverflow-MARQUEE = 3-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

