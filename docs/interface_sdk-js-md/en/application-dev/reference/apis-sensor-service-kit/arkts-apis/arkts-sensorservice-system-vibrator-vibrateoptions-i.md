# VibrateOptions

Defines the vibration options.

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** [VibrateTime](arkts-sensorservice-vibrator-vibratetime-i.md#VibrateTime)

**Required permissions:** ohos.permission.VIBRATE

<!--Device-unnamed-export interface VibrateOptions--><!--Device-unnamed-export interface VibrateOptions-End-->

**System capability:** SystemCapability.Sensors.MiscDevice.Lite

## Modules to Import

```TypeScript
import { VibrateOptions } from 'VibrateOptions';
```

## complete

```TypeScript
complete?: () => void
```

Called when the API call is complete.

**Type:** () =&gt; void

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** [startVibration](arkts-sensorservice-vibrator-startvibration-f.md#startVibration)

**Required permissions:** ohos.permission.VIBRATE

**Model restriction:** This API can be used only in the FA model.

<!--Device-VibrateOptions-complete?: () => void--><!--Device-VibrateOptions-complete?: () => void-End-->

**System capability:** SystemCapability.Sensors.MiscDevice.Lite

## fail

```TypeScript
fail?: (data: string, code: number) => void
```

Called when the API call fails.

**Type:** (data: string, code: number) =&gt; void

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** [startVibration](arkts-sensorservice-vibrator-startvibration-f.md#startVibration)

**Required permissions:** ohos.permission.VIBRATE

**Model restriction:** This API can be used only in the FA model.

<!--Device-VibrateOptions-fail?: (data: string, code: number) => void--><!--Device-VibrateOptions-fail?: (data: string, code: number) => void-End-->

**System capability:** SystemCapability.Sensors.MiscDevice.Lite

## mode

```TypeScript
mode?: 'long' | 'short'
```

Vibration mode. The value **long** indicates long vibration, and **short** indicates short vibration. The default value is **long**.

**Type:** 'long' \| 'short'

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** [VibrateTime](arkts-sensorservice-vibrator-vibratetime-i.md#VibrateTime)

**Required permissions:** ohos.permission.VIBRATE

**Model restriction:** This API can be used only in the FA model.

<!--Device-VibrateOptions-mode?: 'long' | 'short'--><!--Device-VibrateOptions-mode?: 'long' | 'short'-End-->

**System capability:** SystemCapability.Sensors.MiscDevice.Lite

## success

```TypeScript
success: () => void
```

Called when the vibrator data changes.

**Type:** () =&gt; void

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 8

**Substitutes:** [startVibration](arkts-sensorservice-vibrator-startvibration-f.md#startVibration)

**Required permissions:** ohos.permission.VIBRATE

**Model restriction:** This API can be used only in the FA model.

<!--Device-VibrateOptions-success: () => void--><!--Device-VibrateOptions-success: () => void-End-->

**System capability:** SystemCapability.Sensors.MiscDevice.Lite

