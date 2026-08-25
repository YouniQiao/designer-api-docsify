# getStateByUrl

## Modules to Import

```TypeScript
import { router } from 'kits/@kit.ArkUI';
```

## getStateByUrl

```TypeScript
function getStateByUrl(url: string): Array<RouterState>
```

Obtains the status information about a page by its URL.

> **NOTE：**&gt;
> - Since API version 12, you can use the
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
> [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) to obtain the [Router](arkts-arkui-arkui-uicontext-uicontext-c.md) object associated
> with the current UI context.

**Since:** 12

**Deprecated since:** 18

**Substitutes:** [getStateByUrl](arkts-arkui-arkui-uicontext-router-c.md#getstatebyurl)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;RouterState & gt; |
