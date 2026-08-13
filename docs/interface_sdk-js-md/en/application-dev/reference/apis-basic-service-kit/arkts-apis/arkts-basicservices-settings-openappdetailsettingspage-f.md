# openAppDetailSettingsPage

## Modules to Import

```TypeScript
import { settings } from '@kit.BasicServicesKit';
```

## openAppDetailSettingsPage

```TypeScript
function openAppDetailSettingsPage(context: Context, bundleName: string, appIndex?: int): void
```

Open the app detail settings page.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-settings-function openAppDetailSettingsPage(context: Context, bundleName: string, appIndex?: int): void--><!--Device-settings-function openAppDetailSettingsPage(context: Context, bundleName: string, appIndex?: int): void-End-->

**System capability:** SystemCapability.Applications.Settings.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes | Application context. Only UIAbilityContext and UIExtensionContext are supported. |
| bundleName | string | Yes | Application bundle name. |
| appIndex | int | No | Application index. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16900020](../../apis-basic-services-kit/errorcode-settings.md#16900020-failed-to-open-the-settings-page) | Failed to open the settings page via redirection. |
| [16900010](../../apis-basic-services-kit/errorcode-settings.md#16900010-parameter-check-failed) | Parameter error. |

