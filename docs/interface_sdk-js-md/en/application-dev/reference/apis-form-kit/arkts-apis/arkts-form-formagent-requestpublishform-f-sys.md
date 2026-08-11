# requestPublishForm (System API)

## Modules to Import

```TypeScript
import { formAgent } from 'kits/@kit.FormKit';
```

## requestPublishForm

```TypeScript
function requestPublishForm(want: Want, callback: AsyncCallback<string>): void
```

Requests to publish a widget to the widget host. This API uses an asynchronous callback to return the result. The widget host is usually the home screen.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.AGENT_REQUIRE_FORM

<!--Device-formAgent-function requestPublishForm(want: Want, callback: AsyncCallback<string>): void--><!--Device-formAgent-function requestPublishForm(want: Want, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | Publish request, which must contain the following fields: &lt;br&gt;**bundleName**: bundle name of the target widget. &lt;br&gt;**abilityName**: ability of the target widget. &lt;br&gt;parameters: &lt;br&gt;- **ohos.extra.param.key.form_dimension**: dimension of the target widget. &lt;br&gt;- **ohos.extra.param.key.form_name**: name of the target widget. &lt;br&gt;- **ohos.extra.param.key.module_name**: module name of the target widget. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | Callback used to return the widget ID. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;2.Incorrect parameter types; 3.Parameter verification failed. |
| [16501002](../errorcode-form.md#16501002-too-many-widgets) | The number of forms exceeds the upper limit.<br>**Applicable version:** 26.1.0 and later |
| 16501018 | This form does not support publishing.<br>**Applicable version:** 26.1.0 and later |
| 16501017 | There is no space to publish form.<br>**Applicable version:** 26.1.0 and later |
| [16501000](../errorcode-form.md#16501000-internal-function-error) | An internal functional error occurred. |
| [16500050](../errorcode-form.md#16500050-ipc-failure) | IPC connection error. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not a system application. |
| [16501008](../errorcode-form.md#16501008-adding-a-widget-to-the-home-screen-times-out) | Waiting for the form addition to the desktop timed out.<br>**Applicable version:** 12 and later |
| [16500100](../errorcode-form.md#16500100-failed-to-obtain-widget-configuration-information) | Failed to obtain the configuration information. |


## requestPublishForm

```TypeScript
function requestPublishForm(want: Want): Promise<string>
```

Requests to publish a widget to the widget host. This API uses a promise to return the result. The widget host is usually the home screen.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.AGENT_REQUIRE_FORM

<!--Device-formAgent-function requestPublishForm(want: Want): Promise<string>--><!--Device-formAgent-function requestPublishForm(want: Want): Promise<string>-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | Publish request, which must contain the following fields: &lt;br&gt;**bundleName**: bundle name of the target widget. &lt;br&gt;**abilityName**: ability of the target widget. &lt;br&gt;parameters: &lt;br&gt;- **ohos.extra.param.key.form_dimension**: dimension of the target widget. &lt;br&gt;- **ohos.extra.param.key.form_name**: name of the target widget. &lt;br&gt;- **ohos.extra.param.key.module_name**: module name of the target widget. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise used to return the widget ID. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| [16501002](../errorcode-form.md#16501002-too-many-widgets) | The number of forms exceeds the upper limit.<br>**Applicable version:** 26.1.0 and later |
| 16501018 | This form does not support publishing.<br>**Applicable version:** 26.1.0 and later |
| 16501017 | There is no space to publish form.<br>**Applicable version:** 26.1.0 and later |
| [16501000](../errorcode-form.md#16501000-internal-function-error) | An internal functional error occurred. |
| [16500050](../errorcode-form.md#16500050-ipc-failure) | IPC connection error. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not a system application. |
| [16501008](../errorcode-form.md#16501008-adding-a-widget-to-the-home-screen-times-out) | Waiting for the form addition to the desktop timed out.<br>**Applicable version:** 12 and later |
| [16500100](../errorcode-form.md#16500100-failed-to-obtain-widget-configuration-information) | Failed to obtain the configuration information. |

