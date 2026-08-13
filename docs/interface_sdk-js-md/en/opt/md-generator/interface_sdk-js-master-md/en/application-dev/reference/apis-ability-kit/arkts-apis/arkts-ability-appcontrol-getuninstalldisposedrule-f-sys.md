# getUninstallDisposedRule (System API)

## Modules to Import

```TypeScript
import { appControl } from '@kit.AbilityKit';
```

## getUninstallDisposedRule

```TypeScript
function getUninstallDisposedRule(appIdentifier: string, appIndex?: number): UninstallDisposedRule
```

Obtains the uninstallation disposed rule of an application or an application clone.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_DISPOSED_APP_STATUS or ohos.permission.MANAGE_DISPOSED_APP_STATUS

<!--Device-appControl-function getUninstallDisposedRule(appIdentifier: string, appIndex?: int): UninstallDisposedRule--><!--Device-appControl-function getUninstallDisposedRule(appIdentifier: string, appIndex?: int): UninstallDisposedRule-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.AppControl

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| appIdentifier | string | Yes |
| appIndex | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [UninstallDisposedRule](arkts-ability-appcontrol-uninstalldisposedrule-i-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [17700061](../errorcode-bundle.md#17700061-appindex-for-a-clone-is-invalid) |
| [17700074](../errorcode-bundle.md#17700074-invalid-appidentifier) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
