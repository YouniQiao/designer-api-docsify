# activateSceneAnimation (System API)

## Modules to Import

```TypeScript
import { formProvider } from '@kit.FormKit';
```

## activateSceneAnimation

```TypeScript
function activateSceneAnimation(formId: string): Promise<void>
```

Requests to activate a widget. This API takes effect only for   
[scene-based widgets](../../../form/arkts-ui-widget-configuration.md#sceneanimationparams-field). This API uses a promise to return the result. An interactive widget can be in the active or inactive state. In the inactive state, the widget is the same as a common widget. In the active state, the widget can start the   
**LiveFormExtensionAbility** process developed by the widget host to implement animations.

**Since:** 20

<!--Device-formProvider-function activateSceneAnimation(formId: string): Promise<void>--><!--Device-formProvider-function activateSceneAnimation(formId: string): Promise<void>-End-->

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
| [16501003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16501003-widget-not-operatable) |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [16501001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16501001-widget-id-not-exist) |
| [16501000](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16501000-internal-function-error) |
| [16500060](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16500060-service-connection-failure) |
| [16501011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16501011-api-not-supported) |
| [16500050](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16500050-ipc-failure) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16500100](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16500100-failed-to-obtain-widget-configuration-information) |
