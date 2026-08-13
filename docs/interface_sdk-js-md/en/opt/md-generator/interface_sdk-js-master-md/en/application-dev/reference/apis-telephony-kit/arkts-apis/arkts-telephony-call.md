# @ohos.telephony.call

The **call** module provides call management functions, including making calls, redirecting to the dial screen, obtaining the call status, and formatting phone numbers. To subscribe to call status changes, use `observer.on('callStateChange')`.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare namespace call--><!--Device-unnamed-declare namespace call-End-->

**System capability:** SystemCapability.Telephony.CallManager

## Modules to Import

```TypeScript
import { call } from '@kit.TelephonyKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [dial](arkts-telephony-call-dial-f.md#dial) |
| [dial](arkts-telephony-call-dial-f.md#dial) |
| [dial](arkts-telephony-call-dial-f.md#dial) |
| [formatPhoneNumber](arkts-telephony-call-formatphonenumber-f.md#formatPhoneNumber) |
| [formatPhoneNumber](arkts-telephony-call-formatphonenumber-f.md#formatPhoneNumber) |
| [formatPhoneNumber](arkts-telephony-call-formatphonenumber-f.md#formatPhoneNumber) |
| [formatPhoneNumberToE164](arkts-telephony-call-formatphonenumbertoe164-f.md#formatPhoneNumberToE164) |
| [formatPhoneNumberToE164](arkts-telephony-call-formatphonenumbertoe164-f.md#formatPhoneNumberToE164) |
| [getCallState](arkts-telephony-call-getcallstate-f.md#getCallState) |
| [getCallState](arkts-telephony-call-getcallstate-f.md#getCallState) |
| [getCallStateSync](arkts-telephony-call-getcallstatesync-f.md#getCallStateSync) |
| [getCallTransferInfo](arkts-telephony-call-getcalltransferinfo-f.md#getCallTransferInfo) |
| [hasCall](arkts-telephony-call-hascall-f.md#hasCall) |
| [hasCall](arkts-telephony-call-hascall-f.md#hasCall) |
| [hasCallSync](arkts-telephony-call-hascallsync-f.md#hasCallSync) |
| [hasVoiceCapability](arkts-telephony-call-hasvoicecapability-f.md#hasVoiceCapability) |
| [isEmergencyPhoneNumber](arkts-telephony-call-isemergencyphonenumber-f.md#isEmergencyPhoneNumber) |
| [isEmergencyPhoneNumber](arkts-telephony-call-isemergencyphonenumber-f.md#isEmergencyPhoneNumber) |
| [isEmergencyPhoneNumber](arkts-telephony-call-isemergencyphonenumber-f.md#isEmergencyPhoneNumber) |
| [makeCall](arkts-telephony-call-makecall-f.md#makeCall) |
| [makeCall](arkts-telephony-call-makecall-f.md#makeCall) |
| [makeCall](arkts-telephony-call-makecall-f.md#makeCall) |
| [makeCall](arkts-telephony-call-makecall-f.md#makeCall) |
| [makeCallWithToken](arkts-telephony-call-makecallwithtoken-f.md#makeCallWithToken) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [answerCall](arkts-telephony-call-answercall-f-sys.md#answerCall-(System-API)) |
| [answerCall](arkts-telephony-call-answercall-f-sys.md#answerCall-(System-API)) |
| [answerCall](arkts-telephony-call-answercall-f-sys.md#answerCall-(System-API)) |
| [answerCall](arkts-telephony-call-answercall-f-sys.md#answerCall-(System-API)) |
| [answerCall](arkts-telephony-call-answercall-f-sys.md#answerCall-(System-API)) |
| [canSetCallTransferTime](arkts-telephony-call-cansetcalltransfertime-f-sys.md#canSetCallTransferTime-(System-API)) |
| [canSetCallTransferTime](arkts-telephony-call-cansetcalltransfertime-f-sys.md#canSetCallTransferTime-(System-API)) |
| [cancelCallUpgrade](arkts-telephony-call-cancelcallupgrade-f-sys.md#cancelCallUpgrade-(System-API)) |
| [cancelMuted](arkts-telephony-call-cancelmuted-f-sys.md#cancelMuted-(System-API)) |
| [cancelMuted](arkts-telephony-call-cancelmuted-f-sys.md#cancelMuted-(System-API)) |
| [closeUnfinishedUssd](arkts-telephony-call-closeunfinishedussd-f-sys.md#closeUnfinishedUssd-(System-API)) |
| [closeUnfinishedUssd](arkts-telephony-call-closeunfinishedussd-f-sys.md#closeUnfinishedUssd-(System-API)) |
| [combineConference](arkts-telephony-call-combineconference-f-sys.md#combineConference-(System-API)) |
| [combineConference](arkts-telephony-call-combineconference-f-sys.md#combineConference-(System-API)) |
| [controlCamera](arkts-telephony-call-controlcamera-f-sys.md#controlCamera-(System-API)) |
| [dialCall](arkts-telephony-call-dialcall-f-sys.md#dialCall-(System-API)) |
| [dialCall](arkts-telephony-call-dialcall-f-sys.md#dialCall-(System-API)) |
| [dialCall](arkts-telephony-call-dialcall-f-sys.md#dialCall-(System-API)) |
| [disableImsSwitch](arkts-telephony-call-disableimsswitch-f-sys.md#disableImsSwitch-(System-API)) |
| [disableImsSwitch](arkts-telephony-call-disableimsswitch-f-sys.md#disableImsSwitch-(System-API)) |
| [enableImsSwitch](arkts-telephony-call-enableimsswitch-f-sys.md#enableImsSwitch-(System-API)) |
| [enableImsSwitch](arkts-telephony-call-enableimsswitch-f-sys.md#enableImsSwitch-(System-API)) |
| [getCallIdListForConference](arkts-telephony-call-getcallidlistforconference-f-sys.md#getCallIdListForConference-(System-API)) |
| [getCallIdListForConference](arkts-telephony-call-getcallidlistforconference-f-sys.md#getCallIdListForConference-(System-API)) |
| [getCallRestrictionStatus](arkts-telephony-call-getcallrestrictionstatus-f-sys.md#getCallRestrictionStatus-(System-API)) |
| [getCallRestrictionStatus](arkts-telephony-call-getcallrestrictionstatus-f-sys.md#getCallRestrictionStatus-(System-API)) |
| [getCallTransferInfo](arkts-telephony-call-getcalltransferinfo-f-sys.md#getCallTransferInfo-(System-API)) |
| [getCallTransferInfo](arkts-telephony-call-getcalltransferinfo-f-sys.md#getCallTransferInfo-(System-API)) |
| [getCallWaitingStatus](arkts-telephony-call-getcallwaitingstatus-f-sys.md#getCallWaitingStatus-(System-API)) |
| [getCallWaitingStatus](arkts-telephony-call-getcallwaitingstatus-f-sys.md#getCallWaitingStatus-(System-API)) |
| [getMainCallId](arkts-telephony-call-getmaincallid-f-sys.md#getMainCallId-(System-API)) |
| [getMainCallId](arkts-telephony-call-getmaincallid-f-sys.md#getMainCallId-(System-API)) |
| [getSubCallIdList](arkts-telephony-call-getsubcallidlist-f-sys.md#getSubCallIdList-(System-API)) |
| [getSubCallIdList](arkts-telephony-call-getsubcallidlist-f-sys.md#getSubCallIdList-(System-API)) |
| [getVoNRState](arkts-telephony-call-getvonrstate-f-sys.md#getVoNRState-(System-API)) |
| [getVoNRState](arkts-telephony-call-getvonrstate-f-sys.md#getVoNRState-(System-API)) |
| [hangUpCall](arkts-telephony-call-hangupcall-f-sys.md#hangUpCall-(System-API)) |
| [hangUpCall](arkts-telephony-call-hangupcall-f-sys.md#hangUpCall-(System-API)) |
| [hangUpCall](arkts-telephony-call-hangupcall-f-sys.md#hangUpCall-(System-API)) |
| [holdCall](arkts-telephony-call-holdcall-f-sys.md#holdCall-(System-API)) |
| [holdCall](arkts-telephony-call-holdcall-f-sys.md#holdCall-(System-API)) |
| [inputDialerSpecialCode](arkts-telephony-call-inputdialerspecialcode-f-sys.md#inputDialerSpecialCode-(System-API)) |
| [inputDialerSpecialCode](arkts-telephony-call-inputdialerspecialcode-f-sys.md#inputDialerSpecialCode-(System-API)) |
| [isImsSwitchEnabled](arkts-telephony-call-isimsswitchenabled-f-sys.md#isImsSwitchEnabled-(System-API)) |
| [isImsSwitchEnabled](arkts-telephony-call-isimsswitchenabled-f-sys.md#isImsSwitchEnabled-(System-API)) |
| [isImsSwitchEnabledSync](arkts-telephony-call-isimsswitchenabledsync-f-sys.md#isImsSwitchEnabledSync-(System-API)) |
| [isInEmergencyCall](arkts-telephony-call-isinemergencycall-f-sys.md#isInEmergencyCall-(System-API)) |
| [isInEmergencyCall](arkts-telephony-call-isinemergencycall-f-sys.md#isInEmergencyCall-(System-API)) |
| [isNewCallAllowed](arkts-telephony-call-isnewcallallowed-f-sys.md#isNewCallAllowed-(System-API)) |
| [isNewCallAllowed](arkts-telephony-call-isnewcallallowed-f-sys.md#isNewCallAllowed-(System-API)) |
| [isRinging](arkts-telephony-call-isringing-f-sys.md#isRinging-(System-API)) |
| [isRinging](arkts-telephony-call-isringing-f-sys.md#isRinging-(System-API)) |
| [joinConference](arkts-telephony-call-joinconference-f-sys.md#joinConference-(System-API)) |
| [joinConference](arkts-telephony-call-joinconference-f-sys.md#joinConference-(System-API)) |
| [kickOutFromConference](arkts-telephony-call-kickoutfromconference-f-sys.md#kickOutFromConference-(System-API)) |
| [kickOutFromConference](arkts-telephony-call-kickoutfromconference-f-sys.md#kickOutFromConference-(System-API)) |
| [muteRinger](arkts-telephony-call-muteringer-f-sys.md#muteRinger-(System-API)) |
| [muteRinger](arkts-telephony-call-muteringer-f-sys.md#muteRinger-(System-API)) |
| [offAudioDeviceChange](arkts-telephony-call-offaudiodevicechange-f-sys.md#offAudioDeviceChange-(System-API)) |
| [offCallDetailsChange](arkts-telephony-call-offcalldetailschange-f-sys.md#offCallDetailsChange-(System-API)) |
| [offCallDisconnectedCause](arkts-telephony-call-offcalldisconnectedcause-f-sys.md#offCallDisconnectedCause-(System-API)) |
| [offCallEventChange](arkts-telephony-call-offcalleventchange-f-sys.md#offCallEventChange-(System-API)) |
| [offCallSessionEvent](arkts-telephony-call-offcallsessionevent-f-sys.md#offCallSessionEvent-(System-API)) |
| [offCameraCapabilitiesChange](arkts-telephony-call-offcameracapabilitieschange-f-sys.md#offCameraCapabilitiesChange-(System-API)) |
| [offImsCallModeChange](arkts-telephony-call-offimscallmodechange-f-sys.md#offImsCallModeChange-(System-API)) |
| [offMmiCodeResult](arkts-telephony-call-offmmicoderesult-f-sys.md#offMmiCodeResult-(System-API)) |
| [offPeerDimensionsChange](arkts-telephony-call-offpeerdimensionschange-f-sys.md#offPeerDimensionsChange-(System-API)) |
| [offPostDialDelay](arkts-telephony-call-offpostdialdelay-f-sys.md#offPostDialDelay-(System-API)) |
| [offReceiveRttMessage](arkts-telephony-call-offreceiverttmessage-f-sys.md#offReceiveRttMessage-(System-API)) |
| [offRttErrCause](arkts-telephony-call-offrtterrcause-f-sys.md#offRttErrCause-(System-API)) |
| [offRttModifyInd](arkts-telephony-call-offrttmodifyind-f-sys.md#offRttModifyInd-(System-API)) |
| [off_audioDeviceChange](arkts-telephony-call-offaudiodevicechange-f-sys.md) |
| [off_callDetailsChange](arkts-telephony-call-offcalldetailschange-f-sys.md) |
| [off_callDisconnectedCause](arkts-telephony-call-offcalldisconnectedcause-f-sys.md) |
| [off_callEventChange](arkts-telephony-call-offcalleventchange-f-sys.md) |
| [off_callSessionEvent](arkts-telephony-call-offcallsessionevent-f-sys.md) |
| [off_cameraCapabilitiesChange](arkts-telephony-call-offcameracapabilitieschange-f-sys.md) |
| [off_imsCallModeChange](arkts-telephony-call-offimscallmodechange-f-sys.md) |
| [off_mmiCodeResult](arkts-telephony-call-offmmicoderesult-f-sys.md) |
| [off_peerDimensionsChange](arkts-telephony-call-offpeerdimensionschange-f-sys.md) |
| [off_postDialDelay](arkts-telephony-call-offpostdialdelay-f-sys.md) |
| [onAudioDeviceChange](arkts-telephony-call-onaudiodevicechange-f-sys.md#onAudioDeviceChange-(System-API)) |
| [onCallDetailsChange](arkts-telephony-call-oncalldetailschange-f-sys.md#onCallDetailsChange-(System-API)) |
| [onCallDisconnectedCause](arkts-telephony-call-oncalldisconnectedcause-f-sys.md#onCallDisconnectedCause-(System-API)) |
| [onCallEventChange](arkts-telephony-call-oncalleventchange-f-sys.md#onCallEventChange-(System-API)) |
| [onCallSessionEvent](arkts-telephony-call-oncallsessionevent-f-sys.md#onCallSessionEvent-(System-API)) |
| [onCameraCapabilitiesChange](arkts-telephony-call-oncameracapabilitieschange-f-sys.md#onCameraCapabilitiesChange-(System-API)) |
| [onImsCallModeChange](arkts-telephony-call-onimscallmodechange-f-sys.md#onImsCallModeChange-(System-API)) |
| [onMmiCodeResult](arkts-telephony-call-onmmicoderesult-f-sys.md#onMmiCodeResult-(System-API)) |
| [onPeerDimensionsChange](arkts-telephony-call-onpeerdimensionschange-f-sys.md#onPeerDimensionsChange-(System-API)) |
| [onPostDialDelay](arkts-telephony-call-onpostdialdelay-f-sys.md#onPostDialDelay-(System-API)) |
| [onReceiveRttMessage](arkts-telephony-call-onreceiverttmessage-f-sys.md#onReceiveRttMessage-(System-API)) |
| [onRttErrCause](arkts-telephony-call-onrtterrcause-f-sys.md#onRttErrCause-(System-API)) |
| [onRttModifyInd](arkts-telephony-call-onrttmodifyind-f-sys.md#onRttModifyInd-(System-API)) |
| [on_audioDeviceChange](arkts-telephony-call-onaudiodevicechange-f-sys.md) |
| [on_callDetailsChange](arkts-telephony-call-oncalldetailschange-f-sys.md) |
| [on_callDisconnectedCause](arkts-telephony-call-oncalldisconnectedcause-f-sys.md) |
| [on_callEventChange](arkts-telephony-call-oncalleventchange-f-sys.md) |
| [on_callSessionEvent](arkts-telephony-call-oncallsessionevent-f-sys.md) |
| [on_cameraCapabilitiesChange](arkts-telephony-call-oncameracapabilitieschange-f-sys.md) |
| [on_imsCallModeChange](arkts-telephony-call-onimscallmodechange-f-sys.md) |
| [on_mmiCodeResult](arkts-telephony-call-onmmicoderesult-f-sys.md) |
| [on_peerDimensionsChange](arkts-telephony-call-onpeerdimensionschange-f-sys.md) |
| [on_postDialDelay](arkts-telephony-call-onpostdialdelay-f-sys.md) |
| [postDialProceed](arkts-telephony-call-postdialproceed-f-sys.md#postDialProceed-(System-API)) |
| [postDialProceed](arkts-telephony-call-postdialproceed-f-sys.md#postDialProceed-(System-API)) |
| [preloadCallUI](arkts-telephony-call-preloadcallui-f-sys.md#preloadCallUI-(System-API)) |
| [rejectCall](arkts-telephony-call-rejectcall-f-sys.md#rejectCall-(System-API)) |
| [rejectCall](arkts-telephony-call-rejectcall-f-sys.md#rejectCall-(System-API)) |
| [rejectCall](arkts-telephony-call-rejectcall-f-sys.md#rejectCall-(System-API)) |
| [rejectCall](arkts-telephony-call-rejectcall-f-sys.md#rejectCall-(System-API)) |
| [rejectCall](arkts-telephony-call-rejectcall-f-sys.md#rejectCall-(System-API)) |
| [removeMissedIncomingCallNotification](arkts-telephony-call-removemissedincomingcallnotification-f-sys.md#removeMissedIncomingCallNotification-(System-API)) |
| [removeMissedIncomingCallNotification](arkts-telephony-call-removemissedincomingcallnotification-f-sys.md#removeMissedIncomingCallNotification-(System-API)) |
| [sendCallUiEvent](arkts-telephony-call-sendcalluievent-f-sys.md#sendCallUiEvent-(System-API)) |
| [sendRttMessage](arkts-telephony-call-sendrttmessage-f-sys.md#sendRttMessage-(System-API)) |
| [sendUssdResponse](arkts-telephony-call-sendussdresponse-f-sys.md#sendUssdResponse-(System-API)) |
| [separateConference](arkts-telephony-call-separateconference-f-sys.md#separateConference-(System-API)) |
| [separateConference](arkts-telephony-call-separateconference-f-sys.md#separateConference-(System-API)) |
| [setAudioDevice](arkts-telephony-call-setaudiodevice-f-sys.md#setAudioDevice-(System-API)) |
| [setAudioDevice](arkts-telephony-call-setaudiodevice-f-sys.md#setAudioDevice-(System-API)) |
| [setCallRestriction](arkts-telephony-call-setcallrestriction-f-sys.md#setCallRestriction-(System-API)) |
| [setCallRestriction](arkts-telephony-call-setcallrestriction-f-sys.md#setCallRestriction-(System-API)) |
| [setCallRestrictionPassword](arkts-telephony-call-setcallrestrictionpassword-f-sys.md#setCallRestrictionPassword-(System-API)) |
| [setCallRestrictionPassword](arkts-telephony-call-setcallrestrictionpassword-f-sys.md#setCallRestrictionPassword-(System-API)) |
| [setCallTransfer](arkts-telephony-call-setcalltransfer-f-sys.md#setCallTransfer-(System-API)) |
| [setCallTransfer](arkts-telephony-call-setcalltransfer-f-sys.md#setCallTransfer-(System-API)) |
| [setCallWaiting](arkts-telephony-call-setcallwaiting-f-sys.md#setCallWaiting-(System-API)) |
| [setCallWaiting](arkts-telephony-call-setcallwaiting-f-sys.md#setCallWaiting-(System-API)) |
| [setDeviceDirection](arkts-telephony-call-setdevicedirection-f-sys.md#setDeviceDirection-(System-API)) |
| [setDisplaySurface](arkts-telephony-call-setdisplaysurface-f-sys.md#setDisplaySurface-(System-API)) |
| [setMuted](arkts-telephony-call-setmuted-f-sys.md#setMuted-(System-API)) |
| [setMuted](arkts-telephony-call-setmuted-f-sys.md#setMuted-(System-API)) |
| [setPreviewSurface](arkts-telephony-call-setpreviewsurface-f-sys.md#setPreviewSurface-(System-API)) |
| [setRttCapability](arkts-telephony-call-setrttcapability-f-sys.md#setRttCapability-(System-API)) |
| [setVoNRState](arkts-telephony-call-setvonrstate-f-sys.md#setVoNRState-(System-API)) |
| [setVoNRState](arkts-telephony-call-setvonrstate-f-sys.md#setVoNRState-(System-API)) |
| [startDTMF](arkts-telephony-call-startdtmf-f-sys.md#startDTMF-(System-API)) |
| [startDTMF](arkts-telephony-call-startdtmf-f-sys.md#startDTMF-(System-API)) |
| [startRtt](arkts-telephony-call-startrtt-f-sys.md#startRtt-(System-API)) |
| [stopDTMF](arkts-telephony-call-stopdtmf-f-sys.md#stopDTMF-(System-API)) |
| [stopDTMF](arkts-telephony-call-stopdtmf-f-sys.md#stopDTMF-(System-API)) |
| [stopRtt](arkts-telephony-call-stoprtt-f-sys.md#stopRtt-(System-API)) |
| [switchCall](arkts-telephony-call-switchcall-f-sys.md#switchCall-(System-API)) |
| [switchCall](arkts-telephony-call-switchcall-f-sys.md#switchCall-(System-API)) |
| [unHoldCall](arkts-telephony-call-unholdcall-f-sys.md#unHoldCall-(System-API)) |
| [unHoldCall](arkts-telephony-call-unholdcall-f-sys.md#unHoldCall-(System-API)) |
| [unloadCallUI](arkts-telephony-call-unloadcallui-f-sys.md#unloadCallUI-(System-API)) |
| [updateImsCallMode](arkts-telephony-call-updateimscallmode-f-sys.md#updateImsCallMode-(System-API)) |
| [updateImsCallMode](arkts-telephony-call-updateimscallmode-f-sys.md#updateImsCallMode-(System-API)) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DialOptions](arkts-telephony-call-dialoptions-i.md) |
| [EmergencyNumberOptions](arkts-telephony-call-emergencynumberoptions-i.md) |
| [MakeCallOptions](arkts-telephony-call-makecalloptions-i.md) |
| [NumberFormatOptions](arkts-telephony-call-numberformatoptions-i.md) |

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AudioDevice](arkts-telephony-call-audiodevice-i-sys.md) |
| [AudioDeviceCallbackInfo](arkts-telephony-call-audiodevicecallbackinfo-i-sys.md) |
| [CallAttributeOptions](arkts-telephony-call-callattributeoptions-i-sys.md) |
| [CallEventOptions](arkts-telephony-call-calleventoptions-i-sys.md) |
| [CallRestrictionInfo](arkts-telephony-call-callrestrictioninfo-i-sys.md) |
| [CallSessionEvent](arkts-telephony-call-callsessionevent-i-sys.md) |
| [CallTransferInfo](arkts-telephony-call-calltransferinfo-i-sys.md) |
| [CallTransferResult](arkts-telephony-call-calltransferresult-i-sys.md) |
| [CameraCapabilities](arkts-telephony-call-cameracapabilities-i-sys.md) |
| [DialCallOptions](arkts-telephony-call-dialcalloptions-i-sys.md) |
| [DialOptions](arkts-telephony-call-dialoptions-i-sys.md) |
| [DisconnectedDetails](arkts-telephony-call-disconnecteddetails-i-sys.md) |
| [ImsCallModeInfo](arkts-telephony-call-imscallmodeinfo-i-sys.md) |
| [MmiCodeResults](arkts-telephony-call-mmicoderesults-i-sys.md) |
| [NumberMarkInfo](arkts-telephony-call-numbermarkinfo-i-sys.md) |
| [PeerDimensionsDetail](arkts-telephony-call-peerdimensionsdetail-i-sys.md) |
| [RejectMessageOptions](arkts-telephony-call-rejectmessageoptions-i-sys.md) |
| [RttErrorInfo](arkts-telephony-call-rtterrorinfo-i-sys.md) |
| [RttEventInfo](arkts-telephony-call-rtteventinfo-i-sys.md) |
| [RttMessageInfo](arkts-telephony-call-rttmessageinfo-i-sys.md) |
| [VoipCallAttribute](arkts-telephony-call-voipcallattribute-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CCallState](arkts-telephony-call-ccallstate-e.md) |
| [CallState](arkts-telephony-call-callstate-e.md) |
| [TelCallState](arkts-telephony-call-telcallstate-e.md) |

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AudioDeviceType](arkts-telephony-call-audiodevicetype-e-sys.md) |
| [CallAbilityEventId](arkts-telephony-call-callabilityeventid-e-sys.md) |
| [CallRestrictionMode](arkts-telephony-call-callrestrictionmode-e-sys.md) |
| [CallRestrictionType](arkts-telephony-call-callrestrictiontype-e-sys.md) |
| [CallSessionEventId](arkts-telephony-call-callsessioneventid-e-sys.md) |
| [CallTransferSettingType](arkts-telephony-call-calltransfersettingtype-e-sys.md) |
| [CallTransferType](arkts-telephony-call-calltransfertype-e-sys.md) |
| [CallType](arkts-telephony-call-calltype-e-sys.md) |
| [CallWaitingStatus](arkts-telephony-call-callwaitingstatus-e-sys.md) |
| [ConferenceState](arkts-telephony-call-conferencestate-e-sys.md) |
| [DetailedCallState](arkts-telephony-call-detailedcallstate-e-sys.md) |
| [DeviceDirection](arkts-telephony-call-devicedirection-e-sys.md) |
| [DialScene](arkts-telephony-call-dialscene-e-sys.md) |
| [DialType](arkts-telephony-call-dialtype-e-sys.md) |
| [DisconnectedReason](arkts-telephony-call-disconnectedreason-e-sys.md) |
| [ImsCallMode](arkts-telephony-call-imscallmode-e-sys.md) |
| [ImsRttMode](arkts-telephony-call-imsrttmode-e-sys.md) |
| [MarkType](arkts-telephony-call-marktype-e-sys.md) |
| [MmiCodeResult](arkts-telephony-call-mmicoderesult-e-sys.md) |
| [RestrictionStatus](arkts-telephony-call-restrictionstatus-e-sys.md) |
| [RttState](arkts-telephony-call-rttstate-e-sys.md) |
| [TransferStatus](arkts-telephony-call-transferstatus-e-sys.md) |
| [VideoRequestResultType](arkts-telephony-call-videorequestresulttype-e-sys.md) |
| [VideoStateType](arkts-telephony-call-videostatetype-e-sys.md) |
| [VoNRState](arkts-telephony-call-vonrstate-e-sys.md) |
| [XCallType](arkts-telephony-call-xcalltype-e-sys.md) |
<!--DelEnd-->
