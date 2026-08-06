# WindowDensityInfo

Describes the information about the display density of the screen where the window is located and the window's custom display density. It is a scale factor independent of pixel units, that is, a factor for scaling display size.

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-window-interface WindowDensityInfo--><!--Device-window-interface WindowDensityInfo-End-->

**System capability:** SystemCapability.Window.SessionManager

## customDensity

```TypeScript
customDensity: double
```

Custom display size scale factor of the window. The value ranges from 0.5 to 4.0. If this parameter is left unspecified, the system's display size scale factor is used. This parameter takes effect only for the main window. For the child window or system window, it is equivalent to the system's display size scale factor (  
**systemDensity**).

**Type:** double

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-WindowDensityInfo-customDensity: double--><!--Device-WindowDensityInfo-customDensity: double-End-->

**System capability:** SystemCapability.Window.SessionManager

## defaultDensity

```TypeScript
defaultDensity: double
```

Default display size scale factor for the screen where the window is located. The value ranges from 0.5 to 4.0and varies with the screen.

**Type:** double

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-WindowDensityInfo-defaultDensity: double--><!--Device-WindowDensityInfo-defaultDensity: double-End-->

**System capability:** SystemCapability.Window.SessionManager

## systemDensity

```TypeScript
systemDensity: double
```

System's display size scale factor for the screen where the window is located. The value ranges from 0.5 to 4.0and varies according to user settings.

**Type:** double

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-WindowDensityInfo-systemDensity: double--><!--Device-WindowDensityInfo-systemDensity: double-End-->

**System capability:** SystemCapability.Window.SessionManager

