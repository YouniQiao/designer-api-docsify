# VibrateAttribute

Describes the vibration attribute.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-vibrator-interface VibrateAttribute--><!--Device-vibrator-interface VibrateAttribute-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## deviceId

```TypeScript
deviceId?: int
```

Device ID. The default value is **-1**, indicating the local device. Since API version 19, you can use  
[getVibratorInfoSync]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ or [on]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ to query the device ID.

This API can be used in atomic services since API version 19.

**Type:** int

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-VibrateAttribute-deviceId?: int--><!--Device-VibrateAttribute-deviceId?: int-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## id

```TypeScript
id?: int
```

Vibrator ID. The default value is **0**.

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-VibrateAttribute-id?: int--><!--Device-VibrateAttribute-id?: int-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

## usage

```TypeScript
usage: Usage
```

Vibration scenario. The default value is **unknown**. The value must be an enum defined in  
[Usage]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

**Type:** Usage

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-VibrateAttribute-usage: Usage--><!--Device-VibrateAttribute-usage: Usage-End-->

**System capability:** SystemCapability.Sensors.MiscDevice

