# ContentClipMode

Enum of scrollable containers' content clip mode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare enum ContentClipMode--><!--Device-unnamed-export declare enum ContentClipMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## CONTENT_ONLY

```TypeScript
CONTENT_ONLY = 0
```

Clip to content rect inside margin & padding.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContentClipMode-CONTENT_ONLY = 0--><!--Device-ContentClipMode-CONTENT_ONLY = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## BOUNDARY

```TypeScript
BOUNDARY = 1
```

Clip to scrollable's outer rect, including padding but inside margin.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContentClipMode-BOUNDARY = 1--><!--Device-ContentClipMode-BOUNDARY = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SAFE_AREA

```TypeScript
SAFE_AREA = 2
```

Clip to the safeArea of scrollable container.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContentClipMode-SAFE_AREA = 2--><!--Device-ContentClipMode-SAFE_AREA = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

