# VirtualScreenConfig

Describes the virtual screen parameters.

**Since:** 16

**ArkTS mode:** ArkTS-Dyn since version 16; ArkTS-Sta since version 23.

<!--Device-display-interface VirtualScreenConfig--><!--Device-display-interface VirtualScreenConfig-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { display } from '@kit.ArkUI';
```

## density

```TypeScript
density: double
```

Density of the virtual screen, in px. The value is a floating-point number.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 16

**ArkTS mode:** ArkTS-Dyn since version 16; ArkTS-Sta since version 23.

<!--Device-VirtualScreenConfig-density: double--><!--Device-VirtualScreenConfig-density: double-End-->

**System capability:** SystemCapability.Window.SessionManager

## height

```TypeScript
height: long
```

Height of the virtual screen, in px. The value must be a positive integer.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 16

**ArkTS mode:** ArkTS-Dyn since version 16; ArkTS-Sta since version 23.

<!--Device-VirtualScreenConfig-height: long--><!--Device-VirtualScreenConfig-height: long-End-->

**System capability:** SystemCapability.Window.SessionManager

## name

```TypeScript
name: string
```

Name of the virtual screen, which can be customized.

**Type:** string

**Since:** 16

**ArkTS mode:** ArkTS-Dyn since version 16; ArkTS-Sta since version 23.

<!--Device-VirtualScreenConfig-name: string--><!--Device-VirtualScreenConfig-name: string-End-->

**System capability:** SystemCapability.Window.SessionManager

## supportsFocus

```TypeScript
supportsFocus?: boolean
```

Whether the virtual screen is focusable. **true** if focusable, **false** otherwise. The default value is  
**true**.

**Type:** boolean

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-VirtualScreenConfig-supportsFocus?: boolean--><!--Device-VirtualScreenConfig-supportsFocus?: boolean-End-->

**System capability:** SystemCapability.Window.SessionManager

## surfaceId

```TypeScript
surfaceId: string
```

Surface ID of the virtual screen, which can be customized. The maximum length for this parameter is 4096 bytes.If it goes beyond that, only the first 4096 bytes are used.

**Type:** string

**Since:** 16

**ArkTS mode:** ArkTS-Dyn since version 16; ArkTS-Sta since version 23.

<!--Device-VirtualScreenConfig-surfaceId: string--><!--Device-VirtualScreenConfig-surfaceId: string-End-->

**System capability:** SystemCapability.Window.SessionManager

## width

```TypeScript
width: long
```

Width of the virtual screen, in px. The value must be a positive integer.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 16

**ArkTS mode:** ArkTS-Dyn since version 16; ArkTS-Sta since version 23.

<!--Device-VirtualScreenConfig-width: long--><!--Device-VirtualScreenConfig-width: long-End-->

**System capability:** SystemCapability.Window.SessionManager

