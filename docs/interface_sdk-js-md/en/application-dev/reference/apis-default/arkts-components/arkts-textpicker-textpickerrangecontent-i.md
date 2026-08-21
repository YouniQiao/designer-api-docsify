# TextPickerRangeContent

Define the contents of each selector item.

@interface TextPickerRangeContent

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface TextPickerRangeContent--><!--Device-unnamed-export declare interface TextPickerRangeContent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## icon

```TypeScript
icon: string | Resource
```

Image resource. If the value is a string, such as **"/common/hello.png"**, it represents the path to the image.

**Type:** string \| [Resource](../../apis-arkui/arkts-apis/arkts-arkui-resource-t.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerRangeContent-icon: string | Resource--><!--Device-TextPickerRangeContent-icon: string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## text

```TypeScript
text?: string | Resource
```

Text information.

<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>If the text length exceeds the column width, the text will be truncated. </p>

**Type:** string \| [Resource](../../apis-arkui/arkts-apis/arkts-arkui-resource-t.md)

**Default:** ""

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextPickerRangeContent-text?: string | Resource--><!--Device-TextPickerRangeContent-text?: string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

