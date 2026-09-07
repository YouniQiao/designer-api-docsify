# disableAlertBeforeBackPage

## Modules to Import

```TypeScript
import { router } from '@kit.ArkUI';
```

## disableAlertBeforeBackPage

```TypeScript
function disableAlertBeforeBackPage(): void
```

Disables the display of a confirm dialog box before returning to the previous page.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [hideAlertBeforeBackPage](arkts-arkui-arkui-uicontext-router-c.md#hidealertbeforebackpage)

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Examples**

disableAlertBeforeBackPage(): void

```TypeScript
import { router } from '@kit.ArkUI';

router.disableAlertBeforeBackPage();
```
