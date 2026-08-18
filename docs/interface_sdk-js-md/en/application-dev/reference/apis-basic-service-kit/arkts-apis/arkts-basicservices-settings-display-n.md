# display

Provides methods for setting the display effect, including the font size, screen brightness, screen rotation, animation factor, and display color.

**Since:** 23

<!--Device-settings-namespace display--><!--Device-settings-namespace display-End-->

**System capability:** SystemCapability.Applications.Settings.Core

## Modules to Import

```TypeScript
import { settings } from '@kit.BasicServicesKit';
import { settingsLite } from '@kit.BasicServicesKit';
```

## Summary

### Constants

| Name | Description |
| --- | --- |
| [FONT_SCALE](arkts-basicservices-display-con.md#fontscale) | Indicates the scaling factor of fonts, which is a float number. |
| [SCREEN_BRIGHTNESS_STATUS](arkts-basicservices-display-con.md#screenbrightnessstatus) | Indicates the screen brightness. The value ranges from 0 to 255. |
| [AUTO_SCREEN_BRIGHTNESS](arkts-basicservices-display-con.md#autoscreenbrightness) | Specifies whether automatic screen brightness adjustment is enabled. &lt;p&gt;If the value is {@code 1}, automatic adjustment is enabled. If the value is {@code 0}, automatic adjustment is disabled. |
| [AUTO_SCREEN_BRIGHTNESS_MODE](arkts-basicservices-display-con.md#autoscreenbrightnessmode) | Indicates the value of {@code AUTO_SCREEN_BRIGHTNESS} when automatic screen brightness adjustment is used. |
| [MANUAL_SCREEN_BRIGHTNESS_MODE](arkts-basicservices-display-con.md#manualscreenbrightnessmode) | Indicates the value of {@code AUTO_SCREEN_BRIGHTNESS} when manual screen brightness adjustment is used. |
| [SCREEN_OFF_TIMEOUT](arkts-basicservices-display-con.md#screenofftimeout) | Indicates the duration that the device waits before going to sleep after a period of inactivity, in milliseconds. |
| [DEFAULT_SCREEN_ROTATION](arkts-basicservices-display-con.md#defaultscreenrotation) | Indicates the screen rotation when no other policy is available. &lt;p&gt;This constant is invalid when auto-rotation is enabled. When auto-rotation is disabled, the following values are available: &lt;ul&gt; &lt;li&gt;{@code 0} - The screen rotates 0 degrees. &lt;li&gt;{@code 1} - The screen rotates 90 degrees. &lt;li&gt;{@code 2} - The screen rotates 180 degrees. &lt;li&gt;{@code 3} - The screen rotates 270 degrees. &lt;/ul&gt; |
| [ANIMATOR_DURATION_SCALE](arkts-basicservices-display-con.md#animatordurationscale) | Indicates the scaling factor for the animation duration. &lt;p&gt;This affects the start delay and duration of all such animations. If the value is {@code 0}, the animation ends immediately. The default value is {@code 1}. |
| [TRANSITION_ANIMATION_SCALE](arkts-basicservices-display-con.md#transitionanimationscale) | Indicates the scaling factor for transition animations. If the value is {@code 0}, transition animations are disabled. |
| [WINDOW_ANIMATION_SCALE](arkts-basicservices-display-con.md#windowanimationscale) | Indicates the scaling factor for normal window animations. If the value is {@code 0}, window animations are disabled. |
| [DISPLAY_INVERSION_STATUS](arkts-basicservices-display-con.md#displayinversionstatus) | Specifies whether display color inversion is enabled. &lt;p&gt;If the value is {@code 1}, display color inversion is enabled. If the value is {@code 0}, display color inversion is disabled. |

