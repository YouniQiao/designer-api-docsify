# getStateByIndex

## Modules to Import

```TypeScript
import { router } from 'kits/@kit.ArkUI';
```

## getStateByIndex

```TypeScript
function getStateByIndex(index: number): RouterState | undefined
```

通过索引值获取对应页面的状态信息。

> **说明：**
> 
> - 从API version 12开始支持，从API version 18开始废弃，建议使用
> [getStateByIndex](arkts-arkui-arkui-uicontext-router-c.md#getstatebyindex)替代。getStateByIndex需先通过
> [UIContext](arkts-arkui-uicontext.md)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)获取
> [Router](arkts-arkui-uicontext.md)实例，然后通过该实例进行调用。
> 
> - 从API version 12开始，可以通过使用[UIContext](arkts-arkui-uicontext.md)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的
> [Router](arkts-arkui-uicontext.md)对象。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** 18

**Substitutes:** [@ohos.arkui.UIContext:Router#getStateByIndex](arkts-arkui-arkui-uicontext-router-c.md#getstatebyindex)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-router-function getStateByIndex(index: number): RouterState | undefined--><!--Device-router-function getStateByIndex(index: number): RouterState | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | number | Yes | 表示要获取的页面索引，取值范围[1, 页面栈大小]，页面栈最大数量为32。从栈底到栈顶，index从1开始递增。索引不存在时返回undefined。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RouterState](arkts-arkui-router-routerstate-i.md) | 返回对应索引页面的状态信息，包含页面索引、名称、路径和参数。索引不存在时返回undefined。 |

## Examples

```TypeScript
import { router } from '@kit.ArkUI';

let options: router.RouterState | undefined = router.getStateByIndex(1);
if (options != undefined) {
  console.info('index = ' + options.index);
  console.info('name = ' + options.name);
  console.info('path = ' + options.path);
  console.info(`params = ${JSON.stringify(options.params)}`);
}
```

