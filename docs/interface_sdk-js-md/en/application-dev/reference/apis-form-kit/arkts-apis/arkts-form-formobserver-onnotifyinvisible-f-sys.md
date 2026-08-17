# onNotifyInvisible (System API)

## Modules to Import

```TypeScript
import { formObserver } from 'formObserver';
```

## onNotifyInvisible

```TypeScript
function onNotifyInvisible(observerCallback: Callback<Array<formInfo.RunningFormInfo>>): void
```

Listens to the event of notifyInvisible type change. &lt;p&gt;You can use this method to listen to the event of notifyInvisible type change.&lt;/p&gt;

**Since:** 23

**Required permissions:** ohos.permission.OBSERVE_FORM_RUNNING

<!--Device-formObserver-function onNotifyInvisible(observerCallback: Callback<Array<formInfo.RunningFormInfo>>): void--><!--Device-formObserver-function onNotifyInvisible(observerCallback: Callback<Array<formInfo.RunningFormInfo>>): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| observerCallback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;formInfo.RunningFormInfo&gt;&gt; | Yes | The callback is used to return the running form info. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permissions denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not a system application. |


## onNotifyInvisible

```TypeScript
function onNotifyInvisible(
    hostBundleName: string,
    observerCallback: Callback<Array<formInfo.RunningFormInfo>>
  ): void
```

Listens to the event of notifyInvisible type change. &lt;p&gt;You can use this method to listen to the event of notifyInvisible type change for a particular card host.&lt;/p&gt;

**Since:** 23

**Required permissions:** ohos.permission.OBSERVE_FORM_RUNNING

<!--Device-formObserver-function onNotifyInvisible(    hostBundleName: string,    observerCallback: Callback<Array<formInfo.RunningFormInfo>>  ): void--><!--Device-formObserver-function onNotifyInvisible(    hostBundleName: string,    observerCallback: Callback<Array<formInfo.RunningFormInfo>>  ): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| hostBundleName | string | Yes | Indicates the bundle name of the form host application. |
| observerCallback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;formInfo.RunningFormInfo&gt;&gt; | Yes | The callback is used to return the running form info. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permissions denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not a system application. |

