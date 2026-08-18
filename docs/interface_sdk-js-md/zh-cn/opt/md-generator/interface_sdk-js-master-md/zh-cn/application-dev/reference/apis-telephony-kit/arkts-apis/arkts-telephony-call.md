# @ohos.telephony.call

该模块提供呼叫管理功能，包括拨打电话、跳转到拨号界面、获取通话状态、格式化电话号码等。 如需订阅通话状态请使用 [`observer.on('callStateChange')`](arkts-telephony-observer-onnetworkstatechange-f.md#onnetworkstatechange) 。

**起始版本：** 23

<!--Device-unnamed-declare namespace call--><!--Device-unnamed-declare namespace call-End-->

**系统能力：** SystemCapability.Telephony.CallManager

## 导入模块

```TypeScript
```

## 汇总

### 函数

| 名称 |
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
### 函数（系统接口）

| 名称 |
| --- |
| [answerCall](arkts-telephony-call-answercall-f-sys.md#answercall系统接口) |
| [answerCall](arkts-telephony-call-answercall-f-sys.md#answercall系统接口) |
| [answerCall](arkts-telephony-call-answercall-f-sys.md#answercall系统接口) |
| [answerCall](arkts-telephony-call-answercall-f-sys.md#answercall系统接口) |
| [answerCall](arkts-telephony-call-answercall-f-sys.md#answercall系统接口) |
| [canSetCallTransferTime](arkts-telephony-call-cansetcalltransfertime-f-sys.md#cansetcalltransfertime系统接口) |
| [canSetCallTransferTime](arkts-telephony-call-cansetcalltransfertime-f-sys.md#cansetcalltransfertime系统接口) |
| [cancelCallUpgrade](arkts-telephony-call-cancelcallupgrade-f-sys.md#cancelcallupgrade系统接口) |
| [cancelMuted](arkts-telephony-call-cancelmuted-f-sys.md#cancelmuted系统接口) |
| [cancelMuted](arkts-telephony-call-cancelmuted-f-sys.md#cancelmuted系统接口) |
| [closeUnfinishedUssd](arkts-telephony-call-closeunfinishedussd-f-sys.md#closeunfinishedussd系统接口) |
| [closeUnfinishedUssd](arkts-telephony-call-closeunfinishedussd-f-sys.md#closeunfinishedussd系统接口) |
| [combineConference](arkts-telephony-call-combineconference-f-sys.md#combineconference系统接口) |
| [combineConference](arkts-telephony-call-combineconference-f-sys.md#combineconference系统接口) |
| [controlCamera](arkts-telephony-call-controlcamera-f-sys.md#controlcamera系统接口) |
| [dialCall](arkts-telephony-call-dialcall-f-sys.md#dialcall系统接口) |
| [dialCall](arkts-telephony-call-dialcall-f-sys.md#dialcall系统接口) |
| [dialCall](arkts-telephony-call-dialcall-f-sys.md#dialcall系统接口) |
| [disableImsSwitch](arkts-telephony-call-disableimsswitch-f-sys.md#disableimsswitch系统接口) |
| [disableImsSwitch](arkts-telephony-call-disableimsswitch-f-sys.md#disableimsswitch系统接口) |
| [enableImsSwitch](arkts-telephony-call-enableimsswitch-f-sys.md#enableimsswitch系统接口) |
| [enableImsSwitch](arkts-telephony-call-enableimsswitch-f-sys.md#enableimsswitch系统接口) |
| [getCallIdListForConference](arkts-telephony-call-getcallidlistforconference-f-sys.md#getcallidlistforconference系统接口) |
| [getCallIdListForConference](arkts-telephony-call-getcallidlistforconference-f-sys.md#getcallidlistforconference系统接口) |
| [getCallRestrictionStatus](arkts-telephony-call-getcallrestrictionstatus-f-sys.md#getcallrestrictionstatus系统接口) |
| [getCallRestrictionStatus](arkts-telephony-call-getcallrestrictionstatus-f-sys.md#getcallrestrictionstatus系统接口) |
| [getCallTransferInfo](arkts-telephony-call-getcalltransferinfo-f-sys.md#getcalltransferinfo系统接口) |
| [getCallTransferInfo](arkts-telephony-call-getcalltransferinfo-f-sys.md#getcalltransferinfo系统接口) |
| [getCallWaitingStatus](arkts-telephony-call-getcallwaitingstatus-f-sys.md#getcallwaitingstatus系统接口) |
| [getCallWaitingStatus](arkts-telephony-call-getcallwaitingstatus-f-sys.md#getcallwaitingstatus系统接口) |
| [getMainCallId](arkts-telephony-call-getmaincallid-f-sys.md#getmaincallid系统接口) |
| [getMainCallId](arkts-telephony-call-getmaincallid-f-sys.md#getmaincallid系统接口) |
| [getSubCallIdList](arkts-telephony-call-getsubcallidlist-f-sys.md#getsubcallidlist系统接口) |
| [getSubCallIdList](arkts-telephony-call-getsubcallidlist-f-sys.md#getsubcallidlist系统接口) |
| [getVoNRState](arkts-telephony-call-getvonrstate-f-sys.md#getvonrstate系统接口) |
| [getVoNRState](arkts-telephony-call-getvonrstate-f-sys.md#getvonrstate系统接口) |
| [hangUpCall](arkts-telephony-call-hangupcall-f-sys.md#hangupcall系统接口) |
| [hangUpCall](arkts-telephony-call-hangupcall-f-sys.md#hangupcall系统接口) |
| [hangUpCall](arkts-telephony-call-hangupcall-f-sys.md#hangupcall系统接口) |
| [holdCall](arkts-telephony-call-holdcall-f-sys.md#holdcall系统接口) |
| [holdCall](arkts-telephony-call-holdcall-f-sys.md#holdcall系统接口) |
| [inputDialerSpecialCode](arkts-telephony-call-inputdialerspecialcode-f-sys.md#inputdialerspecialcode系统接口) |
| [inputDialerSpecialCode](arkts-telephony-call-inputdialerspecialcode-f-sys.md#inputdialerspecialcode系统接口) |
| [isImsSwitchEnabled](arkts-telephony-call-isimsswitchenabled-f-sys.md#isimsswitchenabled系统接口) |
| [isImsSwitchEnabled](arkts-telephony-call-isimsswitchenabled-f-sys.md#isimsswitchenabled系统接口) |
| [isImsSwitchEnabledSync](arkts-telephony-call-isimsswitchenabledsync-f-sys.md#isimsswitchenabledsync系统接口) |
| [isInEmergencyCall](arkts-telephony-call-isinemergencycall-f-sys.md#isinemergencycall系统接口) |
| [isInEmergencyCall](arkts-telephony-call-isinemergencycall-f-sys.md#isinemergencycall系统接口) |
| [isNewCallAllowed](arkts-telephony-call-isnewcallallowed-f-sys.md#isnewcallallowed系统接口) |
| [isNewCallAllowed](arkts-telephony-call-isnewcallallowed-f-sys.md#isnewcallallowed系统接口) |
| [isRinging](arkts-telephony-call-isringing-f-sys.md#isringing系统接口) |
| [isRinging](arkts-telephony-call-isringing-f-sys.md#isringing系统接口) |
| [joinConference](arkts-telephony-call-joinconference-f-sys.md#joinconference系统接口) |
| [joinConference](arkts-telephony-call-joinconference-f-sys.md#joinconference系统接口) |
| [kickOutFromConference](arkts-telephony-call-kickoutfromconference-f-sys.md#kickoutfromconference系统接口) |
| [kickOutFromConference](arkts-telephony-call-kickoutfromconference-f-sys.md#kickoutfromconference系统接口) |
| [muteRinger](arkts-telephony-call-muteringer-f-sys.md#muteringer系统接口) |
| [muteRinger](arkts-telephony-call-muteringer-f-sys.md#muteringer系统接口) |
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
| [offReceiveRttMessage](arkts-telephony-call-offreceiverttmessage-f-sys.md#offreceiverttmessage系统接口) |
| [offRttErrCause](arkts-telephony-call-offrtterrcause-f-sys.md#offrtterrcause系统接口) |
| [offRttModifyInd](arkts-telephony-call-offrttmodifyind-f-sys.md#offrttmodifyind系统接口) |
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
| [onReceiveRttMessage](arkts-telephony-call-onreceiverttmessage-f-sys.md#onreceiverttmessage系统接口) |
| [onRttErrCause](arkts-telephony-call-onrtterrcause-f-sys.md#onrtterrcause系统接口) |
| [onRttModifyInd](arkts-telephony-call-onrttmodifyind-f-sys.md#onrttmodifyind系统接口) |
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
| [postDialProceed](arkts-telephony-call-postdialproceed-f-sys.md#postdialproceed系统接口) |
| [postDialProceed](arkts-telephony-call-postdialproceed-f-sys.md#postdialproceed系统接口) |
| [preloadCallUI](arkts-telephony-call-preloadcallui-f-sys.md#preloadcallui系统接口) |
| [rejectCall](arkts-telephony-call-rejectcall-f-sys.md#rejectcall系统接口) |
| [rejectCall](arkts-telephony-call-rejectcall-f-sys.md#rejectcall系统接口) |
| [rejectCall](arkts-telephony-call-rejectcall-f-sys.md#rejectcall系统接口) |
| [rejectCall](arkts-telephony-call-rejectcall-f-sys.md#rejectcall系统接口) |
| [rejectCall](arkts-telephony-call-rejectcall-f-sys.md#rejectcall系统接口) |
| [removeMissedIncomingCallNotification](arkts-telephony-call-removemissedincomingcallnotification-f-sys.md#removemissedincomingcallnotification系统接口) |
| [removeMissedIncomingCallNotification](arkts-telephony-call-removemissedincomingcallnotification-f-sys.md#removemissedincomingcallnotification系统接口) |
| [sendCallUiEvent](arkts-telephony-call-sendcalluievent-f-sys.md#sendcalluievent系统接口) |
| [sendRttMessage](arkts-telephony-call-sendrttmessage-f-sys.md#sendrttmessage系统接口) |
| [sendUssdResponse](arkts-telephony-call-sendussdresponse-f-sys.md#sendussdresponse系统接口) |
| [separateConference](arkts-telephony-call-separateconference-f-sys.md#separateconference系统接口) |
| [separateConference](arkts-telephony-call-separateconference-f-sys.md#separateconference系统接口) |
| [setAudioDevice](arkts-telephony-call-setaudiodevice-f-sys.md#setaudiodevice系统接口) |
| [setAudioDevice](arkts-telephony-call-setaudiodevice-f-sys.md#setaudiodevice系统接口) |
| [setCallRestriction](arkts-telephony-call-setcallrestriction-f-sys.md#setcallrestriction系统接口) |
| [setCallRestriction](arkts-telephony-call-setcallrestriction-f-sys.md#setcallrestriction系统接口) |
| [setCallRestrictionPassword](arkts-telephony-call-setcallrestrictionpassword-f-sys.md#setcallrestrictionpassword系统接口) |
| [setCallRestrictionPassword](arkts-telephony-call-setcallrestrictionpassword-f-sys.md#setcallrestrictionpassword系统接口) |
| [setCallTransfer](arkts-telephony-call-setcalltransfer-f-sys.md#setcalltransfer系统接口) |
| [setCallTransfer](arkts-telephony-call-setcalltransfer-f-sys.md#setcalltransfer系统接口) |
| [setCallWaiting](arkts-telephony-call-setcallwaiting-f-sys.md#setcallwaiting系统接口) |
| [setCallWaiting](arkts-telephony-call-setcallwaiting-f-sys.md#setcallwaiting系统接口) |
| [setDeviceDirection](arkts-telephony-call-setdevicedirection-f-sys.md#setdevicedirection系统接口) |
| [setDisplaySurface](arkts-telephony-call-setdisplaysurface-f-sys.md#setdisplaysurface系统接口) |
| [setMuted](arkts-telephony-call-setmuted-f-sys.md#setmuted系统接口) |
| [setMuted](arkts-telephony-call-setmuted-f-sys.md#setmuted系统接口) |
| [setPreviewSurface](arkts-telephony-call-setpreviewsurface-f-sys.md#setpreviewsurface系统接口) |
| [setRttCapability](arkts-telephony-call-setrttcapability-f-sys.md#setrttcapability系统接口) |
| [setVoNRState](arkts-telephony-call-setvonrstate-f-sys.md#setvonrstate系统接口) |
| [setVoNRState](arkts-telephony-call-setvonrstate-f-sys.md#setvonrstate系统接口) |
| [startDTMF](arkts-telephony-call-startdtmf-f-sys.md#startdtmf系统接口) |
| [startDTMF](arkts-telephony-call-startdtmf-f-sys.md#startdtmf系统接口) |
| [startRtt](arkts-telephony-call-startrtt-f-sys.md#startrtt系统接口) |
| [stopDTMF](arkts-telephony-call-stopdtmf-f-sys.md#stopdtmf系统接口) |
| [stopDTMF](arkts-telephony-call-stopdtmf-f-sys.md#stopdtmf系统接口) |
| [stopRtt](arkts-telephony-call-stoprtt-f-sys.md#stoprtt系统接口) |
| [switchCall](arkts-telephony-call-switchcall-f-sys.md#switchcall系统接口) |
| [switchCall](arkts-telephony-call-switchcall-f-sys.md#switchcall系统接口) |
| [unHoldCall](arkts-telephony-call-unholdcall-f-sys.md#unholdcall系统接口) |
| [unHoldCall](arkts-telephony-call-unholdcall-f-sys.md#unholdcall系统接口) |
| [unloadCallUI](arkts-telephony-call-unloadcallui-f-sys.md#unloadcallui系统接口) |
| [updateImsCallMode](arkts-telephony-call-updateimscallmode-f-sys.md#updateimscallmode系统接口) |
| [updateImsCallMode](arkts-telephony-call-updateimscallmode-f-sys.md#updateimscallmode系统接口) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [DialOptions](arkts-telephony-call-dialoptions-i.md) |
| [EmergencyNumberOptions](arkts-telephony-call-emergencynumberoptions-i.md) |
| [MakeCallOptions](arkts-telephony-call-makecalloptions-i.md) |
| [NumberFormatOptions](arkts-telephony-call-numberformatoptions-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
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

### 枚举

| 名称 |
| --- |
| [CCallState](arkts-telephony-call-ccallstate-e.md) |
| [CallState](arkts-telephony-call-callstate-e.md) |
| [TelCallState](arkts-telephony-call-telcallstate-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
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
