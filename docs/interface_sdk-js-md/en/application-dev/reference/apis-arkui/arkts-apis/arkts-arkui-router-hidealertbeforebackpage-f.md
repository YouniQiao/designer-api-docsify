# hideAlertBeforeBackPage

## Modules to Import

```TypeScript
import { router } from 'kits/@kit.ArkUI';
```

## hideAlertBeforeBackPage

```TypeScript
function hideAlertBeforeBackPage(): void
```

Disables the display of a confirm dialog box before returning to the previous page.

> **NOTE：**
> 
> - Since API version 10, you can use the
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
> [UIContext](arkts-arkui-uicontext.md) to obtain the [Router](arkts-arkui-uicontext.md) object associated
> with the current UI context.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 18

**Substitutes:** [@ohos.arkui.UIContext:Router#hideAlertBeforeBackPage](arkts-arkui-arkui-uicontext-router-c.md#hidealertbeforebackpage)

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-router-function hideAlertBeforeBackPage(): void--><!--Device-router-function hideAlertBeforeBackPage(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Examples

```TypeScript
this.getUIContext().getRouter().hideAlertBeforeBackPage();
```

