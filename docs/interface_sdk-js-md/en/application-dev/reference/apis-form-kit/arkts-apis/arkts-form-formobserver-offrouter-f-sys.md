# offRouter (System API)

## Modules to Import

```TypeScript
import { formObserver } from 'formObserver';
```

## offRouter

```TypeScript
function offRouter(hostBundleName?: string, observerCallback?: Callback<formInfo.RunningFormInfo>): void
```

Unregister form router event Listening.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.OBSERVE_FORM_RUNNING

<!--Device-formObserver-function offRouter(hostBundleName?: string, observerCallback?: Callback<formInfo.RunningFormInfo>): void--><!--Device-formObserver-function offRouter(hostBundleName?: string, observerCallback?: Callback<formInfo.RunningFormInfo>): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| hostBundleName | string | No | Indicates the bundle name of the form host application. |
| observerCallback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;formInfo.RunningFormInfo&gt; | No | The callback is used to return the running form info. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permissions denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not a system application. |

