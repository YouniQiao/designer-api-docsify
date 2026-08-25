# WindowLimits

Describes the parameters for window size limits. Applications can obtain the current window size limits (in px) via [getWindowLimits](arkts-arkui-window-window-i.md#getwindowlimits). Starting from API version 22, they can also be obtained via [getWindowLimitsVP](arkts-arkui-window-window-i.md#getwindowlimitsvp) (in vp).The actual window size limits applied are determined by the intersection of the default system limits, application configurations, and runtime settings, with the priority (from highest to lowest) as follows:
1. Window size limits configured by the application via [setWindowLimits](arkts-arkui-window-window-i.md#setwindowlimits).
2. Window size limits specified by the application via [StartOptions](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-startoptions-startoptions-c.md) when the application starts the window through [startAbility](../../apis-ability-kit/arkts-apis/arkts-ability-uiabilitycontext-c.md#startability). (This approach is supported since API version 17.)
3. Window size limits configured by the application in [abilities in the module.json5 file](../../../quick-start/module-configuration-file.md#abilities).
4. Default system limits (which vary depending on the product and window type).

> **NOTE：**&gt;
> For the **maxWidth**, **maxHeight**, **minWidth**, and **minHeight** properties:&gt;
> - The default unit is px. Starting from API version 22, the unit can be px or vp, depending on the setting of
> **pixelUnit**.&gt;
> - The value is an integer. Floating-point values will be rounded down.&gt;
> - The default value is **0**, indicating that the property does not change.&gt;
> - The lower bound of the effective range is the minimum height/width limited by the system.&gt;
> - The upper bound of the effective range is the maximum height/width limited by the system.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { window } from '@kit.ArkUI';
```

## maxHeight

```TypeScript
maxHeight?: int
```

Maximum window height.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Window.SessionManager

## maxWidth

```TypeScript
maxWidth?: int
```

Maximum window width.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Window.SessionManager

## minHeight

```TypeScript
minHeight?: int
```

Minimum window height.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Window.SessionManager

## minWidth

```TypeScript
minWidth?: int
```

Minimum window width.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Window.SessionManager

## pixelUnit

```TypeScript
pixelUnit?: PixelUnit
```

Unit of the window size limits. The default value is **px**. The value can be **px** or **vp**.

**Type:** [PixelUnit](arkts-arkui-window-pixelunit-e.md)

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Window.SessionManager
