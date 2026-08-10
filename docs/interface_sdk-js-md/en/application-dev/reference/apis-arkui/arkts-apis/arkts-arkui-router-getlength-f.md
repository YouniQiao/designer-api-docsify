# getLength

## Modules to Import

```TypeScript
import { router } from 'kits/@kit.ArkUI';
```

## getLength

```TypeScript
function getLength(): string
```

获取当前在页面栈内的页面数量。

> **说明：**
> 
> - 从API version 8开始支持，从API version 18开始废弃，建议使用[getLength](arkts-arkui-arkui-uicontext-router-c.md#getlength)替代。
> getLength需先通过[UIContext](arkts-arkui-uicontext.md)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)获取
> [Router](arkts-arkui-uicontext.md)实例，然后通过该实例进行调用。
> 
> - 从API version 10开始，可以通过使用[UIContext](arkts-arkui-uicontext.md)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的
> [Router](arkts-arkui-uicontext.md)对象。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 18

**Substitutes:** [@ohos.arkui.UIContext:Router#getLength](arkts-arkui-arkui-uicontext-router-c.md#getlength)

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-router-function getLength(): string--><!--Device-router-function getLength(): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| string | 页面数量，页面栈支持最大数值是32。 |

## Examples

```TypeScript
let size = this.getUIContext().getRouter().getLength();
console.info('pages stack size = ' + size);
```

