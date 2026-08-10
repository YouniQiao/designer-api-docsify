# WindowDensityInfo

窗口所在显示设备和窗口自定义的显示密度信息，是与像素单位无关的缩放系数，即显示大小缩放系数。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-window-interface WindowDensityInfo--><!--Device-window-interface WindowDensityInfo-End-->

**System capability:** SystemCapability.Window.SessionManager

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## customDensity

```TypeScript
customDensity: double
```

窗口自定义设置的显示大小缩放系数，该参数取值范围为0.5-4.0。未设置该参数时，将跟随系统显示大小缩放系数变化。该参数仅主窗口生效，在子窗或系统窗口上等于系统显示大小缩放系数(systemDensity)。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-WindowDensityInfo-customDensity: double--><!--Device-WindowDensityInfo-customDensity: double-End-->

**System capability:** SystemCapability.Window.SessionManager

## defaultDensity

```TypeScript
defaultDensity: double
```

窗口所在屏幕的系统默认显示大小缩放系数，跟随窗口所在屏幕变化，该参数变化范围为0.5-4.0。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-WindowDensityInfo-defaultDensity: double--><!--Device-WindowDensityInfo-defaultDensity: double-End-->

**System capability:** SystemCapability.Window.SessionManager

## systemDensity

```TypeScript
systemDensity: double
```

窗口所在屏幕的系统显示大小缩放系数，跟随用户设置变化，该参数变化范围为0.5-4.0。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-WindowDensityInfo-systemDensity: double--><!--Device-WindowDensityInfo-systemDensity: double-End-->

**System capability:** SystemCapability.Window.SessionManager

