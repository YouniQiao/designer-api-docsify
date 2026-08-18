# cancelApplicationAutoStartup (System API)

## Modules to Import

```TypeScript
```

## cancelApplicationAutoStartup

```TypeScript
function cancelApplicationAutoStartup(info: AutoStartupInfo, callback: AsyncCallback<void>): void
```

Cancels the auto-startup setting for an application component. This API uses an asynchronous callback to return the result. Starting from API version 18, this API can be properly called on 2-in-1 devices and wearables. If it is called on other device types, error code 16000050 is returned. For versions earlier than API version 18, this API can be properly called only on 2-in-1 devices. If it is called on other device types, error code 16000050 is returned.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_APP_BOOT

**Model restriction:** This API can be used only in the stage model.

<!--Device-autoStartupManager-function cancelApplicationAutoStartup(info: AutoStartupInfo, callback: AsyncCallback<void>): void--><!--Device-autoStartupManager-function cancelApplicationAutoStartup(info: AutoStartupInfo, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| info | [AutoStartupInfo](arkts-ability-autostartupinfo-i-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [16000004](../errorcode-ability.md#16000004-visibility-verification-failure) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16000013](../errorcode-ability.md#16000013-application-controlled-by-edm) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |


## cancelApplicationAutoStartup

```TypeScript
function cancelApplicationAutoStartup(info: AutoStartupInfo): Promise<void>
```

Cancels the auto-startup setting for an application component. This API uses a promise to return the result. Starting from API version 18, this API can be properly called on 2-in-1 devices and wearables. If it is called on other device types, error code 16000050 is returned. For versions earlier than API version 18, this API can be properly called only on 2-in-1 devices. If it is called on other device types, error code 16000050 is returned.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_APP_BOOT

**Model restriction:** This API can be used only in the stage model.

<!--Device-autoStartupManager-function cancelApplicationAutoStartup(info: AutoStartupInfo): Promise<void>--><!--Device-autoStartupManager-function cancelApplicationAutoStartup(info: AutoStartupInfo): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| info | [AutoStartupInfo](arkts-ability-autostartupinfo-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000004](../errorcode-ability.md#16000004-visibility-verification-failure) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16000013](../errorcode-ability.md#16000013-application-controlled-by-edm) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
