# DisableAlertBeforeBackPageOptions

定义DisableAlertBeforeBackPage参数选项。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 8

**Substitutes:** ohos.router#RouterOptions

<!--Device-unnamed-export interface DisableAlertBeforeBackPageOptions--><!--Device-unnamed-export interface DisableAlertBeforeBackPageOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { BackRouterOptions, DisableAlertBeforeBackPageOptions, RouterOptions, RouterState, EnableAlertBeforeBackPageOptions } from 'kits/@kit.ArkUI';
```

## cancel

```TypeScript
cancel?: (errMsg: string) => void
```

关闭询问对话框失败时触发，errMsg表示返回信息。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 8

**Substitutes:** ohos.router#RouterOptions

<!--Device-DisableAlertBeforeBackPageOptions-cancel?: (errMsg: string) => void--><!--Device-DisableAlertBeforeBackPageOptions-cancel?: (errMsg: string) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| errMsg | string | Yes |  |

## complete

```TypeScript
complete?: () => void
```

当对话框关闭时触发该回调。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 8

**Substitutes:** ohos.router#RouterOptions

<!--Device-DisableAlertBeforeBackPageOptions-complete?: () => void--><!--Device-DisableAlertBeforeBackPageOptions-complete?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## success

```TypeScript
success?: (errMsg: string) => void
```

关闭询问对话框成功时触发，errMsg表示返回信息。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 8

**Substitutes:** ohos.router#RouterOptions

<!--Device-DisableAlertBeforeBackPageOptions-success?: (errMsg: string) => void--><!--Device-DisableAlertBeforeBackPageOptions-success?: (errMsg: string) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| errMsg | string | Yes |  |

