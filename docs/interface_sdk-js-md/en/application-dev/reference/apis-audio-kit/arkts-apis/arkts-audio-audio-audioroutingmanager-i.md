# AudioRoutingManager

This interface implements audio routing management. Before calling any API in AudioRoutingManager, you must use [getRoutingManager](arkts-audio-audio-audiomanager-i.md#getroutingmanager) to obtain an AudioRoutingManager instance. > **NOTE：**> > - The initial APIs of this interface are supported since API version 9.

**Since:** 23

<!--Device-audio-interface AudioRoutingManager--><!--Device-audio-interface AudioRoutingManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

## Modules to Import

```TypeScript
import { audio } from '@kit.AudioKit';
import { audioHaptic } from '@kit.AudioKit';
```

## declareDeviceTypesCompatibility

```TypeScript
declareDeviceTypesCompatibility(deviceTypes: DeviceTypeArray): void
```

Declares the original device types that the application has adapted to. By default, the system returns anonymous device types. This method allows applications to declare which specific device types they have explicitly adapted to. Once declared, the system will return the original device types to the application instead of the anonymous ones. Note: This method only supports device types introduced from API 20 onwards (such as hearing aids and nearlink devices). If this interface is not called for these new device types, the application will only be able to obtain anonymous device types. Legacy device types prior to API 20 do not need this declaration.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioRoutingManager-declareDeviceTypesCompatibility(deviceTypes: DeviceTypeArray): void--><!--Device-AudioRoutingManager-declareDeviceTypesCompatibility(deviceTypes: DeviceTypeArray): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceTypes | [DeviceTypeArray](arkts-audio-audio-devicetypearray-t.md) | Yes | Array of original device types the application has adapted to. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed, the param deviceTypes contains value that is invalid enum or is not device type introduced in API 20 onwards. |

## getAvailableDevices

```TypeScript
getAvailableDevices(deviceUsage: DeviceUsage): AudioDeviceDescriptors
```

Obtains the available audio devices. This API returns the result synchronously.

**Since:** 23

<!--Device-AudioRoutingManager-getAvailableDevices(deviceUsage: DeviceUsage): AudioDeviceDescriptors--><!--Device-AudioRoutingManager-getAvailableDevices(deviceUsage: DeviceUsage): AudioDeviceDescriptors-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceUsage | [DeviceUsage](arkts-audio-audio-deviceusage-e.md) | Yes | Audio device type (classified by usage). |

**Return value:**

| Type | Description |
| --- | --- |
| [AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md) | Device list. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## getDevices

```TypeScript
getDevices(deviceFlag: DeviceFlag, callback: AsyncCallback<AudioDeviceDescriptors>): void
```

Obtains the audio devices with a specific flag. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AudioRoutingManager-getDevices(deviceFlag: DeviceFlag, callback: AsyncCallback<AudioDeviceDescriptors>): void--><!--Device-AudioRoutingManager-getDevices(deviceFlag: DeviceFlag, callback: AsyncCallback<AudioDeviceDescriptors>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceFlag | DeviceFlag | Yes | Audio device flag. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the audio devices obtained; otherwise, **err** is an error object. |

## getDevices

```TypeScript
getDevices(deviceFlag: DeviceFlag): Promise<AudioDeviceDescriptors>
```

Obtains the audio devices with a specific flag. This API uses a promise to return the result.

**Since:** 23

<!--Device-AudioRoutingManager-getDevices(deviceFlag: DeviceFlag): Promise<AudioDeviceDescriptors>--><!--Device-AudioRoutingManager-getDevices(deviceFlag: DeviceFlag): Promise<AudioDeviceDescriptors>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceFlag | DeviceFlag | Yes | Audio device flag. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; | Promise used to return the device list. |

## getDevicesSync

```TypeScript
getDevicesSync(deviceFlag: DeviceFlag): AudioDeviceDescriptors
```

Obtains the audio devices with a specific flag. This API returns the result synchronously.

**Since:** 23

<!--Device-AudioRoutingManager-getDevicesSync(deviceFlag: DeviceFlag): AudioDeviceDescriptors--><!--Device-AudioRoutingManager-getDevicesSync(deviceFlag: DeviceFlag): AudioDeviceDescriptors-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceFlag | DeviceFlag | Yes | Audio device flag. |

**Return value:**

| Type | Description |
| --- | --- |
| [AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md) | Device list. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## getPreferOutputDeviceForRendererInfo

```TypeScript
getPreferOutputDeviceForRendererInfo(rendererInfo: AudioRendererInfo, callback: AsyncCallback<AudioDeviceDescriptors>): void
```

Obtains the output device with the highest priority based on the audio renderer information. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AudioRoutingManager-getPreferOutputDeviceForRendererInfo(rendererInfo: AudioRendererInfo, callback: AsyncCallback<AudioDeviceDescriptors>): void--><!--Device-AudioRoutingManager-getPreferOutputDeviceForRendererInfo(rendererInfo: AudioRendererInfo, callback: AsyncCallback<AudioDeviceDescriptors>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rendererInfo | [AudioRendererInfo](arkts-audio-audio-audiorendererinfo-i.md) | Yes | Audio renderer information. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the output device with the highest priority obtained; otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. Return by callback. |
| [6800301](../errorcode-audio.md#6800301-system-error) | System error. Return by callback. |

## getPreferOutputDeviceForRendererInfo

```TypeScript
getPreferOutputDeviceForRendererInfo(rendererInfo: AudioRendererInfo): Promise<AudioDeviceDescriptors>
```

Obtains the output device with the highest priority based on the audio renderer information. This API uses a promise to return the result.

**Since:** 23

<!--Device-AudioRoutingManager-getPreferOutputDeviceForRendererInfo(rendererInfo: AudioRendererInfo): Promise<AudioDeviceDescriptors>--><!--Device-AudioRoutingManager-getPreferOutputDeviceForRendererInfo(rendererInfo: AudioRendererInfo): Promise<AudioDeviceDescriptors>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rendererInfo | [AudioRendererInfo](arkts-audio-audio-audiorendererinfo-i.md) | Yes | Audio renderer information. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; | Promise used to return the information about the output device with the highest priority. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. Return by promise. |
| [6800301](../errorcode-audio.md#6800301-system-error) | System error. Return by promise. |

## getPreferredInputDeviceForCapturerInfo

```TypeScript
getPreferredInputDeviceForCapturerInfo(capturerInfo: AudioCapturerInfo, callback: AsyncCallback<AudioDeviceDescriptors>): void
```

Obtains the input device with the highest priority based on the audio capturer information. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AudioRoutingManager-getPreferredInputDeviceForCapturerInfo(capturerInfo: AudioCapturerInfo, callback: AsyncCallback<AudioDeviceDescriptors>): void--><!--Device-AudioRoutingManager-getPreferredInputDeviceForCapturerInfo(capturerInfo: AudioCapturerInfo, callback: AsyncCallback<AudioDeviceDescriptors>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| capturerInfo | [AudioCapturerInfo](arkts-audio-audio-audiocapturerinfo-i.md) | Yes | Audio capturer information. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the input device with the highest priority obtained; otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. Return by callback. |
| [6800301](../errorcode-audio.md#6800301-system-error) | System error. Return by callback. |

## getPreferredInputDeviceForCapturerInfo

```TypeScript
getPreferredInputDeviceForCapturerInfo(capturerInfo: AudioCapturerInfo): Promise<AudioDeviceDescriptors>
```

Obtains the input device with the highest priority based on the audio capturer information. This API uses a promise to return the result.

**Since:** 23

<!--Device-AudioRoutingManager-getPreferredInputDeviceForCapturerInfo(capturerInfo: AudioCapturerInfo): Promise<AudioDeviceDescriptors>--><!--Device-AudioRoutingManager-getPreferredInputDeviceForCapturerInfo(capturerInfo: AudioCapturerInfo): Promise<AudioDeviceDescriptors>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| capturerInfo | [AudioCapturerInfo](arkts-audio-audio-audiocapturerinfo-i.md) | Yes | Audio capturer information. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; | Promise used to return the information about the input device with the highest priority. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. Return by promise. |
| [6800301](../errorcode-audio.md#6800301-system-error) | System error. Return by promise. |

## getPreferredInputDeviceForCapturerInfoSync

```TypeScript
getPreferredInputDeviceForCapturerInfoSync(capturerInfo: AudioCapturerInfo): AudioDeviceDescriptors
```

Gets preferred input device for target audio capturer info.

**Since:** 23

<!--Device-AudioRoutingManager-getPreferredInputDeviceForCapturerInfoSync(capturerInfo: AudioCapturerInfo): AudioDeviceDescriptors--><!--Device-AudioRoutingManager-getPreferredInputDeviceForCapturerInfoSync(capturerInfo: AudioCapturerInfo): AudioDeviceDescriptors-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| capturerInfo | [AudioCapturerInfo](arkts-audio-audio-audiocapturerinfo-i.md) | Yes | Audio capturer information. |

**Return value:**

| Type | Description |
| --- | --- |
| [AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md) | Information about the input device with the highest priority. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## getPreferredOutputDeviceForRendererInfoSync

```TypeScript
getPreferredOutputDeviceForRendererInfoSync(rendererInfo: AudioRendererInfo): AudioDeviceDescriptors
```

Obtains the output device with the highest priority based on the audio renderer information. This API returns the result synchronously.

**Since:** 23

<!--Device-AudioRoutingManager-getPreferredOutputDeviceForRendererInfoSync(rendererInfo: AudioRendererInfo): AudioDeviceDescriptors--><!--Device-AudioRoutingManager-getPreferredOutputDeviceForRendererInfoSync(rendererInfo: AudioRendererInfo): AudioDeviceDescriptors-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rendererInfo | [AudioRendererInfo](arkts-audio-audio-audiorendererinfo-i.md) | Yes | Audio renderer information. |

**Return value:**

| Type | Description |
| --- | --- |
| [AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md) | Information about the output device with the highest priority. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## isCommunicationDeviceActive

```TypeScript
isCommunicationDeviceActive(deviceType: CommunicationDeviceType, callback: AsyncCallback<boolean>): void
```

Checks whether a communication device is active. This API uses an asynchronous callback to return the result.

**Since:** 23

<!--Device-AudioRoutingManager-isCommunicationDeviceActive(deviceType: CommunicationDeviceType, callback: AsyncCallback<boolean>): void--><!--Device-AudioRoutingManager-isCommunicationDeviceActive(deviceType: CommunicationDeviceType, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Communication

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceType | [CommunicationDeviceType](arkts-audio-audio-communicationdevicetype-e.md) | Yes | Active audio device type. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;boolean&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is **true** if the device is active or **false** if not active; otherwise, **err** is an error object. |

## isCommunicationDeviceActive

```TypeScript
isCommunicationDeviceActive(deviceType: CommunicationDeviceType): Promise<boolean>
```

Checks whether a communication device is active. This API uses a promise to return the result.

**Since:** 23

<!--Device-AudioRoutingManager-isCommunicationDeviceActive(deviceType: CommunicationDeviceType): Promise<boolean>--><!--Device-AudioRoutingManager-isCommunicationDeviceActive(deviceType: CommunicationDeviceType): Promise<boolean>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Communication

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceType | [CommunicationDeviceType](arkts-audio-audio-communicationdevicetype-e.md) | Yes | Active audio device type. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result, indicating whether the device is active. **true** if active, **false** otherwise. |

## isCommunicationDeviceActiveSync

```TypeScript
isCommunicationDeviceActiveSync(deviceType: CommunicationDeviceType): boolean
```

Checks whether a communication device is active. This API returns the result synchronously.

**Since:** 23

<!--Device-AudioRoutingManager-isCommunicationDeviceActiveSync(deviceType: CommunicationDeviceType): boolean--><!--Device-AudioRoutingManager-isCommunicationDeviceActiveSync(deviceType: CommunicationDeviceType): boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Communication

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceType | [CommunicationDeviceType](arkts-audio-audio-communicationdevicetype-e.md) | Yes | Active audio device type. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result for whether the device is active. **true** if active, **false** otherwise. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## isMicBlockDetectionSupported

```TypeScript
isMicBlockDetectionSupported():Promise<boolean>
```

Checks whether the current device supports microphone blocking detection. This API uses a promise to return the result.

**Since:** 23

<!--Device-AudioRoutingManager-isMicBlockDetectionSupported():Promise<boolean>--><!--Device-AudioRoutingManager-isMicBlockDetectionSupported():Promise<boolean>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result, indicating the support for microphone blocking detection. **true** if supported, **false** otherwise. |

## offAvailableDeviceChange

```TypeScript
offAvailableDeviceChange(callback?: Callback<DeviceChangeAction>): void
```

UnSubscribes to available device change events.

**Since:** 23

<!--Device-AudioRoutingManager-offAvailableDeviceChange(callback?: Callback<DeviceChangeAction>): void--><!--Device-AudioRoutingManager-offAvailableDeviceChange(callback?: Callback<DeviceChangeAction>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[DeviceChangeAction](arkts-audio-audio-devicechangeaction-i.md)&gt; | No | Callback used to obtain the device update details. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## offDeviceChange

```TypeScript
offDeviceChange(callback?: Callback<DeviceChangeAction>): void
```

UnSubscribes to device change events.

**Since:** 23

<!--Device-AudioRoutingManager-offDeviceChange(callback?: Callback<DeviceChangeAction>): void--><!--Device-AudioRoutingManager-offDeviceChange(callback?: Callback<DeviceChangeAction>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[DeviceChangeAction](arkts-audio-audio-devicechangeaction-i.md)&gt; | No | Callback used to obtain the device update details. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## offMicBlockStatusChanged

```TypeScript
offMicBlockStatusChanged(callback?: Callback<DeviceBlockStatusInfo>): void
```

Unsubscribes microphone blocked events.

**Since:** 23

<!--Device-AudioRoutingManager-offMicBlockStatusChanged(callback?: Callback<DeviceBlockStatusInfo>): void--><!--Device-AudioRoutingManager-offMicBlockStatusChanged(callback?: Callback<DeviceBlockStatusInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[DeviceBlockStatusInfo](arkts-audio-audio-deviceblockstatusinfo-i.md)&gt; | No | Callback used to obtain the microphone block status. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## offPreferOutputDeviceChangeForRendererInfo

```TypeScript
offPreferOutputDeviceChangeForRendererInfo(callback?: Callback<AudioDeviceDescriptors>): void
```

UnSubscribes to prefer output device change events.

**Since:** 23

<!--Device-AudioRoutingManager-offPreferOutputDeviceChangeForRendererInfo(callback?: Callback<AudioDeviceDescriptors>): void--><!--Device-AudioRoutingManager-offPreferOutputDeviceChangeForRendererInfo(callback?: Callback<AudioDeviceDescriptors>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; | No | Callback used to obtain the changed prefer devices in subscribe. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## offPreferredInputDeviceChangeForCapturerInfo

```TypeScript
offPreferredInputDeviceChangeForCapturerInfo(callback?: Callback<AudioDeviceDescriptors>): void
```

Unsubscribes to preferred input device change events.

**Since:** 23

<!--Device-AudioRoutingManager-offPreferredInputDeviceChangeForCapturerInfo(callback?: Callback<AudioDeviceDescriptors>): void--><!--Device-AudioRoutingManager-offPreferredInputDeviceChangeForCapturerInfo(callback?: Callback<AudioDeviceDescriptors>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; | No | Callback used to obtain the changed preferred devices in subscribe. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## off_availableDeviceChange('availableDeviceChange')

```TypeScript
off(type: 'availableDeviceChange', callback?: Callback<DeviceChangeAction>): void
```

Unsubscribes from the event indicating that the connection status of an available audio device is changed. This API uses an asynchronous callback to return the result.

**Since:** 12

<!--Device-AudioRoutingManager-off(type: 'availableDeviceChange', callback?: Callback<DeviceChangeAction>): void--><!--Device-AudioRoutingManager-off(type: 'availableDeviceChange', callback?: Callback<DeviceChangeAction>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'availableDeviceChange' | Yes | Event type. The event **'availableDeviceChange'** is triggered when the connection status of available audio devices is changed. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[DeviceChangeAction](arkts-audio-audio-devicechangeaction-i.md)&gt; | No | Callback used to return the available device change details. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## off_deviceChange('deviceChange')

```TypeScript
off(type: 'deviceChange', callback?: Callback<DeviceChangeAction>): void
```

Unsubscribes from the event indicating that the connection status of an audio device is changed. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-AudioRoutingManager-off(type: 'deviceChange', callback?: Callback<DeviceChangeAction>): void--><!--Device-AudioRoutingManager-off(type: 'deviceChange', callback?: Callback<DeviceChangeAction>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'deviceChange' | Yes | Event type. The event **'deviceChange'** is triggered when the connection status of an audio device is changed. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[DeviceChangeAction](arkts-audio-audio-devicechangeaction-i.md)&gt; | No | Callback used to return the device change details. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## off_micBlockStatusChanged('micBlockStatusChanged')

```TypeScript
off(type: 'micBlockStatusChanged', callback?: Callback<DeviceBlockStatusInfo>): void
```

Unsubscribes from the microphone blocked status change event. This API uses an asynchronous callback to return the result.

**Since:** 13

<!--Device-AudioRoutingManager-off(type: 'micBlockStatusChanged', callback?: Callback<DeviceBlockStatusInfo>): void--><!--Device-AudioRoutingManager-off(type: 'micBlockStatusChanged', callback?: Callback<DeviceBlockStatusInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'micBlockStatusChanged' | Yes | Event type. The event **'micBlockStatusChanged'** is triggered when the microphone blocked status is changed. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[DeviceBlockStatusInfo](arkts-audio-audio-deviceblockstatusinfo-i.md)&gt; | No | Callback used to return the microphone blocked status and device information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## off_preferOutputDeviceChangeForRendererInfo('preferOutputDeviceChangeForRendererInfo')

```TypeScript
off(type: 'preferOutputDeviceChangeForRendererInfo', callback?: Callback<AudioDeviceDescriptors>): void
```

Unsubscribes from the change event of the output device with the highest priority. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-AudioRoutingManager-off(type: 'preferOutputDeviceChangeForRendererInfo', callback?: Callback<AudioDeviceDescriptors>): void--><!--Device-AudioRoutingManager-off(type: 'preferOutputDeviceChangeForRendererInfo', callback?: Callback<AudioDeviceDescriptors>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'preferOutputDeviceChangeForRendererInfo' | Yes | Event type. The event **'preferOutputDeviceChangeForRendererInfo'** is triggered when the output device with the highest priority is changed. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; | No | Callback used to return the information about the output device with the highest priority. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## off_preferredInputDeviceChangeForCapturerInfo('preferredInputDeviceChangeForCapturerInfo')

```TypeScript
off(type: 'preferredInputDeviceChangeForCapturerInfo', callback?: Callback<AudioDeviceDescriptors>): void
```

Unsubscribes from the change event of the input device with the highest priority. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-AudioRoutingManager-off(type: 'preferredInputDeviceChangeForCapturerInfo', callback?: Callback<AudioDeviceDescriptors>): void--><!--Device-AudioRoutingManager-off(type: 'preferredInputDeviceChangeForCapturerInfo', callback?: Callback<AudioDeviceDescriptors>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'preferredInputDeviceChangeForCapturerInfo' | Yes | Event type. The event **'preferredInputDeviceChangeForCapturerInfo'** is triggered when the input device with the highest priority is changed. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; | No | Callback used to return the information about the input device with the highest priority. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## onAvailableDeviceChange

```TypeScript
onAvailableDeviceChange(deviceUsage: DeviceUsage, callback: Callback<DeviceChangeAction>): void
```

Subscribes to available device change events. When a device is connected/disconnected, registered clients will receive the callback.

**Since:** 23

<!--Device-AudioRoutingManager-onAvailableDeviceChange(deviceUsage: DeviceUsage, callback: Callback<DeviceChangeAction>): void--><!--Device-AudioRoutingManager-onAvailableDeviceChange(deviceUsage: DeviceUsage, callback: Callback<DeviceChangeAction>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceUsage | [DeviceUsage](arkts-audio-audio-deviceusage-e.md) | Yes | Audio device usage. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[DeviceChangeAction](arkts-audio-audio-devicechangeaction-i.md)&gt; | Yes | Callback used to obtain the device update details. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## onDeviceChange

```TypeScript
onDeviceChange(deviceFlag: DeviceFlag, callback: Callback<DeviceChangeAction>): void
```

Subscribes to device change events. When a device is connected/disconnected, registered clients will receive the callback.

**Since:** 23

<!--Device-AudioRoutingManager-onDeviceChange(deviceFlag: DeviceFlag, callback: Callback<DeviceChangeAction>): void--><!--Device-AudioRoutingManager-onDeviceChange(deviceFlag: DeviceFlag, callback: Callback<DeviceChangeAction>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceFlag | DeviceFlag | Yes | Audio device flag. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[DeviceChangeAction](arkts-audio-audio-devicechangeaction-i.md)&gt; | Yes | Callback used to obtain the device update details. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## onMicBlockStatusChanged

```TypeScript
onMicBlockStatusChanged(callback: Callback<DeviceBlockStatusInfo>): void
```

Subscribes microphone blocked events. Before subscribing, users should query whether block detection is supported on current device. The caller will receive the callback only when it is recording and the used microphones' block status have changed. Currently, block detecting is only support for microphones located on the local device.

**Since:** 23

<!--Device-AudioRoutingManager-onMicBlockStatusChanged(callback: Callback<DeviceBlockStatusInfo>): void--><!--Device-AudioRoutingManager-onMicBlockStatusChanged(callback: Callback<DeviceBlockStatusInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[DeviceBlockStatusInfo](arkts-audio-audio-deviceblockstatusinfo-i.md)&gt; | Yes | Callback used to obtain the microphone block status. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## onPreferOutputDeviceChangeForRendererInfo

```TypeScript
onPreferOutputDeviceChangeForRendererInfo(rendererInfo: AudioRendererInfo, callback: Callback<AudioDeviceDescriptors>): void
```

Subscribes to prefer output device change events. When prefer device for target audio renderer info changes, registered clients will receive the callback.

**Since:** 23

<!--Device-AudioRoutingManager-onPreferOutputDeviceChangeForRendererInfo(rendererInfo: AudioRendererInfo, callback: Callback<AudioDeviceDescriptors>): void--><!--Device-AudioRoutingManager-onPreferOutputDeviceChangeForRendererInfo(rendererInfo: AudioRendererInfo, callback: Callback<AudioDeviceDescriptors>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rendererInfo | [AudioRendererInfo](arkts-audio-audio-audiorendererinfo-i.md) | Yes | Audio renderer information. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; | Yes | Callback used to obtain the changed prefer devices information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## onPreferredInputDeviceChangeForCapturerInfo

```TypeScript
onPreferredInputDeviceChangeForCapturerInfo(capturerInfo: AudioCapturerInfo, callback: Callback<AudioDeviceDescriptors>): void
```

Subscribes to preferred input device change events. When preferred device for target audio capturer info changes, registered clients will receive the callback.

**Since:** 23

<!--Device-AudioRoutingManager-onPreferredInputDeviceChangeForCapturerInfo(capturerInfo: AudioCapturerInfo, callback: Callback<AudioDeviceDescriptors>): void--><!--Device-AudioRoutingManager-onPreferredInputDeviceChangeForCapturerInfo(capturerInfo: AudioCapturerInfo, callback: Callback<AudioDeviceDescriptors>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| capturerInfo | [AudioCapturerInfo](arkts-audio-audio-audiocapturerinfo-i.md) | Yes | Audio capturer information. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; | Yes | Callback used to obtain the changed preferred devices information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## on_availableDeviceChange('availableDeviceChange')

```TypeScript
on(type: 'availableDeviceChange', deviceUsage: DeviceUsage, callback: Callback<DeviceChangeAction>): void
```

Subscribes to the event indicating that the connection status of an available audio device is changed. This API uses an asynchronous callback to return the result.

**Since:** 12

<!--Device-AudioRoutingManager-on(type: 'availableDeviceChange', deviceUsage: DeviceUsage, callback: Callback<DeviceChangeAction>): void--><!--Device-AudioRoutingManager-on(type: 'availableDeviceChange', deviceUsage: DeviceUsage, callback: Callback<DeviceChangeAction>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'availableDeviceChange' | Yes | Event type. The event **'availableDeviceChange'** is triggered when the connection status of available audio devices is changed. |
| deviceUsage | [DeviceUsage](arkts-audio-audio-deviceusage-e.md) | Yes | Audio device type (classified by usage). |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[DeviceChangeAction](arkts-audio-audio-devicechangeaction-i.md)&gt; | Yes | Callback used to return the device change details. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## on_deviceChange('deviceChange')

```TypeScript
on(type: 'deviceChange', deviceFlag: DeviceFlag, callback: Callback<DeviceChangeAction>): void
```

Subscribes to the event indicating that the connection status of an audio device is changed. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-AudioRoutingManager-on(type: 'deviceChange', deviceFlag: DeviceFlag, callback: Callback<DeviceChangeAction>): void--><!--Device-AudioRoutingManager-on(type: 'deviceChange', deviceFlag: DeviceFlag, callback: Callback<DeviceChangeAction>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'deviceChange' | Yes | Event type. The event **'deviceChange'** is triggered when the connection status of an audio device is changed. |
| deviceFlag | DeviceFlag | Yes | Audio device flag. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[DeviceChangeAction](arkts-audio-audio-devicechangeaction-i.md)&gt; | Yes | Callback used to return the device change details. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## on_micBlockStatusChanged('micBlockStatusChanged')

```TypeScript
on(type: 'micBlockStatusChanged', callback: Callback<DeviceBlockStatusInfo>): void
```

Subscribes to the microphone blocked status change event. This API uses an asynchronous callback to return the result. Before using this API, check whether the current device supports microphone blocking detection. This event is triggered when the microphone blocked status changes during recording. Currently, this API takes effect only for the microphone on the local device.

**Since:** 13

<!--Device-AudioRoutingManager-on(type: 'micBlockStatusChanged', callback: Callback<DeviceBlockStatusInfo>): void--><!--Device-AudioRoutingManager-on(type: 'micBlockStatusChanged', callback: Callback<DeviceBlockStatusInfo>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'micBlockStatusChanged' | Yes | Event type. The event **'micBlockStatusChanged'** is triggered when the microphone blocked status is changed. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[DeviceBlockStatusInfo](arkts-audio-audio-deviceblockstatusinfo-i.md)&gt; | Yes | Callback used to return the microphone blocked status and device information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## on_preferOutputDeviceChangeForRendererInfo('preferOutputDeviceChangeForRendererInfo')

```TypeScript
on(type: 'preferOutputDeviceChangeForRendererInfo', rendererInfo: AudioRendererInfo, callback: Callback<AudioDeviceDescriptors>): void
```

Subscribes to the change event of the output device with the highest priority, which is triggered when the output device with the highest priority is changed. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-AudioRoutingManager-on(type: 'preferOutputDeviceChangeForRendererInfo', rendererInfo: AudioRendererInfo, callback: Callback<AudioDeviceDescriptors>): void--><!--Device-AudioRoutingManager-on(type: 'preferOutputDeviceChangeForRendererInfo', rendererInfo: AudioRendererInfo, callback: Callback<AudioDeviceDescriptors>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'preferOutputDeviceChangeForRendererInfo' | Yes | Event type. The event **'preferOutputDeviceChangeForRendererInfo'** is triggered when the output device with the highest priority is changed. |
| rendererInfo | [AudioRendererInfo](arkts-audio-audio-audiorendererinfo-i.md) | Yes | Audio renderer information. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; | Yes | Callback used to return the information about the output device with the highest priority. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## on_preferredInputDeviceChangeForCapturerInfo('preferredInputDeviceChangeForCapturerInfo')

```TypeScript
on(type: 'preferredInputDeviceChangeForCapturerInfo', capturerInfo: AudioCapturerInfo, callback: Callback<AudioDeviceDescriptors>): void
```

Subscribes to the change event of the input device with the highest priority, which is triggered when the input device with the highest priority is changed. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-AudioRoutingManager-on(type: 'preferredInputDeviceChangeForCapturerInfo', capturerInfo: AudioCapturerInfo, callback: Callback<AudioDeviceDescriptors>): void--><!--Device-AudioRoutingManager-on(type: 'preferredInputDeviceChangeForCapturerInfo', capturerInfo: AudioCapturerInfo, callback: Callback<AudioDeviceDescriptors>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Device

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'preferredInputDeviceChangeForCapturerInfo' | Yes | Event type. The event **'preferredInputDeviceChangeForCapturerInfo'** is triggered when the input device with the highest priority is changed. |
| capturerInfo | [AudioCapturerInfo](arkts-audio-audio-audiocapturerinfo-i.md) | Yes | Audio capturer information. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)&gt; | Yes | Callback used to return the information about the input device with the highest priority. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [6800101](../errorcode-audio.md#6800101-invalid-parameter) | Parameter verification failed. |

## setCommunicationDevice

```TypeScript
setCommunicationDevice(deviceType: CommunicationDeviceType, active: boolean, callback: AsyncCallback<void>): void
```

Sets a communication device to the active state. This API uses an asynchronous callback to return the result. This API will be deprecated in a later version due to function design is changed. You are not advised to use it. You are advised to use the [AVCastPicker component](../../../media/avsession/using-switch-call-devices.md) provided by AVSession to switch between call devices.

**Since:** 23

<!--Device-AudioRoutingManager-setCommunicationDevice(deviceType: CommunicationDeviceType, active: boolean, callback: AsyncCallback<void>): void--><!--Device-AudioRoutingManager-setCommunicationDevice(deviceType: CommunicationDeviceType, active: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Multimedia.Audio.Communication

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceType | [CommunicationDeviceType](arkts-audio-audio-communicationdevicetype-e.md) | Yes | Audio device flag. |
| active | boolean | Yes | Active state to set. **true** to set the device to the active state, **false** otherwise. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;void&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

## setCommunicationDevice

```TypeScript
setCommunicationDevice(deviceType: CommunicationDeviceType, active: boolean): Promise<void>
```

Sets a communication device to the active state. This API uses a promise to return the result. This API will be deprecated in a later version due to function design is changed. You are not advised to use it. You are advised to use the [AVCastPicker component](../../../media/avsession/using-switch-call-devices.md) provided by AVSession to switch between call devices.

**Since:** 23

<!--Device-AudioRoutingManager-setCommunicationDevice(deviceType: CommunicationDeviceType, active: boolean): Promise<void>--><!--Device-AudioRoutingManager-setCommunicationDevice(deviceType: CommunicationDeviceType, active: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.Audio.Communication

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceType | [CommunicationDeviceType](arkts-audio-audio-communicationdevicetype-e.md) | Yes | Active audio device type. |
| active | boolean | Yes | Active state to set. **true** to set the device to the active state, **false** otherwise. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

