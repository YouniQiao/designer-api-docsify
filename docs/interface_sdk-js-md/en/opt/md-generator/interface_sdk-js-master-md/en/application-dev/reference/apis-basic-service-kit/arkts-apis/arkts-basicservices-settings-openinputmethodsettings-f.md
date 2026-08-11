# openInputMethodSettings

## Modules to Import

```TypeScript
import { settings } from 'kits/@kit.BasicServicesKit';
```

## openInputMethodSettings

```TypeScript
function openInputMethodSettings(context: Context): void
```

Open the input method settings page.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-settings-function openInputMethodSettings(context: Context): void--><!--Device-settings-function openInputMethodSettings(context: Context): void-End-->

**System capability:** SystemCapability.Applications.Settings.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [16900010](../../apis-basic-services-kit/errorcode-settings.md#16900010-parameter-check-failed) |

## Examples

```TypeScript
import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Go to the input method settings page.
// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
settings.openInputMethodSettings(context);
```
