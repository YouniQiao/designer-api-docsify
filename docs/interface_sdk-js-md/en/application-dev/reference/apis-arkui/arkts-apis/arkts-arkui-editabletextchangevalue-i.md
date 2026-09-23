# EditableTextChangeValue

```TypeScript
interface EditableTextChangeValue
```

Provides detailed information of text changes, including preview text.

**Since:** 15

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## content

```TypeScript
content: string
```

Current text content.

**Type:** string

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## options

```TypeScript
options?: TextChangeOptions
```

Changed text content information.

Default value: undefined.

**Type:** [TextChangeOptions](arkts-arkui-textchangeoptions-i.md)

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## previewText

```TypeScript
previewText?: PreviewText
```

Preview text content information.

Default value: undefined, indicating no preview text content.

**Type:** [PreviewText](arkts-arkui-previewtext-i.md)

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
