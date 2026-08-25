# setKeepAliveForBundle (System API)

## Modules to Import

```TypeScript
import { appManager } from 'kits/@kit.AbilityKit';
```

## setKeepAliveForBundle

```TypeScript
function setKeepAliveForBundle(bundleName: string, userId: number, enable: boolean): Promise<void>
```

Sets or cancels the keep-alive status for an application that belongs to a specified user. This API uses a promise to return the result. Starting from API version 18, this API can be properly called only on 2-in-1 devices and wearables. For versions earlier than API version 18, this API can be properly called only on 2-in-1 devices. If it is called on other device types, error code 801 is returned.

> **NOTE：**&gt;
> - To support keep-alive, **mainElement** in the
> [module.json5](../../../quick-start/module-configuration-file.md) file of the application must be a UIAbility.
> The system initiates the keep-alive operation only when this mainElement has been launched.&gt;
> - On 2-in-1 devices, the application must appear in the status bar within 5 seconds of launch. Otherwise, the
> system revokes the application's keep-alive status and terminate the restarted process.&gt;
> - When the kept-alive application process exits, the system attempts to restart it. If three consecutive restart
> attempts fail, the system stops restarting the process.

**Since:** 14

**Required permissions:** ohos.permission.MANAGE_APP_KEEP_ALIVE

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| userId | number | Yes |
| enable | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [16300005](../errorcode-ability.md#16300005-bundle-information-does-not-exist) |
| [16300008](../errorcode-ability.md#16300008-specified-package-does-not-have-a-main-uiability) |
| [16300009](../errorcode-ability.md#16300009-specified-package-does-not-have-a-status-bar) |
| [16300010](../errorcode-ability.md#16300010-running-application-is-not-attached-to-a-status-bar) |
