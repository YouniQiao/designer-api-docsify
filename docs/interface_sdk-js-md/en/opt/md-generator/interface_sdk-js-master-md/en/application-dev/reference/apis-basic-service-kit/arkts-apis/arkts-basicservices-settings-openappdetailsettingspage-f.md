# openAppDetailSettingsPage

## Modules to Import

```TypeScript
import { settings } from '@kit.BasicServicesKit';
```

## openAppDetailSettingsPage

```TypeScript
function openAppDetailSettingsPage(context: Context, bundleName: string, appIndex?: number): void
```

Open the app detail settings page.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-settings-function openAppDetailSettingsPage(context: Context, bundleName: string, appIndex?: int): void--><!--Device-settings-function openAppDetailSettingsPage(context: Context, bundleName: string, appIndex?: int): void-End-->

**System capability:** SystemCapability.Applications.Settings.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |
| bundleName | string | Yes |
| appIndex | number | No |

**Error codes:**

| Error Code ID |
| --- |
| [16900020](../../apis-basic-services-kit/errorcode-settings.md#16900020-failed-to-open-the-settings-page) |
| [16900010](../../apis-basic-services-kit/errorcode-settings.md#16900010-parameter-check-failed) |

## Examples

```TypeScript
import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
try {
  settings.openAppDetailSettingsPage(context, 'com.example');
} catch (err) {
  console.error(`Failed to open the app detail settings page. code: ${err?.code}, message: ${err?.message}`);
}
```
