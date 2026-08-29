# requestPublishFormCrossDevice (System API)

## Modules to Import

```TypeScript
import { formAgent } from '@kit.FormKit';
```

## requestPublishFormCrossDevice

```TypeScript
function requestPublishFormCrossDevice(peerServiceInfo: formInfo.PeerFormHostServiceInfo, want: Want,
    formBindingData?: formBindingData.FormBindingData): Promise<formInfo.PublishFormCrossDeviceResult>
```

Requests to publish a form to the form host service of the remote device.

**Since:** 26.1.0

**Required permissions:** ohos.permission.AGENT_REQUIRE_FORM

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| peerServiceInfo | formInfo.PeerFormHostServiceInfo | Yes | The peer form host service information. |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | Publish request, which must contain the following fields:    **bundleName**: bundle name of the target form.    **abilityName**: ability of the target form. parameters:    - **ohos.extra.param.key.form_dimension**: dimension of the target form.    - **ohos.extra.param.key.form_name**: name of the target form.    - **ohos.extra.param.key.module_name**: module name of the target form. |
| formBindingData | formBindingData.FormBindingData | No | Data to be used for the update. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;formInfo.PublishFormCrossDeviceResult&gt; | Promise used to return the result of publishing the form across device. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permissions denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not a system application. |
| [16500050](../errorcode-form.md#16500050-ipc-failure) | IPC connection error. |
| 16501020 | Remote form service is unavailable. |
| 16501021 | The peer form application is not installed or the version is too old. |
| [16501002](../errorcode-form.md#16501002-too-many-widgets) | The number of forms exceeds the maximum allowed. |
| 16501017 | There is no space to publish the form. |
| 16501018 | This form does not support publishing. |
