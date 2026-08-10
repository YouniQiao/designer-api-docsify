# Configuration

创建子窗口或系统窗口时的参数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-window-interface Configuration--><!--Device-window-interface Configuration-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## ctx

```TypeScript
ctx?: BaseContext
```

当前应用上下文信息。不设置，则默认为空。&lt;br&gt;FA模型下不需要使用该参数，即可创建子窗口，使用该参数时会报错。&lt;br&gt;Stage模型必须使用该参数，用于创建全局悬浮窗、模态窗或系统窗口。 &lt;br&gt;

**Type:** [BaseContext](../../apis-ability-kit/arkts-apis/arkts-ability-basecontext-c.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Configuration-ctx?: BaseContext--><!--Device-Configuration-ctx?: BaseContext-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## decorEnabled

```TypeScript
decorEnabled?: boolean
```

是否显示窗口装饰，仅在windowType为TYPE_DIALOG时生效。true表示显示，false表示不显示。此参数默认值为false。

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Configuration-decorEnabled?: boolean--><!--Device-Configuration-decorEnabled?: boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

## displayId

```TypeScript
displayId?: long
```

当前屏幕ID。不设置，则默认为父窗口屏幕ID。&lt;br&gt;该参数应为非负整数，且对应屏幕ID存在。&lt;br&gt;扩展屏、异源虚拟屏场景下，全局悬浮窗可通过设置屏幕ID显示在指定屏幕上。&lt;br&gt;模态窗、系统窗设置屏幕ID无效，默认为父窗口屏幕ID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Configuration-displayId?: long--><!--Device-Configuration-displayId?: long-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## name

```TypeScript
name: string
```

窗口名称。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Configuration-name: string--><!--Device-Configuration-name: string-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## parentId

```TypeScript
parentId?: int
```

父窗口ID。不设置，则默认为-1，默认父窗为当前应用上下文对应主窗。&lt;br&gt;FA模型下，该参数应为非负整数，且对应父窗口ID存在。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Configuration-parentId?: int--><!--Device-Configuration-parentId?: int-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

## title

```TypeScript
title?: string
```

`decorEnabled`属性设置为true时，窗口的标题内容。标题显示区域最右端不超过系统三键区域最左端，超过部分以省略号表示。不设置，则默认为空字符串。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Configuration-title?: string--><!--Device-Configuration-title?: string-End-->

**System capability:** SystemCapability.Window.SessionManager

## windowType

```TypeScript
windowType: WindowType
```

窗口类型。

**Type:** [WindowType](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-windowtype-t.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Configuration-windowType: WindowType--><!--Device-Configuration-windowType: WindowType-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

