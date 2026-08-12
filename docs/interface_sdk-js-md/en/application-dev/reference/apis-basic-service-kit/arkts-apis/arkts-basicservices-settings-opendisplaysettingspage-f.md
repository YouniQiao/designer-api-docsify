# openDisplaySettingsPage

## Modules to Import

```TypeScript
import { settings } from '@kit.BasicServicesKit';
```

## openDisplaySettingsPage

```TypeScript
function openDisplaySettingsPage(context: Context): void
```

Open the display settings page.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-settings-function openDisplaySettingsPage(context: Context): void--><!--Device-settings-function openDisplaySettingsPage(context: Context): void-End-->

**System capability:** SystemCapability.Applications.Settings.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes | Application context. Only UIAbilityContext and UIExtensionContext are supported. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16900020](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-basic-services-kit/errorcode-settings.md#16900020-failed-to-open-the-settings-page) | Failed to open the settings page via redirection. |
| [16900010](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-basic-services-kit/errorcode-settings.md#16900010-parameter-check-failed) | Parameter error. |

