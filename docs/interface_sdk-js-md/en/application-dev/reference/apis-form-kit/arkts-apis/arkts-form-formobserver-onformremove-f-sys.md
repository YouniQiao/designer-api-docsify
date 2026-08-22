# onFormRemove (System API)

## Modules to Import

```TypeScript
import { formObserver } from '@kit.FormKit';
```

## onFormRemove

```TypeScript
function onFormRemove(observerCallback: Callback<formInfo.RunningFormInfo>): void
```

Listens to the event of remove form. <p>You can use this method to listen to the event of remove form.</p>

**Since:** 23

**Required permissions:** ohos.permission.OBSERVE_FORM_RUNNING

<!--Device-formObserver-function onFormRemove(observerCallback: Callback<formInfo.RunningFormInfo>): void--><!--Device-formObserver-function onFormRemove(observerCallback: Callback<formInfo.RunningFormInfo>): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| observerCallback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;formInfo.RunningFormInfo&gt; | Yes | The callback is used to return the running form info. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permissions denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not a system application. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |


## onFormRemove

```TypeScript
function onFormRemove(hostBundleName: string, observerCallback: Callback<formInfo.RunningFormInfo>): void
```

Listens to the event of remove form. <p>You can use this method to listen to the event of remove form for a particular card host.</p>

**Since:** 23

**Required permissions:** ohos.permission.OBSERVE_FORM_RUNNING

<!--Device-formObserver-function onFormRemove(hostBundleName: string, observerCallback: Callback<formInfo.RunningFormInfo>): void--><!--Device-formObserver-function onFormRemove(hostBundleName: string, observerCallback: Callback<formInfo.RunningFormInfo>): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| hostBundleName | string | Yes | Indicates the bundle name of the form host application. |
| observerCallback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;formInfo.RunningFormInfo&gt; | Yes | The callback is used to return the running form info. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permissions denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not a system application. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |

