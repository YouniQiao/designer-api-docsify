# hideGeneratorDialog (System API)

## Modules to Import

```TypeScript
import { imageGeneration } from '@kit.ArkUI';
```

## hideGeneratorDialog

```TypeScript
function hideGeneratorDialog(uiContext: UIContext): Promise<void>
```

Hide the AI image generation task popup.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-imageGeneration-function hideGeneratorDialog(uiContext: UIContext): Promise<void>--><!--Device-imageGeneration-function hideGeneratorDialog(uiContext: UIContext): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uiContext | [UIContext](../../apis-na/arkts-apis/arkts-na-arkui-uicontext-uicontext-c.md) | Yes | The context of dialog for ui display. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Returns the result of close operation. |

