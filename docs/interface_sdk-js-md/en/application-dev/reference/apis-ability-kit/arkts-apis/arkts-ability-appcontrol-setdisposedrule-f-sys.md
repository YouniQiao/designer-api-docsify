# setDisposedRule (System API)

## Modules to Import

```TypeScript
import { appControl } from '@kit.AbilityKit';
```

## setDisposedRule

```TypeScript
function setDisposedRule(appId: string, rule: DisposedRule, appIndex?: int): void
```

Sets the disposed rule for an application or an application clone.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_DISPOSED_APP_STATUS

<!--Device-appControl-function setDisposedRule(appId: string, rule: DisposedRule, appIndex?: int): void--><!--Device-appControl-function setDisposedRule(appId: string, rule: DisposedRule, appIndex?: int): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.AppControl

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| appId | string | Yes | appId or appIdentifier of the target application. If a rule is set using appId, it overwrites the one set with appIdentifier, and the reverse is also true.<br>**NOTE：**<br> **appId** is the unique identifier of an application and is determined by the bundle name and signature information of the application. For details about how to obtain **appId**, see How do I obtain appId from application information .<br> [appIdentifier](arkts-ability-bundleinfo-signatureinfo-i.md) is also the unique identifier of an app. For details, see What is appIdentifier. For details about how to obtain **appIdentifier**, see How do I obtain appIdentifier from application information . |
| rule | [DisposedRule](arkts-ability-appcontrol-disposedrule-i-sys.md) | Yes | Disposed rule to set. |
| appIndex | int | No | Index of the application clone. The default value is **0**.<br> The value **0** means to set the disposed rule for the main application. A value greater than 0 means to set the disposed rule for the application clone with the specified index.<br>**Since:** 12 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [17700061](../errorcode-bundle.md#17700061-appindex-for-a-clone-is-invalid) | AppIndex is not in the valid range.<br>**Applicable version:** 12 and later |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied. A non-system application is not allowed to call a system API. |
| [17700005](../errorcode-bundle.md#17700005-appid-is-an-empty-string) | The specified app ID is invalid. |

