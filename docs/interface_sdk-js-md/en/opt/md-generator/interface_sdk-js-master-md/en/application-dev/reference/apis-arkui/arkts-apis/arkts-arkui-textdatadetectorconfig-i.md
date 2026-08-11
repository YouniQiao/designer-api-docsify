# TextDataDetectorConfig

This configuration is only available for the [Text](../../apis-arkgraphics2d/arkts-apis/arkts-graphics-text.md/arkts-graphics-text.md) and [RichEditor](./rich_editor) components.

**Since:** 11

<!--Device-unnamed-declare interface TextDataDetectorConfig--><!--Device-unnamed-declare interface TextDataDetectorConfig-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## color

```TypeScript
color?: ResourceColor
```

Color of the entity after successful text detection.

Default value: **'#ff0a59f7'**

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextDataDetectorConfig-color?: ResourceColor--><!--Device-TextDataDetectorConfig-color?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## decoration

```TypeScript
decoration?: DecorationStyleInterface
```

Decoration style of the entity after successful text detection.

Default value:

{

 type: TextDecorationType.Underline,

 color: same as the entity

 style: TextDecorationStyle.SOLID

}

**Type:** [DecorationStyleInterface](arkts-arkui-decorationstyleinterface-i.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextDataDetectorConfig-decoration?: DecorationStyleInterface--><!--Device-TextDataDetectorConfig-decoration?: DecorationStyleInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enablePreviewMenu

```TypeScript
enablePreviewMenu?: boolean
```

Whether to enable the preview menu displayed when long-pressing recognized text. The value **true** means to enable the preview menu, and **false** means the opposite.

Default value: **false**

When [copyOptions](RichEditorAttribute#copyOptions) is set to **None**, even if **enablePreviewMenu** is set to **true**, long-pressing AI entities will not display the preview menu.

This API can be properly called on phones and tablets, but has no effect on other devices such as PCs, 2-in-1devices, TVs, and wearables.

**Type:** boolean

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-TextDataDetectorConfig-enablePreviewMenu?: boolean--><!--Device-TextDataDetectorConfig-enablePreviewMenu?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onDetectResultUpdate

```TypeScript
onDetectResultUpdate?: Callback<string>
```

Callback invoked when text recognition succeeds.

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt;

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextDataDetectorConfig-onDetectResultUpdate?: Callback<string>--><!--Device-TextDataDetectorConfig-onDetectResultUpdate?: Callback<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## types

```TypeScript
types: TextDataDetectorType[]
```

Entity types for text recognition. Values **null** and **[]** indicate that all types of entities can be recognized.

**Type:** [TextDataDetectorType](arkts-arkui-textdatadetectortype-e.md)[]

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TextDataDetectorConfig-types: TextDataDetectorType[]--><!--Device-TextDataDetectorConfig-types: TextDataDetectorType[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
