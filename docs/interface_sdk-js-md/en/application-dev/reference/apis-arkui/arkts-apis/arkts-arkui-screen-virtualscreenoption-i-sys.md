# VirtualScreenOption (System API)

Defines virtual screen parameters.

**Since:** 23

<!--Device-screen-interface VirtualScreenOption--><!--Device-screen-interface VirtualScreenOption-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { screen } from 'screen';
```

## density

```TypeScript
density: double
```

Density of the virtual screen, in px. The value must be a floating-point number.

**Type:** double

**Since:** 23

<!--Device-VirtualScreenOption-density: double--><!--Device-VirtualScreenOption-density: double-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## height

```TypeScript
height: long
```

Height of the virtual screen, in px. The value must be an integer.

**Type:** long

**Since:** 23

<!--Device-VirtualScreenOption-height: long--><!--Device-VirtualScreenOption-height: long-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## name

```TypeScript
name: string
```

Name of a virtual screen.

**Type:** string

**Since:** 23

<!--Device-VirtualScreenOption-name: string--><!--Device-VirtualScreenOption-name: string-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## supportsFocus

```TypeScript
supportsFocus?: boolean
```

Whether the virtual screen is focusable. **true** if focusable; **false** otherwise. The default value is **true**.

**Type:** boolean

**Since:** 23

<!--Device-VirtualScreenOption-supportsFocus?: boolean--><!--Device-VirtualScreenOption-supportsFocus?: boolean-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## surfaceId

```TypeScript
surfaceId: string
```

Surface ID of the virtual screen.

**Type:** string

**Since:** 23

<!--Device-VirtualScreenOption-surfaceId: string--><!--Device-VirtualScreenOption-surfaceId: string-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## userId

```TypeScript
userId?: int
```

User ID of the virtual screen, which is an integer. The default value is **-1**.

**Type:** int

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-VirtualScreenOption-userId?: int--><!--Device-VirtualScreenOption-userId?: int-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## width

```TypeScript
width: long
```

Width of the virtual screen, in px. The value must be an integer.

**Type:** long

**Since:** 23

<!--Device-VirtualScreenOption-width: long--><!--Device-VirtualScreenOption-width: long-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

