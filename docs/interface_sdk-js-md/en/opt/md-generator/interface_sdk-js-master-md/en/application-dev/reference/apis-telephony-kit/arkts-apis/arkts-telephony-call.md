# @ohos.telephony.call

The **call** module provides call management functions, including making calls, redirecting to the dial screen, obtaining the call status, and formatting phone numbers. To subscribe to call status changes, use [`observer.on('callStateChange')`](arkts-telephony-observer-onnetworkstatechange-f.md#onnetworkstatechange).

**Since:** 23

<!--Device-unnamed-declare namespace call--><!--Device-unnamed-declare namespace call-End-->

**System capability:** SystemCapability.Telephony.CallManager

## Modules to Import

```TypeScript
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [dial](arkts-telephony-call-dial-f.md#dial) |
| [dial](arkts-telephony-call-dial-f.md#dial) |
| [dial](arkts-telephony-call-dial-f.md#dial) |
| [formatPhoneNumber](arkts-telephony-call-formatphonenumber-f.md#formatphonenumber) |
| [formatPhoneNumber](arkts-telephony-call-formatphonenumber-f.md#formatphonenumber) |
| [formatPhoneNumber](arkts-telephony-call-formatphonenumber-f.md#formatphonenumber) |
| [formatPhoneNumberToE164](arkts-telephony-call-formatphonenumbertoe164-f.md#formatphonenumbertoe164) |
| [formatPhoneNumberToE164](arkts-telephony-call-formatphonenumbertoe164-f.md#formatphonenumbertoe164) |
| [getCallState](arkts-telephony-call-getcallstate-f.md#getcallstate) |
| [getCallState](arkts-telephony-call-getcallstate-f.md#getcallstate) |
| [getCallStateSync](arkts-telephony-call-getcallstatesync-f.md#getcallstatesync) |
| [getCallTransferInfo](arkts-telephony-call-getcalltransferinfo-f.md#getcalltransferinfo) |
| [hasCall](arkts-telephony-call-hascall-f.md#hascall) |
| [hasCall](arkts-telephony-call-hascall-f.md#hascall) |
| [hasCallSync](arkts-telephony-call-hascallsync-f.md#hascallsync) |
| [hasVoiceCapability](arkts-telephony-call-hasvoicecapability-f.md#hasvoicecapability) |
| [isEmergencyPhoneNumber](arkts-telephony-call-isemergencyphonenumber-f.md#isemergencyphonenumber) |
| [isEmergencyPhoneNumber](arkts-telephony-call-isemergencyphonenumber-f.md#isemergencyphonenumber) |
| [isEmergencyPhoneNumber](arkts-telephony-call-isemergencyphonenumber-f.md#isemergencyphonenumber) |
| [makeCall](arkts-telephony-call-makecall-f.md#makecall) |
| [makeCall](arkts-telephony-call-makecall-f.md#makecall) |
| [makeCall](arkts-telephony-call-makecall-f.md#makecall) |
| [makeCall](arkts-telephony-call-makecall-f.md#makecall) |
| [makeCallWithToken](arkts-telephony-call-makecallwithtoken-f.md#makecallwithtoken) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [answerCall](arkts-telephony-call-answercall-f-sys.md#answercall-system-api) |
| [answerCall](arkts-telephony-call-answercall-f-sys.md#answercall-system-api) |
| [answerCall](arkts-telephony-call-answercall-f-sys.md#answercall-system-api) |
| [answerCall](arkts-telephony-call-answercall-f-sys.md#answercall-system-api) |
| [answerCall](arkts-telephony-call-answercall-f-sys.md#answercall-system-api) |
| [canSetCallTransferTime](arkts-telephony-call-cansetcalltransfertime-f-sys.md#cansetcalltransfertime-system-api) |
| [canSetCallTransferTime](arkts-telephony-call-cansetcalltransfertime-f-sys.md#cansetcalltransfertime-system-api) |
| [cancelCallUpgrade](arkts-telephony-call-cancelcallupgrade-f-sys.md#cancelcallupgrade-system-api) |
| [cancelMuted](arkts-telephony-call-cancelmuted-f-sys.md#cancelmuted-system-api) |
| [cancelMuted](arkts-telephony-call-cancelmuted-f-sys.md#cancelmuted-system-api) |
| [closeUnfinishedUssd](arkts-telephony-call-closeunfinishedussd-f-sys.md#closeunfinishedussd-system-api) |
| [closeUnfinishedUssd](arkts-telephony-call-closeunfinishedussd-f-sys.md#closeunfinishedussd-system-api) |
| [combineConference](arkts-telephony-call-combineconference-f-sys.md#combineconference-system-api) |
| [combineConference](arkts-telephony-call-combineconference-f-sys.md#combineconference-system-api) |
| [controlCamera](arkts-telephony-call-controlcamera-f-sys.md#controlcamera-system-api) |
| [dialCall](arkts-telephony-call-dialcall-f-sys.md#dialcall-system-api) |
| [dialCall](arkts-telephony-call-dialcall-f-sys.md#dialcall-system-api) |
| [dialCall](arkts-telephony-call-dialcall-f-sys.md#dialcall-system-api) |
| [disableImsSwitch](arkts-telephony-call-disableimsswitch-f-sys.md#disableimsswitch-system-api) |
| [disableImsSwitch](arkts-telephony-call-disableimsswitch-f-sys.md#disableimsswitch-system-api) |
| [enableImsSwitch](arkts-telephony-call-enableimsswitch-f-sys.md#enableimsswitch-system-api) |
| [enableImsSwitch](arkts-telephony-call-enableimsswitch-f-sys.md#enableimsswitch-system-api) |
| [getCallIdListForConference](arkts-telephony-call-getcallidlistforconference-f-sys.md#getcallidlistforconference-system-api) |
| [getCallIdListForConference](arkts-telephony-call-getcallidlistforconference-f-sys.md#getcallidlistforconference-system-api) |
| [getCallRestrictionStatus](arkts-telephony-call-getcallrestrictionstatus-f-sys.md#getcallrestrictionstatus-system-api) |
| [getCallRestrictionStatus](arkts-telephony-call-getcallrestrictionstatus-f-sys.md#getcallrestrictionstatus-system-api) |
| [getCallTransferInfo](arkts-telephony-call-getcalltransferinfo-f-sys.md#getcalltransferinfo-system-api) |
| [getCallTransferInfo](arkts-telephony-call-getcalltransferinfo-f-sys.md#getcalltransferinfo-system-api) |
| [getCallWaitingStatus](arkts-telephony-call-getcallwaitingstatus-f-sys.md#getcallwaitingstatus-system-api) |
| [getCallWaitingStatus](arkts-telephony-call-getcallwaitingstatus-f-sys.md#getcallwaitingstatus-system-api) |
| [getMainCallId](arkts-telephony-call-getmaincallid-f-sys.md#getmaincallid-system-api) |
| [getMainCallId](arkts-telephony-call-getmaincallid-f-sys.md#getmaincallid-system-api) |
| [getSubCallIdList](arkts-telephony-call-getsubcallidlist-f-sys.md#getsubcallidlist-system-api) |
| [getSubCallIdList](arkts-telephony-call-getsubcallidlist-f-sys.md#getsubcallidlist-system-api) |
| [getVoNRState](arkts-telephony-call-getvonrstate-f-sys.md#getvonrstate-system-api) |
| [getVoNRState](arkts-telephony-call-getvonrstate-f-sys.md#getvonrstate-system-api) |
| [hangUpCall](arkts-telephony-call-hangupcall-f-sys.md#hangupcall-system-api) |
| [hangUpCall](arkts-telephony-call-hangupcall-f-sys.md#hangupcall-system-api) |
| [hangUpCall](arkts-telephony-call-hangupcall-f-sys.md#hangupcall-system-api) |
| [holdCall](arkts-telephony-call-holdcall-f-sys.md#holdcall-system-api) |
| [holdCall](arkts-telephony-call-holdcall-f-sys.md#holdcall-system-api) |
| [inputDialerSpecialCode](arkts-telephony-call-inputdialerspecialcode-f-sys.md#inputdialerspecialcode-system-api) |
| [inputDialerSpecialCode](arkts-telephony-call-inputdialerspecialcode-f-sys.md#inputdialerspecialcode-system-api) |
| [isImsSwitchEnabled](arkts-telephony-call-isimsswitchenabled-f-sys.md#isimsswitchenabled-system-api) |
| [isImsSwitchEnabled](arkts-telephony-call-isimsswitchenabled-f-sys.md#isimsswitchenabled-system-api) |
| [isImsSwitchEnabledSync](arkts-telephony-call-isimsswitchenabledsync-f-sys.md#isimsswitchenabledsync-system-api) |
| [isInEmergencyCall](arkts-telephony-call-isinemergencycall-f-sys.md#isinemergencycall-system-api) |
| [isInEmergencyCall](arkts-telephony-call-isinemergencycall-f-sys.md#isinemergencycall-system-api) |
| [isNewCallAllowed](arkts-telephony-call-isnewcallallowed-f-sys.md#isnewcallallowed-system-api) |
| [isNewCallAllowed](arkts-telephony-call-isnewcallallowed-f-sys.md#isnewcallallowed-system-api) |
| [isRinging](arkts-telephony-call-isringing-f-sys.md#isringing-system-api) |
| [isRinging](arkts-telephony-call-isringing-f-sys.md#isringing-system-api) |
| [joinConference](arkts-telephony-call-joinconference-f-sys.md#joinconference-system-api) |
| [joinConference](arkts-telephony-call-joinconference-f-sys.md#joinconference-system-api) |
| [kickOutFromConference](arkts-telephony-call-kickoutfromconference-f-sys.md#kickoutfromconference-system-api) |
| [kickOutFromConference](arkts-telephony-call-kickoutfromconference-f-sys.md#kickoutfromconference-system-api) |
| [muteRinger](arkts-telephony-call-muteringer-f-sys.md#muteringer-system-api) |
| [muteRinger](arkts-telephony-call-muteringer-f-sys.md#muteringer-system-api) |
| [offAudioDeviceChange](arkts-telephony-call-offaudiodevicechange-f-sys.md#offaudiodevicechange) |
| [offCallDetailsChange](arkts-telephony-call-offcalldetailschange-f-sys.md#offcalldetailschange) |
| [offCallDisconnectedCause](arkts-telephony-call-offcalldisconnectedcause-f-sys.md#offcalldisconnectedcause) |
| [offCallEventChange](arkts-telephony-call-offcalleventchange-f-sys.md#offcalleventchange) |
| [offCallSessionEvent](arkts-telephony-call-offcallsessionevent-f-sys.md#offcallsessionevent) |
| [offCameraCapabilitiesChange](arkts-telephony-call-offcameracapabilitieschange-f-sys.md#offcameracapabilitieschange) |
| [offImsCallModeChange](arkts-telephony-call-offimscallmodechange-f-sys.md#offimscallmodechange) |
| [offMmiCodeResult](arkts-telephony-call-offmmicoderesult-f-sys.md#offmmicoderesult) |
| [offPeerDimensionsChange](arkts-telephony-call-offpeerdimensionschange-f-sys.md#offpeerdimensionschange) |
| [offPostDialDelay](arkts-telephony-call-offpostdialdelay-f-sys.md#offpostdialdelay) |
| [offReceiveRttMessage](arkts-telephony-call-offreceiverttmessage-f-sys.md#offreceiverttmessage-system-api) |
| [offRttErrCause](arkts-telephony-call-offrtterrcause-f-sys.md#offrtterrcause-system-api) |
| [offRttModifyInd](arkts-telephony-call-offrttmodifyind-f-sys.md#offrttmodifyind-system-api) |
| [off_audioDeviceChange](arkts-telephony-call-offaudiodevicechange-f-sys.md#offaudiodevicechange) |
| [off_callDetailsChange](arkts-telephony-call-offcalldetailschange-f-sys.md#offcalldetailschange) |
| [off_callDisconnectedCause](arkts-telephony-call-offcalldisconnectedcause-f-sys.md#offcalldisconnectedcause) |
| [off_callEventChange](arkts-telephony-call-offcalleventchange-f-sys.md#offcalleventchange) |
| [off_callSessionEvent](arkts-telephony-call-offcallsessionevent-f-sys.md#offcallsessionevent) |
| [off_cameraCapabilitiesChange](arkts-telephony-call-offcameracapabilitieschange-f-sys.md#offcameracapabilitieschange) |
| [off_imsCallModeChange](arkts-telephony-call-offimscallmodechange-f-sys.md#offimscallmodechange) |
| [off_mmiCodeResult](arkts-telephony-call-offmmicoderesult-f-sys.md#offmmicoderesult) |
| [off_peerDimensionsChange](arkts-telephony-call-offpeerdimensionschange-f-sys.md#offpeerdimensionschange) |
| [off_postDialDelay](arkts-telephony-call-offpostdialdelay-f-sys.md#offpostdialdelay) |
| [onAudioDeviceChange](arkts-telephony-call-onaudiodevicechange-f-sys.md#onaudiodevicechange) |
| [onCallDetailsChange](arkts-telephony-call-oncalldetailschange-f-sys.md#oncalldetailschange) |
| [onCallDisconnectedCause](arkts-telephony-call-oncalldisconnectedcause-f-sys.md#oncalldisconnectedcause) |
| [onCallEventChange](arkts-telephony-call-oncalleventchange-f-sys.md#oncalleventchange) |
| [onCallSessionEvent](arkts-telephony-call-oncallsessionevent-f-sys.md#oncallsessionevent) |
| [onCameraCapabilitiesChange](arkts-telephony-call-oncameracapabilitieschange-f-sys.md#oncameracapabilitieschange) |
| [onImsCallModeChange](arkts-telephony-call-onimscallmodechange-f-sys.md#onimscallmodechange) |
| [onMmiCodeResult](arkts-telephony-call-onmmicoderesult-f-sys.md#onmmicoderesult) |
| [onPeerDimensionsChange](arkts-telephony-call-onpeerdimensionschange-f-sys.md#onpeerdimensionschange) |
| [onPostDialDelay](arkts-telephony-call-onpostdialdelay-f-sys.md#onpostdialdelay) |
| [onReceiveRttMessage](arkts-telephony-call-onreceiverttmessage-f-sys.md#onreceiverttmessage-system-api) |
| [onRttErrCause](arkts-telephony-call-onrtterrcause-f-sys.md#onrtterrcause-system-api) |
| [onRttModifyInd](arkts-telephony-call-onrttmodifyind-f-sys.md#onrttmodifyind-system-api) |
| [on_audioDeviceChange](arkts-telephony-call-onaudiodevicechange-f-sys.md#onaudiodevicechange) |
| [on_callDetailsChange](arkts-telephony-call-oncalldetailschange-f-sys.md#oncalldetailschange) |
| [on_callDisconnectedCause](arkts-telephony-call-oncalldisconnectedcause-f-sys.md#oncalldisconnectedcause) |
| [on_callEventChange](arkts-telephony-call-oncalleventchange-f-sys.md#oncalleventchange) |
| [on_callSessionEvent](arkts-telephony-call-oncallsessionevent-f-sys.md#oncallsessionevent) |
| [on_cameraCapabilitiesChange](arkts-telephony-call-oncameracapabilitieschange-f-sys.md#oncameracapabilitieschange) |
| [on_imsCallModeChange](arkts-telephony-call-onimscallmodechange-f-sys.md#onimscallmodechange) |
| [on_mmiCodeResult](arkts-telephony-call-onmmicoderesult-f-sys.md#onmmicoderesult) |
| [on_peerDimensionsChange](arkts-telephony-call-onpeerdimensionschange-f-sys.md#onpeerdimensionschange) |
| [on_postDialDelay](arkts-telephony-call-onpostdialdelay-f-sys.md#onpostdialdelay) |
| [postDialProceed](arkts-telephony-call-postdialproceed-f-sys.md#postdialproceed-system-api) |
| [postDialProceed](arkts-telephony-call-postdialproceed-f-sys.md#postdialproceed-system-api) |
| [preloadCallUI](arkts-telephony-call-preloadcallui-f-sys.md#preloadcallui-system-api) |
| [rejectCall](arkts-telephony-call-rejectcall-f-sys.md#rejectcall-system-api) |
| [rejectCall](arkts-telephony-call-rejectcall-f-sys.md#rejectcall-system-api) |
| [rejectCall](arkts-telephony-call-rejectcall-f-sys.md#rejectcall-system-api) |
| [rejectCall](arkts-telephony-call-rejectcall-f-sys.md#rejectcall-system-api) |
| [rejectCall](arkts-telephony-call-rejectcall-f-sys.md#rejectcall-system-api) |
| [removeMissedIncomingCallNotification](arkts-telephony-call-removemissedincomingcallnotification-f-sys.md#removemissedincomingcallnotification-system-api) |
| [removeMissedIncomingCallNotification](arkts-telephony-call-removemissedincomingcallnotification-f-sys.md#removemissedincomingcallnotification-system-api) |
| [sendCallUiEvent](arkts-telephony-call-sendcalluievent-f-sys.md#sendcalluievent-system-api) |
| [sendRttMessage](arkts-telephony-call-sendrttmessage-f-sys.md#sendrttmessage-system-api) |
| [sendUssdResponse](arkts-telephony-call-sendussdresponse-f-sys.md#sendussdresponse-system-api) |
| [separateConference](arkts-telephony-call-separateconference-f-sys.md#separateconference-system-api) |
| [separateConference](arkts-telephony-call-separateconference-f-sys.md#separateconference-system-api) |
| [setAudioDevice](arkts-telephony-call-setaudiodevice-f-sys.md#setaudiodevice-system-api) |
| [setAudioDevice](arkts-telephony-call-setaudiodevice-f-sys.md#setaudiodevice-system-api) |
| [setCallRestriction](arkts-telephony-call-setcallrestriction-f-sys.md#setcallrestriction-system-api) |
| [setCallRestriction](arkts-telephony-call-setcallrestriction-f-sys.md#setcallrestriction-system-api) |
| [setCallRestrictionPassword](arkts-telephony-call-setcallrestrictionpassword-f-sys.md#setcallrestrictionpassword-system-api) |
| [setCallRestrictionPassword](arkts-telephony-call-setcallrestrictionpassword-f-sys.md#setcallrestrictionpassword-system-api) |
| [setCallTransfer](arkts-telephony-call-setcalltransfer-f-sys.md#setcalltransfer-system-api) |
| [setCallTransfer](arkts-telephony-call-setcalltransfer-f-sys.md#setcalltransfer-system-api) |
| [setCallWaiting](arkts-telephony-call-setcallwaiting-f-sys.md#setcallwaiting-system-api) |
| [setCallWaiting](arkts-telephony-call-setcallwaiting-f-sys.md#setcallwaiting-system-api) |
| [setDeviceDirection](arkts-telephony-call-setdevicedirection-f-sys.md#setdevicedirection-system-api) |
| [setDisplaySurface](arkts-telephony-call-setdisplaysurface-f-sys.md#setdisplaysurface-system-api) |
| [setMuted](arkts-telephony-call-setmuted-f-sys.md#setmuted-system-api) |
| [setMuted](arkts-telephony-call-setmuted-f-sys.md#setmuted-system-api) |
| [setPreviewSurface](arkts-telephony-call-setpreviewsurface-f-sys.md#setpreviewsurface-system-api) |
| [setRttCapability](arkts-telephony-call-setrttcapability-f-sys.md#setrttcapability-system-api) |
| [setVoNRState](arkts-telephony-call-setvonrstate-f-sys.md#setvonrstate-system-api) |
| [setVoNRState](arkts-telephony-call-setvonrstate-f-sys.md#setvonrstate-system-api) |
| [startDTMF](arkts-telephony-call-startdtmf-f-sys.md#startdtmf-system-api) |
| [startDTMF](arkts-telephony-call-startdtmf-f-sys.md#startdtmf-system-api) |
| [startRtt](arkts-telephony-call-startrtt-f-sys.md#startrtt-system-api) |
| [stopDTMF](arkts-telephony-call-stopdtmf-f-sys.md#stopdtmf-system-api) |
| [stopDTMF](arkts-telephony-call-stopdtmf-f-sys.md#stopdtmf-system-api) |
| [stopRtt](arkts-telephony-call-stoprtt-f-sys.md#stoprtt-system-api) |
| [switchCall](arkts-telephony-call-switchcall-f-sys.md#switchcall-system-api) |
| [switchCall](arkts-telephony-call-switchcall-f-sys.md#switchcall-system-api) |
| [unHoldCall](arkts-telephony-call-unholdcall-f-sys.md#unholdcall-system-api) |
| [unHoldCall](arkts-telephony-call-unholdcall-f-sys.md#unholdcall-system-api) |
| [unloadCallUI](arkts-telephony-call-unloadcallui-f-sys.md#unloadcallui-system-api) |
| [updateImsCallMode](arkts-telephony-call-updateimscallmode-f-sys.md#updateimscallmode-system-api) |
| [updateImsCallMode](arkts-telephony-call-updateimscallmode-f-sys.md#updateimscallmode-system-api) |
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
