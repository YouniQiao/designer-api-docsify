# getStateByUrl

## Modules to Import

```TypeScript
import { router } from 'kits/@kit.ArkUI';
```

## getStateByUrl

```TypeScript
function getStateByUrl(url: string): Array<RouterState>
```

通过url获取对应页面的状态信息。

> **说明：**
> 
> - 从API version 12开始支持，从API version 18开始废弃，建议使用[getStateByUrl](arkts-arkui-arkui-uicontext-router-c.md#getstatebyurl)替
> 代。getStateByUrl需先通过[UIContext](arkts-arkui-uicontext.md)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)获取
> [Router](arkts-arkui-uicontext.md)实例，然后通过该实例进行调用。
> 
> - 从API version 12开始，可以通过使用[UIContext](arkts-arkui-uicontext.md)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的
> [Router](arkts-arkui-uicontext.md)对象。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** 18

**Substitutes:** [@ohos.arkui.UIContext:Router#getStateByUrl](arkts-arkui-arkui-uicontext-router-c.md#getstatebyurl)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-router-function getStateByUrl(url: string): Array<RouterState>--><!--Device-router-function getStateByUrl(url: string): Array<RouterState>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| url | string | Yes | 表示要获取对应页面信息的url。url格式为页面绝对路径，由配置文件中pages列表提供，例如：pages/index/index。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;RouterState&gt; | 匹配指定url的页面状态信息数组，每个元素包含页面索引、名称、路径和参数。 |

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

