# openInputMethodDetail

## Modules to Import

```TypeScript
import { settings } from '@kit.BasicServicesKit';
```

## openInputMethodDetail

```TypeScript
function openInputMethodDetail(context: Context, bundleName: string, inputMethodId: string): void
```

Open the input method detail page.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-settings-function openInputMethodDetail(context: Context, bundleName: string, inputMethodId: string): void--><!--Device-settings-function openInputMethodDetail(context: Context, bundleName: string, inputMethodId: string): void-End-->

**System capability:** SystemCapability.Applications.Settings.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |
| bundleName | string | Yes |
| inputMethodId | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [16900010](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-settings.md#16900010-parameter-check-failed) |

## Examples

```TypeScript
import { settings } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Go to the input method details page.
// Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let bundleName: string = "target inputMethod bundle name";
let inputMethodId: string = "target inputMethod id";
settings.openInputMethodDetail(context, bundleName, inputMethodId);
```
