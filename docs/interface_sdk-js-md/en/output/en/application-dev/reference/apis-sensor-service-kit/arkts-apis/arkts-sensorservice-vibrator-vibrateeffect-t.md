# VibrateEffect

```TypeScript
type VibrateEffect = VibrateTime | VibratePreset | VibrateFromFile | VibrateFromPattern
```

Enumerates vibration effects of the vibrator. You can specify the vibration effect when calling [vibrator.startVibration9+]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ or [vibrator.startVibration9+]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-vibrator-type VibrateEffect = VibrateTime | VibratePreset | VibrateFromFile | VibrateFromPattern--><!--Device-vibrator-type VibrateEffect = VibrateTime | VibratePreset | VibrateFromFile | VibrateFromPattern-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

| Type | Description |
| --- | --- |
| VibrateTime | Triggers vibration based on a specified duration. \_\_\_HTML\_TAG\_USD\_0\_\_\_ This API can be used in atomic services since API version 11. |
| VibratePreset | Triggers vibration based on a preset effect. |
| VibrateFromFile | Triggers vibration based on a custom vibration configuration file. [since 10] |
| VibrateFromPattern | Triggers vibration based on a custom effect. [since 18] |

