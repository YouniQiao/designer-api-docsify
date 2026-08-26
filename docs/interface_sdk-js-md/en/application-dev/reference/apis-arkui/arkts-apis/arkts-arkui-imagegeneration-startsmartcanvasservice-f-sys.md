# startSmartCanvasService (System API)

## Modules to Import

```TypeScript
import imageGeneration from '@kit.ArkUI';
```

## startSmartCanvasService

```TypeScript
function startSmartCanvasService(
    context: common.ServiceExtensionContext | common.UIAbilityContext | common.UIExtensionContext): Promise<void>
```

Start the smart canvas service.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | common.ServiceExtensionContext \| common.UIAbilityContext \| common.UIExtensionContext | Yes | different ability context. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise & lt;void & gt; | Promise that returns no value. |
