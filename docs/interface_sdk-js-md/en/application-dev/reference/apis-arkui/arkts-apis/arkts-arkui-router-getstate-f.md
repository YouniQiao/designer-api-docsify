# getState

## Modules to Import

```TypeScript
import { router } from 'kits/@kit.ArkUI';
```

## getState

```TypeScript
function getState(): RouterState
```

获取栈顶页面的状态信息。

> **说明：**
> 
> - 从API version 8开始支持，从API version 18开始废弃，建议使用[getState](arkts-arkui-arkui-uicontext-router-c.md#getstate)替代。getLength需
> 先通过[UIContext](arkts-arkui-uicontext.md)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)获取
> [Router](arkts-arkui-uicontext.md)实例，然后通过该实例进行调用。
> 
> - 从API version 10开始，可以通过使用[UIContext](arkts-arkui-uicontext.md)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的
> [Router](arkts-arkui-uicontext.md)对象。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 18

**Substitutes:** [@ohos.arkui.UIContext:Router#getState](arkts-arkui-arkui-uicontext-router-c.md#getstate)

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-router-function getState(): RouterState--><!--Device-router-function getState(): RouterState-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [RouterState](arkts-arkui-router-routerstate-i.md) | 栈顶页面的状态信息，包含页面索引、名称、路径和参数。 |

## Examples

```TypeScript
let page = this.getUIContext().getRouter().getState();
console.info('current index = ' + page.index);
console.info('current name = ' + page.name);
console.info('current path = ' + page.path);
```

