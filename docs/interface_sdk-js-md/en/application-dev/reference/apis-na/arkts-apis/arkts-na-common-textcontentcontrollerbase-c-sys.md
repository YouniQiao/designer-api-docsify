# TextContentControllerBase

TextContentControllerBase

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare abstract class TextContentControllerBase--><!--Device-unnamed-export declare abstract class TextContentControllerBase-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getText

```TypeScript
getText(range?: TextRange): string | undefined
```

Gets the text content of the selected range.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TextContentControllerBase-getText(range?: TextRange): string | undefined--><!--Device-TextContentControllerBase-getText(range?: TextRange): string | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| range | [TextRange](../../apis-arkui/arkts-apis/arkts-arkui-textcommon-textrange-i.md) | No | selected range. |

**Return value:**

| Type | Description |
| --- | --- |
| string \| undefined | text content of the selected range. |

