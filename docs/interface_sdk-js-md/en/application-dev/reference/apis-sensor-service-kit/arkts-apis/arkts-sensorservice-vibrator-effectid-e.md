# EffectId

Enumerates the preset vibration effect IDs. This parameter is needed when you call [vibrator.startVibration9+](arkts-sensorservice-vibrator-startvibration-f.md) or [vibrator.stopVibration9+](arkts-sensorservice-vibrator-stopvibration-f.md) to deliver the vibration effect specified by [VibratePreset](arkts-sensorservice-vibrator-vibratepreset-i.md). This parameter supports a variety of values, such as **haptic.clock.timer**. [HapticFeedback&lt;sup&gt;12+&lt;/sup&gt;](arkts-sensorservice-vibrator-hapticfeedback-e.md) provides several frequently used **EffectId** values. &gt; **NOTE：**&gt; &gt; Preset effects vary according to devices. You are advised to call &gt; [vibrator.isSupportEffect](arkts-sensorservice-vibrator-issupporteffect-f.md)&lt;sup&gt;10+&lt;/sup&gt; to check whether the &gt; device supports the preset effect before use.

**Since:** 23

<!--Device-vibrator-enum EffectId--><!--Device-vibrator-enum EffectId-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## EFFECT_CLOCK_TIMER

```TypeScript
EFFECT_CLOCK_TIMER = 'haptic.clock.timer'
```

Vibration effect when a user adjusts the timer.

**Since:** 23

<!--Device-EffectId-EFFECT_CLOCK_TIMER = 'haptic.clock.timer'--><!--Device-EffectId-EFFECT_CLOCK_TIMER = 'haptic.clock.timer'-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

