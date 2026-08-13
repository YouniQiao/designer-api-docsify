# @ohos.telephony.call(Call)

The **call** module provides call management functions, including making calls, redirecting to the dial screen,obtaining the call status, and formatting phone numbers.

To subscribe to call status changes, use  
[`observer.on('callStateChange')`](@ohos.telephony.observer:observer.on(type: 'callStateChange', callback: Callback&lt;CallStateInfo&gt;)).

**Since:** 6

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
| [answerCall](arkts-telephony-call-answercall-f.md#answercall-2) |
| [dial](arkts-telephony-call-dial-f.md#dial) |
| [dial](arkts-telephony-call-dial-f.md#dial-1) |
| [dial](arkts-telephony-call-dial-f.md#dial-2) |
| [formatPhoneNumber](arkts-telephony-call-formatphonenumber-f.md#formatphonenumber) |
| [formatPhoneNumber](arkts-telephony-call-formatphonenumber-f.md#formatphonenumber-1) |
| [formatPhoneNumber](arkts-telephony-call-formatphonenumber-f.md#formatphonenumber-2) |
| [formatPhoneNumberToE164](arkts-telephony-call-formatphonenumbertoe164-f.md#formatphonenumbertoe164) |
| [formatPhoneNumberToE164](arkts-telephony-call-formatphonenumbertoe164-f.md#formatphonenumbertoe164-1) |
| [getCallState](arkts-telephony-call-getcallstate-f.md#getcallstate) |
| [getCallState](arkts-telephony-call-getcallstate-f.md#getcallstate-1) |
| [getCallStateSync](arkts-telephony-call-getcallstatesync-f.md#getcallstatesync) |
| [getCallTransferInfo](arkts-telephony-call-getcalltransferinfo-f.md#getcalltransferinfo) |
| [hangUpCall](arkts-telephony-call-hangupcall-f.md#hangupcall-2) |
| [hasCall](arkts-telephony-call-hascall-f.md#hascall) |
| [hasCall](arkts-telephony-call-hascall-f.md#hascall-1) |
| [hasCallSync](arkts-telephony-call-hascallsync-f.md#hascallsync) |
| [hasVoiceCapability](arkts-telephony-call-hasvoicecapability-f.md#hasvoicecapability) |
| [isEmergencyPhoneNumber](arkts-telephony-call-isemergencyphonenumber-f.md#isemergencyphonenumber) |
| [isEmergencyPhoneNumber](arkts-telephony-call-isemergencyphonenumber-f.md#isemergencyphonenumber-1) |
| [isEmergencyPhoneNumber](arkts-telephony-call-isemergencyphonenumber-f.md#isemergencyphonenumber-2) |
| [makeCall](arkts-telephony-call-makecall-f.md#makecall) |
| [makeCall](arkts-telephony-call-makecall-f.md#makecall-1) |
| [makeCall](arkts-telephony-call-makecall-f.md#makecall-2) |
| [makeCall](arkts-telephony-call-makecall-f.md#makecall-3) |
| [makeCallWithToken](arkts-telephony-call-makecallwithtoken-f.md#makecallwithtoken) |
| [rejectCall](arkts-telephony-call-rejectcall-f.md#rejectcall-3) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [answerCall](arkts-telephony-call-answercall-f-sys.md#answercall) |
| [answerCall](arkts-telephony-call-answercall-f-sys.md#answercall-1) |
| [answerCall](arkts-telephony-call-answercall-f-sys.md#answercall-3) |
| [answerCall](arkts-telephony-call-answercall-f-sys.md#answercall-4) |
| [canSetCallTransferTime](arkts-telephony-call-cansetcalltransfertime-f-sys.md#cansetcalltransfertime) |
| [canSetCallTransferTime](arkts-telephony-call-cansetcalltransfertime-f-sys.md#cansetcalltransfertime-1) |
| [cancelCallUpgrade](arkts-telephony-call-cancelcallupgrade-f-sys.md#cancelcallupgrade) |
| [cancelMuted](arkts-telephony-call-cancelmuted-f-sys.md#cancelmuted) |
| [cancelMuted](arkts-telephony-call-cancelmuted-f-sys.md#cancelmuted-1) |
| [closeUnfinishedUssd](arkts-telephony-call-closeunfinishedussd-f-sys.md#closeunfinishedussd) |
| [closeUnfinishedUssd](arkts-telephony-call-closeunfinishedussd-f-sys.md#closeunfinishedussd-1) |
| [combineConference](arkts-telephony-call-combineconference-f-sys.md#combineconference) |
| [combineConference](arkts-telephony-call-combineconference-f-sys.md#combineconference-1) |
| [controlCamera](arkts-telephony-call-controlcamera-f-sys.md#controlcamera) |
| [dialCall](arkts-telephony-call-dialcall-f-sys.md#dialcall) |
| [dialCall](arkts-telephony-call-dialcall-f-sys.md#dialcall-1) |
| [dialCall](arkts-telephony-call-dialcall-f-sys.md#dialcall-2) |
| [disableImsSwitch](arkts-telephony-call-disableimsswitch-f-sys.md#disableimsswitch) |
| [disableImsSwitch](arkts-telephony-call-disableimsswitch-f-sys.md#disableimsswitch-1) |
| [enableImsSwitch](arkts-telephony-call-enableimsswitch-f-sys.md#enableimsswitch) |
| [enableImsSwitch](arkts-telephony-call-enableimsswitch-f-sys.md#enableimsswitch-1) |
| [getCallIdListForConference](arkts-telephony-call-getcallidlistforconference-f-sys.md#getcallidlistforconference) |
| [getCallIdListForConference](arkts-telephony-call-getcallidlistforconference-f-sys.md#getcallidlistforconference-1) |
| [getCallRestrictionStatus](arkts-telephony-call-getcallrestrictionstatus-f-sys.md#getcallrestrictionstatus) |
| [getCallRestrictionStatus](arkts-telephony-call-getcallrestrictionstatus-f-sys.md#getcallrestrictionstatus-1) |
| [getCallTransferInfo](arkts-telephony-call-getcalltransferinfo-f-sys.md#getcalltransferinfo-1) |
| [getCallTransferInfo](arkts-telephony-call-getcalltransferinfo-f-sys.md#getcalltransferinfo-2) |
| [getCallWaitingStatus](arkts-telephony-call-getcallwaitingstatus-f-sys.md#getcallwaitingstatus) |
| [getCallWaitingStatus](arkts-telephony-call-getcallwaitingstatus-f-sys.md#getcallwaitingstatus-1) |
| [getMainCallId](arkts-telephony-call-getmaincallid-f-sys.md#getmaincallid) |
| [getMainCallId](arkts-telephony-call-getmaincallid-f-sys.md#getmaincallid-1) |
| [getSubCallIdList](arkts-telephony-call-getsubcallidlist-f-sys.md#getsubcallidlist) |
| [getSubCallIdList](arkts-telephony-call-getsubcallidlist-f-sys.md#getsubcallidlist-1) |
| [getVoNRState](arkts-telephony-call-getvonrstate-f-sys.md#getvonrstate) |
| [getVoNRState](arkts-telephony-call-getvonrstate-f-sys.md#getvonrstate-1) |
| [hangUpCall](arkts-telephony-call-hangupcall-f-sys.md#hangupcall) |
| [hangUpCall](arkts-telephony-call-hangupcall-f-sys.md#hangupcall-1) |
| [holdCall](arkts-telephony-call-holdcall-f-sys.md#holdcall) |
| [holdCall](arkts-telephony-call-holdcall-f-sys.md#holdcall-1) |
| [inputDialerSpecialCode](arkts-telephony-call-inputdialerspecialcode-f-sys.md#inputdialerspecialcode) |
| [inputDialerSpecialCode](arkts-telephony-call-inputdialerspecialcode-f-sys.md#inputdialerspecialcode-1) |
| [isImsSwitchEnabled](arkts-telephony-call-isimsswitchenabled-f-sys.md#isimsswitchenabled) |
| [isImsSwitchEnabled](arkts-telephony-call-isimsswitchenabled-f-sys.md#isimsswitchenabled-1) |
| [isImsSwitchEnabledSync](arkts-telephony-call-isimsswitchenabledsync-f-sys.md#isimsswitchenabledsync) |
| [isInEmergencyCall](arkts-telephony-call-isinemergencycall-f-sys.md#isinemergencycall) |
| [isInEmergencyCall](arkts-telephony-call-isinemergencycall-f-sys.md#isinemergencycall-1) |
| [isNewCallAllowed](arkts-telephony-call-isnewcallallowed-f-sys.md#isnewcallallowed) |
| [isNewCallAllowed](arkts-telephony-call-isnewcallallowed-f-sys.md#isnewcallallowed-1) |
| [isRinging](arkts-telephony-call-isringing-f-sys.md#isringing) |
| [isRinging](arkts-telephony-call-isringing-f-sys.md#isringing-1) |
| [joinConference](arkts-telephony-call-joinconference-f-sys.md#joinconference) |
| [joinConference](arkts-telephony-call-joinconference-f-sys.md#joinconference-1) |
| [kickOutFromConference](arkts-telephony-call-kickoutfromconference-f-sys.md#kickoutfromconference) |
| [kickOutFromConference](arkts-telephony-call-kickoutfromconference-f-sys.md#kickoutfromconference-1) |
| [muteRinger](arkts-telephony-call-muteringer-f-sys.md#muteringer) |
| [muteRinger](arkts-telephony-call-muteringer-f-sys.md#muteringer-1) |
| [off](arkts-telephony-call-off-f-sys.md#off) |
| [off](arkts-telephony-call-off-f-sys.md#off-1) |
| [off](arkts-telephony-call-off-f-sys.md#off-2) |
| [off](arkts-telephony-call-off-f-sys.md#off-3) |
| [off](arkts-telephony-call-off-f-sys.md#off-4) |
| [off](arkts-telephony-call-off-f-sys.md#off-5) |
| [off](arkts-telephony-call-off-f-sys.md#off-6) |
| [off](arkts-telephony-call-off-f-sys.md#off-7) |
| [off](arkts-telephony-call-off-f-sys.md#off-8) |
| [off](arkts-telephony-call-off-f-sys.md#off-9) |
| [offReceiveRttMessage](arkts-telephony-call-offreceiverttmessage-f-sys.md#offreceiverttmessage) |
| [offRttErrCause](arkts-telephony-call-offrtterrcause-f-sys.md#offrtterrcause) |
| [offRttModifyInd](arkts-telephony-call-offrttmodifyind-f-sys.md#offrttmodifyind) |
| [on](arkts-telephony-call-on-f-sys.md#on) |
| [on](arkts-telephony-call-on-f-sys.md#on-1) |
| [on](arkts-telephony-call-on-f-sys.md#on-2) |
| [on](arkts-telephony-call-on-f-sys.md#on-3) |
| [on](arkts-telephony-call-on-f-sys.md#on-4) |
| [on](arkts-telephony-call-on-f-sys.md#on-5) |
| [on](arkts-telephony-call-on-f-sys.md#on-6) |
| [on](arkts-telephony-call-on-f-sys.md#on-7) |
| [on](arkts-telephony-call-on-f-sys.md#on-8) |
| [on](arkts-telephony-call-on-f-sys.md#on-9) |
| [onReceiveRttMessage](arkts-telephony-call-onreceiverttmessage-f-sys.md#onreceiverttmessage) |
| [onRttErrCause](arkts-telephony-call-onrtterrcause-f-sys.md#onrtterrcause) |
| [onRttModifyInd](arkts-telephony-call-onrttmodifyind-f-sys.md#onrttmodifyind) |
| [postDialProceed](arkts-telephony-call-postdialproceed-f-sys.md#postdialproceed) |
| [postDialProceed](arkts-telephony-call-postdialproceed-f-sys.md#postdialproceed-1) |
| [preloadCallUI](arkts-telephony-call-preloadcallui-f-sys.md#preloadcallui) |
| [rejectCall](arkts-telephony-call-rejectcall-f-sys.md#rejectcall) |
| [rejectCall](arkts-telephony-call-rejectcall-f-sys.md#rejectcall-1) |
| [rejectCall](arkts-telephony-call-rejectcall-f-sys.md#rejectcall-2) |
| [rejectCall](arkts-telephony-call-rejectcall-f-sys.md#rejectcall-4) |
| [removeMissedIncomingCallNotification](arkts-telephony-call-removemissedincomingcallnotification-f-sys.md#removemissedincomingcallnotification) |
| [removeMissedIncomingCallNotification](arkts-telephony-call-removemissedincomingcallnotification-f-sys.md#removemissedincomingcallnotification-1) |
| [sendCallUiEvent](arkts-telephony-call-sendcalluievent-f-sys.md#sendcalluievent) |
| [sendRttMessage](arkts-telephony-call-sendrttmessage-f-sys.md#sendrttmessage) |
| [sendUssdResponse](arkts-telephony-call-sendussdresponse-f-sys.md#sendussdresponse) |
| [separateConference](arkts-telephony-call-separateconference-f-sys.md#separateconference) |
| [separateConference](arkts-telephony-call-separateconference-f-sys.md#separateconference-1) |
| [setAudioDevice](arkts-telephony-call-setaudiodevice-f-sys.md#setaudiodevice) |
| [setAudioDevice](arkts-telephony-call-setaudiodevice-f-sys.md#setaudiodevice-1) |
| [setCallRestriction](arkts-telephony-call-setcallrestriction-f-sys.md#setcallrestriction) |
| [setCallRestriction](arkts-telephony-call-setcallrestriction-f-sys.md#setcallrestriction-1) |
| [setCallRestrictionPassword](arkts-telephony-call-setcallrestrictionpassword-f-sys.md#setcallrestrictionpassword) |
| [setCallRestrictionPassword](arkts-telephony-call-setcallrestrictionpassword-f-sys.md#setcallrestrictionpassword-1) |
| [setCallTransfer](arkts-telephony-call-setcalltransfer-f-sys.md#setcalltransfer) |
| [setCallTransfer](arkts-telephony-call-setcalltransfer-f-sys.md#setcalltransfer-1) |
| [setCallWaiting](arkts-telephony-call-setcallwaiting-f-sys.md#setcallwaiting) |
| [setCallWaiting](arkts-telephony-call-setcallwaiting-f-sys.md#setcallwaiting-1) |
| [setDeviceDirection](arkts-telephony-call-setdevicedirection-f-sys.md#setdevicedirection) |
| [setDisplaySurface](arkts-telephony-call-setdisplaysurface-f-sys.md#setdisplaysurface) |
| [setMuted](arkts-telephony-call-setmuted-f-sys.md#setmuted) |
| [setMuted](arkts-telephony-call-setmuted-f-sys.md#setmuted-1) |
| [setPreviewSurface](arkts-telephony-call-setpreviewsurface-f-sys.md#setpreviewsurface) |
| [setRttCapability](arkts-telephony-call-setrttcapability-f-sys.md#setrttcapability) |
| [setVoNRState](arkts-telephony-call-setvonrstate-f-sys.md#setvonrstate) |
| [setVoNRState](arkts-telephony-call-setvonrstate-f-sys.md#setvonrstate-1) |
| [startDTMF](arkts-telephony-call-startdtmf-f-sys.md#startdtmf) |
| [startDTMF](arkts-telephony-call-startdtmf-f-sys.md#startdtmf-1) |
| [startRtt](arkts-telephony-call-startrtt-f-sys.md#startrtt) |
| [stopDTMF](arkts-telephony-call-stopdtmf-f-sys.md#stopdtmf) |
| [stopDTMF](arkts-telephony-call-stopdtmf-f-sys.md#stopdtmf-1) |
| [stopRtt](arkts-telephony-call-stoprtt-f-sys.md#stoprtt) |
| [switchCall](arkts-telephony-call-switchcall-f-sys.md#switchcall) |
| [switchCall](arkts-telephony-call-switchcall-f-sys.md#switchcall-1) |
| [unHoldCall](arkts-telephony-call-unholdcall-f-sys.md#unholdcall) |
| [unHoldCall](arkts-telephony-call-unholdcall-f-sys.md#unholdcall-1) |
| [unloadCallUI](arkts-telephony-call-unloadcallui-f-sys.md#unloadcallui) |
| [updateImsCallMode](arkts-telephony-call-updateimscallmode-f-sys.md#updateimscallmode) |
| [updateImsCallMode](arkts-telephony-call-updateimscallmode-f-sys.md#updateimscallmode-1) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CallTransferResult](arkts-telephony-call-calltransferresult-i.md) |
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
| [CallTransferType](arkts-telephony-call-calltransfertype-e.md) |
| [TelCallState](arkts-telephony-call-telcallstate-e.md) |
| [TransferStatus](arkts-telephony-call-transferstatus-e.md) |

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
| [VideoRequestResultType](arkts-telephony-call-videorequestresulttype-e-sys.md) |
| [VideoStateType](arkts-telephony-call-videostatetype-e-sys.md) |
| [VoNRState](arkts-telephony-call-vonrstate-e-sys.md) |
| [XCallType](arkts-telephony-call-xcalltype-e-sys.md) |
<!--DelEnd-->
