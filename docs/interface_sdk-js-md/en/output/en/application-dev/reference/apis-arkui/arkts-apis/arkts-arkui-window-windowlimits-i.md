# WindowLimits

Describes the parameters for window size limits. Applications can obtain the current window size limits (in px) via [getWindowLimits]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_. Starting from API version 22, they can also be obtained via [getWindowLimitsVP]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ (in vp). The actual window size limits applied are determined by the intersection of the default system limits, application configurations, and runtime settings, with the priority (from highest to lowest) as follows: 1. Window size limits configured by the application via [setWindowLimits]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_. 2. Window size limits specified by the application via [StartOptions]\_\_\_JSDOC\_LINK\_DESC\_USD\_4\_\_\_ when the application starts the window through [startAbility]\_\_\_JSDOC\_LINK\_DESC\_USD\_5\_\_\_. (This approach is supported since API version 17.) 3. Window size limits configured by the application in \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_. 4. Default system limits (which vary depending on the product and window type). > **NOTE** > > For the **maxWidth**, **maxHeight**, **minWidth**, and **minHeight** properties: > > - The default unit is px. Starting from API version 22, the unit can be px or vp, depending on the setting of > **pixelUnit**. > > - The value is an integer. Floating-point values will be rounded down. > > - The default value is **0**, indicating that the property does not change. > > - The lower bound of the effective range is the minimum height/width limited by the system. > > - The upper bound of the effective range is the maximum height/width limited by the system.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-window-interface WindowLimits--><!--Device-window-interface WindowLimits-End-->

**System capability:** SystemCapability.Window.SessionManager

## maxHeight

```TypeScript
maxHeight?: int
```

Maximum window height.

**Type:** int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WindowLimits-maxHeight?: int--><!--Device-WindowLimits-maxHeight?: int-End-->

**System capability:** SystemCapability.Window.SessionManager

## maxWidth

```TypeScript
maxWidth?: int
```

Maximum window width.

**Type:** int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WindowLimits-maxWidth?: int--><!--Device-WindowLimits-maxWidth?: int-End-->

**System capability:** SystemCapability.Window.SessionManager

## minHeight

```TypeScript
minHeight?: int
```

Minimum window height.

**Type:** int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WindowLimits-minHeight?: int--><!--Device-WindowLimits-minHeight?: int-End-->

**System capability:** SystemCapability.Window.SessionManager

## minWidth

```TypeScript
minWidth?: int
```

Minimum window width.

**Type:** int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-WindowLimits-minWidth?: int--><!--Device-WindowLimits-minWidth?: int-End-->

**System capability:** SystemCapability.Window.SessionManager

## pixelUnit

```TypeScript
pixelUnit?: PixelUnit
```

Unit of the window size limits. The default value is **px**. The value can be **px** or **vp**.

**Type:** PixelUnit

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-WindowLimits-pixelUnit?: PixelUnit--><!--Device-WindowLimits-pixelUnit?: PixelUnit-End-->

**System capability:** SystemCapability.Window.SessionManager

