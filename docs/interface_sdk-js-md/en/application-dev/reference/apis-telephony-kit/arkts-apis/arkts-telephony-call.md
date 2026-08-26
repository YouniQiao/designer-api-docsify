# @ohos.telephony.call(Call)

The **call** module provides call management functions, including making calls, redirecting to the dial screen, obtaining the call status, and formatting phone numbers.To subscribe to call status changes, use `observer.on('callStateChange')`.

**Since:** 6

**System capability:** SystemCapability.Telephony.CallManager

## Modules to Import

```TypeScript
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [answerCall(Call)](arkts-telephony-call-answercall-f.md) | Answers a call. This API uses an asynchronous callback to return the result. |
| [dial(Call)](arkts-telephony-call-dial-f.md) | Initiates a call. You can set call options as needed. This API uses an asynchronous callback to return the result. |
| [dial(Call)](arkts-telephony-call-dial-f.md) | Initiates a call. You can set call options as needed. This API uses a promise to return the result. |
| [dial(Call)](arkts-telephony-call-dial-f.md) | Initiates a call. This API uses an asynchronous callback to return the result. |
| [formatPhoneNumber(Call)](arkts-telephony-call-formatphonenumber-f.md) | Formats a phone number based on specified formatting options. This API uses an asynchronous callback to return the result.A formatted phone number is a standard numeric string, for example, 555 0100. |
| [formatPhoneNumber(Call)](arkts-telephony-call-formatphonenumber-f.md) | Formats a phone number based on specified formatting options. This API uses a promise to return the result.A formatted phone number is a standard numeric string, for example, 555 0100. |
| [formatPhoneNumber(Call)](arkts-telephony-call-formatphonenumber-f.md) | Formats a phone number. This API uses an asynchronous callback to return the result.A formatted phone number is a standard numeric string, for example, 555 0100. |
| [formatPhoneNumberToE164(Call)](arkts-telephony-call-formatphonenumbertoe164-f.md) | Converts a phone number into the E.164 format. This API uses an asynchronous callback to return the result.The phone number must match the specified country code. For example, for a China phone number, the country code must be **CN**. Otherwise, **null** will be returned. |
| [formatPhoneNumberToE164(Call)](arkts-telephony-call-formatphonenumbertoe164-f.md) | Converts a phone number into the E.164 format. This API uses a promise to return the result.The phone number must match the specified country code. For example, for a China phone number, the country code must be **CN**. Otherwise, **null** will be returned.All country codes are supported. |
| [getCallState(Call)](arkts-telephony-call-getcallstate-f.md) | Obtains the call status. This API uses an asynchronous callback to return the result. |
| [getCallState(Call)](arkts-telephony-call-getcallstate-f.md) | Obtains the call status. This API uses a promise to return the result. |
| [getCallStateSync(Call)](arkts-telephony-call-getcallstatesync-f.md) | Obtains the call status. |
| [getCallTransferInfo(Call)](arkts-telephony-call-getcalltransferinfo-f.md) | Obtains call transfer information with the phone number. This API uses a promise to return the result. |
| [hangUpCall(Call)](arkts-telephony-call-hangupcall-f.md) | Ends a call. This API uses an asynchronous callback to return the result. |
| [hasCall(Call)](arkts-telephony-call-hascall-f.md) | Checks whether a call is in progress. This API uses an asynchronous callback to return the result. |
| [hasCall(Call)](arkts-telephony-call-hascall-f.md) | Checks whether a call is in progress. This API uses a promise to return the result. |
| [hasCallSync(Call)](arkts-telephony-call-hascallsync-f.md) | Checks whether a call is in progress. |
| [hasVoiceCapability(Call)](arkts-telephony-call-hasvoicecapability-f.md) | Checks whether a device supports voice calls. |
| [isEmergencyPhoneNumber(Call)](arkts-telephony-call-isemergencyphonenumber-f.md) | Checks whether the called number is an emergency number based on the phone number. This API uses an asynchronous callback to return the result. |
| [isEmergencyPhoneNumber(Call)](arkts-telephony-call-isemergencyphonenumber-f.md) | Checks whether the called number is an emergency number based on the phone number. This API uses a promise to return the result. |
| [isEmergencyPhoneNumber(Call)](arkts-telephony-call-isemergencyphonenumber-f.md) | Checks whether the called number is an emergency number. This API uses an asynchronous callback to return the result. |
| [makeCall(Call)](arkts-telephony-call-makecall-f.md) | Launches the call screen and displays the dialed number. This API uses an asynchronous callback to return the result. This API can be called only in a UIAbility. |
| [makeCall(Call)](arkts-telephony-call-makecall-f.md) | Launches the call screen and displays the dialed number. This API uses a promise to return the result. This API can be called only in a UIAbility. |
| [makeCall(Call)](arkts-telephony-call-makecall-f.md) | Launches the call screen and displays the dialed number. This API uses a promise to return the result. This API can be called only in a UIAbility. |
| [makeCall(Call)](arkts-telephony-call-makecall-f.md) | Launches the call screen and displays the dialed number. This API uses a promise to return the result. You need to declare the **ohos.permission.START_ABILITIES_FROM_BACKGROUND** permission if you want to call the API in the background. |
| [makeCallWithToken(Call)](arkts-telephony-call-makecallwithtoken-f.md) | Go to the dial screen and the called number is displayed.The authentication challenge value is returned. |
| [rejectCall(Call)](arkts-telephony-call-rejectcall-f.md) | Rejects a call. This API uses an asynchronous callback to return the result. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [answerCall(Call)](arkts-telephony-call-answercall-f-sys.md) | Answers a call. This API uses an asynchronous callback to return the result. |
| [answerCall(Call)](arkts-telephony-call-answercall-f-sys.md) | Answers a call. This API uses a promise to return the result. |
| [answerCall(Call)](arkts-telephony-call-answercall-f-sys.md) | Answers a call. This API uses a promise to return the result. |
| [answerCall(Call)](arkts-telephony-call-answercall-f-sys.md) | Answers the incoming rtt |
| [cancelCallUpgrade(Call)](arkts-telephony-call-cancelcallupgrade-f-sys.md) | Cancels the upgrade of a video call. This API uses a promise to return the result. |
| [cancelMuted(Call)](arkts-telephony-call-cancelmuted-f-sys.md) | Cancels call muting. This API uses an asynchronous callback to return the result. |
| [cancelMuted(Call)](arkts-telephony-call-cancelmuted-f-sys.md) | Cancels call muting. This API uses a promise to return the result. |
| [canSetCallTransferTime(Call)](arkts-telephony-call-cansetcalltransfertime-f-sys.md) | Checks whether the call forwarding time can be set. This API uses an asynchronous callback to return the result. |
| [canSetCallTransferTime(Call)](arkts-telephony-call-cansetcalltransfertime-f-sys.md) | Checks whether the call forwarding time can be set. This API uses a promise to return the result. |
| [closeUnfinishedUssd(Call)](arkts-telephony-call-closeunfinishedussd-f-sys.md) | Cancels the unfinished USSD services. This API uses an asynchronous callback to return the result. |
| [closeUnfinishedUssd(Call)](arkts-telephony-call-closeunfinishedussd-f-sys.md) | Cancels the unfinished USSD services. This API uses a promise to return the result. |
| [combineConference(Call)](arkts-telephony-call-combineconference-f-sys.md) | Combines two calls into a conference call. This API uses an asynchronous callback to return the result. |
| [combineConference(Call)](arkts-telephony-call-combineconference-f-sys.md) | Combines two calls into a conference call. This API uses a promise to return the result. |
| [controlCamera(Call)](arkts-telephony-call-controlcamera-f-sys.md) | Uses the specified camera to make a video call. If **cameraId** is left empty, the camera is disabled. This API uses a promise to return the result. |
| [dialCall(Call)](arkts-telephony-call-dialcall-f-sys.md) | Initiates a call. You can set call options as needed. This API uses an asynchronous callback to return the result. |
| [dialCall(Call)](arkts-telephony-call-dialcall-f-sys.md) | Initiates a call. You can set call options as needed. This API uses a promise to return the result. |
| [dialCall(Call)](arkts-telephony-call-dialcall-f-sys.md) | Initiates a call. This API uses an asynchronous callback to return the result. |
| [disableImsSwitch(Call)](arkts-telephony-call-disableimsswitch-f-sys.md) | Disables the IMS service. This API uses an asynchronous callback to return the result. |
| [disableImsSwitch(Call)](arkts-telephony-call-disableimsswitch-f-sys.md) | Disables the IMS service. This API uses a promise to return the result. |
| [enableImsSwitch(Call)](arkts-telephony-call-enableimsswitch-f-sys.md) | Enables the IMS service. This API uses an asynchronous callback to return the result. |
| [enableImsSwitch(Call)](arkts-telephony-call-enableimsswitch-f-sys.md) | Enables the IMS service. This API uses a promise to return the result. |
| [getCallIdListForConference(Call)](arkts-telephony-call-getcallidlistforconference-f-sys.md) | Obtains the list of call IDs in a conference. This API uses an asynchronous callback to return the result. |
| [getCallIdListForConference(Call)](arkts-telephony-call-getcallidlistforconference-f-sys.md) | Obtains the list of call IDs in a conference. This API uses a promise to return the result. |
| [getCallRestrictionStatus(Call)](arkts-telephony-call-getcallrestrictionstatus-f-sys.md) | Obtains the call restriction status. This API uses an asynchronous callback to return the result. |
| [getCallRestrictionStatus(Call)](arkts-telephony-call-getcallrestrictionstatus-f-sys.md) | Obtains the call restriction status. This API uses a promise to return the result. |
| [getCallTransferInfo(Call)](arkts-telephony-call-getcalltransferinfo-f-sys.md) | Obtains call transfer information. This API uses an asynchronous callback to return the result. |
| [getCallTransferInfo(Call)](arkts-telephony-call-getcalltransferinfo-f-sys.md) | Obtains call transfer information. This API uses a promise to return the result. |
| [getCallWaitingStatus(Call)](arkts-telephony-call-getcallwaitingstatus-f-sys.md) | Obtains the call waiting status. This API uses an asynchronous callback to return the result. |
| [getCallWaitingStatus(Call)](arkts-telephony-call-getcallwaitingstatus-f-sys.md) | Obtains the call waiting status. This API uses a promise to return the result. |
| [getMainCallId(Call)](arkts-telephony-call-getmaincallid-f-sys.md) | Obtains the main call ID. This API uses an asynchronous callback to return the result. |
| [getMainCallId(Call)](arkts-telephony-call-getmaincallid-f-sys.md) | Obtains the main call ID. This API uses a promise to return the result. |
| [getSubCallIdList(Call)](arkts-telephony-call-getsubcallidlist-f-sys.md) | Obtains the list of subcall IDs. This API uses an asynchronous callback to return the result. |
| [getSubCallIdList(Call)](arkts-telephony-call-getsubcallidlist-f-sys.md) | Obtains the list of subcall IDs. This API uses a promise to return the result. |
| [getVoNRState(Call)](arkts-telephony-call-getvonrstate-f-sys.md) | Obtains the status of the VoNR switch. This API uses an asynchronous callback to return the result. |
| [getVoNRState(Call)](arkts-telephony-call-getvonrstate-f-sys.md) | Obtains the status of the VoNR switch. This API uses a promise to return the result. |
| [hangUpCall(Call)](arkts-telephony-call-hangupcall-f-sys.md) | Ends a call. This API uses an asynchronous callback to return the result. |
| [hangUpCall(Call)](arkts-telephony-call-hangupcall-f-sys.md) | Ends a call. This API uses a promise to return the result. |
| [holdCall(Call)](arkts-telephony-call-holdcall-f-sys.md) | Holds a call based on the specified call ID. This API uses an asynchronous callback to return the result. |
| [holdCall(Call)](arkts-telephony-call-holdcall-f-sys.md) | Holds a call based on the specified call ID. This API uses a promise to return the result. |
| [inputDialerSpecialCode(Call)](arkts-telephony-call-inputdialerspecialcode-f-sys.md) | Performs a secret code broadcast. This API uses an asynchronous callback to return the result. |
| [inputDialerSpecialCode(Call)](arkts-telephony-call-inputdialerspecialcode-f-sys.md) | Performs a secret code broadcast. This API uses a promise to return the result. |
| [isImsSwitchEnabled(Call)](arkts-telephony-call-isimsswitchenabled-f-sys.md) | Checks whether the IMS service is enabled. This API uses an asynchronous callback to return the result. |
| [isImsSwitchEnabled(Call)](arkts-telephony-call-isimsswitchenabled-f-sys.md) | Checks whether the IMS service is enabled. This API uses a promise to return the result. |
| [isImsSwitchEnabledSync(Call)](arkts-telephony-call-isimsswitchenabledsync-f-sys.md) | Checks whether the IMS service is enabled. This API returns the result synchronously. |
| [isInEmergencyCall(Call)](arkts-telephony-call-isinemergencycall-f-sys.md) | Checks whether a call is an emergency call. This API uses an asynchronous callback to return the result. |
| [isInEmergencyCall(Call)](arkts-telephony-call-isinemergencycall-f-sys.md) | Checks whether a call is an emergency call. This API uses a promise to return the result. |
| [isNewCallAllowed(Call)](arkts-telephony-call-isnewcallallowed-f-sys.md) | Checks whether a new call is allowed. This API uses an asynchronous callback to return the result. |
| [isNewCallAllowed(Call)](arkts-telephony-call-isnewcallallowed-f-sys.md) | Checks whether a new call is allowed. This API uses a promise to return the result. |
| [isRinging(Call)](arkts-telephony-call-isringing-f-sys.md) | Checks whether the ringtone is playing. This API uses an asynchronous callback to return the result. |
| [isRinging(Call)](arkts-telephony-call-isringing-f-sys.md) | Checks whether the ringtone is playing. This API uses a promise to return the result. |
| [joinConference(Call)](arkts-telephony-call-joinconference-f-sys.md) | Joins a conference call. This API uses an asynchronous callback to return the result. |
| [joinConference(Call)](arkts-telephony-call-joinconference-f-sys.md) | Joins a conference call. This API uses a promise to return the result. |
| [kickOutFromConference(Call)](arkts-telephony-call-kickoutfromconference-f-sys.md) | Removes a specified call from a conference call. This API uses an asynchronous callback to return the result. |
| [kickOutFromConference(Call)](arkts-telephony-call-kickoutfromconference-f-sys.md) | Removes a specified call from a conference call. This API uses a promise to return the result. |
| [muteRinger(Call)](arkts-telephony-call-muteringer-f-sys.md) | Mutes the ringtone while it is playing. It does not work if the ringtone has been muted. This API uses an asynchronous callback to return the result. |
| [muteRinger(Call)](arkts-telephony-call-muteringer-f-sys.md) | Mutes the ringtone while it is playing. It does not work if the ringtone has been muted. This API uses a promise to return the result. |
| off(Call) | Unsubscribes from **callDetailsChange** events. This API uses an asynchronous callback to return the result. |
| off(Call) | Unsubscribes from **callEventChange** events. This API uses an asynchronous callback to return the result. |
| off(Call) | Unsubscribes from **callDisconnectedCause** events. This API uses an asynchronous callback to return the result. |
| [off(Call)](arkts-telephony-call-mmicoderesult-e-sys.md) | Unsubscribes from **mmiCodeResult** events. This API uses an asynchronous callback to return the result. |
| off(Call) | Unsubscribes from **audioDeviceChange** events. This API uses an asynchronous callback to return the result. |
| off(Call) | Unsubscribes from **postDialDelay** events. This API uses an asynchronous callback to return the result. |
| off(Call) | Unsubscribes from **imsCallModeChange** events. This API uses an asynchronous callback to return the result. |
| [off(Call)](arkts-telephony-call-callsessionevent-i-sys.md) | Unsubscribes from **callSessionEvent** events. This API uses an asynchronous callback to return the result. |
| off(Call) | Unsubscribes from **peerDimensionsChange** events. This API uses an asynchronous callback to return the result. |
| off(Call) | Unsubscribes from **cameraCapabilitiesChange** events. This API uses an asynchronous callback to return the result. |
| [offReceiveRttMessage(Call)](arkts-telephony-call-offreceiverttmessage-f-sys.md) | Unsubscribe from the rtt message event. |
| [offRttErrCause(Call)](arkts-telephony-call-offrtterrcause-f-sys.md) | Unsubscribe from the rtt error report event. |
| [offRttModifyInd(Call)](arkts-telephony-call-offrttmodifyind-f-sys.md) | Unsubscribe from the rtt modify indication. |
| on(Call) | Subscribes to **callDetailsChange** events. This API uses an asynchronous callback to return the result. |
| on(Call) | Subscribes to **callEventChange** events. This API uses an asynchronous callback to return the result. |
| on(Call) | Subscribes to **callDisconnectedCause** events. This API uses an asynchronous callback to return the result. |
| [on(Call)](arkts-telephony-call-mmicoderesult-e-sys.md) | Subscribes to **mmiCodeResult** events. This API uses an asynchronous callback to return the result. |
| on(Call) | Subscribes to audio device change events. This API uses an asynchronous callback to return the result. |
| on(Call) | Subscribes to **postDialDelay** events. This API uses an asynchronous callback to return the result. |
| on(Call) | Subscribes to **imsCallModeChange** events. This API uses an asynchronous callback to return the result. |
| [on(Call)](arkts-telephony-call-callsessionevent-i-sys.md) | Subscribes to **callSessionEvent** events. This API uses an asynchronous callback to return the result. |
| on(Call) | Subscribes to **peerDimensionsChange** events. This API uses an asynchronous callback to return the result. |
| on(Call) | Subscribes to **cameraCapabilitiesChange** events. This API uses an asynchronous callback to return the result. |
| [onReceiveRttMessage(Call)](arkts-telephony-call-onreceiverttmessage-f-sys.md) | Subscribe to the rtt message event. |
| [onRttErrCause(Call)](arkts-telephony-call-onrtterrcause-f-sys.md) | Subscribe to the rtt error event. |
| [onRttModifyInd(Call)](arkts-telephony-call-onrttmodifyind-f-sys.md) | Subscribe to the rtt modify indication. |
| [postDialProceed(Call)](arkts-telephony-call-postdialproceed-f-sys.md) | Continues a call by playing a post-dial DTMF string. This API uses an asynchronous callback to return the result.If the called number is in the format of "common phone number + semicolon (;) + DTMF string", for example, **400xxxxxxx;123**, and the listening for **postDialDelay** events is enabled, the system reports a **postDialDelay** event when the call is connected. The application can then call this API to send DTMF tones. |
| [postDialProceed(Call)](arkts-telephony-call-postdialproceed-f-sys.md) | Continues a call by playing a post-dial DTMF string. This API uses a promise to return the result.If the called number is in the format of "common phone number + semicolon (;) + DTMF string", for example, **400xxxxxxx;123**, and the listening for **postDialDelay** events is enabled, the system reports a **postDialDelay** event when the call is connected. The application can then call this API to send DTMF tones. |
| [preloadCallUI(Call)](arkts-telephony-call-preloadcallui-f-sys.md) | Preload callUI. |
| [rejectCall(Call)](arkts-telephony-call-rejectcall-f-sys.md) | Rejects a call. This API uses an asynchronous callback to return the result. |
| [rejectCall(Call)](arkts-telephony-call-rejectcall-f-sys.md) | Rejects a call. This API uses a promise to return the result. |
| [rejectCall(Call)](arkts-telephony-call-rejectcall-f-sys.md) | Rejects a call. This API uses an asynchronous callback to return the result. |
| [rejectCall(Call)](arkts-telephony-call-rejectcall-f-sys.md) | Rejects a call. This API uses an asynchronous callback to return the result. |
| [removeMissedIncomingCallNotification(Call)](arkts-telephony-call-removemissedincomingcallnotification-f-sys.md) | Removes missed call notifications. This API uses an asynchronous callback to return the result. |
| [removeMissedIncomingCallNotification(Call)](arkts-telephony-call-removemissedincomingcallnotification-f-sys.md) | Removes missed call notifications. This API uses a promise to return the result. |
| [sendCallUiEvent(Call)](arkts-telephony-call-sendcalluievent-f-sys.md) | Sends a call UI event. This API uses a promise to return the result. |
| [sendRttMessage(Call)](arkts-telephony-call-sendrttmessage-f-sys.md) | Send rtt message. |
| [sendUssdResponse(Call)](arkts-telephony-call-sendussdresponse-f-sys.md) | Sends a response to the Unstructured Supplementary Service Data (USSD) service to the carrier. |
| [separateConference(Call)](arkts-telephony-call-separateconference-f-sys.md) | Separates calls from a conference call. This API uses an asynchronous callback to return the result. |
| [separateConference(Call)](arkts-telephony-call-separateconference-f-sys.md) | Separates calls from a conference call. This API uses a promise to return the result. |
| [setAudioDevice(Call)](arkts-telephony-call-setaudiodevice-f-sys.md) | Sets the audio device for a call. This API uses an asynchronous callback to return the result. |
| [setAudioDevice(Call)](arkts-telephony-call-setaudiodevice-f-sys.md) | Sets the audio device for a call. This API uses a promise to return the result. |
| [setCallRestriction(Call)](arkts-telephony-call-setcallrestriction-f-sys.md) | Sets the call restriction status. This API uses an asynchronous callback to return the result. |
| [setCallRestriction(Call)](arkts-telephony-call-setcallrestriction-f-sys.md) | Sets the call restriction status. This API uses a promise to return the result. |
| [setCallRestrictionPassword(Call)](arkts-telephony-call-setcallrestrictionpassword-f-sys.md) | Changes the call barring password. This API uses an asynchronous callback to return the result. |
| [setCallRestrictionPassword(Call)](arkts-telephony-call-setcallrestrictionpassword-f-sys.md) | Changes the call barring password. This API uses a promise to return the result. |
| [setCallTransfer(Call)](arkts-telephony-call-setcalltransfer-f-sys.md) | Sets call transfer information. This API uses an asynchronous callback to return the result. |
| [setCallTransfer(Call)](arkts-telephony-call-setcalltransfer-f-sys.md) | Sets call transfer information. This API uses a promise to return the result. |
| [setCallWaiting(Call)](arkts-telephony-call-setcallwaiting-f-sys.md) | Specifies whether to enable the call waiting service. This API uses an asynchronous callback to return the result. |
| [setCallWaiting(Call)](arkts-telephony-call-setcallwaiting-f-sys.md) | Specifies whether to enable the call waiting service. This API uses a promise to return the result. |
| [setDeviceDirection(Call)](arkts-telephony-call-setdevicedirection-f-sys.md) | Sets the video call screen to follow the device direction. This API uses a promise to return the result. |
| [setDisplaySurface(Call)](arkts-telephony-call-setdisplaysurface-f-sys.md) | Sets the remote display window. This API uses a promise to return the result. |
| [setMuted(Call)](arkts-telephony-call-setmuted-f-sys.md) | Sets call muting. This API uses an asynchronous callback to return the result. |
| [setMuted(Call)](arkts-telephony-call-setmuted-f-sys.md) | Sets call muting. This API uses a promise to return the result. |
| [setPreviewSurface(Call)](arkts-telephony-call-setpreviewsurface-f-sys.md) | Sets the local preview window. This API uses a promise to return the result. |
| [setRttCapability(Call)](arkts-telephony-call-setrttcapability-f-sys.md) | Set rtt capability. |
| [setVoNRState(Call)](arkts-telephony-call-setvonrstate-f-sys.md) | Sets the status of the VoNR switch. This API uses an asynchronous callback to return the result. |
| [setVoNRState(Call)](arkts-telephony-call-setvonrstate-f-sys.md) | Sets the status of the VoNR switch. This API uses a promise to return the result. |
| [startDTMF(Call)](arkts-telephony-call-startdtmf-f-sys.md) | Starts playing DTMF tones. This API uses an asynchronous callback to return the result. |
| [startDTMF(Call)](arkts-telephony-call-startdtmf-f-sys.md) | Starts playing DTMF tones. This API uses a promise to return the result. |
| [startRtt(Call)](arkts-telephony-call-startrtt-f-sys.md) | Start rtt. |
| [stopDTMF(Call)](arkts-telephony-call-stopdtmf-f-sys.md) | Stops playing DTMF tones. This API uses an asynchronous callback to return the result. |
| [stopDTMF(Call)](arkts-telephony-call-stopdtmf-f-sys.md) | Stops playing DTMF tones. This API uses a promise to return the result. |
| [stopRtt(Call)](arkts-telephony-call-stoprtt-f-sys.md) | Stop rtt. |
| [switchCall(Call)](arkts-telephony-call-switchcall-f-sys.md) | Switches a call. This API uses an asynchronous callback to return the result. |
| [switchCall(Call)](arkts-telephony-call-switchcall-f-sys.md) | Switches a call. This API uses a promise to return the result. |
| [unHoldCall(Call)](arkts-telephony-call-unholdcall-f-sys.md) | Unholds a call based on the specified call ID. This API uses an asynchronous callback to return the result. |
| [unHoldCall(Call)](arkts-telephony-call-unholdcall-f-sys.md) | Unholds a call based on the specified call ID. This API uses a promise to return the result. |
| [unloadCallUI(Call)](arkts-telephony-call-unloadcallui-f-sys.md) | Unload callUI. |
| [updateImsCallMode(Call)](arkts-telephony-call-updateimscallmode-f-sys.md) | Updates the IMS call mode. This API uses an asynchronous callback to return the result. |
| [updateImsCallMode(Call)](arkts-telephony-call-updateimscallmode-f-sys.md) | Updates the IMS call mode. This API uses a promise to return the result. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [CallTransferResult(Call)](arkts-telephony-call-calltransferresult-i.md) | Defines the call transfer result. |
| [DialOptions(Call)](arkts-telephony-call-dialoptions-i.md) | Provides an option for determining whether a call is a video call. |
| [EmergencyNumberOptions(Call)](arkts-telephony-call-emergencynumberoptions-i.md) | Provides an option for determining whether a number is an emergency number for the SIM card in the specified slot. |
| [MakeCallOptions(Call)](arkts-telephony-call-makecalloptions-i.md) | Provides an option for determining whether a call is a video call. |
| [NumberFormatOptions(Call)](arkts-telephony-call-numberformatoptions-i.md) | Provides an option for number formatting. |

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [AudioDevice(Call)](arkts-telephony-call-audiodevice-i-sys.md) | Enumerates audio devices. |
| [AudioDeviceCallbackInfo(Call)](arkts-telephony-call-audiodevicecallbackinfo-i-sys.md) | Defines the audio device information. |
| [CallAttributeOptions(Call)](arkts-telephony-call-callattributeoptions-i-sys.md) | Defines the call attribute options. |
| [CallEventOptions(Call)](arkts-telephony-call-calleventoptions-i-sys.md) | Defines the call event options. |
| [CallRestrictionInfo(Call)](arkts-telephony-call-callrestrictioninfo-i-sys.md) | Defines the call restriction information. |
| [CallSessionEvent(Call)](arkts-telephony-call-callsessionevent-i-sys.md) | Defines the video call event information. |
| [CallTransferInfo(Call)](arkts-telephony-call-calltransferinfo-i-sys.md) | Defines the call transfer information. |
| [CallTransferResult(Call)](arkts-telephony-call-calltransferresult-i-sys.md) | Defines the call transfer result. |
| [CameraCapabilities(Call)](arkts-telephony-call-cameracapabilities-i-sys.md) | Defines the local image resolution in a video call. |
| [DialCallOptions(Call)](arkts-telephony-call-dialcalloptions-i-sys.md) | Provides an option for determining whether a call is a video call. |
| [DialOptions(Call)](arkts-telephony-call-dialoptions-i-sys.md) | Provides an option for determining whether a call is a video call. |
| [DisconnectedDetails(Call)](arkts-telephony-call-disconnecteddetails-i-sys.md) | Defines the call disconnection cause. |
| [ImsCallModeInfo(Call)](arkts-telephony-call-imscallmodeinfo-i-sys.md) | Defines the video call mode information. |
| [MmiCodeResults(Call)](arkts-telephony-call-mmicoderesults-i-sys.md) | Defines the MMI code result. |
| [NumberMarkInfo(Call)](arkts-telephony-call-numbermarkinfo-i-sys.md) | Defines a number mark. |
| [PeerDimensionsDetail(Call)](arkts-telephony-call-peerdimensionsdetail-i-sys.md) | Defines the peer image resolution in a video call. |
| [RejectMessageOptions(Call)](arkts-telephony-call-rejectmessageoptions-i-sys.md) | Defines options for the call rejection message. |
| [RttErrorInfo(Call)](arkts-telephony-call-rtterrorinfo-i-sys.md) | Indicates the info of the rtt error. |
| [RttEventInfo(Call)](arkts-telephony-call-rtteventinfo-i-sys.md) | Indicates the info of the rtt event. |
| [RttMessageInfo(Call)](arkts-telephony-call-rttmessageinfo-i-sys.md) | Indicates the info of the rtt message. |
| [VoipCallAttribute(Call)](arkts-telephony-call-voipcallattribute-i-sys.md) | Defines the VoIP call information. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [CallState(Call)](arkts-telephony-call-callstate-e.md) | Enumerates call states. |
| [CallTransferType(Call)](arkts-telephony-call-calltransfertype-e.md) | Enumerates call transfer types. |
| [CCallState(Call)](arkts-telephony-call-ccallstate-e.md) | Carrier call state code. |
| [TelCallState(Call)](arkts-telephony-call-telcallstate-e.md) | Enumerates call states. |
| [TransferStatus(Call)](arkts-telephony-call-transferstatus-e.md) | Enumerates call transfer states. |

<!--Del-->
### Enums(System API)

| Name | Description |
| --- | --- |
| [AudioDeviceType(Call)](arkts-telephony-call-audiodevicetype-e-sys.md) | Enumerates audio device types. |
| [CallAbilityEventId(Call)](arkts-telephony-call-callabilityeventid-e-sys.md) | Enumerates call ability event IDs. |
| [CallRestrictionMode(Call)](arkts-telephony-call-callrestrictionmode-e-sys.md) | Enumerates call restriction modes. |
| [CallRestrictionType(Call)](arkts-telephony-call-callrestrictiontype-e-sys.md) | Enumerates call restriction types. |
| [CallSessionEventId(Call)](arkts-telephony-call-callsessioneventid-e-sys.md) | Enumerates video call event types. |
| [CallTransferSettingType(Call)](arkts-telephony-call-calltransfersettingtype-e-sys.md) | Enumerates call transfer setting types. |
| [CallType(Call)](arkts-telephony-call-calltype-e-sys.md) | Enumerates call types. |
| [CallWaitingStatus(Call)](arkts-telephony-call-callwaitingstatus-e-sys.md) | Enumerates call waiting states. |
| [ConferenceState(Call)](arkts-telephony-call-conferencestate-e-sys.md) | Enumerates conference states. |
| [DetailedCallState(Call)](arkts-telephony-call-detailedcallstate-e-sys.md) | Enumerates detailed call states. |
| [DeviceDirection(Call)](arkts-telephony-call-devicedirection-e-sys.md) | Enumerates device directions in a video call. |
| [DialScene(Call)](arkts-telephony-call-dialscene-e-sys.md) | Enumerates dialup scenarios. |
| [DialType(Call)](arkts-telephony-call-dialtype-e-sys.md) | Enumerates dialup types. |
| [DisconnectedReason(Call)](arkts-telephony-call-disconnectedreason-e-sys.md) | Enumerates call disconnection causes. |
| [ImsCallMode(Call)](arkts-telephony-call-imscallmode-e-sys.md) | Enumerates IMS call modes. |
| [ImsRttMode(Call)](arkts-telephony-call-imsrttmode-e-sys.md) | Indicates the mode of the ims rtt. |
| [MarkType(Call)](arkts-telephony-call-marktype-e-sys.md) | Enumerates number mark types. |
| [MmiCodeResult(Call)](arkts-telephony-call-mmicoderesult-e-sys.md) | Defines the MMI code result. |
| [RestrictionStatus(Call)](arkts-telephony-call-restrictionstatus-e-sys.md) | Enumerates call restriction states. |
| [RttState(Call)](arkts-telephony-call-rttstate-e-sys.md) | Indicates the state of the rtt. |
| [VideoRequestResultType(Call)](arkts-telephony-call-videorequestresulttype-e-sys.md) | Enumerates video call upgrade or downgrade request types. |
| [VideoStateType(Call)](arkts-telephony-call-videostatetype-e-sys.md) | Video state type. |
| [VoNRState(Call)](arkts-telephony-call-vonrstate-e-sys.md) | Enumerates VoNR switch states. |
| [XCallType(Call)](arkts-telephony-call-xcalltype-e-sys.md) | Enumerates X-Call types. |
<!--DelEnd-->
