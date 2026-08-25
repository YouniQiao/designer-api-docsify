# deactivateSceneAnimation (System API)

## Modules to Import

```TypeScript
import { formProvider } from 'kits/@kit.FormKit';
```

## deactivateSceneAnimation

```TypeScript
function deactivateSceneAnimation(formId: string): Promise<void>
```

Requests to deactivate a widget. This API takes effect only for [scene-based widgets](../../../form/arkts-ui-widget-configuration.md#sceneanimationparams-field). This API uses a promise to return the result. An interactive widget can be in the active or inactive state. In the inactive state, the widget is the same as a common widget. In the active state, the widget can start the **LiveFormExtensionAbility** process developed by the widget host to implement animations.

**Since:** 20

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [16500050](../errorcode-form.md#16500050-ipc-failure) |
| [16500060](../errorcode-form.md#16500060-service-connection-failure) |
| [16500100](../errorcode-form.md#16500100-failed-to-obtain-widget-configuration-information) |
| [16501000](../errorcode-form.md#16501000-internal-function-error) |
| [16501001](../errorcode-form.md#16501001-widget-id-not-exist) |
| [16501003](../errorcode-form.md#16501003-widget-not-operatable) |
| [16501011](../errorcode-form.md#16501011-api-not-supported) |
