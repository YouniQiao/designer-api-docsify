# SystemBarRegionTint (System API)

单个导航栏或状态栏回调信息。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-window-interface SystemBarRegionTint--><!--Device-window-interface SystemBarRegionTint-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## backgroundColor

```TypeScript
backgroundColor?: string
```

系统栏背景颜色，为十六进制RGB或ARGB颜色，不区分大小写，例如'#00FF00'或'#FF00FF00'。 默认值为'0x66000000'。

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-SystemBarRegionTint-backgroundColor?: string--><!--Device-SystemBarRegionTint-backgroundColor?: string-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## contentColor

```TypeScript
contentColor?: string
```

系统栏文字颜色。 默认值为'0xE5FFFFFF'。

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-SystemBarRegionTint-contentColor?: string--><!--Device-SystemBarRegionTint-contentColor?: string-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## isEnable

```TypeScript
isEnable?: boolean
```

当前系统栏是否显示。true表示显示；false表示不显示。默认值为true。

**Type:** boolean

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-SystemBarRegionTint-isEnable?: boolean--><!--Device-SystemBarRegionTint-isEnable?: boolean-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## region

```TypeScript
region?: Rect
```

当前系统栏的位置及大小。默认值为{0,0,0,0}。

**Type:** [Rect](../../apis-form-kit/arkts-apis/arkts-form-forminfo-rect-i.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-SystemBarRegionTint-region?: Rect--><!--Device-SystemBarRegionTint-region?: Rect-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## type

```TypeScript
type: WindowType
```

当前属性改变的系统栏类型，仅支持类型为导航栏、状态栏的系统栏。

**Type:** [WindowType](../../apis-accessibility-kit/arkts-apis/arkts-accessibility-windowtype-t.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-SystemBarRegionTint-type: WindowType--><!--Device-SystemBarRegionTint-type: WindowType-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

