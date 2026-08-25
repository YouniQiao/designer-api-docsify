# @ohos.telephony.call(拨打电话)

该模块提供呼叫管理功能，包括拨打电话、跳转到拨号界面、获取通话状态、格式化电话号码等。如需订阅通话状态请使用 `observer.on('callStateChange')` 。

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Telephony.CallManager

## 导入模块

```TypeScript
import { call } from '@kit.TelephonyKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [answerCall(拨打电话)](arkts-telephony-call-answercall-f.md) |
| [dial(拨打电话)](arkts-telephony-call-dial-f.md) |
| [dial(拨打电话)](arkts-telephony-call-dial-f.md) |
| [dial(拨打电话)](arkts-telephony-call-dial-f.md) |
| [formatPhoneNumber(拨打电话)](arkts-telephony-call-formatphonenumber-f.md) |
| [formatPhoneNumber(拨打电话)](arkts-telephony-call-formatphonenumber-f.md) |
| [formatPhoneNumber(拨打电话)](arkts-telephony-call-formatphonenumber-f.md) |
| [formatPhoneNumberToE164(拨打电话)](arkts-telephony-call-formatphonenumbertoe164-f.md) |
| [formatPhoneNumberToE164(拨打电话)](arkts-telephony-call-formatphonenumbertoe164-f.md) |
| [getCallState(拨打电话)](arkts-telephony-call-getcallstate-f.md) |
| [getCallState(拨打电话)](arkts-telephony-call-getcallstate-f.md) |
| [getCallStateSync(拨打电话)](arkts-telephony-call-getcallstatesync-f.md) |
| [getCallTransferInfo(拨打电话)](arkts-telephony-call-getcalltransferinfo-f.md) |
| [hangUpCall(拨打电话)](arkts-telephony-call-hangupcall-f.md) |
| [hasCall(拨打电话)](arkts-telephony-call-hascall-f.md) |
| [hasCall(拨打电话)](arkts-telephony-call-hascall-f.md) |
| [hasCallSync(拨打电话)](arkts-telephony-call-hascallsync-f.md) |
| [hasVoiceCapability(拨打电话)](arkts-telephony-call-hasvoicecapability-f.md) |
| [isEmergencyPhoneNumber(拨打电话)](arkts-telephony-call-isemergencyphonenumber-f.md) |
| [isEmergencyPhoneNumber(拨打电话)](arkts-telephony-call-isemergencyphonenumber-f.md) |
| [isEmergencyPhoneNumber(拨打电话)](arkts-telephony-call-isemergencyphonenumber-f.md) |
| [makeCall(拨打电话)](arkts-telephony-call-makecall-f.md) |
| [makeCall(拨打电话)](arkts-telephony-call-makecall-f.md) |
| [makeCall(拨打电话)](arkts-telephony-call-makecall-f.md) |
| [makeCall(拨打电话)](arkts-telephony-call-makecall-f.md) |
| [makeCallWithToken(拨打电话)](arkts-telephony-call-makecallwithtoken-f.md) |
| [rejectCall(拨打电话)](arkts-telephony-call-rejectcall-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [answerCall(拨打电话)](arkts-telephony-call-answercall-f-sys.md) |
| [answerCall(拨打电话)](arkts-telephony-call-answercall-f-sys.md) |
| [answerCall(拨打电话)](arkts-telephony-call-answercall-f-sys.md) |
| [answerCall(拨打电话)](arkts-telephony-call-answercall-f-sys.md) |
| [cancelCallUpgrade(拨打电话)](arkts-telephony-call-cancelcallupgrade-f-sys.md) |
| [cancelMuted(拨打电话)](arkts-telephony-call-cancelmuted-f-sys.md) |
| [cancelMuted(拨打电话)](arkts-telephony-call-cancelmuted-f-sys.md) |
| [canSetCallTransferTime(拨打电话)](arkts-telephony-call-cansetcalltransfertime-f-sys.md) |
| [canSetCallTransferTime(拨打电话)](arkts-telephony-call-cansetcalltransfertime-f-sys.md) |
| [closeUnfinishedUssd(拨打电话)](arkts-telephony-call-closeunfinishedussd-f-sys.md) |
| [closeUnfinishedUssd(拨打电话)](arkts-telephony-call-closeunfinishedussd-f-sys.md) |
| [combineConference(拨打电话)](arkts-telephony-call-combineconference-f-sys.md) |
| [combineConference(拨打电话)](arkts-telephony-call-combineconference-f-sys.md) |
| [controlCamera(拨打电话)](arkts-telephony-call-controlcamera-f-sys.md) |
| [dialCall(拨打电话)](arkts-telephony-call-dialcall-f-sys.md) |
| [dialCall(拨打电话)](arkts-telephony-call-dialcall-f-sys.md) |
| [dialCall(拨打电话)](arkts-telephony-call-dialcall-f-sys.md) |
| [disableImsSwitch(拨打电话)](arkts-telephony-call-disableimsswitch-f-sys.md) |
| [disableImsSwitch(拨打电话)](arkts-telephony-call-disableimsswitch-f-sys.md) |
| [enableImsSwitch(拨打电话)](arkts-telephony-call-enableimsswitch-f-sys.md) |
| [enableImsSwitch(拨打电话)](arkts-telephony-call-enableimsswitch-f-sys.md) |
| [getCallIdListForConference(拨打电话)](arkts-telephony-call-getcallidlistforconference-f-sys.md) |
| [getCallIdListForConference(拨打电话)](arkts-telephony-call-getcallidlistforconference-f-sys.md) |
| [getCallRestrictionStatus(拨打电话)](arkts-telephony-call-getcallrestrictionstatus-f-sys.md) |
| [getCallRestrictionStatus(拨打电话)](arkts-telephony-call-getcallrestrictionstatus-f-sys.md) |
| [getCallTransferInfo(拨打电话)](arkts-telephony-call-getcalltransferinfo-f-sys.md) |
| [getCallTransferInfo(拨打电话)](arkts-telephony-call-getcalltransferinfo-f-sys.md) |
| [getCallWaitingStatus(拨打电话)](arkts-telephony-call-getcallwaitingstatus-f-sys.md) |
| [getCallWaitingStatus(拨打电话)](arkts-telephony-call-getcallwaitingstatus-f-sys.md) |
| [getMainCallId(拨打电话)](arkts-telephony-call-getmaincallid-f-sys.md) |
| [getMainCallId(拨打电话)](arkts-telephony-call-getmaincallid-f-sys.md) |
| [getSubCallIdList(拨打电话)](arkts-telephony-call-getsubcallidlist-f-sys.md) |
| [getSubCallIdList(拨打电话)](arkts-telephony-call-getsubcallidlist-f-sys.md) |
| [getVoNRState(拨打电话)](arkts-telephony-call-getvonrstate-f-sys.md) |
| [getVoNRState(拨打电话)](arkts-telephony-call-getvonrstate-f-sys.md) |
| [hangUpCall(拨打电话)](arkts-telephony-call-hangupcall-f-sys.md) |
| [hangUpCall(拨打电话)](arkts-telephony-call-hangupcall-f-sys.md) |
| [holdCall(拨打电话)](arkts-telephony-call-holdcall-f-sys.md) |
| [holdCall(拨打电话)](arkts-telephony-call-holdcall-f-sys.md) |
| [inputDialerSpecialCode(拨打电话)](arkts-telephony-call-inputdialerspecialcode-f-sys.md) |
| [inputDialerSpecialCode(拨打电话)](arkts-telephony-call-inputdialerspecialcode-f-sys.md) |
| [isImsSwitchEnabled(拨打电话)](arkts-telephony-call-isimsswitchenabled-f-sys.md) |
| [isImsSwitchEnabled(拨打电话)](arkts-telephony-call-isimsswitchenabled-f-sys.md) |
| [isImsSwitchEnabledSync(拨打电话)](arkts-telephony-call-isimsswitchenabledsync-f-sys.md) |
| [isInEmergencyCall(拨打电话)](arkts-telephony-call-isinemergencycall-f-sys.md) |
| [isInEmergencyCall(拨打电话)](arkts-telephony-call-isinemergencycall-f-sys.md) |
| [isNewCallAllowed(拨打电话)](arkts-telephony-call-isnewcallallowed-f-sys.md) |
| [isNewCallAllowed(拨打电话)](arkts-telephony-call-isnewcallallowed-f-sys.md) |
| [isRinging(拨打电话)](arkts-telephony-call-isringing-f-sys.md) |
| [isRinging(拨打电话)](arkts-telephony-call-isringing-f-sys.md) |
| [joinConference(拨打电话)](arkts-telephony-call-joinconference-f-sys.md) |
| [joinConference(拨打电话)](arkts-telephony-call-joinconference-f-sys.md) |
| [kickOutFromConference(拨打电话)](arkts-telephony-call-kickoutfromconference-f-sys.md) |
| [kickOutFromConference(拨打电话)](arkts-telephony-call-kickoutfromconference-f-sys.md) |
| [muteRinger(拨打电话)](arkts-telephony-call-muteringer-f-sys.md) |
| [muteRinger(拨打电话)](arkts-telephony-call-muteringer-f-sys.md) |
| [off(拨打电话)](arkts-telephony-call-off-f-sys.md#offcalldetailschange) |
| [off(拨打电话)](arkts-telephony-call-off-f-sys.md#offcalleventchange) |
| [off(拨打电话)](arkts-telephony-call-off-f-sys.md#offcalldisconnectedcause) |
| [off(拨打电话)](arkts-telephony-call-off-f-sys.md#offmmicoderesult) |
| [off(拨打电话)](arkts-telephony-call-off-f-sys.md#offaudiodevicechange) |
| [off(拨打电话)](arkts-telephony-call-off-f-sys.md#offpostdialdelay) |
| [off(拨打电话)](arkts-telephony-call-off-f-sys.md#offimscallmodechange) |
| [off(拨打电话)](arkts-telephony-call-off-f-sys.md#offcallsessionevent) |
| [off(拨打电话)](arkts-telephony-call-off-f-sys.md#offpeerdimensionschange) |
| [off(拨打电话)](arkts-telephony-call-off-f-sys.md#offcameracapabilitieschange) |
| [offAudioDeviceChange(拨打电话)](arkts-telephony-call-offaudiodevicechange-f-sys.md) |
| [offCallDetailsChange(拨打电话)](arkts-telephony-call-offcalldetailschange-f-sys.md) |
| [offCallDisconnectedCause(拨打电话)](arkts-telephony-call-offcalldisconnectedcause-f-sys.md) |
| [offCallEventChange(拨打电话)](arkts-telephony-call-offcalleventchange-f-sys.md) |
| [offCallSessionEvent(拨打电话)](arkts-telephony-call-offcallsessionevent-f-sys.md) |
| [offCameraCapabilitiesChange(拨打电话)](arkts-telephony-call-offcameracapabilitieschange-f-sys.md) |
| [offImsCallModeChange(拨打电话)](arkts-telephony-call-offimscallmodechange-f-sys.md) |
| [offMmiCodeResult(拨打电话)](arkts-telephony-call-offmmicoderesult-f-sys.md) |
| [offPeerDimensionsChange(拨打电话)](arkts-telephony-call-offpeerdimensionschange-f-sys.md) |
| [offPostDialDelay(拨打电话)](arkts-telephony-call-offpostdialdelay-f-sys.md) |
| [offReceiveRttMessage(拨打电话)](arkts-telephony-call-offreceiverttmessage-f-sys.md) |
| [offRttErrCause(拨打电话)](arkts-telephony-call-offrtterrcause-f-sys.md) |
| [offRttModifyInd(拨打电话)](arkts-telephony-call-offrttmodifyind-f-sys.md) |
| [on(拨打电话)](arkts-telephony-call-on-f-sys.md#oncalldetailschange) |
| [on(拨打电话)](arkts-telephony-call-on-f-sys.md#oncalleventchange) |
| [on(拨打电话)](arkts-telephony-call-on-f-sys.md#oncalldisconnectedcause) |
| [on(拨打电话)](arkts-telephony-call-on-f-sys.md#onmmicoderesult) |
| [on(拨打电话)](arkts-telephony-call-on-f-sys.md#onaudiodevicechange) |
| [on(拨打电话)](arkts-telephony-call-on-f-sys.md#onpostdialdelay) |
| [on(拨打电话)](arkts-telephony-call-on-f-sys.md#onimscallmodechange) |
| [on(拨打电话)](arkts-telephony-call-on-f-sys.md#oncallsessionevent) |
| [on(拨打电话)](arkts-telephony-call-on-f-sys.md#onpeerdimensionschange) |
| [on(拨打电话)](arkts-telephony-call-on-f-sys.md#oncameracapabilitieschange) |
| [onAudioDeviceChange(拨打电话)](arkts-telephony-call-onaudiodevicechange-f-sys.md) |
| [onCallDetailsChange(拨打电话)](arkts-telephony-call-oncalldetailschange-f-sys.md) |
| [onCallDisconnectedCause(拨打电话)](arkts-telephony-call-oncalldisconnectedcause-f-sys.md) |
| [onCallEventChange(拨打电话)](arkts-telephony-call-oncalleventchange-f-sys.md) |
| [onCallSessionEvent(拨打电话)](arkts-telephony-call-oncallsessionevent-f-sys.md) |
| [onCameraCapabilitiesChange(拨打电话)](arkts-telephony-call-oncameracapabilitieschange-f-sys.md) |
| [onImsCallModeChange(拨打电话)](arkts-telephony-call-onimscallmodechange-f-sys.md) |
| [onMmiCodeResult(拨打电话)](arkts-telephony-call-onmmicoderesult-f-sys.md) |
| [onPeerDimensionsChange(拨打电话)](arkts-telephony-call-onpeerdimensionschange-f-sys.md) |
| [onPostDialDelay(拨打电话)](arkts-telephony-call-onpostdialdelay-f-sys.md) |
| [onReceiveRttMessage(拨打电话)](arkts-telephony-call-onreceiverttmessage-f-sys.md) |
| [onRttErrCause(拨打电话)](arkts-telephony-call-onrtterrcause-f-sys.md) |
| [onRttModifyInd(拨打电话)](arkts-telephony-call-onrttmodifyind-f-sys.md) |
| [postDialProceed(拨打电话)](arkts-telephony-call-postdialproceed-f-sys.md) |
| [postDialProceed(拨打电话)](arkts-telephony-call-postdialproceed-f-sys.md) |
| [preloadCallUI(拨打电话)](arkts-telephony-call-preloadcallui-f-sys.md) |
| [rejectCall(拨打电话)](arkts-telephony-call-rejectcall-f-sys.md) |
| [rejectCall(拨打电话)](arkts-telephony-call-rejectcall-f-sys.md) |
| [rejectCall(拨打电话)](arkts-telephony-call-rejectcall-f-sys.md) |
| [rejectCall(拨打电话)](arkts-telephony-call-rejectcall-f-sys.md) |
| [removeMissedIncomingCallNotification(拨打电话)](arkts-telephony-call-removemissedincomingcallnotification-f-sys.md) |
| [removeMissedIncomingCallNotification(拨打电话)](arkts-telephony-call-removemissedincomingcallnotification-f-sys.md) |
| [sendCallUiEvent(拨打电话)](arkts-telephony-call-sendcalluievent-f-sys.md) |
| [sendRttMessage(拨打电话)](arkts-telephony-call-sendrttmessage-f-sys.md) |
| [sendUssdResponse(拨打电话)](arkts-telephony-call-sendussdresponse-f-sys.md) |
| [separateConference(拨打电话)](arkts-telephony-call-separateconference-f-sys.md) |
| [separateConference(拨打电话)](arkts-telephony-call-separateconference-f-sys.md) |
| [setAudioDevice(拨打电话)](arkts-telephony-call-setaudiodevice-f-sys.md) |
| [setAudioDevice(拨打电话)](arkts-telephony-call-setaudiodevice-f-sys.md) |
| [setCallRestriction(拨打电话)](arkts-telephony-call-setcallrestriction-f-sys.md) |
| [setCallRestriction(拨打电话)](arkts-telephony-call-setcallrestriction-f-sys.md) |
| [setCallRestrictionPassword(拨打电话)](arkts-telephony-call-setcallrestrictionpassword-f-sys.md) |
| [setCallRestrictionPassword(拨打电话)](arkts-telephony-call-setcallrestrictionpassword-f-sys.md) |
| [setCallTransfer(拨打电话)](arkts-telephony-call-setcalltransfer-f-sys.md) |
| [setCallTransfer(拨打电话)](arkts-telephony-call-setcalltransfer-f-sys.md) |
| [setCallWaiting(拨打电话)](arkts-telephony-call-setcallwaiting-f-sys.md) |
| [setCallWaiting(拨打电话)](arkts-telephony-call-setcallwaiting-f-sys.md) |
| [setDeviceDirection(拨打电话)](arkts-telephony-call-setdevicedirection-f-sys.md) |
| [setDisplaySurface(拨打电话)](arkts-telephony-call-setdisplaysurface-f-sys.md) |
| [setMuted(拨打电话)](arkts-telephony-call-setmuted-f-sys.md) |
| [setMuted(拨打电话)](arkts-telephony-call-setmuted-f-sys.md) |
| [setPreviewSurface(拨打电话)](arkts-telephony-call-setpreviewsurface-f-sys.md) |
| [setRttCapability(拨打电话)](arkts-telephony-call-setrttcapability-f-sys.md) |
| [setVoNRState(拨打电话)](arkts-telephony-call-setvonrstate-f-sys.md) |
| [setVoNRState(拨打电话)](arkts-telephony-call-setvonrstate-f-sys.md) |
| [startDTMF(拨打电话)](arkts-telephony-call-startdtmf-f-sys.md) |
| [startDTMF(拨打电话)](arkts-telephony-call-startdtmf-f-sys.md) |
| [startRtt(拨打电话)](arkts-telephony-call-startrtt-f-sys.md) |
| [stopDTMF(拨打电话)](arkts-telephony-call-stopdtmf-f-sys.md) |
| [stopDTMF(拨打电话)](arkts-telephony-call-stopdtmf-f-sys.md) |
| [stopRtt(拨打电话)](arkts-telephony-call-stoprtt-f-sys.md) |
| [switchCall(拨打电话)](arkts-telephony-call-switchcall-f-sys.md) |
| [switchCall(拨打电话)](arkts-telephony-call-switchcall-f-sys.md) |
| [unHoldCall(拨打电话)](arkts-telephony-call-unholdcall-f-sys.md) |
| [unHoldCall(拨打电话)](arkts-telephony-call-unholdcall-f-sys.md) |
| [unloadCallUI(拨打电话)](arkts-telephony-call-unloadcallui-f-sys.md) |
| [updateImsCallMode(拨打电话)](arkts-telephony-call-updateimscallmode-f-sys.md) |
| [updateImsCallMode(拨打电话)](arkts-telephony-call-updateimscallmode-f-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [CallTransferResult(拨打电话)](arkts-telephony-call-calltransferresult-i.md) |
| [DialOptions(拨打电话)](arkts-telephony-call-dialoptions-i.md) |
| [EmergencyNumberOptions(拨打电话)](arkts-telephony-call-emergencynumberoptions-i.md) |
| [MakeCallOptions(拨打电话)](arkts-telephony-call-makecalloptions-i.md) |
| [NumberFormatOptions(拨打电话)](arkts-telephony-call-numberformatoptions-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [AudioDevice(拨打电话)](arkts-telephony-call-audiodevice-i-sys.md) |
| [AudioDeviceCallbackInfo(拨打电话)](arkts-telephony-call-audiodevicecallbackinfo-i-sys.md) |
| [CallAttributeOptions(拨打电话)](arkts-telephony-call-callattributeoptions-i-sys.md) |
| [CallEventOptions(拨打电话)](arkts-telephony-call-calleventoptions-i-sys.md) |
| [CallRestrictionInfo(拨打电话)](arkts-telephony-call-callrestrictioninfo-i-sys.md) |
| [CallSessionEvent(拨打电话)](arkts-telephony-call-callsessionevent-i-sys.md) |
| [CallTransferInfo(拨打电话)](arkts-telephony-call-calltransferinfo-i-sys.md) |
| [CallTransferResult(拨打电话)](arkts-telephony-call-calltransferresult-i-sys.md) |
| [CameraCapabilities(拨打电话)](arkts-telephony-call-cameracapabilities-i-sys.md) |
| [DialCallOptions(拨打电话)](arkts-telephony-call-dialcalloptions-i-sys.md) |
| [DialOptions(拨打电话)](arkts-telephony-call-dialoptions-i-sys.md) |
| [DisconnectedDetails(拨打电话)](arkts-telephony-call-disconnecteddetails-i-sys.md) |
| [ImsCallModeInfo(拨打电话)](arkts-telephony-call-imscallmodeinfo-i-sys.md) |
| [MmiCodeResults(拨打电话)](arkts-telephony-call-mmicoderesults-i-sys.md) |
| [NumberMarkInfo(拨打电话)](arkts-telephony-call-numbermarkinfo-i-sys.md) |
| [PeerDimensionsDetail(拨打电话)](arkts-telephony-call-peerdimensionsdetail-i-sys.md) |
| [RejectMessageOptions(拨打电话)](arkts-telephony-call-rejectmessageoptions-i-sys.md) |
| [RttErrorInfo(拨打电话)](arkts-telephony-call-rtterrorinfo-i-sys.md) |
| [RttEventInfo(拨打电话)](arkts-telephony-call-rtteventinfo-i-sys.md) |
| [RttMessageInfo(拨打电话)](arkts-telephony-call-rttmessageinfo-i-sys.md) |
| [VoipCallAttribute(拨打电话)](arkts-telephony-call-voipcallattribute-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [CallState(拨打电话)](arkts-telephony-call-callstate-e.md) |
| [CallTransferType(拨打电话)](arkts-telephony-call-calltransfertype-e.md) |
| [CCallState(拨打电话)](arkts-telephony-call-ccallstate-e.md) |
| [TelCallState(拨打电话)](arkts-telephony-call-telcallstate-e.md) |
| [TransferStatus(拨打电话)](arkts-telephony-call-transferstatus-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [AudioDeviceType(拨打电话)](arkts-telephony-call-audiodevicetype-e-sys.md) |
| [CallAbilityEventId(拨打电话)](arkts-telephony-call-callabilityeventid-e-sys.md) |
| [CallRestrictionMode(拨打电话)](arkts-telephony-call-callrestrictionmode-e-sys.md) |
| [CallRestrictionType(拨打电话)](arkts-telephony-call-callrestrictiontype-e-sys.md) |
| [CallSessionEventId(拨打电话)](arkts-telephony-call-callsessioneventid-e-sys.md) |
| [CallTransferSettingType(拨打电话)](arkts-telephony-call-calltransfersettingtype-e-sys.md) |
| [CallType(拨打电话)](arkts-telephony-call-calltype-e-sys.md) |
| [CallWaitingStatus(拨打电话)](arkts-telephony-call-callwaitingstatus-e-sys.md) |
| [ConferenceState(拨打电话)](arkts-telephony-call-conferencestate-e-sys.md) |
| [DetailedCallState(拨打电话)](arkts-telephony-call-detailedcallstate-e-sys.md) |
| [DeviceDirection(拨打电话)](arkts-telephony-call-devicedirection-e-sys.md) |
| [DialScene(拨打电话)](arkts-telephony-call-dialscene-e-sys.md) |
| [DialType(拨打电话)](arkts-telephony-call-dialtype-e-sys.md) |
| [DisconnectedReason(拨打电话)](arkts-telephony-call-disconnectedreason-e-sys.md) |
| [ImsCallMode(拨打电话)](arkts-telephony-call-imscallmode-e-sys.md) |
| [ImsRttMode(拨打电话)](arkts-telephony-call-imsrttmode-e-sys.md) |
| [MarkType(拨打电话)](arkts-telephony-call-marktype-e-sys.md) |
| [MmiCodeResult(拨打电话)](arkts-telephony-call-mmicoderesult-e-sys.md) |
| [RestrictionStatus(拨打电话)](arkts-telephony-call-restrictionstatus-e-sys.md) |
| [RttState(拨打电话)](arkts-telephony-call-rttstate-e-sys.md) |
| [VideoRequestResultType(拨打电话)](arkts-telephony-call-videorequestresulttype-e-sys.md) |
| [VideoStateType(拨打电话)](arkts-telephony-call-videostatetype-e-sys.md) |
| [VoNRState(拨打电话)](arkts-telephony-call-vonrstate-e-sys.md) |
| [XCallType(拨打电话)](arkts-telephony-call-xcalltype-e-sys.md) |
<!--DelEnd-->
