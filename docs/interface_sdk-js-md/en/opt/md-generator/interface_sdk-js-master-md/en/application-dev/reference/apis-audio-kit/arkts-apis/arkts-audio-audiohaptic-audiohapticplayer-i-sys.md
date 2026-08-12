# AudioHapticPlayer

Implements audio-haptic playback. Before calling any API in AudioHapticPlayer, you must use   
[createPlayer](arkts-audio-audiohaptic-audiohapticmanager-i.md#createPlayer) to create an AudioHapticPlayer instance.

**Since:** 11

<!--Device-audioHaptic-interface AudioHapticPlayer--><!--Device-audioHaptic-interface AudioHapticPlayer-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

## Modules to Import

```TypeScript
import { audioHaptic } from '@kit.AudioKit';
```

## enableHapticsInSilentMode

```TypeScript
enableHapticsInSilentMode(enable: boolean): void
```

Enable haptics when the ringer mode is silent mode.This function should be called before player start or after stop, and before release.

**Since:** 20

<!--Device-AudioHapticPlayer-enableHapticsInSilentMode(enable: boolean): void--><!--Device-AudioHapticPlayer-enableHapticsInSilentMode(enable: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## isHapticsIntensityAdjustmentSupported

```TypeScript
isHapticsIntensityAdjustmentSupported(): boolean
```

Check whether the device supports haptics intensity adjustment.

**Since:** 20

<!--Device-AudioHapticPlayer-isHapticsIntensityAdjustmentSupported(): boolean--><!--Device-AudioHapticPlayer-isHapticsIntensityAdjustmentSupported(): boolean-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## isHapticsRampSupported

```TypeScript
isHapticsRampSupported(): boolean
```

Check whether the device supports haptics intensity ramp effect.

**Since:** 20

<!--Device-AudioHapticPlayer-isHapticsRampSupported(): boolean--><!--Device-AudioHapticPlayer-isHapticsRampSupported(): boolean-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## setHapticsIntensity

```TypeScript
setHapticsIntensity(intensity: number): Promise<void>
```

Set haptics intensity for this player. This method uses a promise to return the result.This function should be called before player release, and can only set once for each starting process.

**Since:** 20

<!--Device-AudioHapticPlayer-setHapticsIntensity(intensity: double): Promise<void>--><!--Device-AudioHapticPlayer-setHapticsIntensity(intensity: double): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| intensity | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [5400108](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400108-parameter-value-out-of-range) |

## setHapticsRamp

```TypeScript
setHapticsRamp(duration: number, startIntensity: number, endIntensity: number): Promise<void>
```

Set haptics intensity ramp effect for this player. This method uses a promise to return the result.This function should be called before player start or after stop, and before release.

**Since:** 20

<!--Device-AudioHapticPlayer-setHapticsRamp(duration: int, startIntensity: double, endIntensity: double): Promise<void>--><!--Device-AudioHapticPlayer-setHapticsRamp(duration: int, startIntensity: double, endIntensity: double): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| duration | number | Yes |
| startIntensity | number | Yes |
| endIntensity | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [5400102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400102-unsupported-operation) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [5400108](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400108-parameter-value-out-of-range) |
