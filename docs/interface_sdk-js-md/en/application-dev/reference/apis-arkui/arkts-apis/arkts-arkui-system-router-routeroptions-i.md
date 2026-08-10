# RouterOptions

定义路由器的选项。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** ohos.router#RouterOptions

<!--Device-unnamed-export interface RouterOptions--><!--Device-unnamed-export interface RouterOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

## Modules to Import

```TypeScript
import { BackRouterOptions, DisableAlertBeforeBackPageOptions, RouterOptions, RouterState, EnableAlertBeforeBackPageOptions } from 'kits/@kit.ArkUI';
```

## params

```TypeScript
params?: Object
```

表示路由跳转时要同时传递到目标页面的数据。跳转到目标页面后，使用getParams()获取传递的参数，此外，在类web范式中，参数也可以在页面中直接使用，如this.keyValue(keyValue为跳转时params参数中的key值)，如果目标页面中已有该字段，则其值会被传入的字段值覆盖。

**Type:** Object

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** ohos.router.RouterOptions#params

<!--Device-RouterOptions-params?: Object--><!--Device-RouterOptions-params?: Object-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

## uri

```TypeScript
uri: string
```

目标页面的uri，可以是以下的两种格式：

1. 页面的绝对路径，由config.json文件中的页面列表提供。例如：

- pages/index/index  
- pages/detail/detail

2. 特定路径。如果URI为斜杠（/），则显示主页。

**Type:** string

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** ohos.router.RouterOptions#url

<!--Device-RouterOptions-uri: string--><!--Device-RouterOptions-uri: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

