# ContentClipMode

```TypeScript
declare enum ContentClipMode
```

Enumerates the content clipping modes for the scrollable container.

The figure below illustrates the clipping areas corresponding to each enumeration value after the component has been configured with margin and padding attributes.

**Since:** 14

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## CONTENT_ONLY

```TypeScript
CONTENT_ONLY = 0
```

Clip to the content area, corresponding to the green area in the figure.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## BOUNDARY

```TypeScript
BOUNDARY = 1
```

Clip to the component area, corresponding to the entire blue area in the figure.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SAFE_AREA

```TypeScript
SAFE_AREA = 2
```

Clip to the safe area configured for the component, corresponding to the entire yellow area in the figure.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
