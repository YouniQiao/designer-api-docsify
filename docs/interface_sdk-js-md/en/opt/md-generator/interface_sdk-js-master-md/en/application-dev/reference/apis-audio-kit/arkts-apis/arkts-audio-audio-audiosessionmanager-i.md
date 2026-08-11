# AudioSessionManager

This interface implements audio session management.

Before calling any API in AudioSessionManager, you must use  
[getSessionManager](arkts-audio-audio-audiomanager-i.md#getsessionmanager) to obtain an AudioSessionManager instance.

> **NOTE：**
> 
> - The initial APIs of this interface are supported since API version 12.

**Since:** 12

<!--Device-audio-interface AudioSessionManager--><!--Device-audio-interface AudioSessionManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## activateAudioSession

```TypeScript
activateAudioSession(strategy: AudioSessionStrategy): Promise<void>
```

Activates an audio session. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AudioSessionManager-activateAudioSession(strategy: AudioSessionStrategy): Promise<void>--><!--Device-AudioSessionManager-activateAudioSession(strategy: AudioSessionStrategy): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strategy | [AudioSessionStrategy](arkts-audio-audio-audiosessionstrategy-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [6800301](../errorcode-audio.md#6800301-system-error) |

## clearSelectedMediaInputDevice

```TypeScript
clearSelectedMediaInputDevice(): Promise<void>
```

Clears the media input device set by calling  
[selectMediaInputDevice](arkts-audio-audio-audiosessionmanager-i.md#selectmediainputdevice). This API uses a promise to return the result.

**Since:** 21

<!--Device-AudioSessionManager-clearSelectedMediaInputDevice(): Promise<void>--><!--Device-AudioSessionManager-clearSelectedMediaInputDevice(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6800301](../errorcode-audio.md#6800301-system-error) |

## deactivateAudioSession

```TypeScript
deactivateAudioSession(): Promise<void>
```

Deactivates this audio session. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AudioSessionManager-deactivateAudioSession(): Promise<void>--><!--Device-AudioSessionManager-deactivateAudioSession(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6800301](../errorcode-audio.md#6800301-system-error) |

## enableMuteSuggestionWhenMixWithOthers

```TypeScript
enableMuteSuggestionWhenMixWithOthers(enable: boolean): void
```

Enables mute suggestion notifications for mixed playback.

Typically, when the audio mixing mode is used, if two applications plays audio at the same time, their audio streams are mixed. In certain scenarios (such as games or broadcasts), applications can mute their own audio to provide a better user experience.

If this feature is enabled, mute and unmute suggestions will be sent through the  
[AudioSessionStateChangedEvent](arkts-audio-audio-audiosessionstatechangedevent-i.md) callback after the audio session state change event is subscribed to. Receiving the muted suggestion indicates that another application starts to play audio, and the played audio and the audio of this application cannot be mixed.

This feature can be used only by audio sessions for which  
[AudioSessionScene](arkts-audio-audio-audiosessionscene-e.md) has been set and the  
**CONCURRENCY_MIX_WITH_OTHERS** mode has been activated. This feature takes effect only once when the audio session is activated. You need to enable it again before each activation of the audio session.

For details, see  
[Enabling Mute Suggestion Notifications for Mixed Playback](../../../media/audio/audio-session-management.md#enabling-mute-suggestion-notifications-for-mixed-playback).

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioSessionManager-enableMuteSuggestionWhenMixWithOthers(enable: boolean): void--><!--Device-AudioSessionManager-enableMuteSuggestionWhenMixWithOthers(enable: boolean): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6800103](../errorcode-audio.md#6800103-unsupported-state) |
| [6800301](../errorcode-audio.md#6800301-system-error) |

## getAvailableDevices

```TypeScript
getAvailableDevices(deviceUsage: DeviceUsage): AudioDeviceDescriptors
```

Obtains the available audio devices.

**Since:** 21

<!--Device-AudioSessionManager-getAvailableDevices(deviceUsage: DeviceUsage): AudioDeviceDescriptors--><!--Device-AudioSessionManager-getAvailableDevices(deviceUsage: DeviceUsage): AudioDeviceDescriptors-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceUsage | [DeviceUsage](arkts-audio-audio-deviceusage-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [6800301](../errorcode-audio.md#6800301-system-error) |

## getBluetoothAndNearlinkPreferredRecordCategory

```TypeScript
getBluetoothAndNearlinkPreferredRecordCategory(): BluetoothAndNearlinkPreferredRecordCategory
```

Obtains the preferred device category for recording with Bluetooth or NearLink, which is set by calling  
[setBluetoothAndNearlinkPreferredRecordCategory](arkts-audio-audio-audiosessionmanager-i.md#setbluetoothandnearlinkpreferredrecordcategory).

**Since:** 21

<!--Device-AudioSessionManager-getBluetoothAndNearlinkPreferredRecordCategory(): BluetoothAndNearlinkPreferredRecordCategory--><!--Device-AudioSessionManager-getBluetoothAndNearlinkPreferredRecordCategory(): BluetoothAndNearlinkPreferredRecordCategory-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [BluetoothAndNearlinkPreferredRecordCategory](arkts-audio-audio-bluetoothandnearlinkpreferredrecordcategory-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [6800301](../errorcode-audio.md#6800301-system-error) |

## getDefaultOutputDevice

```TypeScript
getDefaultOutputDevice(): DeviceType
```

Obtains the default audio output device set by calling  
[setDefaultOutputDevice](arkts-audio-audio-audiosessionmanager-i.md#setdefaultoutputdevice).

**Since:** 20

<!--Device-AudioSessionManager-getDefaultOutputDevice(): DeviceType--><!--Device-AudioSessionManager-getDefaultOutputDevice(): DeviceType-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DeviceType](../../apis-localization-kit/arkts-apis/arkts-localization-resourcemanager-devicetype-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [6800103](../errorcode-audio.md#6800103-unsupported-state) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## getSelectedMediaInputDevice

```TypeScript
getSelectedMediaInputDevice(): AudioDeviceDescriptor
```

Obtains the media input device set by calling  
[selectMediaInputDevice](arkts-audio-audio-audiosessionmanager-i.md#selectmediainputdevice). If no device has been specified, the device with **deviceType** set to **INVALID** is returned.

**Since:** 21

<!--Device-AudioSessionManager-getSelectedMediaInputDevice(): AudioDeviceDescriptor--><!--Device-AudioSessionManager-getSelectedMediaInputDevice(): AudioDeviceDescriptor-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AudioDeviceDescriptor](arkts-audio-audio-audiodevicedescriptor-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [6800301](../errorcode-audio.md#6800301-system-error) |

## isAudioSessionActivated

```TypeScript
isAudioSessionActivated(): boolean
```

Checks whether this audio session is activated.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AudioSessionManager-isAudioSessionActivated(): boolean--><!--Device-AudioSessionManager-isAudioSessionActivated(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## isOtherMediaPlaying

```TypeScript
isOtherMediaPlaying(): boolean
```

Check whether any other application is currently playing audio of the four media types: **MUSIC**, **MOVIE**,  
**AUDIOBOOK**, and **GAME**. Audio sessions that have activated these media types will also be checked.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioSessionManager-isOtherMediaPlaying(): boolean--><!--Device-AudioSessionManager-isOtherMediaPlaying(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## off('audioSessionDeactivated')

```TypeScript
off(type: 'audioSessionDeactivated', callback?: Callback<AudioSessionDeactivatedEvent>): void
```

Unsubscribes from the audio session deactivation event. This API uses an asynchronous callback to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AudioSessionManager-off(type: 'audioSessionDeactivated', callback?: Callback<AudioSessionDeactivatedEvent>): void--><!--Device-AudioSessionManager-off(type: 'audioSessionDeactivated', callback?: Callback<AudioSessionDeactivatedEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'audioSessionDeactivated' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioSessionDeactivatedEvent&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## off('audioSessionStateChanged')

```TypeScript
off(type: 'audioSessionStateChanged', callback?: Callback<AudioSessionStateChangedEvent>): void
```

Unsubscribes from the audio session state change event. This API uses an asynchronous callback to return the result.

**Since:** 20

<!--Device-AudioSessionManager-off(type: 'audioSessionStateChanged', callback?: Callback<AudioSessionStateChangedEvent>): void--><!--Device-AudioSessionManager-off(type: 'audioSessionStateChanged', callback?: Callback<AudioSessionStateChangedEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'audioSessionStateChanged' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioSessionStateChangedEvent&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [6800301](../errorcode-audio.md#6800301-system-error) |

## off('currentOutputDeviceChanged')

```TypeScript
off(type: 'currentOutputDeviceChanged', callback?: Callback<CurrentOutputDeviceChangedEvent>): void
```

Unsubscribes from the current output device change event. This API uses an asynchronous callback to return the result.

**Since:** 20

<!--Device-AudioSessionManager-off(type: 'currentOutputDeviceChanged', callback?: Callback<CurrentOutputDeviceChangedEvent>): void--><!--Device-AudioSessionManager-off(type: 'currentOutputDeviceChanged', callback?: Callback<CurrentOutputDeviceChangedEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'currentOutputDeviceChanged' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;CurrentOutputDeviceChangedEvent&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [6800301](../errorcode-audio.md#6800301-system-error) |

## off('availableDeviceChange')

```TypeScript
off(type: 'availableDeviceChange', callback?: Callback<DeviceChangeAction>): void
```

Unsubscribes from the event indicating that the connection status of an available audio device is changed.

**Since:** 21

<!--Device-AudioSessionManager-off(type: 'availableDeviceChange', callback?: Callback<DeviceChangeAction>): void--><!--Device-AudioSessionManager-off(type: 'availableDeviceChange', callback?: Callback<DeviceChangeAction>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'availableDeviceChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DeviceChangeAction&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [6800301](../errorcode-audio.md#6800301-system-error) |

## off('currentInputDeviceChanged')

```TypeScript
off(type: 'currentInputDeviceChanged', callback?: Callback<CurrentInputDeviceChangedEvent>): void
```

Unsubscribes from the current input device change event.

**Since:** 21

<!--Device-AudioSessionManager-off(type: 'currentInputDeviceChanged', callback?: Callback<CurrentInputDeviceChangedEvent>): void--><!--Device-AudioSessionManager-off(type: 'currentInputDeviceChanged', callback?: Callback<CurrentInputDeviceChangedEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'currentInputDeviceChanged' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;CurrentInputDeviceChangedEvent&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [6800301](../errorcode-audio.md#6800301-system-error) |

## on('audioSessionDeactivated')

```TypeScript
on(type: 'audioSessionDeactivated', callback: Callback<AudioSessionDeactivatedEvent>): void
```

Subscribes to the audio session deactivation event, which is triggered when an audio session is deactivated. This API uses an asynchronous callback to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-AudioSessionManager-on(type: 'audioSessionDeactivated', callback: Callback<AudioSessionDeactivatedEvent>): void--><!--Device-AudioSessionManager-on(type: 'audioSessionDeactivated', callback: Callback<AudioSessionDeactivatedEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'audioSessionDeactivated' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioSessionDeactivatedEvent&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## on('audioSessionStateChanged')

```TypeScript
on(type: 'audioSessionStateChanged', callback: Callback<AudioSessionStateChangedEvent>): void
```

Subscribes to the audio session state change event, which is triggered when the audio session focus is changed.This API uses an asynchronous callback to return the result.

**Since:** 20

<!--Device-AudioSessionManager-on(type: 'audioSessionStateChanged', callback: Callback<AudioSessionStateChangedEvent>): void--><!--Device-AudioSessionManager-on(type: 'audioSessionStateChanged', callback: Callback<AudioSessionStateChangedEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'audioSessionStateChanged' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AudioSessionStateChangedEvent&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6800102](../errorcode-audio.md#6800102-memory-allocation-failure) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [6800301](../errorcode-audio.md#6800301-system-error) |

## on('currentOutputDeviceChanged')

```TypeScript
on(type: 'currentOutputDeviceChanged', callback: Callback<CurrentOutputDeviceChangedEvent>): void
```

Subscribes to the current output device change event, which is triggered when the current output device is changed. This API uses an asynchronous callback to return the result.

**Since:** 20

<!--Device-AudioSessionManager-on(type: 'currentOutputDeviceChanged', callback: Callback<CurrentOutputDeviceChangedEvent>): void--><!--Device-AudioSessionManager-on(type: 'currentOutputDeviceChanged', callback: Callback<CurrentOutputDeviceChangedEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'currentOutputDeviceChanged' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;CurrentOutputDeviceChangedEvent&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6800102](../errorcode-audio.md#6800102-memory-allocation-failure) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [6800301](../errorcode-audio.md#6800301-system-error) |

## on('availableDeviceChange')

```TypeScript
on(type: 'availableDeviceChange', deviceUsage: DeviceUsage, callback: Callback<DeviceChangeAction>): void
```

Subscribes to the event indicating that the connection status of an available audio device is changed.

**Since:** 21

<!--Device-AudioSessionManager-on(type: 'availableDeviceChange', deviceUsage: DeviceUsage, callback: Callback<DeviceChangeAction>): void--><!--Device-AudioSessionManager-on(type: 'availableDeviceChange', deviceUsage: DeviceUsage, callback: Callback<DeviceChangeAction>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'availableDeviceChange' | Yes |
| deviceUsage | [DeviceUsage](arkts-audio-audio-deviceusage-e.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DeviceChangeAction&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [6800301](../errorcode-audio.md#6800301-system-error) |

## on('currentInputDeviceChanged')

```TypeScript
on(type: 'currentInputDeviceChanged', callback: Callback<CurrentInputDeviceChangedEvent>): void
```

Subscribes to the current input device change event, which is triggered when the current input device is changed.

**Since:** 21

<!--Device-AudioSessionManager-on(type: 'currentInputDeviceChanged', callback: Callback<CurrentInputDeviceChangedEvent>): void--><!--Device-AudioSessionManager-on(type: 'currentInputDeviceChanged', callback: Callback<CurrentInputDeviceChangedEvent>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'currentInputDeviceChanged' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;CurrentInputDeviceChangedEvent&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [6800301](../errorcode-audio.md#6800301-system-error) |

## selectMediaInputDevice

```TypeScript
selectMediaInputDevice(inputAudioDevice: AudioDeviceDescriptor): Promise<void>
```

Selects a media input device. This API uses a promise to return the result.

> **NOTE：**
> 
> - This API is not suitable for VoIP call recording; that is, it does not apply to scenarios where
> [SourceType](arkts-audio-audio-sourcetype-e.md) is **SOURCE_TYPE_VOICE_COMMUNICATION**.
> 
> - Before calling this API, call [getAvailableDevices](arkts-audio-audio-audiosessionmanager-i.md#getavailabledevices) to
> query the list of available input devices and select an input device from the list.
> 
> - If there are recording streams of other applications with higher priorities in the system, the actual input
> device used will follow the input device selected by these applications.
> 
> - Applications can listen for the
> [currentInputDeviceChanged](audio.AudioSessionManager.on(type: 'currentInputDeviceChanged', callback: Callback&lt;CurrentInputDeviceChangedEvent&gt;))
> event to find out the actual input device being used.

**Since:** 21

<!--Device-AudioSessionManager-selectMediaInputDevice(inputAudioDevice: AudioDeviceDescriptor): Promise<void>--><!--Device-AudioSessionManager-selectMediaInputDevice(inputAudioDevice: AudioDeviceDescriptor): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| inputAudioDevice | [AudioDeviceDescriptor](arkts-audio-audio-audiodevicedescriptor-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [6800301](../errorcode-audio.md#6800301-system-error) |

## setAudioSessionBehavior

```TypeScript
setAudioSessionBehavior(behavior: number): void
```

Sets audio session behavior parameters. (Multiple flags can be combined.)

> **NOTE：**
> 
> If this API is called while an audio session is active, you must call the
> [activateAudioSession](arkts-audio-audio-audiosessionmanager-i.md#activateaudiosession) API again
> for the settings to take effect.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioSessionManager-setAudioSessionBehavior(behavior: int): void--><!--Device-AudioSessionManager-setAudioSessionBehavior(behavior: int): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| behavior | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6800103](../errorcode-audio.md#6800103-unsupported-state) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |

## setAudioSessionScene

```TypeScript
setAudioSessionScene(scene: AudioSessionScene): void
```

Sets an audio session scene.

**Since:** 20

<!--Device-AudioSessionManager-setAudioSessionScene(scene: AudioSessionScene): void--><!--Device-AudioSessionManager-setAudioSessionScene(scene: AudioSessionScene): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| scene | [AudioSessionScene](arkts-audio-audio-audiosessionscene-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [6800103](../errorcode-audio.md#6800103-unsupported-state) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [6800301](../errorcode-audio.md#6800301-system-error) |

## setBluetoothAndNearlinkPreferredRecordCategory

```TypeScript
setBluetoothAndNearlinkPreferredRecordCategory(category: BluetoothAndNearlinkPreferredRecordCategory): Promise<void>
```

Sets the preferred device category for recording with Bluetooth or NearLink. This API uses a promise to return the result.

> **NOTE：**
> 
> - Applications can set this category before connecting to Bluetooth or NearLink devices, and the system
> prioritizes using the device for recording when the device is connected.
> 
> - If there are recording streams of other applications with higher priorities in the system, the actual input
> device used will follow the input device selected by these applications.
> 
> - Applications can listen for the
> [currentInputDeviceChanged](audio.AudioSessionManager.on(type: 'currentInputDeviceChanged', callback: Callback&lt;CurrentInputDeviceChangedEvent&gt;))
> event to find out the actual input device being used.

**Since:** 21

<!--Device-AudioSessionManager-setBluetoothAndNearlinkPreferredRecordCategory(category: BluetoothAndNearlinkPreferredRecordCategory): Promise<void>--><!--Device-AudioSessionManager-setBluetoothAndNearlinkPreferredRecordCategory(category: BluetoothAndNearlinkPreferredRecordCategory): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| category | [BluetoothAndNearlinkPreferredRecordCategory](arkts-audio-audio-bluetoothandnearlinkpreferredrecordcategory-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [6800301](../errorcode-audio.md#6800301-system-error) |

## setCapturerMuteHint

```TypeScript
setCapturerMuteHint(mute: boolean): Promise<void>
```

Set mute hint for all capturer streams in the current audio session. It dose not mute the recording stream, only affects internal processing strategy.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioSessionManager-setCapturerMuteHint(mute: boolean): Promise<void>--><!--Device-AudioSessionManager-setCapturerMuteHint(mute: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mute | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6800103](../errorcode-audio.md#6800103-unsupported-state) |

## setDefaultOutputDevice

```TypeScript
setDefaultOutputDevice(deviceType: DeviceType): Promise<void>
```

Sets the default audio output device. This API uses a promise to return the result.

> **NOTE：**
> 
> - This API applies to the following scenario: When
> [AudioSessionScene](arkts-audio-audio-audiosessionscene-e.md) is set to **VoIP**, the setting takes
> effect immediately after the AudioSession is activated. For non-VoIP scenarios, the setting does not take
> effect upon AudioSession activation. Instead, the setting applies when
> [StreamUsage](arkts-audio-audio-streamusage-e.md) for playback is voice message, VoIP voice call,
> or VoIP video call. Supported devices include the earpiece, speaker, and system default device.
> 
> - This API can be called at any time after an AudioSessionManager instance is created. The system records the
> device set by the application. However, the setting takes effect only after the AudioSession is activated. When
> the application starts playing, if an external device like Bluetooth headsets or wired headsets is connected,
> the system prioritizes audio output through the external device. Otherwise, the system uses the device set by
> the application.

**Since:** 20

<!--Device-AudioSessionManager-setDefaultOutputDevice(deviceType: DeviceType): Promise<void>--><!--Device-AudioSessionManager-setDefaultOutputDevice(deviceType: DeviceType): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceType | [DeviceType](../../apis-localization-kit/arkts-apis/arkts-localization-resourcemanager-devicetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6800102](../errorcode-audio.md#6800102-memory-allocation-failure) |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [6800301](../errorcode-audio.md#6800301-system-error) |

## setMediaOutputDevice

```TypeScript
setMediaOutputDevice(deviceType: DeviceType): Promise<void>
```

Set the audio output device to the built-in speaker, when other audio peripherals are connected, such as bluetooth headphones or wired headsets. It should be noted that this interface only applies to media streams.In scenarios where there are concurrent playback streams with higher priority or user selects the output device through system UI, the actual output device used by the application may differ from the selected one. The application can obtain currently active output device by subscribing to the currentOutputDeviceChanged event.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioSessionManager-setMediaOutputDevice(deviceType: DeviceType): Promise<void>--><!--Device-AudioSessionManager-setMediaOutputDevice(deviceType: DeviceType): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceType | [DeviceType](../../apis-localization-kit/arkts-apis/arkts-localization-resourcemanager-devicetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) |
| [6800301](../errorcode-audio.md#6800301-system-error) |
