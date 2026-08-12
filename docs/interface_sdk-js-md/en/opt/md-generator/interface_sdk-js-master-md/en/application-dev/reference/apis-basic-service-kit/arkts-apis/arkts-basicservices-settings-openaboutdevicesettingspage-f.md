# openAboutDeviceSettingsPage

## Modules to Import

```TypeScript
import { settings } from '@kit.BasicServicesKit';
```

## openAboutDeviceSettingsPage

```TypeScript
function openAboutDeviceSettingsPage(context: Context): void
```

Open the about device settings page.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-settings-function openAboutDeviceSettingsPage(context: Context): void--><!--Device-settings-function openAboutDeviceSettingsPage(context: Context): void-End-->

**System capability:** SystemCapability.Applications.Settings.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [16900020](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-settings.md#16900020-failed-to-open-the-settings-page) |
| [16900010](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-settings.md#16900010-parameter-check-failed) |

## Examples

```TypeScript
import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
try {
  settings.openAboutDeviceSettingsPage(context);
} catch (err) {
  console.error(`Failed to open the about device settings page. code: ${err?.code}, message: ${err?.message}`);
}
```
