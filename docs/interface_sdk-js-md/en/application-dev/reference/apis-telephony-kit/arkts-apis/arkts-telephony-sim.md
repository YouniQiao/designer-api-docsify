# @ohos.telephony.sim

Provides applications with APIs for obtaining SIM card status, card file information, and card specifications. SIM cards include SIM, USIM, and CSIM cards.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace sim--><!--Device-unnamed-declare namespace sim-End-->

**System capability:** SystemCapability.Telephony.CoreService

## Modules to Import

```TypeScript
import { sim } from 'sim';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getActiveSimAccountInfoList](arkts-telephony-sim-getactivesimaccountinfolist-f.md#getActiveSimAccountInfoList) | Get the list of active SIM card account information. |
| [getActiveSimAccountInfoList](arkts-telephony-sim-getactivesimaccountinfolist-f.md#getActiveSimAccountInfoList) | Get the list of active SIM card account information. |
| [getCardType](arkts-telephony-sim-getcardtype-f.md#getCardType) | Obtains the type of the SIM card installed in a specified slot. |
| [getCardType](arkts-telephony-sim-getcardtype-f.md#getCardType) | Obtains the type of the SIM card installed in a specified slot. |
| [getCardTypeSync](arkts-telephony-sim-getcardtypesync-f.md#getCardTypeSync) | Obtains the type of the SIM card inserted in a specified slot. |
| [getDefaultVoiceSimId](arkts-telephony-sim-getdefaultvoicesimid-f.md#getDefaultVoiceSimId) | Obtains the default SIM ID for the voice service. |
| [getDefaultVoiceSimId](arkts-telephony-sim-getdefaultvoicesimid-f.md#getDefaultVoiceSimId) | Obtains the default SIM ID for the voice service. |
| [getDefaultVoiceSlotId](arkts-telephony-sim-getdefaultvoiceslotid-f.md#getDefaultVoiceSlotId) | Obtains the default card slot for the voice service. |
| [getDefaultVoiceSlotId](arkts-telephony-sim-getdefaultvoiceslotid-f.md#getDefaultVoiceSlotId) | Obtains the default card slot for the voice service. |
| [getISOCountryCodeForSim](arkts-telephony-sim-getisocountrycodeforsim-f.md#getISOCountryCodeForSim) | Obtains the ISO country code of the SIM card in a specified slot. |
| [getISOCountryCodeForSim](arkts-telephony-sim-getisocountrycodeforsim-f.md#getISOCountryCodeForSim) | Obtains the ISO country code of the SIM card in a specified slot. |
| [getISOCountryCodeForSimSync](arkts-telephony-sim-getisocountrycodeforsimsync-f.md#getISOCountryCodeForSimSync) | Obtains the ISO country code of the SIM card in a specified slot. |
| [getMaxSimCount](arkts-telephony-sim-getmaxsimcount-f.md#getMaxSimCount) | Obtains the maximum number of SIM cards that can be used simultaneously on the device, that is, the maximum number of SIM card slots. |
| [getOpKey](arkts-telephony-sim-getopkey-f.md#getOpKey) | Obtains the operator key of the SIM card in a specified slot. |
| [getOpKey](arkts-telephony-sim-getopkey-f.md#getOpKey) | Obtains the operator key of the SIM card in a specified slot. |
| [getOpKeySync](arkts-telephony-sim-getopkeysync-f.md#getOpKeySync) | Obtains the operator key of the SIM card in a specified slot. |
| [getOpName](arkts-telephony-sim-getopname-f.md#getOpName) | Obtains the operator name of the SIM card in a specified slot. |
| [getOpName](arkts-telephony-sim-getopname-f.md#getOpName) | Obtains the operator name of the SIM card in a specified slot. |
| [getOpNameSync](arkts-telephony-sim-getopnamesync-f.md#getOpNameSync) | Obtains the operator name of the SIM card in a specified slot. |
| [getSimAccountInfo](arkts-telephony-sim-getsimaccountinfo-f.md#getSimAccountInfo) | Get account information of SIM card. |
| [getSimAccountInfo](arkts-telephony-sim-getsimaccountinfo-f.md#getSimAccountInfo) | Get account information of SIM card. |
| [getSimLabel](arkts-telephony-sim-getsimlabel-f.md#getSimLabel) | Obtains the SIM card label. |
| [getSimLabel](arkts-telephony-sim-getsimlabel-f.md#getSimLabel) | Obtains the SIM card label. |
| [getSimLabelSync](arkts-telephony-sim-getsimlabelsync-f.md#getSimLabelSync) | Obtains the SIM card label synchronously. |
| [getSimOperatorNumeric](arkts-telephony-sim-getsimoperatornumeric-f.md#getSimOperatorNumeric) | Obtains the home PLMN number of the SIM card in a specified slot. &lt;p&gt;The value is recorded in the SIM card and is irrelevant to the network with which the SIM card is currently registered. |
| [getSimOperatorNumeric](arkts-telephony-sim-getsimoperatornumeric-f.md#getSimOperatorNumeric) | Obtains the home PLMN number of the SIM card in a specified slot. &lt;p&gt;The value is recorded in the SIM card and is irrelevant to the network with which the SIM card is currently registered. |
| [getSimOperatorNumericSync](arkts-telephony-sim-getsimoperatornumericsync-f.md#getSimOperatorNumericSync) | Obtains the home PLMN number of the SIM card in a specified slot. &lt;p&gt;The value is recorded in the SIM card and is irrelevant to the network with which the SIM card is currently registered. |
| [getSimSpn](arkts-telephony-sim-getsimspn-f.md#getSimSpn) | Obtains the service provider name (SPN) of the SIM card in a specified slot. &lt;p&gt;The value is recorded in the EFSPN file of the SIM card and is irrelevant to the network with which the SIM card is currently registered. |
| [getSimSpn](arkts-telephony-sim-getsimspn-f.md#getSimSpn) | Obtains the service provider name (SPN) of the SIM card in a specified slot. &lt;p&gt;The value is recorded in the EFSPN file of the SIM card and is irrelevant to the network with which the SIM card is currently registered. |
| [getSimSpnSync](arkts-telephony-sim-getsimspnsync-f.md#getSimSpnSync) | Obtains the service provider name (SPN) of the SIM card in a specified slot. &lt;p&gt;The value is recorded in the EFSPN file of the SIM card and is irrelevant to the network with which the SIM card is currently registered. |
| [getSimState](arkts-telephony-sim-getsimstate-f.md#getSimState) | Obtains the state of the SIM card in a specified slot. |
| [getSimState](arkts-telephony-sim-getsimstate-f.md#getSimState) | Obtains the state of the SIM card in a specified slot. |
| [getSimStateSync](arkts-telephony-sim-getsimstatesync-f.md#getSimStateSync) | Obtains the state of the SIM card in a specified slot. |
| [hasOperatorPrivileges](arkts-telephony-sim-hasoperatorprivileges-f.md#hasOperatorPrivileges) | Checks whether your application (the caller) has been granted the operator permissions. |
| [hasOperatorPrivileges](arkts-telephony-sim-hasoperatorprivileges-f.md#hasOperatorPrivileges) | Checks whether your application (the caller) has been granted the operator permissions. |
| [hasSimCard](arkts-telephony-sim-hassimcard-f.md#hasSimCard) | Checks whether a SIM card is inserted in a specified slot. |
| [hasSimCard](arkts-telephony-sim-hassimcard-f.md#hasSimCard) | Checks whether a SIM card is inserted in a specified slot. |
| [hasSimCardSync](arkts-telephony-sim-hassimcardsync-f.md#hasSimCardSync) | Checks whether a SIM card is inserted in a specified slot. |
| [isSimActive](arkts-telephony-sim-issimactive-f.md#isSimActive) | Checks whether the SIM card in a specified slot is activated. |
| [isSimActive](arkts-telephony-sim-issimactive-f.md#isSimActive) | Checks whether the SIM card in a specified slot is activated. |
| [isSimActiveSync](arkts-telephony-sim-issimactivesync-f.md#isSimActiveSync) | Checks whether the SIM card in a specified slot is activated. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [activateSim](arkts-telephony-sim-activatesim-f-sys.md#activateSim) | Activate the SIM card in the specified slot. |
| [activateSim](arkts-telephony-sim-activatesim-f-sys.md#activateSim-(System-API)) | Activate the SIM card in the specified slot. |
| [addIccDiallingNumbers](arkts-telephony-sim-addiccdiallingnumbers-f-sys.md#addIccDiallingNumbers) | Add dialing number information to SIM card. |
| [addIccDiallingNumbers](arkts-telephony-sim-addiccdiallingnumbers-f-sys.md#addIccDiallingNumbers-(System-API)) | Add dialing number information to SIM card. |
| [alterPin](arkts-telephony-sim-alterpin-f-sys.md#alterPin) | Change Pin Password. |
| [alterPin](arkts-telephony-sim-alterpin-f-sys.md#alterPin-(System-API)) | Change Pin Password. |
| [alterPin2](arkts-telephony-sim-alterpin2-f-sys.md#alterPin2) | Change Pin2 password. |
| [alterPin2](arkts-telephony-sim-alterpin2-f-sys.md#alterPin2-(System-API)) | Change Pin2 password. |
| [deactivateSim](arkts-telephony-sim-deactivatesim-f-sys.md#deactivateSim) | Disable SIM card in specified slot. |
| [deactivateSim](arkts-telephony-sim-deactivatesim-f-sys.md#deactivateSim-(System-API)) | Disable SIM card in specified slot. |
| [delIccDiallingNumbers](arkts-telephony-sim-deliccdiallingnumbers-f-sys.md#delIccDiallingNumbers) | Delete dialing number information on SIM card. |
| [delIccDiallingNumbers](arkts-telephony-sim-deliccdiallingnumbers-f-sys.md#delIccDiallingNumbers-(System-API)) | Delete dialing number information on SIM card. |
| [getAllSimAccountInfoList](arkts-telephony-sim-getallsimaccountinfolist-f-sys.md#getAllSimAccountInfoList) | Get the list of all SIM card account information. |
| [getAllSimAccountInfoList](arkts-telephony-sim-getallsimaccountinfolist-f-sys.md#getAllSimAccountInfoList-(System-API)) | Get the list of all SIM card account information. |
| [getDsdsMode](arkts-telephony-sim-getdsdsmode-f-sys.md#getDsdsMode) | Obtains the value of dsds mode. |
| [getDsdsMode](arkts-telephony-sim-getdsdsmode-f-sys.md#getDsdsMode-(System-API)) | Obtains the value of dsds mode. |
| [getIMSI](arkts-telephony-sim-getimsi-f-sys.md#getIMSI) | Get the international mobile subscriber ID. |
| [getIMSI](arkts-telephony-sim-getimsi-f-sys.md#getIMSI-(System-API)) | Get the international mobile subscriber ID. |
| [getLockState](arkts-telephony-sim-getlockstate-f-sys.md#getLockState) | Get the lock status of the SIM card in the specified slot. |
| [getLockState](arkts-telephony-sim-getlockstate-f-sys.md#getLockState-(System-API)) | Get the lock status of the SIM card in the specified slot. |
| [getOperatorConfigs](arkts-telephony-sim-getoperatorconfigs-f-sys.md#getOperatorConfigs) | Obtains the operatorconfigs of the SIM card in a specified slot. |
| [getOperatorConfigs](arkts-telephony-sim-getoperatorconfigs-f-sys.md#getOperatorConfigs-(System-API)) | Obtains the operatorconfigs of the SIM card in a specified slot. |
| [getShowName](arkts-telephony-sim-getshowname-f-sys.md#getShowName) | Gets the name of the SIM card in the specified slot. |
| [getShowName](arkts-telephony-sim-getshowname-f-sys.md#getShowName-(System-API)) | Gets the name of the SIM card in the specified slot. |
| [getShowNumber](arkts-telephony-sim-getshownumber-f-sys.md#getShowNumber) | Get the SIM card number of the specified card slot. |
| [getShowNumber](arkts-telephony-sim-getshownumber-f-sys.md#getShowNumber-(System-API)) | Get the SIM card number of the specified card slot. |
| [getSimAuthentication](arkts-telephony-sim-getsimauthentication-f-sys.md#getSimAuthentication) | Performs SIM card authentication. |
| [getSimGid1](arkts-telephony-sim-getsimgid1-f-sys.md#getSimGid1) | Obtains the Group Identifier Level 1 (GID1) of the SIM card in a specified slot. The GID1 is recorded in the EFGID1 file of the SIM card. |
| [getSimGid1](arkts-telephony-sim-getsimgid1-f-sys.md#getSimGid1-(System-API)) | Obtains the Group Identifier Level 1 (GID1) of the SIM card in a specified slot. The GID1 is recorded in the EFGID1 file of the SIM card. |
| [getSimIccId](arkts-telephony-sim-getsimiccid-f-sys.md#getSimIccId) | Obtains the ICCID of the SIM card in a specified slot. &lt;p&gt;The ICCID is a unique identifier of a SIM card. It consists of 20 digits and is recorded in the EFICCID file of the SIM card. |
| [getSimIccId](arkts-telephony-sim-getsimiccid-f-sys.md#getSimIccId-(System-API)) | Obtains the ICCID of the SIM card in a specified slot. &lt;p&gt;The ICCID is a unique identifier of a SIM card. It consists of 20 digits and is recorded in the EFICCID file of the SIM card. |
| [getSimTelephoneNumber](arkts-telephony-sim-getsimtelephonenumber-f-sys.md#getSimTelephoneNumber) | Obtains the MSISDN of the SIM card in a specified slot. The MSISDN is recorded in the EFMSISDN file of the SIM card. |
| [getSimTelephoneNumber](arkts-telephony-sim-getsimtelephonenumber-f-sys.md#getSimTelephoneNumber-(System-API)) | Obtains the MSISDN of the SIM card in a specified slot. The MSISDN is recorded in the EFMSISDN file of the SIM card. |
| [getVoiceMailIdentifier](arkts-telephony-sim-getvoicemailidentifier-f-sys.md#getVoiceMailIdentifier) | Obtains the alpha identifier of the voice mailbox of the SIM card in a specified slot. |
| [getVoiceMailIdentifier](arkts-telephony-sim-getvoicemailidentifier-f-sys.md#getVoiceMailIdentifier-(System-API)) | Obtains the alpha identifier of the voice mailbox of the SIM card in a specified slot. |
| [getVoiceMailNumber](arkts-telephony-sim-getvoicemailnumber-f-sys.md#getVoiceMailNumber) | Obtains the voice mailbox number of the SIM card in a specified slot. |
| [getVoiceMailNumber](arkts-telephony-sim-getvoicemailnumber-f-sys.md#getVoiceMailNumber-(System-API)) | Obtains the voice mailbox number of the SIM card in a specified slot. |
| [isOperatorSimCard](arkts-telephony-sim-isoperatorsimcard-f-sys.md#isOperatorSimCard) | Indicates whether the SIM card in a specified slot is a specified operator. |
| [queryIccDiallingNumbers](arkts-telephony-sim-queryiccdiallingnumbers-f-sys.md#queryIccDiallingNumbers) | Query dialing number information on SIM card. |
| [queryIccDiallingNumbers](arkts-telephony-sim-queryiccdiallingnumbers-f-sys.md#queryIccDiallingNumbers-(System-API)) | Query dialing number information on SIM card. |
| [sendEnvelopeCmd](arkts-telephony-sim-sendenvelopecmd-f-sys.md#sendEnvelopeCmd) | Send envelope command to SIM card. |
| [sendEnvelopeCmd](arkts-telephony-sim-sendenvelopecmd-f-sys.md#sendEnvelopeCmd-(System-API)) | Send envelope command to SIM card. |
| [sendTerminalResponseCmd](arkts-telephony-sim-sendterminalresponsecmd-f-sys.md#sendTerminalResponseCmd) | Send terminal response command to SIM card. |
| [sendTerminalResponseCmd](arkts-telephony-sim-sendterminalresponsecmd-f-sys.md#sendTerminalResponseCmd-(System-API)) | Send terminal response command to SIM card. |
| [setDefaultVoiceSlotId](arkts-telephony-sim-setdefaultvoiceslotid-f-sys.md#setDefaultVoiceSlotId) | Set the card slot ID of the default voice service. |
| [setDefaultVoiceSlotId](arkts-telephony-sim-setdefaultvoiceslotid-f-sys.md#setDefaultVoiceSlotId-(System-API)) | Set the card slot ID of the default voice service. |
| [setLockState](arkts-telephony-sim-setlockstate-f-sys.md#setLockState) | Set the lock status of the SIM card in the specified slot. |
| [setLockState](arkts-telephony-sim-setlockstate-f-sys.md#setLockState-(System-API)) | Set the lock status of the SIM card in the specified slot. |
| [setShowName](arkts-telephony-sim-setshowname-f-sys.md#setShowName) | Set the SIM card display name of the specified card slot. |
| [setShowName](arkts-telephony-sim-setshowname-f-sys.md#setShowName-(System-API)) | Set the SIM card display name of the specified card slot. |
| [setShowNumber](arkts-telephony-sim-setshownumber-f-sys.md#setShowNumber) | Set the SIM card number in the specified slot. |
| [setShowNumber](arkts-telephony-sim-setshownumber-f-sys.md#setShowNumber-(System-API)) | Set the SIM card number in the specified slot. |
| [setSimLabelIndex](arkts-telephony-sim-setsimlabelindex-f-sys.md#setSimLabelIndex) | Set the SIM card labelIndex. |
| [setVoiceMailInfo](arkts-telephony-sim-setvoicemailinfo-f-sys.md#setVoiceMailInfo) | Sets the voice mail information. |
| [setVoiceMailInfo](arkts-telephony-sim-setvoicemailinfo-f-sys.md#setVoiceMailInfo-(System-API)) | Sets the voice mail information. |
| [unlockPin](arkts-telephony-sim-unlockpin-f-sys.md#unlockPin) | Unlock the SIM card password of the specified card slot. |
| [unlockPin](arkts-telephony-sim-unlockpin-f-sys.md#unlockPin-(System-API)) | Unlock the SIM card password of the specified card slot. |
| [unlockPin2](arkts-telephony-sim-unlockpin2-f-sys.md#unlockPin2) | Unlock the SIM card password of the specified card slot. |
| [unlockPin2](arkts-telephony-sim-unlockpin2-f-sys.md#unlockPin2-(System-API)) | Unlock the SIM card password of the specified card slot. |
| [unlockPuk](arkts-telephony-sim-unlockpuk-f-sys.md#unlockPuk) | Unlock the SIM card password in the specified card slot. |
| [unlockPuk](arkts-telephony-sim-unlockpuk-f-sys.md#unlockPuk-(System-API)) | Unlock the SIM card password in the specified card slot. |
| [unlockPuk2](arkts-telephony-sim-unlockpuk2-f-sys.md#unlockPuk2) | Unlock the SIM card password in the specified card slot. |
| [unlockPuk2](arkts-telephony-sim-unlockpuk2-f-sys.md#unlockPuk2-(System-API)) | Unlock the SIM card password in the specified card slot. |
| [unlockSimLock](arkts-telephony-sim-unlocksimlock-f-sys.md#unlockSimLock) | Unlock SIM card. |
| [unlockSimLock](arkts-telephony-sim-unlocksimlock-f-sys.md#unlockSimLock-(System-API)) | Unlock SIM card. |
| [updateIccDiallingNumbers](arkts-telephony-sim-updateiccdiallingnumbers-f-sys.md#updateIccDiallingNumbers) | Update dialing number information on SIM card. |
| [updateIccDiallingNumbers](arkts-telephony-sim-updateiccdiallingnumbers-f-sys.md#updateIccDiallingNumbers-(System-API)) | Update dialing number information on SIM card. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [IccAccountInfo](arkts-telephony-sim-iccaccountinfo-i.md) | Defines the ICC account information. |
| [SimLabel](arkts-telephony-sim-simlabel-i.md) | Defines the SIM card label. |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [DiallingNumbersInfo](arkts-telephony-sim-diallingnumbersinfo-i-sys.md) | Defines the contact number information. |
| [IccAccountInfo](arkts-telephony-sim-iccaccountinfo-i-sys.md) | Defines the ICC account information. |
| [LockInfo](arkts-telephony-sim-lockinfo-i-sys.md) | Defines the personalized lock information. |
| [LockStatusResponse](arkts-telephony-sim-lockstatusresponse-i-sys.md) | Defines the personalized lock information. |
| [OperatorConfig](arkts-telephony-sim-operatorconfig-i-sys.md) | Defines the carrier configuration. |
| [PersoLockInfo](arkts-telephony-sim-persolockinfo-i-sys.md) | Defines the personalized lock information. |
| [SimAuthenticationResponse](arkts-telephony-sim-simauthenticationresponse-i-sys.md) | Defines the SIM card authentication response. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [CardType](arkts-telephony-sim-cardtype-e.md) | Indicates the SIM card types. |
| [SimState](arkts-telephony-sim-simstate-e.md) | Indicates the SIM card states. |
| [SimType](arkts-telephony-sim-simtype-e.md) | Indicates the SIM card type. |

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [AuthType](arkts-telephony-sim-authtype-e-sys.md) | Indicates the Authentication type |
| [ContactType](arkts-telephony-sim-contacttype-e-sys.md) | Indicates the contact types. |
| [DsdsMode](arkts-telephony-sim-dsdsmode-e-sys.md) | Indicates the Dsds Mode. |
| [LockState](arkts-telephony-sim-lockstate-e-sys.md) | Indicates the lock states. |
| [LockType](arkts-telephony-sim-locktype-e-sys.md) | Indicates the lock types. |
| [OperatorConfigKey](arkts-telephony-sim-operatorconfigkey-e-sys.md) | Indicates the carrier configuration keys. |
| [OperatorSimCard](arkts-telephony-sim-operatorsimcard-e-sys.md) | Indicates the operator of SIM. |
| [PersoLockType](arkts-telephony-sim-persolocktype-e-sys.md) | Indicates the personalized lock types. |
<!--DelEnd-->

