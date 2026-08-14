# openDoubleClickSettingsPage

## Modules to Import

```TypeScript
import { settings } from 'settings';
```

## openDoubleClickSettingsPage

```TypeScript
function openDoubleClickSettingsPage(context: Context): void
```

1. Opens the settings page for double-pressing the Down key. 2. This API is used to set the default application started by double-pressing the Down key.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-settings-function openDoubleClickSettingsPage(context: Context): void--><!--Device-settings-function openDoubleClickSettingsPage(context: Context): void-End-->

**System capability:** SystemCapability.Applications.Settings.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes | 1. Application context. 2. Specify this parameter to set the application started by double-pressing the Down key. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16900020](../../apis-basic-services-kit/errorcode-settings.md#16900020-failed-to-open-the-settings-page) | 1. The setting page cannot be opened through redirection. 2. Internal error |
| [16900010](../../apis-basic-services-kit/errorcode-settings.md#16900010-parameter-check-failed) | 1. The parameter is incorrect. 2. The parameter is not transferred or the transferred parameter is invalid. |

