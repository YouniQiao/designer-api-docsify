# AudioHapticPlayer

音振播放器，提供音振协同播放功能。在调用AudioHapticPlayer的接口前，需要先通过  
[createPlayer](arkts-audio-audiohaptic-audiohapticmanager-i.md#createplayer)创建实例。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-audioHaptic-interface AudioHapticPlayer--><!--Device-audioHaptic-interface AudioHapticPlayer-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

## Modules to Import

```TypeScript
import { audioHaptic } from 'kits/@kit.AudioKit';
```

## enableHapticsInSilentMode

```TypeScript
enableHapticsInSilentMode(enable: boolean): void
```

Enable haptics when the ringer mode is silent mode.这个方法只能在播放器start前，或stop后release前调用

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-AudioHapticPlayer-enableHapticsInSilentMode(enable: boolean): void--><!--Device-AudioHapticPlayer-enableHapticsInSilentMode(enable: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | use { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5400102 | Operate not permit in current state. |
| 202 | Caller is not a system application. |

## isHapticsIntensityAdjustmentSupported

```TypeScript
isHapticsIntensityAdjustmentSupported(): boolean
```

Check whether the device supports haptics intensity adjustment.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-AudioHapticPlayer-isHapticsIntensityAdjustmentSupported(): boolean--><!--Device-AudioHapticPlayer-isHapticsIntensityAdjustmentSupported(): boolean-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| boolean | { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | Caller is not a system application. |

## isHapticsRampSupported

```TypeScript
isHapticsRampSupported(): boolean
```

Check whether the device supports haptics intensity ramp effect.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-AudioHapticPlayer-isHapticsRampSupported(): boolean--><!--Device-AudioHapticPlayer-isHapticsRampSupported(): boolean-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| boolean | { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | Caller is not a system application. |

## setHapticsIntensity

ArkTS-Dyn:
```TypeScript
setHapticsIntensity(intensity: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
setHapticsIntensity(intensity: double): Promise<void>
```

Set haptics intensity for this player. This method uses a promise to return the result.这个方法只能在播放器释放前调用，并且每次播放过程只能设置一次。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-AudioHapticPlayer-setHapticsIntensity(intensity: double): Promise<void>--><!--Device-AudioHapticPlayer-setHapticsIntensity(intensity: double): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| intensity | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Target Haptics intensity. The value ranges from 0.00 to 1.00, where 1.00 indicates the maximum intensity (100%). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Function is not supported in current device. |
| 5400102 | Operate not permit in current state. |
| 202 | Caller is not a system application. |
| 5400108 | Parameter out of range. |

## setHapticsRamp

ArkTS-Dyn:
```TypeScript
setHapticsRamp(duration: number, startIntensity: number, endIntensity: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
setHapticsRamp(duration: int, startIntensity: double, endIntensity: double): Promise<void>
```

Set haptics intensity ramp effect for this player. This method uses a promise to return the result.这个方法只能在播放器start前，或stop后release前调用

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-AudioHapticPlayer-setHapticsRamp(duration: int, startIntensity: double, endIntensity: double): Promise<void>--><!--Device-AudioHapticPlayer-setHapticsRamp(duration: int, startIntensity: double, endIntensity: double): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| duration | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | ramp duration to set, unit is milliseconds. The value should be an integer, and not less than 100. |
| startIntensity | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | Starting intensity for Haptics ramp to set. The value ranges from 0.00 to 1.00. 1.00 indicates the maximum intensity (100%). |
| endIntensity | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | End intensity for haptics ramp to set. The value ranges from 0.00 to 1.00. 1.00 indicates the maximum intensity (100%). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise used to return the result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Function is not supported in current device. |
| 5400102 | Operate not permit in current state. |
| 202 | Caller is not a system application. |
| 5400108 | Parameter out of range. |

