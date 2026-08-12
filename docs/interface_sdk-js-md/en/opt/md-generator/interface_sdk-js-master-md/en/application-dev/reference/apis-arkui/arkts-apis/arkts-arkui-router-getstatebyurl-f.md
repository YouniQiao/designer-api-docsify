# getStateByUrl

## Modules to Import

```TypeScript
import { router } from '@kit.ArkUI';
```

## getStateByUrl

```TypeScript
function getStateByUrl(url: string): Array<RouterState>
```

Obtains the status information about a page by its URL.

> **NOTE：**
> 
> - Since API version 12, you can use the
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
> [UIContext](@ohos.arkui.UIContext) to obtain the [Router](@ohos.arkui.UIContext) object associated
> with the current UI context.

**Since:** 12

**Deprecated since:** 18

**Substitutes:** [getStateByUrl](arkts-arkui-arkui-uicontext-router-c.md#getStateByUrl)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-router-function getStateByUrl(url: string): Array<RouterState>--><!--Device-router-function getStateByUrl(url: string): Array<RouterState>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;RouterState & gt; |

## Examples

```TypeScript
import { router } from '@kit.ArkUI';

let options: Array<router.RouterState> = router.getStateByUrl('pages/index');
for (let i: number = 0; i < options.length; i++) {
  console.info('index = ' + options[i].index);
  console.info('name = ' + options[i].name);
  console.info('path = ' + options[i].path);
  console.info('params = ' + options[i].params);
}
```
