# deactivateSceneAnimation (System API)

## Modules to Import

```TypeScript
import { formProvider } from 'kits/@kit.FormKit';
```

## deactivateSceneAnimation

```TypeScript
function deactivateSceneAnimation(formId: string): Promise<void>
```

Requests to deactivate a widget. This API takes effect only for   
[scene-based widgets](../../../form/arkts-ui-widget-configuration.md#sceneanimationparams-field). This API uses a promise to return the result. An interactive widget can be in the active or inactive state. In the inactive state, the widget is the same as a common widget. In the active state, the widget can start the   
**LiveFormExtensionAbility** process developed by the widget host to implement animations.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-formProvider-function deactivateSceneAnimation(formId: string): Promise<void>--><!--Device-formProvider-function deactivateSceneAnimation(formId: string): Promise<void>-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| formId | string | Yes | Widget ID. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 16501003 | The form cannot be operated by the current application. |
| 801 | Capability not supported.function deactivateSceneAnimation can not work correctly due to limited device capabilities. |
| 16501001 | The ID of the form to be operated does not exist. |
| 16501000 | An internal functional error occurred. |
| 16500060 | Service connection error. |
| 16501011 | The form cannot support this operation. |
| 16500050 | IPC connection error. |
| 202 | The application is not a system application. |
| 16500100 | Failed to obtain the configuration information. |

