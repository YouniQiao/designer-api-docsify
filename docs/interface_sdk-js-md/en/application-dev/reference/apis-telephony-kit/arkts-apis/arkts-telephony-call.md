# @ohos.telephony.call(Call)

The **call** module provides call management functions, including making calls, redirecting to the dial screen, obtaining the call status, and formatting phone numbers.To subscribe to call status changes, use `observer.on('callStateChange')`.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Telephony.CallManager

## Modules to Import

```TypeScript
import { call } from '@kit.TelephonyKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [answerCall(Call)](arkts-telephony-call-answercall-f.md) |
| [dial(Call)](arkts-telephony-call-dial-f.md) |
| [dial(Call)](arkts-telephony-call-dial-f.md) |
| [dial(Call)](arkts-telephony-call-dial-f.md) |
| [formatPhoneNumber(Call)](arkts-telephony-call-formatphonenumber-f.md) |
| [formatPhoneNumber(Call)](arkts-telephony-call-formatphonenumber-f.md) |
| [formatPhoneNumber(Call)](arkts-telephony-call-formatphonenumber-f.md) |
| [formatPhoneNumberToE164(Call)](arkts-telephony-call-formatphonenumbertoe164-f.md) |
| [formatPhoneNumberToE164(Call)](arkts-telephony-call-formatphonenumbertoe164-f.md) |
| [getCallState(Call)](arkts-telephony-call-getcallstate-f.md) |
| [getCallState(Call)](arkts-telephony-call-getcallstate-f.md) |
| [getCallStateSync(Call)](arkts-telephony-call-getcallstatesync-f.md) |
| [getCallTransferInfo(Call)](arkts-telephony-call-getcalltransferinfo-f.md) |
| [hangUpCall(Call)](arkts-telephony-call-hangupcall-f.md) |
| [hasCall(Call)](arkts-telephony-call-hascall-f.md) |
| [hasCall(Call)](arkts-telephony-call-hascall-f.md) |
| [hasCallSync(Call)](arkts-telephony-call-hascallsync-f.md) |
| [hasVoiceCapability(Call)](arkts-telephony-call-hasvoicecapability-f.md) |
| [isEmergencyPhoneNumber(Call)](arkts-telephony-call-isemergencyphonenumber-f.md) |
| [isEmergencyPhoneNumber(Call)](arkts-telephony-call-isemergencyphonenumber-f.md) |
| [isEmergencyPhoneNumber(Call)](arkts-telephony-call-isemergencyphonenumber-f.md) |
| [makeCall(Call)](arkts-telephony-call-makecall-f.md) |
| [makeCall(Call)](arkts-telephony-call-makecall-f.md) |
| [makeCall(Call)](arkts-telephony-call-makecall-f.md) |
| [makeCall(Call)](arkts-telephony-call-makecall-f.md) |
| [makeCallWithToken(Call)](arkts-telephony-call-makecallwithtoken-f.md) |
| [rejectCall(Call)](arkts-telephony-call-rejectcall-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [answerCall(Call)](arkts-telephony-call-answercall-f-sys.md) |
| [answerCall(Call)](arkts-telephony-call-answercall-f-sys.md) |
| [answerCall(Call)](arkts-telephony-call-answercall-f-sys.md) |
| [answerCall(Call)](arkts-telephony-call-answercall-f-sys.md) |
| [cancelCallUpgrade(Call)](arkts-telephony-call-cancelcallupgrade-f-sys.md) |
| [cancelMuted(Call)](arkts-telephony-call-cancelmuted-f-sys.md) |
| [cancelMuted(Call)](arkts-telephony-call-cancelmuted-f-sys.md) |
| [canSetCallTransferTime(Call)](arkts-telephony-call-cansetcalltransfertime-f-sys.md) |
| [canSetCallTransferTime(Call)](arkts-telephony-call-cansetcalltransfertime-f-sys.md) |
| [closeUnfinishedUssd(Call)](arkts-telephony-call-closeunfinishedussd-f-sys.md) |
| [closeUnfinishedUssd(Call)](arkts-telephony-call-closeunfinishedussd-f-sys.md) |
| [combineConference(Call)](arkts-telephony-call-combineconference-f-sys.md) |
| [combineConference(Call)](arkts-telephony-call-combineconference-f-sys.md) |
| [controlCamera(Call)](arkts-telephony-call-controlcamera-f-sys.md) |
| [dialCall(Call)](arkts-telephony-call-dialcall-f-sys.md) |
| [dialCall(Call)](arkts-telephony-call-dialcall-f-sys.md) |
| [dialCall(Call)](arkts-telephony-call-dialcall-f-sys.md) |
| [disableImsSwitch(Call)](arkts-telephony-call-disableimsswitch-f-sys.md) |
| [disableImsSwitch(Call)](arkts-telephony-call-disableimsswitch-f-sys.md) |
| [enableImsSwitch(Call)](arkts-telephony-call-enableimsswitch-f-sys.md) |
| [enableImsSwitch(Call)](arkts-telephony-call-enableimsswitch-f-sys.md) |
| [getCallIdListForConference(Call)](arkts-telephony-call-getcallidlistforconference-f-sys.md) |
| [getCallIdListForConference(Call)](arkts-telephony-call-getcallidlistforconference-f-sys.md) |
| [getCallRestrictionStatus(Call)](arkts-telephony-call-getcallrestrictionstatus-f-sys.md) |
| [getCallRestrictionStatus(Call)](arkts-telephony-call-getcallrestrictionstatus-f-sys.md) |
| [getCallTransferInfo(Call)](arkts-telephony-call-getcalltransferinfo-f-sys.md) |
| [getCallTransferInfo(Call)](arkts-telephony-call-getcalltransferinfo-f-sys.md) |
| [getCallWaitingStatus(Call)](arkts-telephony-call-getcallwaitingstatus-f-sys.md) |
| [getCallWaitingStatus(Call)](arkts-telephony-call-getcallwaitingstatus-f-sys.md) |
| [getMainCallId(Call)](arkts-telephony-call-getmaincallid-f-sys.md) |
| [getMainCallId(Call)](arkts-telephony-call-getmaincallid-f-sys.md) |
| [getSubCallIdList(Call)](arkts-telephony-call-getsubcallidlist-f-sys.md) |
| [getSubCallIdList(Call)](arkts-telephony-call-getsubcallidlist-f-sys.md) |
| [getVoNRState(Call)](arkts-telephony-call-getvonrstate-f-sys.md) |
| [getVoNRState(Call)](arkts-telephony-call-getvonrstate-f-sys.md) |
| [hangUpCall(Call)](arkts-telephony-call-hangupcall-f-sys.md) |
| [hangUpCall(Call)](arkts-telephony-call-hangupcall-f-sys.md) |
| [holdCall(Call)](arkts-telephony-call-holdcall-f-sys.md) |
| [holdCall(Call)](arkts-telephony-call-holdcall-f-sys.md) |
| [inputDialerSpecialCode(Call)](arkts-telephony-call-inputdialerspecialcode-f-sys.md) |
| [inputDialerSpecialCode(Call)](arkts-telephony-call-inputdialerspecialcode-f-sys.md) |
| [isImsSwitchEnabled(Call)](arkts-telephony-call-isimsswitchenabled-f-sys.md) |
| [isImsSwitchEnabled(Call)](arkts-telephony-call-isimsswitchenabled-f-sys.md) |
| [isImsSwitchEnabledSync(Call)](arkts-telephony-call-isimsswitchenabledsync-f-sys.md) |
| [isInEmergencyCall(Call)](arkts-telephony-call-isinemergencycall-f-sys.md) |
| [isInEmergencyCall(Call)](arkts-telephony-call-isinemergencycall-f-sys.md) |
| [isNewCallAllowed(Call)](arkts-telephony-call-isnewcallallowed-f-sys.md) |
| [isNewCallAllowed(Call)](arkts-telephony-call-isnewcallallowed-f-sys.md) |
| [isRinging(Call)](arkts-telephony-call-isringing-f-sys.md) |
| [isRinging(Call)](arkts-telephony-call-isringing-f-sys.md) |
| [joinConference(Call)](arkts-telephony-call-joinconference-f-sys.md) |
| [joinConference(Call)](arkts-telephony-call-joinconference-f-sys.md) |
| [kickOutFromConference(Call)](arkts-telephony-call-kickoutfromconference-f-sys.md) |
| [kickOutFromConference(Call)](arkts-telephony-call-kickoutfromconference-f-sys.md) |
| [muteRinger(Call)](arkts-telephony-call-muteringer-f-sys.md) |
| [muteRinger(Call)](arkts-telephony-call-muteringer-f-sys.md) |
| [off(Call)](arkts-telephony-call-off-f-sys.md#offcalldetailschange) |
| [off(Call)](arkts-telephony-call-off-f-sys.md#offcalleventchange) |
| [off(Call)](arkts-telephony-call-off-f-sys.md#offcalldisconnectedcause) |
| [off(Call)](arkts-telephony-call-off-f-sys.md#offmmicoderesult) |
| [off(Call)](arkts-telephony-call-off-f-sys.md#offaudiodevicechange) |
| [off(Call)](arkts-telephony-call-off-f-sys.md#offpostdialdelay) |
| [off(Call)](arkts-telephony-call-off-f-sys.md#offimscallmodechange) |
| [off(Call)](arkts-telephony-call-off-f-sys.md#offcallsessionevent) |
| [off(Call)](arkts-telephony-call-off-f-sys.md#offpeerdimensionschange) |
| [off(Call)](arkts-telephony-call-off-f-sys.md#offcameracapabilitieschange) |
| [offAudioDeviceChange(Call)](arkts-telephony-call-offaudiodevicechange-f-sys.md) |
| [offCallDetailsChange(Call)](arkts-telephony-call-offcalldetailschange-f-sys.md) |
| [offCallDisconnectedCause(Call)](arkts-telephony-call-offcalldisconnectedcause-f-sys.md) |
| [offCallEventChange(Call)](arkts-telephony-call-offcalleventchange-f-sys.md) |
| [offCallSessionEvent(Call)](arkts-telephony-call-offcallsessionevent-f-sys.md) |
| [offCameraCapabilitiesChange(Call)](arkts-telephony-call-offcameracapabilitieschange-f-sys.md) |
| [offImsCallModeChange(Call)](arkts-telephony-call-offimscallmodechange-f-sys.md) |
| [offMmiCodeResult(Call)](arkts-telephony-call-offmmicoderesult-f-sys.md) |
| [offPeerDimensionsChange(Call)](arkts-telephony-call-offpeerdimensionschange-f-sys.md) |
| [offPostDialDelay(Call)](arkts-telephony-call-offpostdialdelay-f-sys.md) |
| [offReceiveRttMessage(Call)](arkts-telephony-call-offreceiverttmessage-f-sys.md) |
| [offRttErrCause(Call)](arkts-telephony-call-offrtterrcause-f-sys.md) |
| [offRttModifyInd(Call)](arkts-telephony-call-offrttmodifyind-f-sys.md) |
| [on(Call)](arkts-telephony-call-on-f-sys.md#oncalldetailschange) |
| [on(Call)](arkts-telephony-call-on-f-sys.md#oncalleventchange) |
| [on(Call)](arkts-telephony-call-on-f-sys.md#oncalldisconnectedcause) |
| [on(Call)](arkts-telephony-call-on-f-sys.md#onmmicoderesult) |
| [on(Call)](arkts-telephony-call-on-f-sys.md#onaudiodevicechange) |
| [on(Call)](arkts-telephony-call-on-f-sys.md#onpostdialdelay) |
| [on(Call)](arkts-telephony-call-on-f-sys.md#onimscallmodechange) |
| [on(Call)](arkts-telephony-call-on-f-sys.md#oncallsessionevent) |
| [on(Call)](arkts-telephony-call-on-f-sys.md#onpeerdimensionschange) |
| [on(Call)](arkts-telephony-call-on-f-sys.md#oncameracapabilitieschange) |
| [onAudioDeviceChange(Call)](arkts-telephony-call-onaudiodevicechange-f-sys.md) |
| [onCallDetailsChange(Call)](arkts-telephony-call-oncalldetailschange-f-sys.md) |
| [onCallDisconnectedCause(Call)](arkts-telephony-call-oncalldisconnectedcause-f-sys.md) |
| [onCallEventChange(Call)](arkts-telephony-call-oncalleventchange-f-sys.md) |
| [onCallSessionEvent(Call)](arkts-telephony-call-oncallsessionevent-f-sys.md) |
| [onCameraCapabilitiesChange(Call)](arkts-telephony-call-oncameracapabilitieschange-f-sys.md) |
| [onImsCallModeChange(Call)](arkts-telephony-call-onimscallmodechange-f-sys.md) |
| [onMmiCodeResult(Call)](arkts-telephony-call-onmmicoderesult-f-sys.md) |
| [onPeerDimensionsChange(Call)](arkts-telephony-call-onpeerdimensionschange-f-sys.md) |
| [onPostDialDelay(Call)](arkts-telephony-call-onpostdialdelay-f-sys.md) |
| [onReceiveRttMessage(Call)](arkts-telephony-call-onreceiverttmessage-f-sys.md) |
| [onRttErrCause(Call)](arkts-telephony-call-onrtterrcause-f-sys.md) |
| [onRttModifyInd(Call)](arkts-telephony-call-onrttmodifyind-f-sys.md) |
| [postDialProceed(Call)](arkts-telephony-call-postdialproceed-f-sys.md) |
| [postDialProceed(Call)](arkts-telephony-call-postdialproceed-f-sys.md) |
| [preloadCallUI(Call)](arkts-telephony-call-preloadcallui-f-sys.md) |
| [rejectCall(Call)](arkts-telephony-call-rejectcall-f-sys.md) |
| [rejectCall(Call)](arkts-telephony-call-rejectcall-f-sys.md) |
| [rejectCall(Call)](arkts-telephony-call-rejectcall-f-sys.md) |
| [rejectCall(Call)](arkts-telephony-call-rejectcall-f-sys.md) |
| [removeMissedIncomingCallNotification(Call)](arkts-telephony-call-removemissedincomingcallnotification-f-sys.md) |
| [removeMissedIncomingCallNotification(Call)](arkts-telephony-call-removemissedincomingcallnotification-f-sys.md) |
| [sendCallUiEvent(Call)](arkts-telephony-call-sendcalluievent-f-sys.md) |
| [sendRttMessage(Call)](arkts-telephony-call-sendrttmessage-f-sys.md) |
| [sendUssdResponse(Call)](arkts-telephony-call-sendussdresponse-f-sys.md) |
| [separateConference(Call)](arkts-telephony-call-separateconference-f-sys.md) |
| [separateConference(Call)](arkts-telephony-call-separateconference-f-sys.md) |
| [setAudioDevice(Call)](arkts-telephony-call-setaudiodevice-f-sys.md) |
| [setAudioDevice(Call)](arkts-telephony-call-setaudiodevice-f-sys.md) |
| [setCallRestriction(Call)](arkts-telephony-call-setcallrestriction-f-sys.md) |
| [setCallRestriction(Call)](arkts-telephony-call-setcallrestriction-f-sys.md) |
| [setCallRestrictionPassword(Call)](arkts-telephony-call-setcallrestrictionpassword-f-sys.md) |
| [setCallRestrictionPassword(Call)](arkts-telephony-call-setcallrestrictionpassword-f-sys.md) |
| [setCallTransfer(Call)](arkts-telephony-call-setcalltransfer-f-sys.md) |
| [setCallTransfer(Call)](arkts-telephony-call-setcalltransfer-f-sys.md) |
| [setCallWaiting(Call)](arkts-telephony-call-setcallwaiting-f-sys.md) |
| [setCallWaiting(Call)](arkts-telephony-call-setcallwaiting-f-sys.md) |
| [setDeviceDirection(Call)](arkts-telephony-call-setdevicedirection-f-sys.md) |
| [setDisplaySurface(Call)](arkts-telephony-call-setdisplaysurface-f-sys.md) |
| [setMuted(Call)](arkts-telephony-call-setmuted-f-sys.md) |
| [setMuted(Call)](arkts-telephony-call-setmuted-f-sys.md) |
| [setPreviewSurface(Call)](arkts-telephony-call-setpreviewsurface-f-sys.md) |
| [setRttCapability(Call)](arkts-telephony-call-setrttcapability-f-sys.md) |
| [setVoNRState(Call)](arkts-telephony-call-setvonrstate-f-sys.md) |
| [setVoNRState(Call)](arkts-telephony-call-setvonrstate-f-sys.md) |
| [startDTMF(Call)](arkts-telephony-call-startdtmf-f-sys.md) |
| [startDTMF(Call)](arkts-telephony-call-startdtmf-f-sys.md) |
| [startRtt(Call)](arkts-telephony-call-startrtt-f-sys.md) |
| [stopDTMF(Call)](arkts-telephony-call-stopdtmf-f-sys.md) |
| [stopDTMF(Call)](arkts-telephony-call-stopdtmf-f-sys.md) |
| [stopRtt(Call)](arkts-telephony-call-stoprtt-f-sys.md) |
| [switchCall(Call)](arkts-telephony-call-switchcall-f-sys.md) |
| [switchCall(Call)](arkts-telephony-call-switchcall-f-sys.md) |
| [unHoldCall(Call)](arkts-telephony-call-unholdcall-f-sys.md) |
| [unHoldCall(Call)](arkts-telephony-call-unholdcall-f-sys.md) |
| [unloadCallUI(Call)](arkts-telephony-call-unloadcallui-f-sys.md) |
| [updateImsCallMode(Call)](arkts-telephony-call-updateimscallmode-f-sys.md) |
| [updateImsCallMode(Call)](arkts-telephony-call-updateimscallmode-f-sys.md) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CallTransferResult(Call)](arkts-telephony-call-calltransferresult-i.md) |
| [DialOptions(Call)](arkts-telephony-call-dialoptions-i.md) |
| [EmergencyNumberOptions(Call)](arkts-telephony-call-emergencynumberoptions-i.md) |
| [MakeCallOptions(Call)](arkts-telephony-call-makecalloptions-i.md) |
| [NumberFormatOptions(Call)](arkts-telephony-call-numberformatoptions-i.md) |

<!--Del-->
### Interfaces(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AudioDevice(Call)](arkts-telephony-call-audiodevice-i-sys.md) |
| [AudioDeviceCallbackInfo(Call)](arkts-telephony-call-audiodevicecallbackinfo-i-sys.md) |
| [CallAttributeOptions(Call)](arkts-telephony-call-callattributeoptions-i-sys.md) |
| [CallEventOptions(Call)](arkts-telephony-call-calleventoptions-i-sys.md) |
| [CallRestrictionInfo(Call)](arkts-telephony-call-callrestrictioninfo-i-sys.md) |
| [CallSessionEvent(Call)](arkts-telephony-call-callsessionevent-i-sys.md) |
| [CallTransferInfo(Call)](arkts-telephony-call-calltransferinfo-i-sys.md) |
| [CallTransferResult(Call)](arkts-telephony-call-calltransferresult-i-sys.md) |
| [CameraCapabilities(Call)](arkts-telephony-call-cameracapabilities-i-sys.md) |
| [DialCallOptions(Call)](arkts-telephony-call-dialcalloptions-i-sys.md) |
| [DialOptions(Call)](arkts-telephony-call-dialoptions-i-sys.md) |
| [DisconnectedDetails(Call)](arkts-telephony-call-disconnecteddetails-i-sys.md) |
| [ImsCallModeInfo(Call)](arkts-telephony-call-imscallmodeinfo-i-sys.md) |
| [MmiCodeResults(Call)](arkts-telephony-call-mmicoderesults-i-sys.md) |
| [NumberMarkInfo(Call)](arkts-telephony-call-numbermarkinfo-i-sys.md) |
| [PeerDimensionsDetail(Call)](arkts-telephony-call-peerdimensionsdetail-i-sys.md) |
| [RejectMessageOptions(Call)](arkts-telephony-call-rejectmessageoptions-i-sys.md) |
| [RttErrorInfo(Call)](arkts-telephony-call-rtterrorinfo-i-sys.md) |
| [RttEventInfo(Call)](arkts-telephony-call-rtteventinfo-i-sys.md) |
| [RttMessageInfo(Call)](arkts-telephony-call-rttmessageinfo-i-sys.md) |
| [VoipCallAttribute(Call)](arkts-telephony-call-voipcallattribute-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CallState(Call)](arkts-telephony-call-callstate-e.md) |
| [CallTransferType(Call)](arkts-telephony-call-calltransfertype-e.md) |
| [CCallState(Call)](arkts-telephony-call-ccallstate-e.md) |
| [TelCallState(Call)](arkts-telephony-call-telcallstate-e.md) |
| [TransferStatus(Call)](arkts-telephony-call-transferstatus-e.md) |

<!--Del-->
### Enums(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AudioDeviceType(Call)](arkts-telephony-call-audiodevicetype-e-sys.md) |
| [CallAbilityEventId(Call)](arkts-telephony-call-callabilityeventid-e-sys.md) |
| [CallRestrictionMode(Call)](arkts-telephony-call-callrestrictionmode-e-sys.md) |
| [CallRestrictionType(Call)](arkts-telephony-call-callrestrictiontype-e-sys.md) |
| [CallSessionEventId(Call)](arkts-telephony-call-callsessioneventid-e-sys.md) |
| [CallTransferSettingType(Call)](arkts-telephony-call-calltransfersettingtype-e-sys.md) |
| [CallType(Call)](arkts-telephony-call-calltype-e-sys.md) |
| [CallWaitingStatus(Call)](arkts-telephony-call-callwaitingstatus-e-sys.md) |
| [ConferenceState(Call)](arkts-telephony-call-conferencestate-e-sys.md) |
| [DetailedCallState(Call)](arkts-telephony-call-detailedcallstate-e-sys.md) |
| [DeviceDirection(Call)](arkts-telephony-call-devicedirection-e-sys.md) |
| [DialScene(Call)](arkts-telephony-call-dialscene-e-sys.md) |
| [DialType(Call)](arkts-telephony-call-dialtype-e-sys.md) |
| [DisconnectedReason(Call)](arkts-telephony-call-disconnectedreason-e-sys.md) |
| [ImsCallMode(Call)](arkts-telephony-call-imscallmode-e-sys.md) |
| [ImsRttMode(Call)](arkts-telephony-call-imsrttmode-e-sys.md) |
| [MarkType(Call)](arkts-telephony-call-marktype-e-sys.md) |
| [MmiCodeResult(Call)](arkts-telephony-call-mmicoderesult-e-sys.md) |
| [RestrictionStatus(Call)](arkts-telephony-call-restrictionstatus-e-sys.md) |
| [RttState(Call)](arkts-telephony-call-rttstate-e-sys.md) |
| [VideoRequestResultType(Call)](arkts-telephony-call-videorequestresulttype-e-sys.md) |
| [VideoStateType(Call)](arkts-telephony-call-videostatetype-e-sys.md) |
| [VoNRState(Call)](arkts-telephony-call-vonrstate-e-sys.md) |
| [XCallType(Call)](arkts-telephony-call-xcalltype-e-sys.md) |
<!--DelEnd-->
