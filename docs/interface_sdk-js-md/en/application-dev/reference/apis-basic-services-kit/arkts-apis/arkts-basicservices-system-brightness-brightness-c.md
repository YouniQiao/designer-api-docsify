# Brightness

The module provides APIs for querying and adjusting the screen brightness and mode.

**Since:** 3

**Deprecated since:** 7

<!--Device-unnamed-export default class Brightness--><!--Device-unnamed-export default class Brightness-End-->

**System capability:** SystemCapability.PowerManager.DisplayPowerManager.Lite

## Modules to Import

```TypeScript
import { Brightness, BrightnessModeResponse, BrightnessResponse, GetBrightnessModeOptions, GetBrightnessOptions, SetBrightnessModeOptions, SetBrightnessOptions, SetKeepScreenOnOptions } from '@kit.BasicServicesKit';
```

## getMode

```TypeScript
static getMode(options?: GetBrightnessModeOptions): void
```

Obtains the screen brightness adjustment mode.

**Since:** 3

**Deprecated since:** 7

<!--Device-Brightness-static getMode(options?: GetBrightnessModeOptions): void--><!--Device-Brightness-static getMode(options?: GetBrightnessModeOptions): void-End-->

**System capability:** SystemCapability.PowerManager.DisplayPowerManager.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [GetBrightnessModeOptions](arkts-basicservices-system-brightness-getbrightnessmodeoptions-i.md) | No | Options for obtaining the screen brightness mode. This parameter is optional and is left blank by default. |

## getValue

```TypeScript
static getValue(options?: GetBrightnessOptions): void
```

Obtains the current screen brightness.

**Since:** 3

**Deprecated since:** 7

<!--Device-Brightness-static getValue(options?: GetBrightnessOptions): void--><!--Device-Brightness-static getValue(options?: GetBrightnessOptions): void-End-->

**System capability:** SystemCapability.PowerManager.DisplayPowerManager.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [GetBrightnessOptions](arkts-basicservices-system-brightness-getbrightnessoptions-i.md) | No | Options for obtaining the screen brightness. This parameter is optional and is left blank by default. |

## setKeepScreenOn

```TypeScript
static setKeepScreenOn(options?: SetKeepScreenOnOptions): void
```

Sets whether to always keep the screen on. Call this API in **onShow()**.

**NOTE：**

- This API is no longer maintained since API version 7 except for lite wearables. You are advised to use [window.setWindowKeepScreenOn()](../../../reference/apis-arkui/arkts-apis-window-Window.md#setwindowkeepscreenon) instead.

- On Lite Wearables, this API can only prevent the system from turning off the screen due to inactivity timeout (automatic). It cannot prevent screen-off caused by user actions (such as covering the screen) or the end of the keep-screen-on period.

**Since:** 3

**Deprecated since:** 7

**Substitutes:** setWindowKeepScreenOn

<!--Device-Brightness-static setKeepScreenOn(options?: SetKeepScreenOnOptions): void--><!--Device-Brightness-static setKeepScreenOn(options?: SetKeepScreenOnOptions): void-End-->

**System capability:** SystemCapability.PowerManager.DisplayPowerManager.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [SetKeepScreenOnOptions](arkts-basicservices-system-brightness-setkeepscreenonoptions-i.md) | No | Options for setting the screen to be steady on. This parameter is optional and is left blank by default. |

## setMode

```TypeScript
static setMode(options?: SetBrightnessModeOptions): void
```

Sets the screen brightness adjustment mode.

**Since:** 3

**Deprecated since:** 7

<!--Device-Brightness-static setMode(options?: SetBrightnessModeOptions): void--><!--Device-Brightness-static setMode(options?: SetBrightnessModeOptions): void-End-->

**System capability:** SystemCapability.PowerManager.DisplayPowerManager.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [SetBrightnessModeOptions](arkts-basicservices-system-brightness-setbrightnessmodeoptions-i.md) | No | Options for setting the screen brightness mode. This parameter is optional and is left blank by default. |

## setValue

```TypeScript
static setValue(options?: SetBrightnessOptions): void
```

Sets the screen brightness.

**Since:** 3

**Deprecated since:** 7

**Substitutes:** [setValue](arkts-basicservices-brightness-setvalue-f-sys.md)

<!--Device-Brightness-static setValue(options?: SetBrightnessOptions): void--><!--Device-Brightness-static setValue(options?: SetBrightnessOptions): void-End-->

**System capability:** SystemCapability.PowerManager.DisplayPowerManager.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [SetBrightnessOptions](arkts-basicservices-system-brightness-setbrightnessoptions-i.md) | No | Options for setting the screen brightness. This parameter is optional and is left blank by default. |

