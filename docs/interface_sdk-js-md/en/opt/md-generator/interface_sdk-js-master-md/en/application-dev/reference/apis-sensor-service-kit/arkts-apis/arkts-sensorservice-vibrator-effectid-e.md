# EffectId

Enumerates the preset vibration effect IDs. This parameter is needed when you call [vibrator.startVibration9+](arkts-sensorservice-vibrator-startvibration-f.md#startVibration) or [vibrator.stopVibration9+](arkts-sensorservice-vibrator-stopvibration-f.md#stopVibration) to deliver the vibration effect specified by [VibratePreset](arkts-sensorservice-vibrator-vibratepreset-i.md#VibratePreset). This parameter supports a variety of values, such as **haptic.clock.timer**. [HapticFeedback&lt;sup&gt;12+&lt;/sup&gt;](arkts-sensorservice-vibrator-hapticfeedback-e.md#HapticFeedback) provides several frequently used **EffectId** values. > **NOTE：**> > Preset effects vary according to devices. You are advised to call > [vibrator.isSupportEffect](arkts-sensorservice-vibrator-issupporteffect-f.md#isSupportEffect)&lt;sup&gt;10+&lt;/sup&gt; to check whether the > device supports the preset effect before use.

**Since:** 23

**Deprecated since:** -1

<!--Device-vibrator-enum EffectId--><!--Device-vibrator-enum EffectId-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## EFFECT_CLOCK_TIMER

```TypeScript
EFFECT_CLOCK_TIMER = 'haptic.clock.timer'
```

Vibration effect when a user adjusts the timer.

**Since:** 23

**Deprecated since:** -1

<!--Device-EffectId-EFFECT_CLOCK_TIMER = 'haptic.clock.timer'--><!--Device-EffectId-EFFECT_CLOCK_TIMER = 'haptic.clock.timer'-End-->

**System capability:** SystemCapability.Sensors.MiscDevice
