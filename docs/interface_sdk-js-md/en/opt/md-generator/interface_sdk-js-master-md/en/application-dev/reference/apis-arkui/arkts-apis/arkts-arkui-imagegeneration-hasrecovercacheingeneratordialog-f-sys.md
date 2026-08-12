# hasRecoverCacheInGeneratorDialog (System API)

## Modules to Import

```TypeScript
import { imageGeneration } from '@kit.ArkUI';
```

## hasRecoverCacheInGeneratorDialog

```TypeScript
function hasRecoverCacheInGeneratorDialog(uiContext: UIContext): boolean
```

Check whether cache files that can be restored exist in GeneratorDialog.The persistent cache file is used to store configuration parameters for AI image generation.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-imageGeneration-function hasRecoverCacheInGeneratorDialog(uiContext: UIContext): boolean--><!--Device-imageGeneration-function hasRecoverCacheInGeneratorDialog(uiContext: UIContext): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uiContext | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
