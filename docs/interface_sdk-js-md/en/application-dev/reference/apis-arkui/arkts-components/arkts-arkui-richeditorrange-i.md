# RichEditorRange

Defines the range of the **RichEditor**.

**Since:** 10

<!--Device-unnamed-declare interface RichEditorRange--><!--Device-unnamed-declare interface RichEditorRange-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## end

```TypeScript
end?: number
```

End position of the span whose style needs to be updated. If this parameter is left empty or set to a value beyond the range, it indicates infinity.

**Type:** number

**Default:** text length

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RichEditorRange-end?: number--><!--Device-RichEditorRange-end?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## start

```TypeScript
start?: number
```

Start position of the span whose style needs to be updated. If this parameter is left empty or set to a negative value, the value **0** will be used.

**Type:** number

**Default:** 0

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RichEditorRange-start?: number--><!--Device-RichEditorRange-start?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

