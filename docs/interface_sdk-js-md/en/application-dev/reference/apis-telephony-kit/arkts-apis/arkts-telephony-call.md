# @ohos.telephony.call

The **call** module provides call management functions, including making calls, redirecting to the dial screen, obtaining the call status, and formatting phone numbers. To subscribe to call status changes, use [`observer.on('callStateChange')`](arkts-telephony-observer-onnetworkstatechange-f.md#onnetworkstatechange).

**Since:** 23

<!--Device-unnamed-declare namespace call--><!--Device-unnamed-declare namespace call-End-->

**System capability:** SystemCapability.Telephony.CallManager

## Modules to Import

```TypeScript
import { call } from 'call';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [dial](arkts-telephony-call-dial-f.md#dial) | Initiates a call. You can set call options as needed. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API is supported since API version 6 and deprecated since API version 9. The substitute API is available > only for system applications. |
| [dial](arkts-telephony-call-dial-f.md#dial) | Initiates a call. You can set call options as needed. This API uses a promise to return the result. > **NOTE：**> > This API is supported since API version 6 and deprecated since API version 9. The substitute API is available > only for system applications. |
| [dial](arkts-telephony-call-dial-f.md#dial) | Initiates a call. This API uses an asynchronous callback to return the result. > **NOTE：**> > This API is supported since API version 6 and deprecated since API version 9. The substitute API is available > only for system applications. |
| [formatPhoneNumber](arkts-telephony-call-formatphonenumber-f.md#formatphonenumber) | Formats a phone number based on specified formatting options. This API uses an asynchronous callback to return the result. A formatted phone number is a standard numeric string, for example, 555 0100. |
| [formatPhoneNumber](arkts-telephony-call-formatphonenumber-f.md#formatphonenumber) | Formats a phone number based on specified formatting options. This API uses a promise to return the result. A formatted phone number is a standard numeric string, for example, 555 0100. |
| [formatPhoneNumber](arkts-telephony-call-formatphonenumber-f.md#formatphonenumber) | Formats a phone number. This API uses an asynchronous callback to return the result. A formatted phone number is a standard numeric string, for example, 555 0100. |
| [formatPhoneNumberToE164](arkts-telephony-call-formatphonenumbertoe164-f.md#formatphonenumbertoe164) | Converts a phone number into the E.164 format. This API uses an asynchronous callback to return the result. The phone number must match the specified country code. For example, for a China phone number, the country code must be **CN**. Otherwise, **null** will be returned. |
| [formatPhoneNumberToE164](arkts-telephony-call-formatphonenumbertoe164-f.md#formatphonenumbertoe164) | Converts a phone number into the E.164 format. This API uses a promise to return the result. The phone number must match the specified country code. For example, for a China phone number, the country code must be **CN**. Otherwise, **null** will be returned. All country codes are supported. |
| [getCallState](arkts-telephony-call-getcallstate-f.md#getcallstate) | Obtains the call status. This API uses an asynchronous callback to return the result. |
| [getCallState](arkts-telephony-call-getcallstate-f.md#getcallstate) | Obtains the call status. This API uses a promise to return the result. |
| [getCallStateSync](arkts-telephony-call-getcallstatesync-f.md#getcallstatesync) | Obtains the call status. |
| [getCallTransferInfo](arkts-telephony-call-getcalltransferinfo-f.md#getcalltransferinfo) | Obtains call transfer information with the phone number. This API uses a promise to return the result. |
| [hasCall](arkts-telephony-call-hascall-f.md#hascall) | Checks whether a call is in progress. This API uses an asynchronous callback to return the result. |
| [hasCall](arkts-telephony-call-hascall-f.md#hascall) | Checks whether a call is in progress. This API uses a promise to return the result. |
| [hasCallSync](arkts-telephony-call-hascallsync-f.md#hascallsync) | Checks whether a call is in progress. |
| [hasVoiceCapability](arkts-telephony-call-hasvoicecapability-f.md#hasvoicecapability) | Checks whether a device supports voice calls. |
| [isEmergencyPhoneNumber](arkts-telephony-call-isemergencyphonenumber-f.md#isemergencyphonenumber) | Checks whether the called number is an emergency number based on the phone number. This API uses an asynchronous callback to return the result. |
| [isEmergencyPhoneNumber](arkts-telephony-call-isemergencyphonenumber-f.md#isemergencyphonenumber) | Checks whether the called number is an emergency number based on the phone number. This API uses a promise to return the result. |
| [isEmergencyPhoneNumber](arkts-telephony-call-isemergencyphonenumber-f.md#isemergencyphonenumber) | Checks whether the called number is an emergency number. This API uses an asynchronous callback to return the result. |
| [makeCall](arkts-telephony-call-makecall-f.md#makecall) | Launches the call screen and displays the dialed number. This API uses an asynchronous callback to return the result. This API can be called only in a UIAbility. |
| [makeCall](arkts-telephony-call-makecall-f.md#makecall) | Launches the call screen and displays the dialed number. This API uses a promise to return the result. This API can be called only in a UIAbility. |
| [makeCall](arkts-telephony-call-makecall-f.md#makecall) | Launches the call screen and displays the dialed number. This API uses a promise to return the result. This API can be called only in a UIAbility. |
| [makeCall](arkts-telephony-call-makecall-f.md#makecall) | Launches the call screen and displays the dialed number. This API uses a promise to return the result. You need to declare the **ohos.permission.START_ABILITIES_FROM_BACKGROUND** permission if you want to call the API in the background. |
| [makeCallWithToken](arkts-telephony-call-makecallwithtoken-f.md#makecallwithtoken) | Go to the dial screen and the called number is displayed.The authentication challenge value is returned. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [answerCall](arkts-telephony-call-answercall-f-sys.md#answercall) | Answers a call. This API uses an asynchronous callback to return the result. |
| [answerCall](arkts-telephony-call-answercall-f-sys.md#answercall-system-api) | Answers a call. This API uses a promise to return the result. |
| [answerCall](arkts-telephony-call-answercall-f-sys.md#answercall-system-api) | Answers a call. This API uses an asynchronous callback to return the result. |
| [answerCall](arkts-telephony-call-answercall-f-sys.md#answercall-system-api) | Answers a call. This API uses a promise to return the result. |
| [answerCall](arkts-telephony-call-answercall-f-sys.md#answercall-system-api) | Answers the incoming rtt |
| [canSetCallTransferTime](arkts-telephony-call-cansetcalltransfertime-f-sys.md#cansetcalltransfertime) | Checks whether the call forwarding time can be set. This API uses an asynchronous callback to return the result. |
| [canSetCallTransferTime](arkts-telephony-call-cansetcalltransfertime-f-sys.md#cansetcalltransfertime-system-api) | Checks whether the call forwarding time can be set. This API uses a promise to return the result. |
| [cancelCallUpgrade](arkts-telephony-call-cancelcallupgrade-f-sys.md#cancelcallupgrade) | Cancels the upgrade of a video call. This API uses a promise to return the result. |
| [cancelMuted](arkts-telephony-call-cancelmuted-f-sys.md#cancelmuted) | Cancels call muting. This API uses an asynchronous callback to return the result. |
| [cancelMuted](arkts-telephony-call-cancelmuted-f-sys.md#cancelmuted-system-api) | Cancels call muting. This API uses a promise to return the result. |
| [closeUnfinishedUssd](arkts-telephony-call-closeunfinishedussd-f-sys.md#closeunfinishedussd) | Cancels the unfinished USSD services. This API uses an asynchronous callback to return the result. |
| [closeUnfinishedUssd](arkts-telephony-call-closeunfinishedussd-f-sys.md#closeunfinishedussd-system-api) | Cancels the unfinished USSD services. This API uses a promise to return the result. |
| [combineConference](arkts-telephony-call-combineconference-f-sys.md#combineconference) | Combines two calls into a conference call. This API uses an asynchronous callback to return the result. |
| [combineConference](arkts-telephony-call-combineconference-f-sys.md#combineconference-system-api) | Combines two calls into a conference call. This API uses a promise to return the result. |
| [controlCamera](arkts-telephony-call-controlcamera-f-sys.md#controlcamera) | Uses the specified camera to make a video call. If **cameraId** is left empty, the camera is disabled. This API uses a promise to return the result. |
| [dialCall](arkts-telephony-call-dialcall-f-sys.md#dialcall) | Initiates a call. You can set call options as needed. This API uses an asynchronous callback to return the result. |
| [dialCall](arkts-telephony-call-dialcall-f-sys.md#dialcall-system-api) | Initiates a call. You can set call options as needed. This API uses a promise to return the result. |
| [dialCall](arkts-telephony-call-dialcall-f-sys.md#dialcall-system-api) | Initiates a call. This API uses an asynchronous callback to return the result. |
| [disableImsSwitch](arkts-telephony-call-disableimsswitch-f-sys.md#disableimsswitch) | Disables the IMS service. This API uses an asynchronous callback to return the result. |
| [disableImsSwitch](arkts-telephony-call-disableimsswitch-f-sys.md#disableimsswitch-system-api) | Disables the IMS service. This API uses a promise to return the result. |
| [enableImsSwitch](arkts-telephony-call-enableimsswitch-f-sys.md#enableimsswitch) | Enables the IMS service. This API uses an asynchronous callback to return the result. |
| [enableImsSwitch](arkts-telephony-call-enableimsswitch-f-sys.md#enableimsswitch-system-api) | Enables the IMS service. This API uses a promise to return the result. |
| [getCallIdListForConference](arkts-telephony-call-getcallidlistforconference-f-sys.md#getcallidlistforconference) | Obtains the list of call IDs in a conference. This API uses an asynchronous callback to return the result. |
| [getCallIdListForConference](arkts-telephony-call-getcallidlistforconference-f-sys.md#getcallidlistforconference-system-api) | Obtains the list of call IDs in a conference. This API uses a promise to return the result. |
| [getCallRestrictionStatus](arkts-telephony-call-getcallrestrictionstatus-f-sys.md#getcallrestrictionstatus) | Obtains the call restriction status. This API uses an asynchronous callback to return the result. |
| [getCallRestrictionStatus](arkts-telephony-call-getcallrestrictionstatus-f-sys.md#getcallrestrictionstatus-system-api) | Obtains the call restriction status. This API uses a promise to return the result. |
| [getCallTransferInfo](arkts-telephony-call-getcalltransferinfo-f-sys.md#getcalltransferinfo-system-api) | Obtains call transfer information. This API uses an asynchronous callback to return the result. |
| [getCallTransferInfo](arkts-telephony-call-getcalltransferinfo-f-sys.md#getcalltransferinfo-system-api) | Obtains call transfer information. This API uses a promise to return the result. |
| [getCallWaitingStatus](arkts-telephony-call-getcallwaitingstatus-f-sys.md#getcallwaitingstatus) | Obtains the call waiting status. This API uses an asynchronous callback to return the result. |
| [getCallWaitingStatus](arkts-telephony-call-getcallwaitingstatus-f-sys.md#getcallwaitingstatus-system-api) | Obtains the call waiting status. This API uses a promise to return the result. |
| [getMainCallId](arkts-telephony-call-getmaincallid-f-sys.md#getmaincallid) | Obtains the main call ID. This API uses an asynchronous callback to return the result. |
| [getMainCallId](arkts-telephony-call-getmaincallid-f-sys.md#getmaincallid-system-api) | Obtains the main call ID. This API uses a promise to return the result. |
| [getSubCallIdList](arkts-telephony-call-getsubcallidlist-f-sys.md#getsubcallidlist) | Obtains the list of subcall IDs. This API uses an asynchronous callback to return the result. |
| [getSubCallIdList](arkts-telephony-call-getsubcallidlist-f-sys.md#getsubcallidlist-system-api) | Obtains the list of subcall IDs. This API uses a promise to return the result. |
| [getVoNRState](arkts-telephony-call-getvonrstate-f-sys.md#getvonrstate) | Obtains the status of the VoNR switch. This API uses an asynchronous callback to return the result. |
| [getVoNRState](arkts-telephony-call-getvonrstate-f-sys.md#getvonrstate-system-api) | Obtains the status of the VoNR switch. This API uses a promise to return the result. |
| [hangUpCall](arkts-telephony-call-hangupcall-f-sys.md#hangupcall) | Ends a call. This API uses an asynchronous callback to return the result. |
| [hangUpCall](arkts-telephony-call-hangupcall-f-sys.md#hangupcall-system-api) | Ends a call. This API uses a promise to return the result. |
| [hangUpCall](arkts-telephony-call-hangupcall-f-sys.md#hangupcall-system-api) | Ends a call. This API uses an asynchronous callback to return the result. |
| [holdCall](arkts-telephony-call-holdcall-f-sys.md#holdcall) | Holds a call based on the specified call ID. This API uses an asynchronous callback to return the result. |
| [holdCall](arkts-telephony-call-holdcall-f-sys.md#holdcall-system-api) | Holds a call based on the specified call ID. This API uses a promise to return the result. |
| [inputDialerSpecialCode](arkts-telephony-call-inputdialerspecialcode-f-sys.md#inputdialerspecialcode) | Performs a secret code broadcast. This API uses an asynchronous callback to return the result. |
| [inputDialerSpecialCode](arkts-telephony-call-inputdialerspecialcode-f-sys.md#inputdialerspecialcode-system-api) | Performs a secret code broadcast. This API uses a promise to return the result. |
| [isImsSwitchEnabled](arkts-telephony-call-isimsswitchenabled-f-sys.md#isimsswitchenabled) | Checks whether the IMS service is enabled. This API uses an asynchronous callback to return the result. |
| [isImsSwitchEnabled](arkts-telephony-call-isimsswitchenabled-f-sys.md#isimsswitchenabled-system-api) | Checks whether the IMS service is enabled. This API uses a promise to return the result. |
| [isImsSwitchEnabledSync](arkts-telephony-call-isimsswitchenabledsync-f-sys.md#isimsswitchenabledsync) | Checks whether the IMS service is enabled. This API returns the result synchronously. |
| [isInEmergencyCall](arkts-telephony-call-isinemergencycall-f-sys.md#isinemergencycall) | Checks whether a call is an emergency call. This API uses an asynchronous callback to return the result. |
| [isInEmergencyCall](arkts-telephony-call-isinemergencycall-f-sys.md#isinemergencycall-system-api) | Checks whether a call is an emergency call. This API uses a promise to return the result. |
| [isNewCallAllowed](arkts-telephony-call-isnewcallallowed-f-sys.md#isnewcallallowed) | Checks whether a new call is allowed. This API uses an asynchronous callback to return the result. |
| [isNewCallAllowed](arkts-telephony-call-isnewcallallowed-f-sys.md#isnewcallallowed-system-api) | Checks whether a new call is allowed. This API uses a promise to return the result. |
| [isRinging](arkts-telephony-call-isringing-f-sys.md#isringing) | Checks whether the ringtone is playing. This API uses an asynchronous callback to return the result. |
| [isRinging](arkts-telephony-call-isringing-f-sys.md#isringing-system-api) | Checks whether the ringtone is playing. This API uses a promise to return the result. |
| [joinConference](arkts-telephony-call-joinconference-f-sys.md#joinconference) | Joins a conference call. This API uses an asynchronous callback to return the result. |
| [joinConference](arkts-telephony-call-joinconference-f-sys.md#joinconference-system-api) | Joins a conference call. This API uses a promise to return the result. |
| [kickOutFromConference](arkts-telephony-call-kickoutfromconference-f-sys.md#kickoutfromconference) | Removes a specified call from a conference call. This API uses an asynchronous callback to return the result. |
| [kickOutFromConference](arkts-telephony-call-kickoutfromconference-f-sys.md#kickoutfromconference-system-api) | Removes a specified call from a conference call. This API uses a promise to return the result. |
| [muteRinger](arkts-telephony-call-muteringer-f-sys.md#muteringer) | Mutes the ringtone while it is playing. It does not work if the ringtone has been muted. This API uses an asynchronous callback to return the result. |
| [muteRinger](arkts-telephony-call-muteringer-f-sys.md#muteringer-system-api) | Mutes the ringtone while it is playing. It does not work if the ringtone has been muted. This API uses a promise to return the result. |
| [offAudioDeviceChange](arkts-telephony-call-offaudiodevicechange-f-sys.md#offaudiodevicechange) | Unsubscribe from the audioDeviceChange event. |
| [offCallDetailsChange](arkts-telephony-call-offcalldetailschange-f-sys.md#offcalldetailschange) | Unsubscribe from the callDetailsChange event. |
| [offCallDisconnectedCause](arkts-telephony-call-offcalldisconnectedcause-f-sys.md#offcalldisconnectedcause) | Unsubscribe from the callDisconnectedCause event. |
| [offCallEventChange](arkts-telephony-call-offcalleventchange-f-sys.md#offcalleventchange) | Unsubscribe from the callEventChange event. |
| [offCallSessionEvent](arkts-telephony-call-offcallsessionevent-f-sys.md#offcallsessionevent) | Unsubscribe from the callSessionEvent. |
| [offCameraCapabilitiesChange](arkts-telephony-call-offcameracapabilitieschange-f-sys.md#offcameracapabilitieschange) | Unsubscribe from the cameraCapabilitiesChange event. |
| [offImsCallModeChange](arkts-telephony-call-offimscallmodechange-f-sys.md#offimscallmodechange) | Unsubscribe from the imsCallModeChange event. |
| [offMmiCodeResult](arkts-telephony-call-offmmicoderesult-f-sys.md#offmmicoderesult) | Unsubscribe from the mmiCodeResult event. |
| [offPeerDimensionsChange](arkts-telephony-call-offpeerdimensionschange-f-sys.md#offpeerdimensionschange) | Unsubscribe from the peerDimensionsChange event. |
| [offPostDialDelay](arkts-telephony-call-offpostdialdelay-f-sys.md#offpostdialdelay) | Unsubscribe from the postDialDelay event. |
| [offReceiveRttMessage](arkts-telephony-call-offreceiverttmessage-f-sys.md#offreceiverttmessage) | Unsubscribe from the rtt message event. |
| [offRttErrCause](arkts-telephony-call-offrtterrcause-f-sys.md#offrtterrcause) | Unsubscribe from the rtt error report event. |
| [offRttModifyInd](arkts-telephony-call-offrttmodifyind-f-sys.md#offrttmodifyind) | Unsubscribe from the rtt modify indication. |
| [off_audioDeviceChange](arkts-telephony-call-offaudiodevicechange-f-sys.md#offaudiodevicechange) | Unsubscribes from **audioDeviceChange** events. This API uses an asynchronous callback to return the result. |
| [off_callDetailsChange](arkts-telephony-call-offcalldetailschange-f-sys.md#offcalldetailschange) | Unsubscribes from **callDetailsChange** events. This API uses an asynchronous callback to return the result. |
| [off_callDisconnectedCause](arkts-telephony-call-offcalldisconnectedcause-f-sys.md#offcalldisconnectedcause) | Unsubscribes from **callDisconnectedCause** events. This API uses an asynchronous callback to return the result. |
| [off_callEventChange](arkts-telephony-call-offcalleventchange-f-sys.md#offcalleventchange) | Unsubscribes from **callEventChange** events. This API uses an asynchronous callback to return the result. |
| [off_callSessionEvent](arkts-telephony-call-offcallsessionevent-f-sys.md#offcallsessionevent) | Unsubscribes from **callSessionEvent** events. This API uses an asynchronous callback to return the result. |
| [off_cameraCapabilitiesChange](arkts-telephony-call-offcameracapabilitieschange-f-sys.md#offcameracapabilitieschange) | Unsubscribes from **cameraCapabilitiesChange** events. This API uses an asynchronous callback to return the result. |
| [off_imsCallModeChange](arkts-telephony-call-offimscallmodechange-f-sys.md#offimscallmodechange) | Unsubscribes from **imsCallModeChange** events. This API uses an asynchronous callback to return the result. |
| [off_mmiCodeResult](arkts-telephony-call-offmmicoderesult-f-sys.md#offmmicoderesult) | Unsubscribes from **mmiCodeResult** events. This API uses an asynchronous callback to return the result. |
| [off_peerDimensionsChange](arkts-telephony-call-offpeerdimensionschange-f-sys.md#offpeerdimensionschange) | Unsubscribes from **peerDimensionsChange** events. This API uses an asynchronous callback to return the result. |
| [off_postDialDelay](arkts-telephony-call-offpostdialdelay-f-sys.md#offpostdialdelay) | Unsubscribes from **postDialDelay** events. This API uses an asynchronous callback to return the result. |
| [onAudioDeviceChange](arkts-telephony-call-onaudiodevicechange-f-sys.md#onaudiodevicechange) | Subscribe to the audioDeviceChange event. |
| [onCallDetailsChange](arkts-telephony-call-oncalldetailschange-f-sys.md#oncalldetailschange) | Subscribe to the callDetailsChange event. |
| [onCallDisconnectedCause](arkts-telephony-call-oncalldisconnectedcause-f-sys.md#oncalldisconnectedcause) | Subscribe to the callDisconnectedCause event. |
| [onCallEventChange](arkts-telephony-call-oncalleventchange-f-sys.md#oncalleventchange) | Subscribe to the callEventChange event. |
| [onCallSessionEvent](arkts-telephony-call-oncallsessionevent-f-sys.md#oncallsessionevent) | Subscribe to the callSessionEvent. |
| [onCameraCapabilitiesChange](arkts-telephony-call-oncameracapabilitieschange-f-sys.md#oncameracapabilitieschange) | Subscribe to the cameraCapabilitiesChange event. |
| [onImsCallModeChange](arkts-telephony-call-onimscallmodechange-f-sys.md#onimscallmodechange) | Subscribe to the imsCallModeChange event. |
| [onMmiCodeResult](arkts-telephony-call-onmmicoderesult-f-sys.md#onmmicoderesult) | Subscribe to the mmiCodeResult event. |
| [onPeerDimensionsChange](arkts-telephony-call-onpeerdimensionschange-f-sys.md#onpeerdimensionschange) | Subscribe to the peerDimensionsChange event. |
| [onPostDialDelay](arkts-telephony-call-onpostdialdelay-f-sys.md#onpostdialdelay) | Subscribe to the postDialDelay event. |
| [onReceiveRttMessage](arkts-telephony-call-onreceiverttmessage-f-sys.md#onreceiverttmessage) | Subscribe to the rtt message event. |
| [onRttErrCause](arkts-telephony-call-onrtterrcause-f-sys.md#onrtterrcause) | Subscribe to the rtt error event. |
| [onRttModifyInd](arkts-telephony-call-onrttmodifyind-f-sys.md#onrttmodifyind) | Subscribe to the rtt modify indication. |
| [on_audioDeviceChange](arkts-telephony-call-onaudiodevicechange-f-sys.md#onaudiodevicechange) | Subscribes to audio device change events. This API uses an asynchronous callback to return the result. |
| [on_callDetailsChange](arkts-telephony-call-oncalldetailschange-f-sys.md#oncalldetailschange) | Subscribes to **callDetailsChange** events. This API uses an asynchronous callback to return the result. |
| [on_callDisconnectedCause](arkts-telephony-call-oncalldisconnectedcause-f-sys.md#oncalldisconnectedcause) | Subscribes to **callDisconnectedCause** events. This API uses an asynchronous callback to return the result. |
| [on_callEventChange](arkts-telephony-call-oncalleventchange-f-sys.md#oncalleventchange) | Subscribes to **callEventChange** events. This API uses an asynchronous callback to return the result. |
| [on_callSessionEvent](arkts-telephony-call-oncallsessionevent-f-sys.md#oncallsessionevent) | Subscribes to **callSessionEvent** events. This API uses an asynchronous callback to return the result. |
| [on_cameraCapabilitiesChange](arkts-telephony-call-oncameracapabilitieschange-f-sys.md#oncameracapabilitieschange) | Subscribes to **cameraCapabilitiesChange** events. This API uses an asynchronous callback to return the result. |
| [on_imsCallModeChange](arkts-telephony-call-onimscallmodechange-f-sys.md#onimscallmodechange) | Subscribes to **imsCallModeChange** events. This API uses an asynchronous callback to return the result. |
| [on_mmiCodeResult](arkts-telephony-call-onmmicoderesult-f-sys.md#onmmicoderesult) | Subscribes to **mmiCodeResult** events. This API uses an asynchronous callback to return the result. |
| [on_peerDimensionsChange](arkts-telephony-call-onpeerdimensionschange-f-sys.md#onpeerdimensionschange) | Subscribes to **peerDimensionsChange** events. This API uses an asynchronous callback to return the result. |
| [on_postDialDelay](arkts-telephony-call-onpostdialdelay-f-sys.md#onpostdialdelay) | Subscribes to **postDialDelay** events. This API uses an asynchronous callback to return the result. |
| [postDialProceed](arkts-telephony-call-postdialproceed-f-sys.md#postdialproceed) | Continues a call by playing a post-dial DTMF string. This API uses an asynchronous callback to return the result. If the called number is in the format of "common phone number + semicolon (;) + DTMF string", for example, **400xxxxxxx;123**, and the listening for **postDialDelay** events is enabled, the system reports a **postDialDelay** event when the call is connected. The application can then call this API to send DTMF tones. |
| [postDialProceed](arkts-telephony-call-postdialproceed-f-sys.md#postdialproceed-system-api) | Continues a call by playing a post-dial DTMF string. This API uses a promise to return the result. If the called number is in the format of "common phone number + semicolon (;) + DTMF string", for example, **400xxxxxxx;123**, and the listening for **postDialDelay** events is enabled, the system reports a **postDialDelay** event when the call is connected. The application can then call this API to send DTMF tones. |
| [preloadCallUI](arkts-telephony-call-preloadcallui-f-sys.md#preloadcallui) | Preload callUI. |
| [rejectCall](arkts-telephony-call-rejectcall-f-sys.md#rejectcall) | Rejects a call. This API uses an asynchronous callback to return the result. |
| [rejectCall](arkts-telephony-call-rejectcall-f-sys.md#rejectcall-system-api) | Rejects a call. This API uses a promise to return the result. |
| [rejectCall](arkts-telephony-call-rejectcall-f-sys.md#rejectcall-system-api) | Rejects a call. This API uses an asynchronous callback to return the result. |
| [rejectCall](arkts-telephony-call-rejectcall-f-sys.md#rejectcall-system-api) | Rejects a call. This API uses an asynchronous callback to return the result. |
| [rejectCall](arkts-telephony-call-rejectcall-f-sys.md#rejectcall-system-api) | Rejects a call. This API uses an asynchronous callback to return the result. |
| [removeMissedIncomingCallNotification](arkts-telephony-call-removemissedincomingcallnotification-f-sys.md#removemissedincomingcallnotification) | Removes missed call notifications. This API uses an asynchronous callback to return the result. |
| [removeMissedIncomingCallNotification](arkts-telephony-call-removemissedincomingcallnotification-f-sys.md#removemissedincomingcallnotification-system-api) | Removes missed call notifications. This API uses a promise to return the result. |
| [sendCallUiEvent](arkts-telephony-call-sendcalluievent-f-sys.md#sendcalluievent) | Sends a call UI event. This API uses a promise to return the result. |
| [sendRttMessage](arkts-telephony-call-sendrttmessage-f-sys.md#sendrttmessage) | Send rtt message. |
| [sendUssdResponse](arkts-telephony-call-sendussdresponse-f-sys.md#sendussdresponse) | Sends a response to the Unstructured Supplementary Service Data (USSD) service to the carrier. |
| [separateConference](arkts-telephony-call-separateconference-f-sys.md#separateconference) | Separates calls from a conference call. This API uses an asynchronous callback to return the result. |
| [separateConference](arkts-telephony-call-separateconference-f-sys.md#separateconference-system-api) | Separates calls from a conference call. This API uses a promise to return the result. |
| [setAudioDevice](arkts-telephony-call-setaudiodevice-f-sys.md#setaudiodevice) | Sets the audio device for a call. This API uses an asynchronous callback to return the result. |
| [setAudioDevice](arkts-telephony-call-setaudiodevice-f-sys.md#setaudiodevice-system-api) | Sets the audio device for a call. This API uses a promise to return the result. |
| [setCallRestriction](arkts-telephony-call-setcallrestriction-f-sys.md#setcallrestriction) | Sets the call restriction status. This API uses an asynchronous callback to return the result. |
| [setCallRestriction](arkts-telephony-call-setcallrestriction-f-sys.md#setcallrestriction-system-api) | Sets the call restriction status. This API uses a promise to return the result. |
| [setCallRestrictionPassword](arkts-telephony-call-setcallrestrictionpassword-f-sys.md#setcallrestrictionpassword) | Changes the call barring password. This API uses an asynchronous callback to return the result. |
| [setCallRestrictionPassword](arkts-telephony-call-setcallrestrictionpassword-f-sys.md#setcallrestrictionpassword-system-api) | Changes the call barring password. This API uses a promise to return the result. |
| [setCallTransfer](arkts-telephony-call-setcalltransfer-f-sys.md#setcalltransfer) | Sets call transfer information. This API uses an asynchronous callback to return the result. |
| [setCallTransfer](arkts-telephony-call-setcalltransfer-f-sys.md#setcalltransfer-system-api) | Sets call transfer information. This API uses a promise to return the result. |
| [setCallWaiting](arkts-telephony-call-setcallwaiting-f-sys.md#setcallwaiting) | Specifies whether to enable the call waiting service. This API uses an asynchronous callback to return the result. |
| [setCallWaiting](arkts-telephony-call-setcallwaiting-f-sys.md#setcallwaiting-system-api) | Specifies whether to enable the call waiting service. This API uses a promise to return the result. |
| [setDeviceDirection](arkts-telephony-call-setdevicedirection-f-sys.md#setdevicedirection) | Sets the video call screen to follow the device direction. This API uses a promise to return the result. |
| [setDisplaySurface](arkts-telephony-call-setdisplaysurface-f-sys.md#setdisplaysurface) | Sets the remote display window. This API uses a promise to return the result. |
| [setMuted](arkts-telephony-call-setmuted-f-sys.md#setmuted) | Sets call muting. This API uses an asynchronous callback to return the result. |
| [setMuted](arkts-telephony-call-setmuted-f-sys.md#setmuted-system-api) | Sets call muting. This API uses a promise to return the result. |
| [setPreviewSurface](arkts-telephony-call-setpreviewsurface-f-sys.md#setpreviewsurface) | Sets the local preview window. This API uses a promise to return the result. |
| [setRttCapability](arkts-telephony-call-setrttcapability-f-sys.md#setrttcapability) | Set rtt capability. |
| [setVoNRState](arkts-telephony-call-setvonrstate-f-sys.md#setvonrstate) | Sets the status of the VoNR switch. This API uses an asynchronous callback to return the result. |
| [setVoNRState](arkts-telephony-call-setvonrstate-f-sys.md#setvonrstate-system-api) | Sets the status of the VoNR switch. This API uses a promise to return the result. |
| [startDTMF](arkts-telephony-call-startdtmf-f-sys.md#startdtmf) | Starts playing DTMF tones. This API uses an asynchronous callback to return the result. |
| [startDTMF](arkts-telephony-call-startdtmf-f-sys.md#startdtmf-system-api) | Starts playing DTMF tones. This API uses a promise to return the result. |
| [startRtt](arkts-telephony-call-startrtt-f-sys.md#startrtt) | Start rtt. |
| [stopDTMF](arkts-telephony-call-stopdtmf-f-sys.md#stopdtmf) | Stops playing DTMF tones. This API uses an asynchronous callback to return the result. |
| [stopDTMF](arkts-telephony-call-stopdtmf-f-sys.md#stopdtmf-system-api) | Stops playing DTMF tones. This API uses a promise to return the result. |
| [stopRtt](arkts-telephony-call-stoprtt-f-sys.md#stoprtt) | Stop rtt. |
| [switchCall](arkts-telephony-call-switchcall-f-sys.md#switchcall) | Switches a call. This API uses an asynchronous callback to return the result. |
| [switchCall](arkts-telephony-call-switchcall-f-sys.md#switchcall-system-api) | Switches a call. This API uses a promise to return the result. |
| [unHoldCall](arkts-telephony-call-unholdcall-f-sys.md#unholdcall) | Unholds a call based on the specified call ID. This API uses an asynchronous callback to return the result. |
| [unHoldCall](arkts-telephony-call-unholdcall-f-sys.md#unholdcall-system-api) | Unholds a call based on the specified call ID. This API uses a promise to return the result. |
| [unloadCallUI](arkts-telephony-call-unloadcallui-f-sys.md#unloadcallui) | Unload callUI. |
| [updateImsCallMode](arkts-telephony-call-updateimscallmode-f-sys.md#updateimscallmode) | Updates the IMS call mode. This API uses an asynchronous callback to return the result. |
| [updateImsCallMode](arkts-telephony-call-updateimscallmode-f-sys.md#updateimscallmode-system-api) | Updates the IMS call mode. This API uses a promise to return the result. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [DialOptions](arkts-telephony-call-dialoptions-i.md) | Provides an option for determining whether a call is a video call. |
| [EmergencyNumberOptions](arkts-telephony-call-emergencynumberoptions-i.md) | Provides an option for determining whether a number is an emergency number for the SIM card in the specified slot. |
| [MakeCallOptions](arkts-telephony-call-makecalloptions-i.md) | Provides an option for determining whether a call is a video call. |
| [NumberFormatOptions](arkts-telephony-call-numberformatoptions-i.md) | Provides an option for number formatting. |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [AudioDevice](arkts-telephony-call-audiodevice-i-sys.md) | Enumerates audio devices. |
| [AudioDeviceCallbackInfo](arkts-telephony-call-audiodevicecallbackinfo-i-sys.md) | Defines the audio device information. |
| [CallAttributeOptions](arkts-telephony-call-callattributeoptions-i-sys.md) | Defines the call attribute options. |
| [CallEventOptions](arkts-telephony-call-calleventoptions-i-sys.md) | Defines the call event options. |
| [CallRestrictionInfo](arkts-telephony-call-callrestrictioninfo-i-sys.md) | Defines the call restriction information. |
| [CallSessionEvent](arkts-telephony-call-callsessionevent-i-sys.md) | Defines the video call event information. |
| [CallTransferInfo](arkts-telephony-call-calltransferinfo-i-sys.md) | Defines the call transfer information. |
| [CallTransferResult](arkts-telephony-call-calltransferresult-i-sys.md) | Defines the call transfer result. |
| [CameraCapabilities](arkts-telephony-call-cameracapabilities-i-sys.md) | Defines the local image resolution in a video call. |
| [DialCallOptions](arkts-telephony-call-dialcalloptions-i-sys.md) | Provides an option for determining whether a call is a video call. |
| [DialOptions](arkts-telephony-call-dialoptions-i-sys.md) | Provides an option for determining whether a call is a video call. |
| [DisconnectedDetails](arkts-telephony-call-disconnecteddetails-i-sys.md) | Defines the call disconnection cause. |
| [ImsCallModeInfo](arkts-telephony-call-imscallmodeinfo-i-sys.md) | Defines the video call mode information. |
| [MmiCodeResults](arkts-telephony-call-mmicoderesults-i-sys.md) | Defines the MMI code result. |
| [NumberMarkInfo](arkts-telephony-call-numbermarkinfo-i-sys.md) | Defines a number mark. |
| [PeerDimensionsDetail](arkts-telephony-call-peerdimensionsdetail-i-sys.md) | Defines the peer image resolution in a video call. |
| [RejectMessageOptions](arkts-telephony-call-rejectmessageoptions-i-sys.md) | Defines options for the call rejection message. |
| [RttErrorInfo](arkts-telephony-call-rtterrorinfo-i-sys.md) | Indicates the info of the rtt error. |
| [RttEventInfo](arkts-telephony-call-rtteventinfo-i-sys.md) | Indicates the info of the rtt event. |
| [RttMessageInfo](arkts-telephony-call-rttmessageinfo-i-sys.md) | Indicates the info of the rtt message. |
| [VoipCallAttribute](arkts-telephony-call-voipcallattribute-i-sys.md) | Defines the VoIP call information. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [CCallState](arkts-telephony-call-ccallstate-e.md) | Carrier call state code. |
| [CallState](arkts-telephony-call-callstate-e.md) | Enumerates call states. |
| [TelCallState](arkts-telephony-call-telcallstate-e.md) | Enumerates call states. |

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [AudioDeviceType](arkts-telephony-call-audiodevicetype-e-sys.md) | Enumerates audio device types. |
| [CallAbilityEventId](arkts-telephony-call-callabilityeventid-e-sys.md) | Enumerates call ability event IDs. |
| [CallRestrictionMode](arkts-telephony-call-callrestrictionmode-e-sys.md) | Enumerates call restriction modes. |
| [CallRestrictionType](arkts-telephony-call-callrestrictiontype-e-sys.md) | Enumerates call restriction types. |
| [CallSessionEventId](arkts-telephony-call-callsessioneventid-e-sys.md) | Enumerates video call event types. |
| [CallTransferSettingType](arkts-telephony-call-calltransfersettingtype-e-sys.md) | Enumerates call transfer setting types. |
| [CallTransferType](arkts-telephony-call-calltransfertype-e-sys.md) | Enumerates call transfer types. |
| [CallType](arkts-telephony-call-calltype-e-sys.md) | Enumerates call types. |
| [CallWaitingStatus](arkts-telephony-call-callwaitingstatus-e-sys.md) | Enumerates call waiting states. |
| [ConferenceState](arkts-telephony-call-conferencestate-e-sys.md) | Enumerates conference states. |
| [DetailedCallState](arkts-telephony-call-detailedcallstate-e-sys.md) | Enumerates detailed call states. |
| [DeviceDirection](arkts-telephony-call-devicedirection-e-sys.md) | Enumerates device directions in a video call. |
| [DialScene](arkts-telephony-call-dialscene-e-sys.md) | Enumerates dialup scenarios. |
| [DialType](arkts-telephony-call-dialtype-e-sys.md) | Enumerates dialup types. |
| [DisconnectedReason](arkts-telephony-call-disconnectedreason-e-sys.md) | Enumerates call disconnection causes. |
| [ImsCallMode](arkts-telephony-call-imscallmode-e-sys.md) | Enumerates IMS call modes. |
| [ImsRttMode](arkts-telephony-call-imsrttmode-e-sys.md) | Indicates the mode of the ims rtt. |
| [MarkType](arkts-telephony-call-marktype-e-sys.md) | Enumerates number mark types. |
| [MmiCodeResult](arkts-telephony-call-mmicoderesult-e-sys.md) | Defines the MMI code result. |
| [RestrictionStatus](arkts-telephony-call-restrictionstatus-e-sys.md) | Enumerates call restriction states. |
| [RttState](arkts-telephony-call-rttstate-e-sys.md) | Indicates the state of the rtt. |
| [TransferStatus](arkts-telephony-call-transferstatus-e-sys.md) | Enumerates call transfer states. |
| [VideoRequestResultType](arkts-telephony-call-videorequestresulttype-e-sys.md) | Enumerates video call upgrade or downgrade request types. |
| [VideoStateType](arkts-telephony-call-videostatetype-e-sys.md) | Video state type. |
| [VoNRState](arkts-telephony-call-vonrstate-e-sys.md) | Enumerates VoNR switch states. |
| [XCallType](arkts-telephony-call-xcalltype-e-sys.md) | Enumerates X-Call types. |
<!--DelEnd-->

