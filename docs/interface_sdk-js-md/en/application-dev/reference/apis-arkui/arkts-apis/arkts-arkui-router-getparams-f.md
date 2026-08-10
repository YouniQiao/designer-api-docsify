# getParams

## Modules to Import

```TypeScript
import { router } from 'kits/@kit.ArkUI';
```

## getParams

```TypeScript
function getParams(): Object
```

获取发起跳转的页面往当前页传入的参数。

> **说明：**
> 
> - 从API version 8开始支持，从API version 18开始废弃，建议使用[getParams](arkts-arkui-arkui-uicontext-router-c.md#getparams)替代。
> getParams需先通过[UIContext](arkts-arkui-uicontext.md)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)获取
> [Router](arkts-arkui-uicontext.md)实例，然后通过该实例进行调用。
> 
> - 从API version 10开始，可以通过使用[UIContext](arkts-arkui-uicontext.md)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的
> [Router](arkts-arkui-uicontext.md)对象。
> 
> getParams只获取当前页面的参数，并不会清除页面关联的参数。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 18

**Substitutes:** [@ohos.arkui.UIContext:Router#getParams](arkts-arkui-arkui-uicontext-router-c.md#getparams)

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-router-function getParams(): Object--><!--Device-router-function getParams(): Object-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| Object | 发起跳转的页面往当前页传入的参数。 |

## Examples

```TypeScript
this.getUIContext().getRouter().getParams();
```

