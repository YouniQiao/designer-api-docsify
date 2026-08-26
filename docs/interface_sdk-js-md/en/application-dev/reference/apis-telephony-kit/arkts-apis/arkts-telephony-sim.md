# @ohos.telephony.sim(SIM Management)

The **sim** module provides basic SIM card management functions. With the APIs provided by this module, you can obtain the ISO country code, home PLMN ID, service provider name, SIM card status, type, installation status, and activation status of the SIM card in the specified slot.

**Since:** 6

**System capability:** SystemCapability.Telephony.CoreService

## Modules to Import

```TypeScript
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getActiveSimAccountInfoList(SIM Management)](arkts-telephony-sim-getactivesimaccountinfolist-f.md) | Obtains the list of activated SIM card accounts. This API uses an asynchronous callback to return the result.  **Required permission**: ohos.permission.GET_TELEPHONY_STATE |
| [getActiveSimAccountInfoList(SIM Management)](arkts-telephony-sim-getactivesimaccountinfolist-f.md) | Obtains the list of activated SIM card accounts. This API uses a promise to return the result.  **Required permission**: ohos.permission.GET_TELEPHONY_STATE |
| [getCardType(SIM Management)](arkts-telephony-sim-getcardtype-f.md) | Obtains the type of the SIM card in the specified slot. This API uses an asynchronous callback to return the result. |
| [getCardType(SIM Management)](arkts-telephony-sim-getcardtype-f.md) | Obtains the type of the SIM card in the specified slot. This API uses a promise to return the result. |
| [getCardTypeSync(SIM Management)](arkts-telephony-sim-getcardtypesync-f.md) | Obtains the type of the SIM card in the specified slot. |
| [getDefaultVoiceSimId(SIM Management)](arkts-telephony-sim-getdefaultvoicesimid-f.md) | Obtains the default slot ID of the SIM card that provides voice services. This API uses an asynchronous callback to return the result. |
| [getDefaultVoiceSimId(SIM Management)](arkts-telephony-sim-getdefaultvoicesimid-f.md) | Obtains the default slot ID of the SIM card that provides voice services. This API uses a promise to return the result. |
| [getDefaultVoiceSlotId(SIM Management)](arkts-telephony-sim-getdefaultvoiceslotid-f.md) | Obtains the default slot ID of the SIM card that provides voice services. This API uses an asynchronous callback to return the result. |
| [getDefaultVoiceSlotId(SIM Management)](arkts-telephony-sim-getdefaultvoiceslotid-f.md) | Obtains the default slot ID of the SIM card that provides voice services. This API uses a promise to return the result. |
| [getISOCountryCodeForSim(SIM Management)](arkts-telephony-sim-getisocountrycodeforsim-f.md) | Obtains the ISO country code of the SIM card in the specified slot. This API uses an asynchronous callback to return the result. |
| [getISOCountryCodeForSim(SIM Management)](arkts-telephony-sim-getisocountrycodeforsim-f.md) | Obtains the ISO country code of the SIM card in the specified slot. This API uses a promise to return the result. |
| [getISOCountryCodeForSimSync(SIM Management)](arkts-telephony-sim-getisocountrycodeforsimsync-f.md) | Obtains the ISO country code of the SIM card in the specified slot. |
| [getMaxSimCount(SIM Management)](arkts-telephony-sim-getmaxsimcount-f.md) | Obtains the number of card slots. |
| [getOpKey(SIM Management)](arkts-telephony-sim-getopkey-f.md) | Obtains the opkey of the SIM card in the specified slot. This API uses an asynchronous callback to return the result. |
| [getOpKey(SIM Management)](arkts-telephony-sim-getopkey-f.md) | Obtains the opkey of the SIM card in the specified slot. This API uses a promise to return the result. |
| [getOpKeySync(SIM Management)](arkts-telephony-sim-getopkeysync-f.md) | Obtains the opkey of the SIM card in the specified slot. |
| [getOpName(SIM Management)](arkts-telephony-sim-getopname-f.md) | Obtains the OpName of the SIM card in the specified slot. This API uses an asynchronous callback to return the result. |
| [getOpName(SIM Management)](arkts-telephony-sim-getopname-f.md) | Obtains the OpName of the SIM card in the specified slot. This API uses a promise to return the result. |
| [getOpNameSync(SIM Management)](arkts-telephony-sim-getopnamesync-f.md) | Obtains the OpName of the SIM card in the specified slot. |
| [getSimAccountInfo(SIM Management)](arkts-telephony-sim-getsimaccountinfo-f.md) | Obtains SIM card account information. This API uses an asynchronous callback to return the result.  **Required permission**: ohos.permission.GET_TELEPHONY_STATE |
| [getSimAccountInfo(SIM Management)](arkts-telephony-sim-getsimaccountinfo-f.md) | Obtains SIM card account information. This API uses a promise to return the result.  **Required permission**: ohos.permission.GET_TELEPHONY_STATE |
| [getSimLabel(SIM Management)](arkts-telephony-sim-getsimlabel-f.md) | Checks the mapping between card slot IDs and SIM cards.  - Slot 1 corresponds to SIM card 1 or SIM card 2.  - Slot 2 corresponds to SIM card 2 or eSIMX. |
| [getSimLabel(SIM Management)](arkts-telephony-sim-getsimlabel-f.md) | Obtains the SIM card label. This API uses a promise to return the result. |
| [getSimLabelSync(SIM Management)](arkts-telephony-sim-getsimlabelsync-f.md) | Obtains the SIM card label based on the specified SIM card slot ID. |
| [getSimOperatorNumeric(SIM Management)](arkts-telephony-sim-getsimoperatornumeric-f.md) | Obtains the home public land mobile network (PLMN) ID of the SIM card in the specified slot. This API uses an asynchronous callback to return the result. |
| [getSimOperatorNumeric(SIM Management)](arkts-telephony-sim-getsimoperatornumeric-f.md) | Obtains the home PLMN ID of the SIM card in the specified slot. This API uses a promise to return the result. |
| [getSimOperatorNumericSync(SIM Management)](arkts-telephony-sim-getsimoperatornumericsync-f.md) | Obtains the home PLMN ID of the SIM card in the specified slot. This API returns the result synchronously. |
| [getSimSpn(SIM Management)](arkts-telephony-sim-getsimspn-f.md) | Obtains the service provider name (SPN) of the SIM card in the specified slot. This API uses an asynchronous callback to return the result. |
| [getSimSpn(SIM Management)](arkts-telephony-sim-getsimspn-f.md) | Obtains the SPN of the SIM card in the specified slot. This API uses a promise to return the result. |
| [getSimSpnSync(SIM Management)](arkts-telephony-sim-getsimspnsync-f.md) | Obtains the SPN of the SIM card in the specified slot. This API returns the result synchronously. |
| [getSimState(SIM Management)](arkts-telephony-sim-getsimstate-f.md) | Obtains the state of the SIM card in the specified slot. This API uses an asynchronous callback to return the result. |
| [getSimState(SIM Management)](arkts-telephony-sim-getsimstate-f.md) | Obtains the state of the SIM card in the specified slot. This API uses a promise to return the result. |
| [getSimStateSync(SIM Management)](arkts-telephony-sim-getsimstatesync-f.md) | Obtains the state of the SIM card in the specified slot. |
| [hasOperatorPrivileges(SIM Management)](arkts-telephony-sim-hasoperatorprivileges-f.md) | Checks whether the application (caller) has been granted the operator permission. This API uses an asynchronous callback to return the result. |
| [hasOperatorPrivileges(SIM Management)](arkts-telephony-sim-hasoperatorprivileges-f.md) | Checks whether the application (caller) has been granted the operator permission. This API uses a promise to return the result. |
| [hasSimCard(SIM Management)](arkts-telephony-sim-hassimcard-f.md) | Checks whether the SIM card in the specified slot is installed. This API uses an asynchronous callback to return the result. |
| [hasSimCard(SIM Management)](arkts-telephony-sim-hassimcard-f.md) | Checks whether the SIM card in the specified slot is installed. This API uses a promise to return the result. |
| [hasSimCardSync(SIM Management)](arkts-telephony-sim-hassimcardsync-f.md) | Checks whether the SIM card in the specified slot is installed. |
| [isSimActive(SIM Management)](arkts-telephony-sim-issimactive-f.md) | Checks whether the SIM card in the specified slot is activated. This API uses an asynchronous callback to return the result. |
| [isSimActive(SIM Management)](arkts-telephony-sim-issimactive-f.md) | Checks whether the SIM card in the specified slot is activated. This API uses a promise to return the result. |
| [isSimActiveSync(SIM Management)](arkts-telephony-sim-issimactivesync-f.md) | Checks whether the SIM card in the specified slot is activated. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [activateSim(SIM Management)](arkts-telephony-sim-activatesim-f-sys.md) | Activate the SIM card in the specified slot. |
| [activateSim(SIM Management)](arkts-telephony-sim-activatesim-f-sys.md) | Activate the SIM card in the specified slot. |
| [addIccDiallingNumbers(SIM Management)](arkts-telephony-sim-addiccdiallingnumbers-f-sys.md) | Add dialing number information to SIM card. |
| [addIccDiallingNumbers(SIM Management)](arkts-telephony-sim-addiccdiallingnumbers-f-sys.md) | Add dialing number information to SIM card. |
| [alterPin(SIM Management)](arkts-telephony-sim-alterpin-f-sys.md) | Change Pin Password. |
| [alterPin(SIM Management)](arkts-telephony-sim-alterpin-f-sys.md) | Change Pin Password. |
| [alterPin2(SIM Management)](arkts-telephony-sim-alterpin2-f-sys.md) | Change Pin2 password. |
| [alterPin2(SIM Management)](arkts-telephony-sim-alterpin2-f-sys.md) | Change Pin2 password. |
| [deactivateSim(SIM Management)](arkts-telephony-sim-deactivatesim-f-sys.md) | Disable SIM card in specified slot. |
| [deactivateSim(SIM Management)](arkts-telephony-sim-deactivatesim-f-sys.md) | Disable SIM card in specified slot. |
| [delIccDiallingNumbers(SIM Management)](arkts-telephony-sim-deliccdiallingnumbers-f-sys.md) | Delete dialing number information on SIM card. |
| [delIccDiallingNumbers(SIM Management)](arkts-telephony-sim-deliccdiallingnumbers-f-sys.md) | Delete dialing number information on SIM card. |
| [getAllSimAccountInfoList(SIM Management)](arkts-telephony-sim-getallsimaccountinfolist-f-sys.md) | Get the list of all SIM card account information. |
| [getAllSimAccountInfoList(SIM Management)](arkts-telephony-sim-getallsimaccountinfolist-f-sys.md) | Get the list of all SIM card account information. |
| [getDsdsMode(SIM Management)](arkts-telephony-sim-getdsdsmode-f-sys.md) | Obtains the value of dsds mode. |
| [getDsdsMode(SIM Management)](arkts-telephony-sim-getdsdsmode-f-sys.md) | Obtains the value of dsds mode. |
| [getIMSI(SIM Management)](arkts-telephony-sim-getimsi-f-sys.md) | Get the international mobile subscriber ID. |
| [getIMSI(SIM Management)](arkts-telephony-sim-getimsi-f-sys.md) | Get the international mobile subscriber ID. |
| [getLockState(SIM Management)](arkts-telephony-sim-getlockstate-f-sys.md) | Get the lock status of the SIM card in the specified slot. |
| [getLockState(SIM Management)](arkts-telephony-sim-getlockstate-f-sys.md) | Get the lock status of the SIM card in the specified slot. |
| [getOperatorConfigs(SIM Management)](arkts-telephony-sim-getoperatorconfigs-f-sys.md) | Obtains the operatorconfigs of the SIM card in a specified slot. |
| [getOperatorConfigs(SIM Management)](arkts-telephony-sim-getoperatorconfigs-f-sys.md) | Obtains the operatorconfigs of the SIM card in a specified slot. |
| [getShowName(SIM Management)](arkts-telephony-sim-getshowname-f-sys.md) | Gets the name of the SIM card in the specified slot. |
| [getShowName(SIM Management)](arkts-telephony-sim-getshowname-f-sys.md) | Gets the name of the SIM card in the specified slot. |
| [getShowNumber(SIM Management)](arkts-telephony-sim-getshownumber-f-sys.md) | Get the SIM card number of the specified card slot. |
| [getShowNumber(SIM Management)](arkts-telephony-sim-getshownumber-f-sys.md) | Get the SIM card number of the specified card slot. |
| [getSimAuthentication(SIM Management)](arkts-telephony-sim-getsimauthentication-f-sys.md) | Performs SIM card authentication. |
| [getSimGid1(SIM Management)](arkts-telephony-sim-getsimgid1-f-sys.md) | Obtains the Group Identifier Level 1 (GID1) of the SIM card in a specified slot. The GID1 is recorded in the EFGID1 file of the SIM card. |
| [getSimGid1(SIM Management)](arkts-telephony-sim-getsimgid1-f-sys.md) | Obtains the Group Identifier Level 1 (GID1) of the SIM card in a specified slot. The GID1 is recorded in the EFGID1 file of the SIM card. |
| [getSimIccId(SIM Management)](arkts-telephony-sim-getsimiccid-f-sys.md) | Obtains the ICCID of the SIM card in a specified slot. & lt;p & gt;The ICCID is a unique identifier of a SIM card. It consists of 20 digits and is recorded in the EFICCID file of the SIM card. |
| [getSimIccId(SIM Management)](arkts-telephony-sim-getsimiccid-f-sys.md) | Obtains the ICCID of the SIM card in a specified slot. & lt;p & gt;The ICCID is a unique identifier of a SIM card. It consists of 20 digits and is recorded in the EFICCID file of the SIM card. |
| [getSimTelephoneNumber(SIM Management)](arkts-telephony-sim-getsimtelephonenumber-f-sys.md) | Obtains the MSISDN of the SIM card in a specified slot. The MSISDN is recorded in the EFMSISDN file of the SIM card. |
| [getSimTelephoneNumber(SIM Management)](arkts-telephony-sim-getsimtelephonenumber-f-sys.md) | Obtains the MSISDN of the SIM card in a specified slot. The MSISDN is recorded in the EFMSISDN file of the SIM card. |
| [getVoiceMailIdentifier(SIM Management)](arkts-telephony-sim-getvoicemailidentifier-f-sys.md) | Obtains the alpha identifier of the voice mailbox of the SIM card in a specified slot. |
| [getVoiceMailIdentifier(SIM Management)](arkts-telephony-sim-getvoicemailidentifier-f-sys.md) | Obtains the alpha identifier of the voice mailbox of the SIM card in a specified slot. |
| [getVoiceMailNumber(SIM Management)](arkts-telephony-sim-getvoicemailnumber-f-sys.md) | Obtains the voice mailbox number of the SIM card in a specified slot. |
| [getVoiceMailNumber(SIM Management)](arkts-telephony-sim-getvoicemailnumber-f-sys.md) | Obtains the voice mailbox number of the SIM card in a specified slot. |
| [isOperatorSimCard(SIM Management)](arkts-telephony-sim-isoperatorsimcard-f-sys.md) | Indicates whether the SIM card in a specified slot is a specified operator. |
| [queryIccDiallingNumbers(SIM Management)](arkts-telephony-sim-queryiccdiallingnumbers-f-sys.md) | Query dialing number information on SIM card. |
| [queryIccDiallingNumbers(SIM Management)](arkts-telephony-sim-queryiccdiallingnumbers-f-sys.md) | Query dialing number information on SIM card. |
| [sendEnvelopeCmd(SIM Management)](arkts-telephony-sim-sendenvelopecmd-f-sys.md) | Send envelope command to SIM card. |
| [sendEnvelopeCmd(SIM Management)](arkts-telephony-sim-sendenvelopecmd-f-sys.md) | Send envelope command to SIM card. |
| [sendTerminalResponseCmd(SIM Management)](arkts-telephony-sim-sendterminalresponsecmd-f-sys.md) | Send terminal response command to SIM card. |
| [sendTerminalResponseCmd(SIM Management)](arkts-telephony-sim-sendterminalresponsecmd-f-sys.md) | Send terminal response command to SIM card. |
| [setDefaultVoiceSlotId(SIM Management)](arkts-telephony-sim-setdefaultvoiceslotid-f-sys.md) | Set the card slot ID of the default voice service. |
| [setDefaultVoiceSlotId(SIM Management)](arkts-telephony-sim-setdefaultvoiceslotid-f-sys.md) | Set the card slot ID of the default voice service. |
| [setLockState(SIM Management)](arkts-telephony-sim-setlockstate-f-sys.md) | Set the lock status of the SIM card in the specified slot. |
| [setLockState(SIM Management)](arkts-telephony-sim-setlockstate-f-sys.md) | Set the lock status of the SIM card in the specified slot. |
| [setShowName(SIM Management)](arkts-telephony-sim-setshowname-f-sys.md) | Set the SIM card display name of the specified card slot. |
| [setShowName(SIM Management)](arkts-telephony-sim-setshowname-f-sys.md) | Set the SIM card display name of the specified card slot. |
| [setShowNumber(SIM Management)](arkts-telephony-sim-setshownumber-f-sys.md) | Set the SIM card number in the specified slot. |
| [setShowNumber(SIM Management)](arkts-telephony-sim-setshownumber-f-sys.md) | Set the SIM card number in the specified slot. |
| [setSimLabelIndex(SIM Management)](arkts-telephony-sim-setsimlabelindex-f-sys.md) | Set the SIM card labelIndex. |
| [setVoiceMailInfo(SIM Management)](arkts-telephony-sim-setvoicemailinfo-f-sys.md) | Sets the voice mail information. |
| [setVoiceMailInfo(SIM Management)](arkts-telephony-sim-setvoicemailinfo-f-sys.md) | Sets the voice mail information. |
| [unlockPin(SIM Management)](arkts-telephony-sim-unlockpin-f-sys.md) | Unlock the SIM card password of the specified card slot. |
| [unlockPin(SIM Management)](arkts-telephony-sim-unlockpin-f-sys.md) | Unlock the SIM card password of the specified card slot. |
| [unlockPin2(SIM Management)](arkts-telephony-sim-unlockpin2-f-sys.md) | Unlock the SIM card password of the specified card slot. |
| [unlockPin2(SIM Management)](arkts-telephony-sim-unlockpin2-f-sys.md) | Unlock the SIM card password of the specified card slot. |
| [unlockPuk(SIM Management)](arkts-telephony-sim-unlockpuk-f-sys.md) | Unlock the SIM card password in the specified card slot. |
| [unlockPuk(SIM Management)](arkts-telephony-sim-unlockpuk-f-sys.md) | Unlock the SIM card password in the specified card slot. |
| [unlockPuk2(SIM Management)](arkts-telephony-sim-unlockpuk2-f-sys.md) | Unlock the SIM card password in the specified card slot. |
| [unlockPuk2(SIM Management)](arkts-telephony-sim-unlockpuk2-f-sys.md) | Unlock the SIM card password in the specified card slot. |
| [unlockSimLock(SIM Management)](arkts-telephony-sim-unlocksimlock-f-sys.md) | Unlock SIM card. |
| [unlockSimLock(SIM Management)](arkts-telephony-sim-unlocksimlock-f-sys.md) | Unlock SIM card. |
| [updateIccDiallingNumbers(SIM Management)](arkts-telephony-sim-updateiccdiallingnumbers-f-sys.md) | Update dialing number information on SIM card. |
| [updateIccDiallingNumbers(SIM Management)](arkts-telephony-sim-updateiccdiallingnumbers-f-sys.md) | Update dialing number information on SIM card. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [IccAccountInfo(SIM Management)](arkts-telephony-sim-iccaccountinfo-i.md) | Defines the ICC account information. |
| [SimLabel(SIM Management)](arkts-telephony-sim-simlabel-i.md) | Defines the SIM card label. |

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [DiallingNumbersInfo(SIM Management)](arkts-telephony-sim-diallingnumbersinfo-i-sys.md) | Defines the contact number information. |
| [IccAccountInfo(SIM Management)](arkts-telephony-sim-iccaccountinfo-i-sys.md) | Defines the ICC account information. |
| [LockInfo(SIM Management)](arkts-telephony-sim-lockinfo-i-sys.md) | Defines the personalized lock information. |
| [LockStatusResponse(SIM Management)](arkts-telephony-sim-lockstatusresponse-i-sys.md) | Defines the personalized lock information. |
| [OperatorConfig(SIM Management)](arkts-telephony-sim-operatorconfig-i-sys.md) | Defines the carrier configuration. |
| [PersoLockInfo(SIM Management)](arkts-telephony-sim-persolockinfo-i-sys.md) | Defines the personalized lock information. |
| [SimAuthenticationResponse(SIM Management)](arkts-telephony-sim-simauthenticationresponse-i-sys.md) | Defines the SIM card authentication response. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [CardType(SIM Management)](arkts-telephony-sim-cardtype-e.md) | Enumerates SIM card types. |
| [SimState(SIM Management)](arkts-telephony-sim-simstate-e.md) | Enumerates SIM card states. |
| [SimType(SIM Management)](arkts-telephony-sim-simtype-e.md) | Enumerates the SIM card types. |

<!--Del-->
### Enums(System API)

| Name | Description |
| --- | --- |
| [AuthType(SIM Management)](arkts-telephony-sim-authtype-e-sys.md) | Indicates the Authentication type |
| [ContactType(SIM Management)](arkts-telephony-sim-contacttype-e-sys.md) | Indicates the contact types. |
| [DsdsMode(SIM Management)](arkts-telephony-sim-dsdsmode-e-sys.md) | Indicates the Dsds Mode. |
| [LockState(SIM Management)](arkts-telephony-sim-lockstate-e-sys.md) | Indicates the lock states. |
| [LockType(SIM Management)](arkts-telephony-sim-locktype-e-sys.md) | Indicates the lock types. |
| [OperatorConfigKey(SIM Management)](arkts-telephony-sim-operatorconfigkey-e-sys.md) | Indicates the carrier configuration keys. |
| [OperatorSimCard(SIM Management)](arkts-telephony-sim-operatorsimcard-e-sys.md) | Indicates the operator of SIM. |
| [PersoLockType(SIM Management)](arkts-telephony-sim-persolocktype-e-sys.md) | Indicates the personalized lock types. |
<!--DelEnd-->
