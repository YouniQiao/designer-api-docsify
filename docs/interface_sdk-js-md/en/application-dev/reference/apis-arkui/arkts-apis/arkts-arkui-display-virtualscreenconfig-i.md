# VirtualScreenConfig

创建虚拟屏幕的参数。

**Since:** 16

**ArkTS mode:** ArkTS-Dyn since version 16; ArkTS-Sta since version 23.

<!--Device-display-interface VirtualScreenConfig--><!--Device-display-interface VirtualScreenConfig-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## density

```TypeScript
density: double
```

指定虚拟屏幕的密度，单位为px，该参数为浮点数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 16

**ArkTS mode:** ArkTS-Dyn since version 16; ArkTS-Sta since version 23.

<!--Device-VirtualScreenConfig-density: double--><!--Device-VirtualScreenConfig-density: double-End-->

**System capability:** SystemCapability.Window.SessionManager

## height

```TypeScript
height: long
```

指定虚拟屏幕的高度，单位为px，该参数应为正整数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 16

**ArkTS mode:** ArkTS-Dyn since version 16; ArkTS-Sta since version 23.

<!--Device-VirtualScreenConfig-height: long--><!--Device-VirtualScreenConfig-height: long-End-->

**System capability:** SystemCapability.Window.SessionManager

## name

```TypeScript
name: string
```

指定虚拟屏幕的名称，用户可自行定义。

**Type:** string

**Since:** 16

**ArkTS mode:** ArkTS-Dyn since version 16; ArkTS-Sta since version 23.

<!--Device-VirtualScreenConfig-name: string--><!--Device-VirtualScreenConfig-name: string-End-->

**System capability:** SystemCapability.Window.SessionManager

## supportsFocus

```TypeScript
supportsFocus?: boolean
```

指定虚拟屏幕是否可获得焦点。true表示可获焦，false表示不可获焦，默认值为true。

**Type:** boolean

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-VirtualScreenConfig-supportsFocus?: boolean--><!--Device-VirtualScreenConfig-supportsFocus?: boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

## surfaceId

```TypeScript
surfaceId: string
```

指定虚拟屏幕的surfaceId，用户可自行定义，该参数最大长度为4096个字节，超出最大长度时则取前4096个字节。

**Type:** string

**Since:** 16

**ArkTS mode:** ArkTS-Dyn since version 16; ArkTS-Sta since version 23.

<!--Device-VirtualScreenConfig-surfaceId: string--><!--Device-VirtualScreenConfig-surfaceId: string-End-->

**System capability:** SystemCapability.Window.SessionManager

## width

```TypeScript
width: long
```

指定虚拟屏幕的宽度，单位为px，该参数应为正整数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 16

**ArkTS mode:** ArkTS-Dyn since version 16; ArkTS-Sta since version 23.

<!--Device-VirtualScreenConfig-width: long--><!--Device-VirtualScreenConfig-width: long-End-->

**System capability:** SystemCapability.Window.SessionManager

