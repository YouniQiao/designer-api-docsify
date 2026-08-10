# VirtualScreenOption (System API)

创建虚拟屏幕的参数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-screen-interface VirtualScreenOption--><!--Device-screen-interface VirtualScreenOption-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { screen } from 'kits/@kit.ArkUI';
```

## density

```TypeScript
density: double
```

指定虚拟屏幕的密度，该参数为浮点数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VirtualScreenOption-density: double--><!--Device-VirtualScreenOption-density: double-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## height

```TypeScript
height: long
```

指定虚拟屏幕的高度，单位为px，该参数应为整数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VirtualScreenOption-height: long--><!--Device-VirtualScreenOption-height: long-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## name

```TypeScript
name: string
```

指定虚拟屏幕的名称。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VirtualScreenOption-name: string--><!--Device-VirtualScreenOption-name: string-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## supportsFocus

```TypeScript
supportsFocus?: boolean
```

指定虚拟屏幕是否可获得焦点。true表示可获焦，false表示不可获焦，默认值为true。

**Type:** boolean

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-VirtualScreenOption-supportsFocus?: boolean--><!--Device-VirtualScreenOption-supportsFocus?: boolean-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## surfaceId

```TypeScript
surfaceId: string
```

指定虚拟屏幕的surfaceId。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VirtualScreenOption-surfaceId: string--><!--Device-VirtualScreenOption-surfaceId: string-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## userId

```TypeScript
userId?: int
```

指定虚拟屏幕的用户ID，该参数为整数。默认值为-1。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-VirtualScreenOption-userId?: int--><!--Device-VirtualScreenOption-userId?: int-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## width

```TypeScript
width: long
```

指定虚拟屏幕的宽度，单位为px，该参数应为整数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VirtualScreenOption-width: long--><!--Device-VirtualScreenOption-width: long-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

