# getState

## Modules to Import

```TypeScript
import { router } from '@kit.ArkUI';
```

## getState

```TypeScript
function getState(): RouterState
```

Obtains state information about the page at the top of the navigation stack. > **NOTE：**> > - Since API version 10, you can use the > [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in > [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md#UIContext) to obtain the [Router](arkts-arkui-arkui-uicontext-uicontext-c.md#UIContext) object associated > with the current UI context.

**Since:** 8

**Deprecated since:** 18

**Substitutes:** [getState](arkts-arkui-arkui-uicontext-router-c.md#getState)

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-router-function getState(): RouterState--><!--Device-router-function getState(): RouterState-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RouterState](arkts-arkui-router-routerstate-i.md) |

## Examples

```TypeScript
let page = this.getUIContext().getRouter().getState();
console.info('current index = ' + page.index);
console.info('current name = ' + page.name);
console.info('current path = ' + page.path);
```
