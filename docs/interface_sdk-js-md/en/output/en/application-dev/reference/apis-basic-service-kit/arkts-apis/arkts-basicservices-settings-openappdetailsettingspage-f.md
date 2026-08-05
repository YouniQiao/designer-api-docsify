# openAppDetailSettingsPage

## openAppDetailSettingsPage

```TypeScript
function openAppDetailSettingsPage(context: Context, bundleName: string, appIndex?: int): void
```

Open the app detail settings page.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-settings-function openAppDetailSettingsPage(context: Context, bundleName: string, appIndex?: int): void--><!--Device-settings-function openAppDetailSettingsPage(context: Context, bundleName: string, appIndex?: int): void-End-->

**System capability:** SystemCapability.Applications.Settings.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Application context. Only UIAbilityContext and UIExtensionContext are supported. |
| bundleName | string | Yes | Application bundle name. |
| appIndex | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | No | Application index. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16900010](../../apis-basic-services-kit/errorcode-settings.md#16900010-parameter-check-failed) | Parameter error. |
| [16900020](../../apis-basic-services-kit/errorcode-settings.md#16900020-failed-to-open-the-settings-page) | Failed to open the settings page via redirection. |

