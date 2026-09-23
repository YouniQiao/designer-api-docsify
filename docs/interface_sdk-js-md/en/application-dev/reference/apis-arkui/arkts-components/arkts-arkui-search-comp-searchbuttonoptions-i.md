# SearchButtonOptions

```TypeScript
interface SearchButtonOptions
```

Defines the SearchButton options.

**Since:** 10

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## autoDisable

```TypeScript
autoDisable?: Boolean
```

Whether the button is grayed out and not clickable when the Search component has no text content.

Default value: false

true indicates that the button graying-out feature is enabled, and false indicates that it is not enabled.

**Type:** Boolean

**Default:** false

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontColor

```TypeScript
fontColor?: ResourceColor
```

Font color of the text button. **Atomic service API:** This API is supported in atomic services since API version 11.

**Type:** [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md)

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontSize

```TypeScript
fontSize?: Length
```

Font size of the text button. If no unit is specified, the default unit is vp. Percentage is not supported. If a percentage is passed in, it does not take effect.

Default value: follows the theme. **Atomic service API:** This API is supported in atomic services since API version 11.

**Type:** [Length](../arkts-apis/arkts-arkui-length-t.md)

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
