# BackRouterOptions

定义路由器返回的选项。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 8

**Substitutes:** ohos.router#RouterOptions

<!--Device-unnamed-export interface BackRouterOptions--><!--Device-unnamed-export interface BackRouterOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { BackRouterOptions, DisableAlertBeforeBackPageOptions, RouterOptions, RouterState, EnableAlertBeforeBackPageOptions } from 'kits/@kit.ArkUI';
```

## params

```TypeScript
params?: Object
```

返回时要同时传递到目标页面的数据。

**Type:** Object

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 8

**Substitutes:** ohos.router.RouterOptions#params

<!--Device-BackRouterOptions-params?: Object--><!--Device-BackRouterOptions-params?: Object-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

## uri

```TypeScript
uri?: string
```

返回到指定uri的界面，如果页面栈上没有uri页面，则不响应该情况。如果uri未设置，则返回上一页。

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 8

**Substitutes:** ohos.router.RouterOptions#url

<!--Device-BackRouterOptions-uri?: string--><!--Device-BackRouterOptions-uri?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

