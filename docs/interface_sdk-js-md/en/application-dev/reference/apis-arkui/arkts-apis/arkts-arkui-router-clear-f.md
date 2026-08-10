# clear

## Modules to Import

```TypeScript
import { router } from 'kits/@kit.ArkUI';
```

## clear

```TypeScript
function clear(): void
```

清空页面栈中的所有历史页面，仅保留当前页面作为栈顶页面。

> **说明：**
> 
> - 从API version 8开始支持，从API version 18开始废弃，建议使用[clear](arkts-arkui-arkui-uicontext-router-c.md#clear)替代。clear需先通过
> [UIContext](arkts-arkui-uicontext.md)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)获取
> [Router](arkts-arkui-uicontext.md)实例，然后通过该实例进行调用。
> 
> - 从API version 10开始，可以通过使用[UIContext](arkts-arkui-uicontext.md)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的
> [Router](arkts-arkui-uicontext.md)对象。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 18

**Substitutes:** [@ohos.arkui.UIContext:Router#clear](arkts-arkui-arkui-uicontext-router-c.md#clear)

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-router-function clear(): void--><!--Device-router-function clear(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Examples

```TypeScript
this.getUIContext().getRouter().clear();
```

