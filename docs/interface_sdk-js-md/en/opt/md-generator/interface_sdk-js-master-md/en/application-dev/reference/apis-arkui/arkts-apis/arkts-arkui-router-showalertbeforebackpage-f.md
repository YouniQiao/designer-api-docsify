# showAlertBeforeBackPage

## Modules to Import

```TypeScript
import { router } from '@kit.ArkUI';
```

## showAlertBeforeBackPage

```TypeScript
function showAlertBeforeBackPage(options: EnableAlertOptions): void
```

Enables the display of a confirm dialog box before returning to the previous page.

> **NOTE：**
> 
> - Since API version 10, you can use the
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
> [UIContext](@ohos.arkui.UIContext) to obtain the [Router](@ohos.arkui.UIContext) object associated
> with the current UI context.

**Since:** 9

**Deprecated since:** 18

**Substitutes:** [showAlertBeforeBackPage](arkts-arkui-arkui-uicontext-router-c.md#showAlertBeforeBackPage)

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-router-function showAlertBeforeBackPage(options: EnableAlertOptions): void--><!--Device-router-function showAlertBeforeBackPage(options: EnableAlertOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [EnableAlertOptions](arkts-arkui-router-enablealertoptions-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [100001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-internal.md#100001-internal-error) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  this.getUIContext().getRouter().showAlertBeforeBackPage({
    message: 'Message Info'
  });
} catch (err) {
  console.error(`showAlertBeforeBackPage failed. Code: ${(err as BusinessError).code}, message: ${(err as BusinessError).message}`);
}
```
