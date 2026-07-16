# UndoStyle

Enumerates the options for whether to retain the original style during undo/redo operations.

**Since:** 20

<!--Device-unnamed-declare enum UndoStyle--><!--Device-unnamed-declare enum UndoStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## CLEAR_STYLE

```TypeScript
CLEAR_STYLE = 0
```

Undo/Redo operations do not retain the original style.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-UndoStyle-CLEAR_STYLE = 0--><!--Device-UndoStyle-CLEAR_STYLE = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## KEEP_STYLE

```TypeScript
KEEP_STYLE = 1
```

Undo/Redo operations retain the original style.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-UndoStyle-KEEP_STYLE = 1--><!--Device-UndoStyle-KEEP_STYLE = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

