# VibratorInfoParam

Defines the vibrator parameters. If **VibratorInfoParam** is left unspecified, an API applies to all vibrators of the local device by default.

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-vibrator-interface VibratorInfoParam--><!--Device-vibrator-interface VibratorInfoParam-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## deviceId

```TypeScript
deviceId?: int
```

Device ID. The default value is **-1**, indicating the local device. Since API version 19, you can use  
[getVibratorInfoSync]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ or [on]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ to query the device ID.

**Type:** int

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-VibratorInfoParam-deviceId?: int--><!--Device-VibratorInfoParam-deviceId?: int-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## vibratorId

```TypeScript
vibratorId?: int
```

Vibrator ID. The default value is **0**, which indicates all vibrators of the local device. Since API version 19,you can use [getVibratorInfoSync]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ or [on]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ to query the vibrator ID.

**Type:** int

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-VibratorInfoParam-vibratorId?: int--><!--Device-VibratorInfoParam-vibratorId?: int-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

