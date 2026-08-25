# openDoubleClickSettingsPage

## Modules to Import

```TypeScript
import { settings } from 'kits/@kit.BasicServicesKit';
```

## openDoubleClickSettingsPage

```TypeScript
function openDoubleClickSettingsPage(context: Context): void
```

1. Opens the settings page for number-pressing the Down key.
2. This API is used to set the default application started by number-pressing the Down key.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Applications.Settings.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [16900010](../errorcode-settings.md#16900010-parameter-check-failed) |
| [16900020](../errorcode-settings.md#16900020-failed-to-open-the-settings-page) |
