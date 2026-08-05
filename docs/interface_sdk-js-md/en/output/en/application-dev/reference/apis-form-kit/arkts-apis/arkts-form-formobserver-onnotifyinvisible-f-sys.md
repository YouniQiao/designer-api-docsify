# onNotifyInvisible (System API)

## onNotifyInvisible

```TypeScript
function onNotifyInvisible(observerCallback: Callback<Array<formInfo.RunningFormInfo>>): void
```

Listens to the event of notifyInvisible type change. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_You can use this method to listen to the event of notifyInvisible type change.\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.OBSERVE_FORM_RUNNING

<!--Device-formObserver-function onNotifyInvisible(observerCallback: Callback<Array<formInfo.RunningFormInfo>>): void--><!--Device-formObserver-function onNotifyInvisible(observerCallback: Callback<Array<formInfo.RunningFormInfo>>): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| observerCallback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Array&lt;formInfo.RunningFormInfo&gt;&gt; | Yes | The callback is used to return the running form info. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permissions denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not a system application. |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |


## onNotifyInvisible

```TypeScript
function onNotifyInvisible(
    hostBundleName: string,
    observerCallback: Callback<Array<formInfo.RunningFormInfo>>
  ): void
```

Listens to the event of notifyInvisible type change. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_You can use this method to listen to the event of notifyInvisible type change for a particular card host.\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.OBSERVE_FORM_RUNNING

<!--Device-formObserver-function onNotifyInvisible(    hostBundleName: string,    observerCallback: Callback<Array<formInfo.RunningFormInfo>>  ): void--><!--Device-formObserver-function onNotifyInvisible(    hostBundleName: string,    observerCallback: Callback<Array<formInfo.RunningFormInfo>>  ): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| hostBundleName | string | Yes | Indicates the bundle name of the form host application. |
| observerCallback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Array&lt;formInfo.RunningFormInfo&gt;&gt; | Yes | The callback is used to return the running form info. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permissions denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | The application is not a system application. |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |

