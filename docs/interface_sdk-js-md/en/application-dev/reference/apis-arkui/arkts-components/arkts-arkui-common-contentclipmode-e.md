# ContentClipMode

Enum of scrollable containers' content clip mode.

**Since:** 14

<!--Device-unnamed-declare enum ContentClipMode--><!--Device-unnamed-declare enum ContentClipMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## CONTENT_ONLY

```TypeScript
CONTENT_ONLY = 0
```

Clip to content rect inside margin & padding.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-ContentClipMode-CONTENT_ONLY = 0--><!--Device-ContentClipMode-CONTENT_ONLY = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## BOUNDARY

```TypeScript
BOUNDARY = 1
```

Clip to scrollable's outer rect, including padding but inside margin.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-ContentClipMode-BOUNDARY = 1--><!--Device-ContentClipMode-BOUNDARY = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SAFE_AREA

```TypeScript
SAFE_AREA = 2
```

Clip to the safeArea of scrollable container.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-ContentClipMode-SAFE_AREA = 2--><!--Device-ContentClipMode-SAFE_AREA = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

