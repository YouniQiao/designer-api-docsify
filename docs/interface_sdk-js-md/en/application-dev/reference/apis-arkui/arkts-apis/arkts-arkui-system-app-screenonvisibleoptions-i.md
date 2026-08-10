# ScreenOnVisibleOptions

定义屏幕上可见接口的选项。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

<!--Device-unnamed-export interface ScreenOnVisibleOptions--><!--Device-unnamed-export interface ScreenOnVisibleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AppResponse, ScreenOnVisibleOptions, RequestFullWindowOptions } from 'kits/@kit.ArkUI';
```

## complete

```TypeScript
complete?: () => void
```

接口调用结束的回调函数。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScreenOnVisibleOptions-complete?: () => void--><!--Device-ScreenOnVisibleOptions-complete?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fail

```TypeScript
fail?: (data: string, code: number) => void
```

接口调用失败的回调函数。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScreenOnVisibleOptions-fail?: (data: string, code: number) => void--><!--Device-ScreenOnVisibleOptions-fail?: (data: string, code: number) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | string | Yes |  |
| code | number | Yes |  |

## success

```TypeScript
success?: () => void
```

接口调用成功的回调函数。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScreenOnVisibleOptions-success?: () => void--><!--Device-ScreenOnVisibleOptions-success?: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## visible

```TypeScript
visible?: boolean
```

是否启动保活，默认值false。

**Type:** boolean

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ScreenOnVisibleOptions-visible?: boolean--><!--Device-ScreenOnVisibleOptions-visible?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

