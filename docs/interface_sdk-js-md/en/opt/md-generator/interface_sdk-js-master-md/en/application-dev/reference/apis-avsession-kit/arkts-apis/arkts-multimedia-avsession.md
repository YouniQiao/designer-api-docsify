# @ohos.multimedia.avsession

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare namespace avSession--><!--Device-unnamed-declare namespace avSession-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## Modules to Import

```TypeScript
import { avSession } from '@kit.AVSessionKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [createAVSession](arkts-avsession-avsession-createavsession-f.md#createAVSession) |
| [createAVSession](arkts-avsession-avsession-createavsession-f.md#createAVSession) |
| [getAVSession](arkts-avsession-avsession-getavsession-f.md#getAVSession) |
| [isDesktopLyricSupported](arkts-avsession-avsession-isdesktoplyricsupported-f.md#isDesktopLyricSupported) |
| [offSessionCreate](arkts-avsession-avsession-offsessioncreate-f.md#offSessionCreate) |
| [offSessionDestroy](arkts-avsession-avsession-offsessiondestroy-f.md#offSessionDestroy) |
| [offTopSessionChange](arkts-avsession-avsession-offtopsessionchange-f.md#offTopSessionChange) |
| [onSessionCreate](arkts-avsession-avsession-onsessioncreate-f.md#onSessionCreate) |
| [onSessionDestroy](arkts-avsession-avsession-onsessiondestroy-f.md#onSessionDestroy) |
| [onTopSessionChange](arkts-avsession-avsession-ontopsessionchange-f.md#onTopSessionChange) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [castAudio](arkts-avsession-avsession-castaudio-f-sys.md#castAudio-(System-API)) |
| [castAudio](arkts-avsession-avsession-castaudio-f-sys.md#castAudio-(System-API)) |
| [castAudioSession](arkts-avsession-avsession-castaudiosession-f-sys.md#castAudioSession-(System-API)) |
| [castAudioSession](arkts-avsession-avsession-castaudiosession-f-sys.md#castAudioSession-(System-API)) |
| [castAudioSessionAll](arkts-avsession-avsession-castaudiosessionall-f-sys.md#castAudioSessionAll-(System-API)) |
| [createController](arkts-avsession-avsession-createcontroller-f-sys.md#createController-(System-API)) |
| [createController](arkts-avsession-avsession-createcontroller-f-sys.md#createController-(System-API)) |
| [getAVCastController](arkts-avsession-avsession-getavcastcontroller-f-sys.md#getAVCastController-(System-API)) |
| [getAVCastController](arkts-avsession-avsession-getavcastcontroller-f-sys.md#getAVCastController-(System-API)) |
| [getAVCastController](arkts-avsession-avsession-getavcastcontroller-f-sys.md#getAVCastController-(System-API)) |
| [getAVCastController](arkts-avsession-avsession-getavcastcontroller-f-sys.md#getAVCastController-(System-API)) |
| [getAllSessionDescriptors](arkts-avsession-avsession-getallsessiondescriptors-f-sys.md#getAllSessionDescriptors-(System-API)) |
| [getAllSessionDescriptors](arkts-avsession-avsession-getallsessiondescriptors-f-sys.md#getAllSessionDescriptors-(System-API)) |
| [getDistributedSessionController](arkts-avsession-avsession-getdistributedsessioncontroller-f-sys.md#getDistributedSessionController-(System-API)) |
| [getHistoricalAVQueueInfos](arkts-avsession-avsession-gethistoricalavqueueinfos-f-sys.md#getHistoricalAVQueueInfos-(System-API)) |
| [getHistoricalAVQueueInfos](arkts-avsession-avsession-gethistoricalavqueueinfos-f-sys.md#getHistoricalAVQueueInfos-(System-API)) |
| [getHistoricalSessionDescriptors](arkts-avsession-avsession-gethistoricalsessiondescriptors-f-sys.md#getHistoricalSessionDescriptors-(System-API)) |
| [getHistoricalSessionDescriptors](arkts-avsession-avsession-gethistoricalsessiondescriptors-f-sys.md#getHistoricalSessionDescriptors-(System-API)) |
| [getSessionDescriptors](arkts-avsession-avsession-getsessiondescriptors-f-sys.md#getSessionDescriptors-(System-API)) |
| [offActiveSessionChanged](arkts-avsession-avsession-offactivesessionchanged-f-sys.md#offActiveSessionChanged-(System-API)) |
| [offDeviceAvailable](arkts-avsession-avsession-offdeviceavailable-f-sys.md#offDeviceAvailable-(System-API)) |
| [offDeviceLogEvent](arkts-avsession-avsession-offdevicelogevent-f-sys.md#offDeviceLogEvent-(System-API)) |
| [offDeviceOffline](arkts-avsession-avsession-offdeviceoffline-f-sys.md#offDeviceOffline-(System-API)) |
| [offDeviceStateChanged](arkts-avsession-avsession-offdevicestatechanged-f-sys.md#offDeviceStateChanged-(System-API)) |
| [offDistributedSessionChange](arkts-avsession-avsession-offdistributedsessionchange-f-sys.md#offDistributedSessionChange-(System-API)) |
| [offSessionServiceDie](arkts-avsession-avsession-offsessionservicedie-f-sys.md#offSessionServiceDie-(System-API)) |
| [offSystemCommonEvent](arkts-avsession-avsession-offsystemcommonevent-f-sys.md#offSystemCommonEvent-(System-API)) |
| [off_deviceAvailable](arkts-avsession-avsession-offdeviceavailable-f-sys.md) |
| [off_deviceLogEvent](arkts-avsession-avsession-offdevicelogevent-f-sys.md) |
| [off_deviceOffline](arkts-avsession-avsession-offdeviceoffline-f-sys.md) |
| [off_deviceStateChanged](arkts-avsession-avsession-offdevicestatechanged-f-sys.md) |
| [off_distributedSessionChange](arkts-avsession-avsession-offdistributedsessionchange-f-sys.md) |
| [off_sessionCreate](arkts-avsession-avsession-offsessioncreate-f-sys.md#off_sessionCreate) |
| [off_sessionDestroy](arkts-avsession-avsession-offsessiondestroy-f-sys.md#off_sessionDestroy) |
| [off_sessionServiceDie](arkts-avsession-avsession-offsessionservicedie-f-sys.md) |
| [off_topSessionChange](arkts-avsession-avsession-offtopsessionchange-f-sys.md#off_topSessionChange) |
| [onActiveSessionChanged](arkts-avsession-avsession-onactivesessionchanged-f-sys.md#onActiveSessionChanged-(System-API)) |
| [onDeviceAvailable](arkts-avsession-avsession-ondeviceavailable-f-sys.md#onDeviceAvailable-(System-API)) |
| [onDeviceLogEvent](arkts-avsession-avsession-ondevicelogevent-f-sys.md#onDeviceLogEvent-(System-API)) |
| [onDeviceOffline](arkts-avsession-avsession-ondeviceoffline-f-sys.md#onDeviceOffline-(System-API)) |
| [onDeviceStateChanged](arkts-avsession-avsession-ondevicestatechanged-f-sys.md#onDeviceStateChanged-(System-API)) |
| [onDistributedSessionChange](arkts-avsession-avsession-ondistributedsessionchange-f-sys.md#onDistributedSessionChange-(System-API)) |
| [onSessionServiceDie](arkts-avsession-avsession-onsessionservicedie-f-sys.md#onSessionServiceDie-(System-API)) |
| [onSystemCommonEvent](arkts-avsession-avsession-onsystemcommonevent-f-sys.md#onSystemCommonEvent-(System-API)) |
| [on_deviceAvailable](arkts-avsession-avsession-ondeviceavailable-f-sys.md) |
| [on_deviceLogEvent](arkts-avsession-avsession-ondevicelogevent-f-sys.md) |
| [on_deviceOffline](arkts-avsession-avsession-ondeviceoffline-f-sys.md) |
| [on_deviceStateChanged](arkts-avsession-avsession-ondevicestatechanged-f-sys.md) |
| [on_distributedSessionChange](arkts-avsession-avsession-ondistributedsessionchange-f-sys.md) |
| [on_sessionCreate](arkts-avsession-avsession-onsessioncreate-f-sys.md#on_sessionCreate) |
| [on_sessionDestroy](arkts-avsession-avsession-onsessiondestroy-f-sys.md#on_sessionDestroy) |
| [on_sessionServiceDie](arkts-avsession-avsession-onsessionservicedie-f-sys.md) |
| [on_topSessionChange](arkts-avsession-avsession-ontopsessionchange-f-sys.md#on_topSessionChange) |
| [sendSystemAVKeyEvent](arkts-avsession-avsession-sendsystemavkeyevent-f-sys.md#sendSystemAVKeyEvent-(System-API)) |
| [sendSystemAVKeyEvent](arkts-avsession-avsession-sendsystemavkeyevent-f-sys.md#sendSystemAVKeyEvent-(System-API)) |
| [sendSystemCommonCommand](arkts-avsession-avsession-sendsystemcommoncommand-f-sys.md#sendSystemCommonCommand-(System-API)) |
| [sendSystemControlCommand](arkts-avsession-avsession-sendsystemcontrolcommand-f-sys.md#sendSystemControlCommand-(System-API)) |
| [sendSystemControlCommand](arkts-avsession-avsession-sendsystemcontrolcommand-f-sys.md#sendSystemControlCommand-(System-API)) |
| [setDiscoverable](arkts-avsession-avsession-setdiscoverable-f-sys.md#setDiscoverable-(System-API)) |
| [setDiscoverable](arkts-avsession-avsession-setdiscoverable-f-sys.md#setDiscoverable-(System-API)) |
| [startAVPlayback](arkts-avsession-avsession-startavplayback-f-sys.md#startAVPlayback-(System-API)) |
| [startAVPlayback](arkts-avsession-avsession-startavplayback-f-sys.md#startAVPlayback-(System-API)) |
| [startCastDeviceDiscovery](arkts-avsession-avsession-startcastdevicediscovery-f-sys.md#startCastDeviceDiscovery-(System-API)) |
| [startCastDeviceDiscovery](arkts-avsession-avsession-startcastdevicediscovery-f-sys.md#startCastDeviceDiscovery-(System-API)) |
| [startCastDeviceDiscovery](arkts-avsession-avsession-startcastdevicediscovery-f-sys.md#startCastDeviceDiscovery-(System-API)) |
| [startCasting](arkts-avsession-avsession-startcasting-f-sys.md#startCasting-(System-API)) |
| [startCasting](arkts-avsession-avsession-startcasting-f-sys.md#startCasting-(System-API)) |
| [startDeviceLogging](arkts-avsession-avsession-startdevicelogging-f-sys.md#startDeviceLogging-(System-API)) |
| [stopCastDeviceDiscovery](arkts-avsession-avsession-stopcastdevicediscovery-f-sys.md#stopCastDeviceDiscovery-(System-API)) |
| [stopCastDeviceDiscovery](arkts-avsession-avsession-stopcastdevicediscovery-f-sys.md#stopCastDeviceDiscovery-(System-API)) |
| [stopCasting](arkts-avsession-avsession-stopcasting-f-sys.md#stopCasting-(System-API)) |
| [stopCasting](arkts-avsession-avsession-stopcasting-f-sys.md#stopCasting-(System-API)) |
| [stopDeviceLogging](arkts-avsession-avsession-stopdevicelogging-f-sys.md#stopDeviceLogging-(System-API)) |
<!--DelEnd-->

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AVCastPickerHelper](arkts-avsession-avsession-avcastpickerhelper-c.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AVCallState](arkts-avsession-avsession-avcallstate-i.md) |
| [AVCastControlCommand](arkts-avsession-avsession-avcastcontrolcommand-i.md) |
| [AVCastController](arkts-avsession-avsession-avcastcontroller-i.md) |
| [AVCastPickerOptions](arkts-avsession-avsession-avcastpickeroptions-i.md) |
| [AVControlCommand](arkts-avsession-avsession-avcontrolcommand-i.md) |
| [AVMediaDescription](arkts-avsession-avsession-avmediadescription-i.md) |
| [AVMetadata](arkts-avsession-avsession-avmetadata-i.md) |
| [AVPlaybackState](arkts-avsession-avsession-avplaybackstate-i.md) |
| [AVQueueItem](arkts-avsession-avsession-avqueueitem-i.md) |
| [AVSession](arkts-avsession-avsession-avsession-i.md) |
| [AVSessionController](arkts-avsession-avsession-avsessioncontroller-i.md) |
| [AudioCapabilities](arkts-avsession-avsession-audiocapabilities-i.md) |
| [CallMetadata](arkts-avsession-avsession-callmetadata-i.md) |
| [CastDisplayInfo](arkts-avsession-avsession-castdisplayinfo-i.md) |
| [CommandInfo](arkts-avsession-avsession-commandinfo-i.md) |
| [DesktopLyricState](arkts-avsession-avsession-desktoplyricstate-i.md) |
| [DeviceInfo](arkts-avsession-avsession-deviceinfo-i.md) |
| [MenuPosition](arkts-avsession-avsession-menuposition-i.md) |
| [OutputDeviceInfo](arkts-avsession-avsession-outputdeviceinfo-i.md) |
| [PlaybackPosition](arkts-avsession-avsession-playbackposition-i.md) |

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AVCastController](arkts-avsession-avsession-avcastcontroller-i-sys.md) |
| [AVQueueInfo](arkts-avsession-avsession-avqueueinfo-i-sys.md) |
| [AVSessionDescriptor](arkts-avsession-avsession-avsessiondescriptor-i-sys.md) |
| [DeviceInfo](arkts-avsession-avsession-deviceinfo-i-sys.md) |
| [DeviceState](arkts-avsession-avsession-devicestate-i-sys.md) |
| [HiPlayDeviceInfo](arkts-avsession-avsession-hiplaydeviceinfo-i-sys.md) |
| [SessionToken](arkts-avsession-avsession-sessiontoken-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AVCastCategory](arkts-avsession-avsession-avcastcategory-e.md) |
| [AVSessionErrorCode](arkts-avsession-avsession-avsessionerrorcode-e.md) |
| [BackgroundPlayMode](arkts-avsession-avsession-backgroundplaymode-e.md) |
| [CallState](arkts-avsession-avsession-callstate-e.md) |
| [CallerType](arkts-avsession-avsession-callertype-e.md) |
| [CastDisplayState](arkts-avsession-avsession-castdisplaystate-e.md) |
| [ConnectionState](arkts-avsession-avsession-connectionstate-e.md) |
| [DecoderType](arkts-avsession-avsession-decodertype-e.md) |
| [DeviceType](arkts-avsession-avsession-devicetype-e.md) |
| [DisplayTag](arkts-avsession-avsession-displaytag-e.md) |
| [ExtraKey](arkts-avsession-avsession-extrakey-e.md) |
| [LoopMode](arkts-avsession-avsession-loopmode-e.md) |
| [PlaybackState](arkts-avsession-avsession-playbackstate-e.md) |
| [ProtocolType](arkts-avsession-avsession-protocoltype-e.md) |
| [ResolutionLevel](arkts-avsession-avsession-resolutionlevel-e.md) |
| [SkipIntervals](arkts-avsession-avsession-skipintervals-e.md) |

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ConnectionState](arkts-avsession-avsession-connectionstate-e-sys.md) |
| [DeviceLogEventCode](arkts-avsession-avsession-devicelogeventcode-e-sys.md) |
| [DistributedSessionType](arkts-avsession-avsession-distributedsessiontype-e-sys.md) |
| [ExtraKey](arkts-avsession-avsession-extrakey-e-sys.md) |
| [ProtocolType](arkts-avsession-avsession-protocoltype-e-sys.md) |
| [SessionCategory](arkts-avsession-avsession-sessioncategory-e-sys.md) |
<!--DelEnd-->

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AVCastControlCommandType](arkts-avsession-avsession-avcastcontrolcommandtype-t.md) |
| [AVControlCommandType](arkts-avsession-avsession-avcontrolcommandtype-t.md) |
| [AVMediaCenterControlType](arkts-avsession-avsession-avmediacentercontroltype-t.md) |
| [AVSessionType](arkts-avsession-avsession-avsessiontype-t.md) |
| [ConnectionEvent](arkts-avsession-avsession-connectionevent-t.md) |
| [EventProcess](arkts-avsession-avsession-eventprocess-t.md) |
| [ExtraInfo](arkts-avsession-avsession-extrainfo-t.md) |
| [KeyRequestCallback](arkts-avsession-avsession-keyrequestcallback-t.md) |
| [NoParamCallback](arkts-avsession-avsession-noparamcallback-t.md) |
| [TwoParamCallback](arkts-avsession-avsession-twoparamcallback-t.md) |
| [VideoSizeEvent](arkts-avsession-avsession-videosizeevent-t.md) |
