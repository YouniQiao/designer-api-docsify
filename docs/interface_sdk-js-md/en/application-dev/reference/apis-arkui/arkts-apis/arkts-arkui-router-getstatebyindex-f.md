# getStateByIndex

## Modules to Import

```TypeScript
import { router } from '@kit.ArkUI';
```

## getStateByIndex

```TypeScript
function getStateByIndex(index: number): RouterState | undefined
```

Obtains the status information about a page by its index.

> **NOTE：**
> 
> - Since API version 12, you can use the &gt; [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in &gt; [UIContext](../../apis-default/arkts-apis/arkts-arkui-uicontext-uicontext-c.md) to obtain the [Router](../../apis-default/arkts-apis/arkts-arkui-uicontext-uicontext-c.md) object associated &gt; with the current UI context.

**Since:** 12

**Deprecated since:** 18

**Substitutes:** [getStateByIndex](../../apis-default/arkts-apis/arkts-arkui-uicontext-router-c.md#getstatebyindex)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-router-function getStateByIndex(index: number): RouterState | undefined--><!--Device-router-function getStateByIndex(index: number): RouterState | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | number | Yes | Index of the target page. The index starts from 1 from the bottom to the top of the stack. |

**Return value:**

| Type | Description |
| --- | --- |
| RouterState \| undefined | State information about the target page; **undefined** if the specified index does not exist. |

**Examples**

```TypeScript
let options: router.RouterState | undefined = router.getStateByIndex(1);
if (options != undefined) {
  console.info('index = ' + options.index);
  console.info('name = ' + options.name);
  console.info('path = ' + options.path);
  console.info(`params = ${JSON.stringify(options.params)}`);
}
```

