# showGeneratorDialog (System API)

## Modules to Import

```TypeScript
import { imageGeneration } from 'kits/@kit.ArkUI';
```

## showGeneratorDialog

```TypeScript
function showGeneratorDialog(uiContext: UIContext, options?: GeneratorDialogOptions): Promise<Array<GeneratorResult>>
```

Open the AI image generation task popup and perform AI image generation operations.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-imageGeneration-function showGeneratorDialog(uiContext: UIContext, options?: GeneratorDialogOptions): Promise<Array<GeneratorResult>>--><!--Device-imageGeneration-function showGeneratorDialog(uiContext: UIContext, options?: GeneratorDialogOptions): Promise<Array<GeneratorResult>>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uiContext | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c-sys.md) | Yes |
| options | [GeneratorDialogOptions](arkts-arkui-imagegeneration-generatordialogoptions-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;GeneratorResult&gt;&gt; |
