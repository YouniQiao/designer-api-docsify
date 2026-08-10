# Router

通过不同的uri访问不同的页面。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** ohos.router#router

<!--Device-unnamed-export default class Router--><!--Device-unnamed-export default class Router-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

## Modules to Import

```TypeScript
import { BackRouterOptions, DisableAlertBeforeBackPageOptions, RouterOptions, RouterState, EnableAlertBeforeBackPageOptions } from 'kits/@kit.ArkUI';
```

## back

```TypeScript
static back(options?: BackRouterOptions): void
```

返回上一页面或指定的页面。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** ohos.router.router#back

<!--Device-Router-static back(options?: BackRouterOptions): void--><!--Device-Router-static back(options?: BackRouterOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [BackRouterOptions](arkts-arkui-system-router-backrouteroptions-i.md) | No | 详细请参考BackRouterOptions。 |

## clear

```TypeScript
static clear(): void
```

清空页面栈中的所有历史页面，仅保留当前页面作为栈顶页面。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** ohos.router.router#clear

<!--Device-Router-static clear(): void--><!--Device-Router-static clear(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## disableAlertBeforeBackPage

```TypeScript
static disableAlertBeforeBackPage(options?: DisableAlertBeforeBackPageOptions): void
```

禁用页面返回询问对话框。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 8

**Substitutes:** ohos.router.router#hideAlertBeforeBackPage

<!--Device-Router-static disableAlertBeforeBackPage(options?: DisableAlertBeforeBackPageOptions): void--><!--Device-Router-static disableAlertBeforeBackPage(options?: DisableAlertBeforeBackPageOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [DisableAlertBeforeBackPageOptions](arkts-arkui-system-router-disablealertbeforebackpageoptions-i.md) | No | 详细请参见DisableAlertBeforeBackPageOptions。 |

## enableAlertBeforeBackPage

```TypeScript
static enableAlertBeforeBackPage(options: EnableAlertBeforeBackPageOptions): void
```

开启页面返回询问对话框。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 8

**Substitutes:** ohos.router.router#showAlertBeforeBackPage

<!--Device-Router-static enableAlertBeforeBackPage(options: EnableAlertBeforeBackPageOptions): void--><!--Device-Router-static enableAlertBeforeBackPage(options: EnableAlertBeforeBackPageOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [EnableAlertBeforeBackPageOptions](arkts-arkui-system-router-enablealertbeforebackpageoptions-i.md) | Yes | 详细请参见EnableAlertBeforeBackPageOptions。 |

## getLength

```TypeScript
static getLength(): string
```

获取当前在页面栈内的页面数量。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** ohos.router.router#getLength

<!--Device-Router-static getLength(): string--><!--Device-Router-static getLength(): string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| string | 页面数量，页面栈支持最大数值是32。 |

## getParams

```TypeScript
static getParams(): ParamsInterface
```

获取当前页面的参数信息。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 8

**Substitutes:** ohos.router.router#getParams

<!--Device-Router-static getParams(): ParamsInterface--><!--Device-Router-static getParams(): ParamsInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [ParamsInterface](arkts-arkui-paramsinterface-t.md) | 详细请参见ParamsInterface。 |

## getState

```TypeScript
static getState(): RouterState
```

获取当前页面的状态信息。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** ohos.router.router#getState

<!--Device-Router-static getState(): RouterState--><!--Device-Router-static getState(): RouterState-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [RouterState](arkts-arkui-router-routerstate-i.md) | 详细请参见RouterState。 |

## push

```TypeScript
static push(options: RouterOptions): void
```

跳转到应用内的指定页面。

> **说明：**
> 
> 页面路由栈支持的最大Page数量为32。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** ohos.router.router#push

<!--Device-Router-static push(options: RouterOptions): void--><!--Device-Router-static push(options: RouterOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RouterOptions](arkts-arkui-system-router-routeroptions-i.md) | Yes | 页面路由参数，详细请参考RouterOptions。 |

## replace

```TypeScript
static replace(options: RouterOptions): void
```

用应用内的某个页面替换当前页面，并销毁被替换的页面。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** ohos.router.router#replace

<!--Device-Router-static replace(options: RouterOptions): void--><!--Device-Router-static replace(options: RouterOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RouterOptions](arkts-arkui-system-router-routeroptions-i.md) | Yes | 页面路由参数，详细请参考RouterOptions。 |

