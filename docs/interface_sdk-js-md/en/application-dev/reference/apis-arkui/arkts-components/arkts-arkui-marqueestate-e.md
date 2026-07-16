# MarqueeState

Enumerates the return values of the marquee state callback.

**Since:** 18

<!--Device-unnamed-declare enum MarqueeState--><!--Device-unnamed-declare enum MarqueeState-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## START

```TypeScript
START = 0
```

The marquee starts scrolling.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MarqueeState-START = 0--><!--Device-MarqueeState-START = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## BOUNCE

```TypeScript
BOUNCE = 1
```

The marquee completes one scroll movement. If the number of **loops** is not 1, this value will be returned multiple times.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MarqueeState-BOUNCE = 1--><!--Device-MarqueeState-BOUNCE = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## FINISH

```TypeScript
FINISH = 2
```

All loops of the marquee are completed.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-MarqueeState-FINISH = 2--><!--Device-MarqueeState-FINISH = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

