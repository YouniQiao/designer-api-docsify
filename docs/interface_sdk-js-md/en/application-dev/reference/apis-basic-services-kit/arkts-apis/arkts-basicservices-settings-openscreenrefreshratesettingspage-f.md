# openScreenRefreshRateSettingsPage

## Modules to Import

```TypeScript
import { settings } from '@kit.BasicServicesKit';
import { settingsLite } from '@kit.BasicServicesKit';
```

## openScreenRefreshRateSettingsPage

```TypeScript
function openScreenRefreshRateSettingsPage(context: Context): void
```

Open the screen refresh rate settings page.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-settings-function openScreenRefreshRateSettingsPage(context: Context): void--><!--Device-settings-function openScreenRefreshRateSettingsPage(context: Context): void-End-->

**System capability:** SystemCapability.Applications.Settings.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes | Application context. Only UIAbilityContext and UIExtensionContext are supported. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16900010](../errorcode-settings.md#16900010-parameter-check-failed) | Parameter error. |
| [16900020](../errorcode-settings.md#16900020-failed-to-open-the-settings-page) | Failed to open the settings page via redirection. |

