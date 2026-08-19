# @ohos.multimedia.avsession

**Since:** 23

<!--Device-unnamed-declare namespace avSession--><!--Device-unnamed-declare namespace avSession-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## Modules to Import

```TypeScript
import { avSession } from '@kit.AVSessionKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [createAVSession](arkts-avsession-avsession-createavsession-f.md) | Create an AVSession instance. An ability can only create one AVSession |
| [createAVSession](arkts-avsession-avsession-createavsession-f.md) | Create an AVSession instance. An ability can only create one AVSession |
| [getAVSession](arkts-avsession-avsession-getavsession-f.md) | Get an AVSession instance if already created. |
| [isDesktopLyricSupported](arkts-avsession-avsession-isdesktoplyricsupported-f.md) | Whether desktop lyric feature is supported. |
| [offSessionCreate](arkts-avsession-avsession-offsessioncreate-f.md) | Unregister session create callback |
| [offSessionDestroy](arkts-avsession-avsession-offsessiondestroy-f.md) | Unregister session destroy callback |
| [offTopSessionChange](arkts-avsession-avsession-offtopsessionchange-f.md) | Unregister top session changed callback |
| [onSessionCreate](arkts-avsession-avsession-onsessioncreate-f.md) | Register session create callback |
| [onSessionDestroy](arkts-avsession-avsession-onsessiondestroy-f.md) | Register session destroy callback |
| [onTopSessionChange](arkts-avsession-avsession-ontopsessionchange-f.md) | Register top session changed callback |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [castAudio](arkts-avsession-avsession-castaudio-f-sys.md) | Cast Audio to the remote devices or cast back local device |
| [castAudio](arkts-avsession-avsession-castaudio-f-sys.md) | Cast Audio to the remote devices or cast back local device |
| [castAudioSession](arkts-avsession-avsession-castaudiosession-f-sys.md) | Cast Audio to the remote devices or cast back local device |
| [castAudioSession](arkts-avsession-avsession-castaudiosession-f-sys.md) | Cast Audio to the remote devices or cast back local device |
| [castAudioSessionAll](arkts-avsession-avsession-castaudiosessionall-f-sys.md) | Cast all the media audio to the remote devices or cast back local device |
| [createController](arkts-avsession-avsession-createcontroller-f-sys.md) | Create an avsession controller |
| [createController](arkts-avsession-avsession-createcontroller-f-sys.md) | Create an avsession controller |
| [getAVCastController](arkts-avsession-avsession-getavcastcontroller-f-sys.md) | Register a callback to retrieve an avsession cast controller. This function can be used at both side to get the same controller to do the playback control. |
| [getAVCastController](arkts-avsession-avsession-getavcastcontroller-f-sys.md) | Register a callback to retrieve an avsession cast controller. This function can be used at both side to get the same controller to do the playback control. |
| [getAVCastController](arkts-avsession-avsession-getavcastcontroller-f-sys.md) | Get the current session's remote controller client. If the avsession is not under casting state, the controller will return null. |
| [getAVCastController](arkts-avsession-avsession-getavcastcontroller-f-sys.md) | Get the current session's remote controller client. If the avsession is not under casting state, the controller will return undefined. |
| [getAllSessionDescriptors](arkts-avsession-avsession-getallsessiondescriptors-f-sys.md) | Get all avsession descriptors of the system |
| [getAllSessionDescriptors](arkts-avsession-avsession-getallsessiondescriptors-f-sys.md) | Get all avsession descriptors which can be shown on system entrance. |
| [getDistributedSessionController](arkts-avsession-avsession-getdistributedsessioncontroller-f-sys.md) | Get distributed avsession controller |
| [getHistoricalAVQueueInfos](arkts-avsession-avsession-gethistoricalavqueueinfos-f-sys.md) | Get history play list information records. |
| [getHistoricalAVQueueInfos](arkts-avsession-avsession-gethistoricalavqueueinfos-f-sys.md) | Get history play list information records. |
| [getHistoricalSessionDescriptors](arkts-avsession-avsession-gethistoricalsessiondescriptors-f-sys.md) | Get history avsession records. These sessions have been destroyed. |
| [getHistoricalSessionDescriptors](arkts-avsession-avsession-gethistoricalsessiondescriptors-f-sys.md) | Get history avsession records. These sessions have been destroyed. |
| [getSessionDescriptors](arkts-avsession-avsession-getsessiondescriptors-f-sys.md) | Get session descriptors of the system based on different session category. |
| [offActiveSessionChanged](arkts-avsession-avsession-offactivesessionchanged-f-sys.md) | Unregister active session changed callback. |
| [offDeviceAvailable](arkts-avsession-avsession-offdeviceavailable-f-sys.md) | Unregister device discovery callback |
| [offDeviceLogEvent](arkts-avsession-avsession-offdevicelogevent-f-sys.md) | UnRegister log event callback. |
| [offDeviceOffline](arkts-avsession-avsession-offdeviceoffline-f-sys.md) | Unregister device offline callback |
| [offDeviceStateChanged](arkts-avsession-avsession-offdevicestatechanged-f-sys.md) | Unregisters a system callback for the device connection phase. |
| [offDistributedSessionChange](arkts-avsession-avsession-offdistributedsessionchange-f-sys.md) | Unregister distributed session changed callback |
| [offSessionServiceDie](arkts-avsession-avsession-offsessionservicedie-f-sys.md) | Unregister Session service death callback, notifying the application to clean up resources. |
| [offSystemCommonEvent](arkts-avsession-avsession-offsystemcommonevent-f-sys.md) | Unregister system common event callback |
| [off_deviceAvailable](arkts-avsession-avsession-offdeviceavailable-f-sys.md) | Unregister device discovery callback |
| [off_deviceLogEvent](arkts-avsession-avsession-offdevicelogevent-f-sys.md) | UnRegister log event callback. |
| [off_deviceOffline](arkts-avsession-avsession-offdeviceoffline-f-sys.md) | Unregister device offline callback |
| [off_deviceStateChanged](arkts-avsession-avsession-offdevicestatechanged-f-sys.md) | Unregisters a system callback for the device connection phase. |
| [off_distributedSessionChange](arkts-avsession-avsession-offdistributedsessionchange-f-sys.md) | Unregister distributed session changed callback |
| [off_sessionCreate](arkts-avsession-avsession-offsessioncreate-f-sys.md#offsessioncreate) | Unregister session create callback |
| [off_sessionDestroy](arkts-avsession-avsession-offsessiondestroy-f-sys.md#offsessiondestroy) | Unregister session destroy callback |
| [off_sessionServiceDie](arkts-avsession-avsession-offsessionservicedie-f-sys.md) | Unregister Session service death callback, notifying the application to clean up resources. |
| [off_topSessionChange](arkts-avsession-avsession-offtopsessionchange-f-sys.md#offtopsessionchange) | Unregister top session changed callback |
| [onActiveSessionChanged](arkts-avsession-avsession-onactivesessionchanged-f-sys.md) | Register active session changed callback. |
| [onDeviceAvailable](arkts-avsession-avsession-ondeviceavailable-f-sys.md) | Register device discovery callback |
| [onDeviceLogEvent](arkts-avsession-avsession-ondevicelogevent-f-sys.md) | Register log event callback. |
| [onDeviceOffline](arkts-avsession-avsession-ondeviceoffline-f-sys.md) | Register device offline callback |
| [onDeviceStateChanged](arkts-avsession-avsession-ondevicestatechanged-f-sys.md) | Registers a system callback for the device connection phase. The callback includes information such as error codes, connection status, radar errors, and user behavior codes. |
| [onDistributedSessionChange](arkts-avsession-avsession-ondistributedsessionchange-f-sys.md) | Register distributed session changed callback |
| [onSessionServiceDie](arkts-avsession-avsession-onsessionservicedie-f-sys.md) | Register Session service death callback, notifying the application to clean up resources. |
| [onSystemCommonEvent](arkts-avsession-avsession-onsystemcommonevent-f-sys.md) | Register system common event callback |
| [on_deviceAvailable](arkts-avsession-avsession-ondeviceavailable-f-sys.md) | Register device discovery callback |
| [on_deviceLogEvent](arkts-avsession-avsession-ondevicelogevent-f-sys.md) | Register log event callback. |
| [on_deviceOffline](arkts-avsession-avsession-ondeviceoffline-f-sys.md) | Register device offline callback |
| [on_deviceStateChanged](arkts-avsession-avsession-ondevicestatechanged-f-sys.md) | Registers a system callback for the device connection phase. The callback includes information such as error codes, connection status, radar errors, and user behavior codes. |
| [on_distributedSessionChange](arkts-avsession-avsession-ondistributedsessionchange-f-sys.md) | Register distributed session changed callback |
| [on_sessionCreate](arkts-avsession-avsession-onsessioncreate-f-sys.md#onsessioncreate) | Register session create callback |
| [on_sessionDestroy](arkts-avsession-avsession-onsessiondestroy-f-sys.md#onsessiondestroy) | Register session destroy callback |
| [on_sessionServiceDie](arkts-avsession-avsession-onsessionservicedie-f-sys.md) | Register Session service death callback, notifying the application to clean up resources. |
| [on_topSessionChange](arkts-avsession-avsession-ontopsessionchange-f-sys.md#ontopsessionchange) | Register top session changed callback |
| [sendSystemAVKeyEvent](arkts-avsession-avsession-sendsystemavkeyevent-f-sys.md) | Send system media key event.The system automatically selects the recipient. |
| [sendSystemAVKeyEvent](arkts-avsession-avsession-sendsystemavkeyevent-f-sys.md) | Send system media key event.The system automatically selects the recipient. |
| [sendSystemCommonCommand](arkts-avsession-avsession-sendsystemcommoncommand-f-sys.md) | Send system control command. The system automatically selects the recipient. |
| [sendSystemControlCommand](arkts-avsession-avsession-sendsystemcontrolcommand-f-sys.md) | Send system control command.The system automatically selects the recipient. |
| [sendSystemControlCommand](arkts-avsession-avsession-sendsystemcontrolcommand-f-sys.md) | Send system control command.The system automatically selects the recipient. |
| [setDiscoverable](arkts-avsession-avsession-setdiscoverable-f-sys.md) | Enable or disable device to be discoverable, used at sink side. |
| [setDiscoverable](arkts-avsession-avsession-setdiscoverable-f-sys.md) | Enable or disable device to be discoverable, used at sink side. |
| [startAVPlayback](arkts-avsession-avsession-startavplayback-f-sys.md) | Start an application for media playback. |
| [startAVPlayback](arkts-avsession-avsession-startavplayback-f-sys.md) | Start an application for media playback with command info. |
| [startCastDeviceDiscovery](arkts-avsession-avsession-startcastdevicediscovery-f-sys.md) | Start device discovery. |
| [startCastDeviceDiscovery](arkts-avsession-avsession-startcastdevicediscovery-f-sys.md) | Start device discovery. |
| [startCastDeviceDiscovery](arkts-avsession-avsession-startcastdevicediscovery-f-sys.md) | Start device discovery. |
| [startCasting](arkts-avsession-avsession-startcasting-f-sys.md) | Cast resource to remote device. |
| [startCasting](arkts-avsession-avsession-startcasting-f-sys.md) | Cast resource to remote device. |
| [startDeviceLogging](arkts-avsession-avsession-startdevicelogging-f-sys.md) | Begin to write device logs into a file descriptor for the purpose of problem locating. If the logs exceed max file size, no logs will be written and DEVICE_LOG_FULL event will be omitted. |
| [stopCastDeviceDiscovery](arkts-avsession-avsession-stopcastdevicediscovery-f-sys.md) | Stop device discovery. |
| [stopCastDeviceDiscovery](arkts-avsession-avsession-stopcastdevicediscovery-f-sys.md) | Stop device discovery. |
| [stopCasting](arkts-avsession-avsession-stopcasting-f-sys.md) | Stop current cast and disconnect device connection. |
| [stopCasting](arkts-avsession-avsession-stopcasting-f-sys.md) | Stop current cast and disconnect device connection. |
| [stopDeviceLogging](arkts-avsession-avsession-stopdevicelogging-f-sys.md) | Stop the current device written even the discovery is ongoing. |
<!--DelEnd-->

### Classes

| Name | Description |
| --- | --- |
| [AVCastPickerHelper](arkts-avsession-avsession-avcastpickerhelper-c.md) | A helper to enable a picker to select output devices |

### Interfaces

| Name | Description |
| --- | --- |
| [AVCallState](arkts-avsession-avsession-avcallstate-i.md) | Used to indicate the call state of the current call. |
| [AVCastControlCommand](arkts-avsession-avsession-avcastcontrolcommand-i.md) | The definition of cast command to be sent to the session |
| [AVCastController](arkts-avsession-avsession-avcastcontroller-i.md) | AVCastController definition used to implement a remote control when a cast is connected |
| [AVCastPickerOptions](arkts-avsession-avsession-avcastpickeroptions-i.md) | An option to make different picker usage |
| [AVControlCommand](arkts-avsession-avsession-avcontrolcommand-i.md) | The definition of command to be sent to the session |
| [AVMediaDescription](arkts-avsession-avsession-avmediadescription-i.md) | The description of the media for an item in the playlist of the session |
| [AVMetadata](arkts-avsession-avsession-avmetadata-i.md) | The metadata of the current media.Used to set the properties of the current media file |
| [AVPlaybackState](arkts-avsession-avsession-avplaybackstate-i.md) | Used to indicate the playback state of the current media. If the playback state of the media changes, it needs to be updated synchronously |
| [AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md) | The item in the playlist of the session |
| [AVSession](arkts-avsession-avsession-avsession-i.md) | AVSession object. |
| [AVSessionController](arkts-avsession-avsession-avsessioncontroller-i.md) | Session controller,used to control media playback and get media information |
| [AudioCapabilities](arkts-avsession-avsession-audiocapabilities-i.md) | Audio capabilities. |
| [CallMetadata](arkts-avsession-avsession-callmetadata-i.md) | The metadata of the current call. |
| [CastDisplayInfo](arkts-avsession-avsession-castdisplayinfo-i.md) | Define the information for extended display screen. |
| [CommandInfo](arkts-avsession-avsession-commandinfo-i.md) | The definition of command information to be sent to the session |
| [DesktopLyricState](arkts-avsession-avsession-desktoplyricstate-i.md) | Desktop lyric state definition. |
| [DeviceInfo](arkts-avsession-avsession-deviceinfo-i.md) | Device Information Definition |
| [MenuPosition](arkts-avsession-avsession-menuposition-i.md) | Position definition of one component on which the menu will bind and popup. |
| [OutputDeviceInfo](arkts-avsession-avsession-outputdeviceinfo-i.md) | Target Device Information Definition |
| [PlaybackPosition](arkts-avsession-avsession-playbackposition-i.md) | Playback position definition |

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [AVCastController](arkts-avsession-avsession-avcastcontroller-i-sys.md) | AVCastController definition used to implement a remote control when a cast is connected |
| [AVQueueInfo](arkts-avsession-avsession-avqueueinfo-i-sys.md) | The play list information definition. |
| [AVSessionDescriptor](arkts-avsession-avsession-avsessiondescriptor-i-sys.md) | The description of the session |
| [DeviceInfo](arkts-avsession-avsession-deviceinfo-i-sys.md) | Device Information Definition |
| [DeviceState](arkts-avsession-avsession-devicestate-i-sys.md) | Device state used to describe states including discovery, authentication and other scenes. |
| [HiPlayDeviceInfo](arkts-avsession-avsession-hiplaydeviceinfo-i-sys.md) | HiPlay Device Information Definition |
| [SessionToken](arkts-avsession-avsession-sessiontoken-i-sys.md) | Session token. Used to judge the legitimacy of the session. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [AVCastCategory](arkts-avsession-avsession-avcastcategory-e.md) | cast category indicating different playback scenes |
| [AVSessionErrorCode](arkts-avsession-avsession-avsessionerrorcode-e.md) | Enumerates ErrorCode types, returns in BusinessError.code. |
| [BackgroundPlayMode](arkts-avsession-avsession-backgroundplaymode-e.md) | Supported background play mode definitions. |
| [CallState](arkts-avsession-avsession-callstate-e.md) | Enumeration of current call state |
| [CallerType](arkts-avsession-avsession-callertype-e.md) | Enumerates CallerType including caller source type. |
| [CastDisplayState](arkts-avsession-avsession-castdisplaystate-e.md) | Enumerates the cast display states. |
| [ConnectionState](arkts-avsession-avsession-connectionstate-e.md) | Define the device connection state. |
| [DecoderType](arkts-avsession-avsession-decodertype-e.md) | The defination of decoder type. |
| [DeviceType](arkts-avsession-avsession-devicetype-e.md) | Device type definition |
| [DisplayTag](arkts-avsession-avsession-displaytag-e.md) | The pre-defined display tag by system. |
| [ExtraKey](arkts-avsession-avsession-extrakey-e.md) | Define some common extra keys used in different scenarios. |
| [LoopMode](arkts-avsession-avsession-loopmode-e.md) | Loop Play Mode Definition |
| [PlaybackState](arkts-avsession-avsession-playbackstate-e.md) | Definition of current playback state |
| [ProtocolType](arkts-avsession-avsession-protocoltype-e.md) | Define different protocol capability |
| [ResolutionLevel](arkts-avsession-avsession-resolutionlevel-e.md) | The defination of suggested resolution. |
| [SkipIntervals](arkts-avsession-avsession-skipintervals-e.md) | Supported skip intervals definition |

<!--Del-->
### Enums(System API)

| Name | Description |
| --- | --- |
| [ConnectionState](arkts-avsession-avsession-connectionstate-e-sys.md) | Define the device connection state. |
| [DeviceLogEventCode](arkts-avsession-avsession-devicelogeventcode-e-sys.md) | Enumerates device log event code. |
| [DistributedSessionType](arkts-avsession-avsession-distributedsessiontype-e-sys.md) | Define different distributed session type |
| [ExtraKey](arkts-avsession-avsession-extrakey-e-sys.md) | Define some common extra keys used in different scenarios. |
| [ProtocolType](arkts-avsession-avsession-protocoltype-e-sys.md) | Define different protocol capability |
| [SessionCategory](arkts-avsession-avsession-sessioncategory-e-sys.md) | Session category for different scenes. |
<!--DelEnd-->

### Types

| Name | Description |
| --- | --- |
| [AVCastControlCommandType](arkts-avsession-avsession-avcastcontrolcommandtype-t.md) | The type of control command |
| [AVControlCommandType](arkts-avsession-avsession-avcontrolcommandtype-t.md) | The type of control command. |
| [AVMediaCenterControlType](arkts-avsession-avsession-avmediacentercontroltype-t.md) | The type of media center control command, which can be used to determine the button displayed on the media center. |
| [AVSessionType](arkts-avsession-avsession-avsessiontype-t.md) | Session type supports audio & video, voice_call, video_call, photo |
| [ConnectionEvent](arkts-avsession-avsession-connectionevent-t.md) | The connection event supplied by system to indicate device state and information. |
| [EventProcess](arkts-avsession-avsession-eventprocess-t.md) | The general process funcation with an event and arguments. |
| [ExtraInfo](arkts-avsession-avsession-extrainfo-t.md) | The extra info object. |
| [KeyRequestCallback](arkts-avsession-avsession-keyrequestcallback-t.md) | The callback of key request. |
| [NoParamCallback](arkts-avsession-avsession-noparamcallback-t.md) | Defines the basic callback. |
| [TwoParamCallback](arkts-avsession-avsession-twoparamcallback-t.md) | Defines the callback type including two parameters. |
| [VideoSizeEvent](arkts-avsession-avsession-videosizeevent-t.md) | The video size event. |

