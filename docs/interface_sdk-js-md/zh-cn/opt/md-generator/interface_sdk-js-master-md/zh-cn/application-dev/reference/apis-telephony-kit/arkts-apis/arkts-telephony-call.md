# @ohos.telephony.call

该模块提供呼叫管理功能，包括拨打电话、跳转到拨号界面、获取通话状态、格式化电话号码等。 如需订阅通话状态请使用 `observer.on('callStateChange')` 。

**起始版本：** 23

**废弃版本：** -1

<!--Device-unnamed-declare namespace call--><!--Device-unnamed-declare namespace call-End-->

**系统能力：** SystemCapability.Telephony.CallManager

## 汇总

### 函数

| 名称 |
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
### 函数（系统接口）

| 名称 |
| --- |
| [answerCall](arkts-telephony-call-answercall-f-sys.md#answerCall（系统接口）) |
| [answerCall](arkts-telephony-call-answercall-f-sys.md#answerCall（系统接口）) |
| [answerCall](arkts-telephony-call-answercall-f-sys.md#answerCall（系统接口）) |
| [answerCall](arkts-telephony-call-answercall-f-sys.md#answerCall（系统接口）) |
| [answerCall](arkts-telephony-call-answercall-f-sys.md#answerCall（系统接口）) |
| [canSetCallTransferTime](arkts-telephony-call-cansetcalltransfertime-f-sys.md#canSetCallTransferTime（系统接口）) |
| [canSetCallTransferTime](arkts-telephony-call-cansetcalltransfertime-f-sys.md#canSetCallTransferTime（系统接口）) |
| [cancelCallUpgrade](arkts-telephony-call-cancelcallupgrade-f-sys.md#cancelCallUpgrade（系统接口）) |
| [cancelMuted](arkts-telephony-call-cancelmuted-f-sys.md#cancelMuted（系统接口）) |
| [cancelMuted](arkts-telephony-call-cancelmuted-f-sys.md#cancelMuted（系统接口）) |
| [closeUnfinishedUssd](arkts-telephony-call-closeunfinishedussd-f-sys.md#closeUnfinishedUssd（系统接口）) |
| [closeUnfinishedUssd](arkts-telephony-call-closeunfinishedussd-f-sys.md#closeUnfinishedUssd（系统接口）) |
| [combineConference](arkts-telephony-call-combineconference-f-sys.md#combineConference（系统接口）) |
| [combineConference](arkts-telephony-call-combineconference-f-sys.md#combineConference（系统接口）) |
| [controlCamera](arkts-telephony-call-controlcamera-f-sys.md#controlCamera（系统接口）) |
| [dialCall](arkts-telephony-call-dialcall-f-sys.md#dialCall（系统接口）) |
| [dialCall](arkts-telephony-call-dialcall-f-sys.md#dialCall（系统接口）) |
| [dialCall](arkts-telephony-call-dialcall-f-sys.md#dialCall（系统接口）) |
| [disableImsSwitch](arkts-telephony-call-disableimsswitch-f-sys.md#disableImsSwitch（系统接口）) |
| [disableImsSwitch](arkts-telephony-call-disableimsswitch-f-sys.md#disableImsSwitch（系统接口）) |
| [enableImsSwitch](arkts-telephony-call-enableimsswitch-f-sys.md#enableImsSwitch（系统接口）) |
| [enableImsSwitch](arkts-telephony-call-enableimsswitch-f-sys.md#enableImsSwitch（系统接口）) |
| [getCallIdListForConference](arkts-telephony-call-getcallidlistforconference-f-sys.md#getCallIdListForConference（系统接口）) |
| [getCallIdListForConference](arkts-telephony-call-getcallidlistforconference-f-sys.md#getCallIdListForConference（系统接口）) |
| [getCallRestrictionStatus](arkts-telephony-call-getcallrestrictionstatus-f-sys.md#getCallRestrictionStatus（系统接口）) |
| [getCallRestrictionStatus](arkts-telephony-call-getcallrestrictionstatus-f-sys.md#getCallRestrictionStatus（系统接口）) |
| [getCallTransferInfo](arkts-telephony-call-getcalltransferinfo-f-sys.md#getCallTransferInfo（系统接口）) |
| [getCallTransferInfo](arkts-telephony-call-getcalltransferinfo-f-sys.md#getCallTransferInfo（系统接口）) |
| [getCallWaitingStatus](arkts-telephony-call-getcallwaitingstatus-f-sys.md#getCallWaitingStatus（系统接口）) |
| [getCallWaitingStatus](arkts-telephony-call-getcallwaitingstatus-f-sys.md#getCallWaitingStatus（系统接口）) |
| [getMainCallId](arkts-telephony-call-getmaincallid-f-sys.md#getMainCallId（系统接口）) |
| [getMainCallId](arkts-telephony-call-getmaincallid-f-sys.md#getMainCallId（系统接口）) |
| [getSubCallIdList](arkts-telephony-call-getsubcallidlist-f-sys.md#getSubCallIdList（系统接口）) |
| [getSubCallIdList](arkts-telephony-call-getsubcallidlist-f-sys.md#getSubCallIdList（系统接口）) |
| [getVoNRState](arkts-telephony-call-getvonrstate-f-sys.md#getVoNRState（系统接口）) |
| [getVoNRState](arkts-telephony-call-getvonrstate-f-sys.md#getVoNRState（系统接口）) |
| [hangUpCall](arkts-telephony-call-hangupcall-f-sys.md#hangUpCall（系统接口）) |
| [hangUpCall](arkts-telephony-call-hangupcall-f-sys.md#hangUpCall（系统接口）) |
| [hangUpCall](arkts-telephony-call-hangupcall-f-sys.md#hangUpCall（系统接口）) |
| [holdCall](arkts-telephony-call-holdcall-f-sys.md#holdCall（系统接口）) |
| [holdCall](arkts-telephony-call-holdcall-f-sys.md#holdCall（系统接口）) |
| [inputDialerSpecialCode](arkts-telephony-call-inputdialerspecialcode-f-sys.md#inputDialerSpecialCode（系统接口）) |
| [inputDialerSpecialCode](arkts-telephony-call-inputdialerspecialcode-f-sys.md#inputDialerSpecialCode（系统接口）) |
| [isImsSwitchEnabled](arkts-telephony-call-isimsswitchenabled-f-sys.md#isImsSwitchEnabled（系统接口）) |
| [isImsSwitchEnabled](arkts-telephony-call-isimsswitchenabled-f-sys.md#isImsSwitchEnabled（系统接口）) |
| [isImsSwitchEnabledSync](arkts-telephony-call-isimsswitchenabledsync-f-sys.md#isImsSwitchEnabledSync（系统接口）) |
| [isInEmergencyCall](arkts-telephony-call-isinemergencycall-f-sys.md#isInEmergencyCall（系统接口）) |
| [isInEmergencyCall](arkts-telephony-call-isinemergencycall-f-sys.md#isInEmergencyCall（系统接口）) |
| [isNewCallAllowed](arkts-telephony-call-isnewcallallowed-f-sys.md#isNewCallAllowed（系统接口）) |
| [isNewCallAllowed](arkts-telephony-call-isnewcallallowed-f-sys.md#isNewCallAllowed（系统接口）) |
| [isRinging](arkts-telephony-call-isringing-f-sys.md#isRinging（系统接口）) |
| [isRinging](arkts-telephony-call-isringing-f-sys.md#isRinging（系统接口）) |
| [joinConference](arkts-telephony-call-joinconference-f-sys.md#joinConference（系统接口）) |
| [joinConference](arkts-telephony-call-joinconference-f-sys.md#joinConference（系统接口）) |
| [kickOutFromConference](arkts-telephony-call-kickoutfromconference-f-sys.md#kickOutFromConference（系统接口）) |
| [kickOutFromConference](arkts-telephony-call-kickoutfromconference-f-sys.md#kickOutFromConference（系统接口）) |
| [muteRinger](arkts-telephony-call-muteringer-f-sys.md#muteRinger（系统接口）) |
| [muteRinger](arkts-telephony-call-muteringer-f-sys.md#muteRinger（系统接口）) |
| [offAudioDeviceChange](arkts-telephony-call-offaudiodevicechange-f-sys.md#offAudioDeviceChange（系统接口）) |
| [offCallDetailsChange](arkts-telephony-call-offcalldetailschange-f-sys.md#offCallDetailsChange（系统接口）) |
| [offCallDisconnectedCause](arkts-telephony-call-offcalldisconnectedcause-f-sys.md#offCallDisconnectedCause（系统接口）) |
| [offCallEventChange](arkts-telephony-call-offcalleventchange-f-sys.md#offCallEventChange（系统接口）) |
| [offCallSessionEvent](arkts-telephony-call-offcallsessionevent-f-sys.md#offCallSessionEvent（系统接口）) |
| [offCameraCapabilitiesChange](arkts-telephony-call-offcameracapabilitieschange-f-sys.md#offCameraCapabilitiesChange（系统接口）) |
| [offImsCallModeChange](arkts-telephony-call-offimscallmodechange-f-sys.md#offImsCallModeChange（系统接口）) |
| [offMmiCodeResult](arkts-telephony-call-offmmicoderesult-f-sys.md#offMmiCodeResult（系统接口）) |
| [offPeerDimensionsChange](arkts-telephony-call-offpeerdimensionschange-f-sys.md#offPeerDimensionsChange（系统接口）) |
| [offPostDialDelay](arkts-telephony-call-offpostdialdelay-f-sys.md#offPostDialDelay（系统接口）) |
| [offReceiveRttMessage](arkts-telephony-call-offreceiverttmessage-f-sys.md#offReceiveRttMessage（系统接口）) |
| [offRttErrCause](arkts-telephony-call-offrtterrcause-f-sys.md#offRttErrCause（系统接口）) |
| [offRttModifyInd](arkts-telephony-call-offrttmodifyind-f-sys.md#offRttModifyInd（系统接口）) |
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
| [onAudioDeviceChange](arkts-telephony-call-onaudiodevicechange-f-sys.md#onAudioDeviceChange（系统接口）) |
| [onCallDetailsChange](arkts-telephony-call-oncalldetailschange-f-sys.md#onCallDetailsChange（系统接口）) |
| [onCallDisconnectedCause](arkts-telephony-call-oncalldisconnectedcause-f-sys.md#onCallDisconnectedCause（系统接口）) |
| [onCallEventChange](arkts-telephony-call-oncalleventchange-f-sys.md#onCallEventChange（系统接口）) |
| [onCallSessionEvent](arkts-telephony-call-oncallsessionevent-f-sys.md#onCallSessionEvent（系统接口）) |
| [onCameraCapabilitiesChange](arkts-telephony-call-oncameracapabilitieschange-f-sys.md#onCameraCapabilitiesChange（系统接口）) |
| [onImsCallModeChange](arkts-telephony-call-onimscallmodechange-f-sys.md#onImsCallModeChange（系统接口）) |
| [onMmiCodeResult](arkts-telephony-call-onmmicoderesult-f-sys.md#onMmiCodeResult（系统接口）) |
| [onPeerDimensionsChange](arkts-telephony-call-onpeerdimensionschange-f-sys.md#onPeerDimensionsChange（系统接口）) |
| [onPostDialDelay](arkts-telephony-call-onpostdialdelay-f-sys.md#onPostDialDelay（系统接口）) |
| [onReceiveRttMessage](arkts-telephony-call-onreceiverttmessage-f-sys.md#onReceiveRttMessage（系统接口）) |
| [onRttErrCause](arkts-telephony-call-onrtterrcause-f-sys.md#onRttErrCause（系统接口）) |
| [onRttModifyInd](arkts-telephony-call-onrttmodifyind-f-sys.md#onRttModifyInd（系统接口）) |
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
| [postDialProceed](arkts-telephony-call-postdialproceed-f-sys.md#postDialProceed（系统接口）) |
| [postDialProceed](arkts-telephony-call-postdialproceed-f-sys.md#postDialProceed（系统接口）) |
| [preloadCallUI](arkts-telephony-call-preloadcallui-f-sys.md#preloadCallUI（系统接口）) |
| [rejectCall](arkts-telephony-call-rejectcall-f-sys.md#rejectCall（系统接口）) |
| [rejectCall](arkts-telephony-call-rejectcall-f-sys.md#rejectCall（系统接口）) |
| [rejectCall](arkts-telephony-call-rejectcall-f-sys.md#rejectCall（系统接口）) |
| [rejectCall](arkts-telephony-call-rejectcall-f-sys.md#rejectCall（系统接口）) |
| [rejectCall](arkts-telephony-call-rejectcall-f-sys.md#rejectCall（系统接口）) |
| [removeMissedIncomingCallNotification](arkts-telephony-call-removemissedincomingcallnotification-f-sys.md#removeMissedIncomingCallNotification（系统接口）) |
| [removeMissedIncomingCallNotification](arkts-telephony-call-removemissedincomingcallnotification-f-sys.md#removeMissedIncomingCallNotification（系统接口）) |
| [sendCallUiEvent](arkts-telephony-call-sendcalluievent-f-sys.md#sendCallUiEvent（系统接口）) |
| [sendRttMessage](arkts-telephony-call-sendrttmessage-f-sys.md#sendRttMessage（系统接口）) |
| [sendUssdResponse](arkts-telephony-call-sendussdresponse-f-sys.md#sendUssdResponse（系统接口）) |
| [separateConference](arkts-telephony-call-separateconference-f-sys.md#separateConference（系统接口）) |
| [separateConference](arkts-telephony-call-separateconference-f-sys.md#separateConference（系统接口）) |
| [setAudioDevice](arkts-telephony-call-setaudiodevice-f-sys.md#setAudioDevice（系统接口）) |
| [setAudioDevice](arkts-telephony-call-setaudiodevice-f-sys.md#setAudioDevice（系统接口）) |
| [setCallRestriction](arkts-telephony-call-setcallrestriction-f-sys.md#setCallRestriction（系统接口）) |
| [setCallRestriction](arkts-telephony-call-setcallrestriction-f-sys.md#setCallRestriction（系统接口）) |
| [setCallRestrictionPassword](arkts-telephony-call-setcallrestrictionpassword-f-sys.md#setCallRestrictionPassword（系统接口）) |
| [setCallRestrictionPassword](arkts-telephony-call-setcallrestrictionpassword-f-sys.md#setCallRestrictionPassword（系统接口）) |
| [setCallTransfer](arkts-telephony-call-setcalltransfer-f-sys.md#setCallTransfer（系统接口）) |
| [setCallTransfer](arkts-telephony-call-setcalltransfer-f-sys.md#setCallTransfer（系统接口）) |
| [setCallWaiting](arkts-telephony-call-setcallwaiting-f-sys.md#setCallWaiting（系统接口）) |
| [setCallWaiting](arkts-telephony-call-setcallwaiting-f-sys.md#setCallWaiting（系统接口）) |
| [setDeviceDirection](arkts-telephony-call-setdevicedirection-f-sys.md#setDeviceDirection（系统接口）) |
| [setDisplaySurface](arkts-telephony-call-setdisplaysurface-f-sys.md#setDisplaySurface（系统接口）) |
| [setMuted](arkts-telephony-call-setmuted-f-sys.md#setMuted（系统接口）) |
| [setMuted](arkts-telephony-call-setmuted-f-sys.md#setMuted（系统接口）) |
| [setPreviewSurface](arkts-telephony-call-setpreviewsurface-f-sys.md#setPreviewSurface（系统接口）) |
| [setRttCapability](arkts-telephony-call-setrttcapability-f-sys.md#setRttCapability（系统接口）) |
| [setVoNRState](arkts-telephony-call-setvonrstate-f-sys.md#setVoNRState（系统接口）) |
| [setVoNRState](arkts-telephony-call-setvonrstate-f-sys.md#setVoNRState（系统接口）) |
| [startDTMF](arkts-telephony-call-startdtmf-f-sys.md#startDTMF（系统接口）) |
| [startDTMF](arkts-telephony-call-startdtmf-f-sys.md#startDTMF（系统接口）) |
| [startRtt](arkts-telephony-call-startrtt-f-sys.md#startRtt（系统接口）) |
| [stopDTMF](arkts-telephony-call-stopdtmf-f-sys.md#stopDTMF（系统接口）) |
| [stopDTMF](arkts-telephony-call-stopdtmf-f-sys.md#stopDTMF（系统接口）) |
| [stopRtt](arkts-telephony-call-stoprtt-f-sys.md#stopRtt（系统接口）) |
| [switchCall](arkts-telephony-call-switchcall-f-sys.md#switchCall（系统接口）) |
| [switchCall](arkts-telephony-call-switchcall-f-sys.md#switchCall（系统接口）) |
| [unHoldCall](arkts-telephony-call-unholdcall-f-sys.md#unHoldCall（系统接口）) |
| [unHoldCall](arkts-telephony-call-unholdcall-f-sys.md#unHoldCall（系统接口）) |
| [unloadCallUI](arkts-telephony-call-unloadcallui-f-sys.md#unloadCallUI（系统接口）) |
| [updateImsCallMode](arkts-telephony-call-updateimscallmode-f-sys.md#updateImsCallMode（系统接口）) |
| [updateImsCallMode](arkts-telephony-call-updateimscallmode-f-sys.md#updateImsCallMode（系统接口）) |
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
