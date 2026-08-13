# @ohos.telephony.sim

Provides applications with APIs for obtaining SIM card status, card file information, and card specifications. SIM cards include SIM, USIM, and CSIM cards.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare namespace sim--><!--Device-unnamed-declare namespace sim-End-->

**System capability:** SystemCapability.Telephony.CoreService

## Modules to Import

```TypeScript
import { sim } from '@kit.TelephonyKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getActiveSimAccountInfoList](arkts-telephony-sim-getactivesimaccountinfolist-f.md#getActiveSimAccountInfoList) |
| [getActiveSimAccountInfoList](arkts-telephony-sim-getactivesimaccountinfolist-f.md#getActiveSimAccountInfoList) |
| [getCardType](arkts-telephony-sim-getcardtype-f.md#getCardType) |
| [getCardType](arkts-telephony-sim-getcardtype-f.md#getCardType) |
| [getCardTypeSync](arkts-telephony-sim-getcardtypesync-f.md#getCardTypeSync) |
| [getDefaultVoiceSimId](arkts-telephony-sim-getdefaultvoicesimid-f.md#getDefaultVoiceSimId) |
| [getDefaultVoiceSimId](arkts-telephony-sim-getdefaultvoicesimid-f.md#getDefaultVoiceSimId) |
| [getDefaultVoiceSlotId](arkts-telephony-sim-getdefaultvoiceslotid-f.md#getDefaultVoiceSlotId) |
| [getDefaultVoiceSlotId](arkts-telephony-sim-getdefaultvoiceslotid-f.md#getDefaultVoiceSlotId) |
| [getISOCountryCodeForSim](arkts-telephony-sim-getisocountrycodeforsim-f.md#getISOCountryCodeForSim) |
| [getISOCountryCodeForSim](arkts-telephony-sim-getisocountrycodeforsim-f.md#getISOCountryCodeForSim) |
| [getISOCountryCodeForSimSync](arkts-telephony-sim-getisocountrycodeforsimsync-f.md#getISOCountryCodeForSimSync) |
| [getMaxSimCount](arkts-telephony-sim-getmaxsimcount-f.md#getMaxSimCount) |
| [getOpKey](arkts-telephony-sim-getopkey-f.md#getOpKey) |
| [getOpKey](arkts-telephony-sim-getopkey-f.md#getOpKey) |
| [getOpKeySync](arkts-telephony-sim-getopkeysync-f.md#getOpKeySync) |
| [getOpName](arkts-telephony-sim-getopname-f.md#getOpName) |
| [getOpName](arkts-telephony-sim-getopname-f.md#getOpName) |
| [getOpNameSync](arkts-telephony-sim-getopnamesync-f.md#getOpNameSync) |
| [getSimAccountInfo](arkts-telephony-sim-getsimaccountinfo-f.md#getSimAccountInfo) |
| [getSimAccountInfo](arkts-telephony-sim-getsimaccountinfo-f.md#getSimAccountInfo) |
| [getSimLabel](arkts-telephony-sim-getsimlabel-f.md#getSimLabel) |
| [getSimLabel](arkts-telephony-sim-getsimlabel-f.md#getSimLabel) |
| [getSimLabelSync](arkts-telephony-sim-getsimlabelsync-f.md#getSimLabelSync) |
| [getSimOperatorNumeric](arkts-telephony-sim-getsimoperatornumeric-f.md#getSimOperatorNumeric) |
| [getSimOperatorNumeric](arkts-telephony-sim-getsimoperatornumeric-f.md#getSimOperatorNumeric) |
| [getSimOperatorNumericSync](arkts-telephony-sim-getsimoperatornumericsync-f.md#getSimOperatorNumericSync) |
| [getSimSpn](arkts-telephony-sim-getsimspn-f.md#getSimSpn) |
| [getSimSpn](arkts-telephony-sim-getsimspn-f.md#getSimSpn) |
| [getSimSpnSync](arkts-telephony-sim-getsimspnsync-f.md#getSimSpnSync) |
| [getSimState](arkts-telephony-sim-getsimstate-f.md#getSimState) |
| [getSimState](arkts-telephony-sim-getsimstate-f.md#getSimState) |
| [getSimStateSync](arkts-telephony-sim-getsimstatesync-f.md#getSimStateSync) |
| [hasOperatorPrivileges](arkts-telephony-sim-hasoperatorprivileges-f.md#hasOperatorPrivileges) |
| [hasOperatorPrivileges](arkts-telephony-sim-hasoperatorprivileges-f.md#hasOperatorPrivileges) |
| [hasSimCard](arkts-telephony-sim-hassimcard-f.md#hasSimCard) |
| [hasSimCard](arkts-telephony-sim-hassimcard-f.md#hasSimCard) |
| [hasSimCardSync](arkts-telephony-sim-hassimcardsync-f.md#hasSimCardSync) |
| [isSimActive](arkts-telephony-sim-issimactive-f.md#isSimActive) |
| [isSimActive](arkts-telephony-sim-issimactive-f.md#isSimActive) |
| [isSimActiveSync](arkts-telephony-sim-issimactivesync-f.md#isSimActiveSync) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [activateSim](arkts-telephony-sim-activatesim-f-sys.md#activateSim-(System-API)) |
| [activateSim](arkts-telephony-sim-activatesim-f-sys.md#activateSim-(System-API)) |
| [addIccDiallingNumbers](arkts-telephony-sim-addiccdiallingnumbers-f-sys.md#addIccDiallingNumbers-(System-API)) |
| [addIccDiallingNumbers](arkts-telephony-sim-addiccdiallingnumbers-f-sys.md#addIccDiallingNumbers-(System-API)) |
| [alterPin](arkts-telephony-sim-alterpin-f-sys.md#alterPin-(System-API)) |
| [alterPin](arkts-telephony-sim-alterpin-f-sys.md#alterPin-(System-API)) |
| [alterPin2](arkts-telephony-sim-alterpin2-f-sys.md#alterPin2-(System-API)) |
| [alterPin2](arkts-telephony-sim-alterpin2-f-sys.md#alterPin2-(System-API)) |
| [deactivateSim](arkts-telephony-sim-deactivatesim-f-sys.md#deactivateSim-(System-API)) |
| [deactivateSim](arkts-telephony-sim-deactivatesim-f-sys.md#deactivateSim-(System-API)) |
| [delIccDiallingNumbers](arkts-telephony-sim-deliccdiallingnumbers-f-sys.md#delIccDiallingNumbers-(System-API)) |
| [delIccDiallingNumbers](arkts-telephony-sim-deliccdiallingnumbers-f-sys.md#delIccDiallingNumbers-(System-API)) |
| [getAllSimAccountInfoList](arkts-telephony-sim-getallsimaccountinfolist-f-sys.md#getAllSimAccountInfoList-(System-API)) |
| [getAllSimAccountInfoList](arkts-telephony-sim-getallsimaccountinfolist-f-sys.md#getAllSimAccountInfoList-(System-API)) |
| [getDsdsMode](arkts-telephony-sim-getdsdsmode-f-sys.md#getDsdsMode-(System-API)) |
| [getDsdsMode](arkts-telephony-sim-getdsdsmode-f-sys.md#getDsdsMode-(System-API)) |
| [getIMSI](arkts-telephony-sim-getimsi-f-sys.md#getIMSI-(System-API)) |
| [getIMSI](arkts-telephony-sim-getimsi-f-sys.md#getIMSI-(System-API)) |
| [getLockState](arkts-telephony-sim-getlockstate-f-sys.md#getLockState-(System-API)) |
| [getLockState](arkts-telephony-sim-getlockstate-f-sys.md#getLockState-(System-API)) |
| [getOperatorConfigs](arkts-telephony-sim-getoperatorconfigs-f-sys.md#getOperatorConfigs-(System-API)) |
| [getOperatorConfigs](arkts-telephony-sim-getoperatorconfigs-f-sys.md#getOperatorConfigs-(System-API)) |
| [getShowName](arkts-telephony-sim-getshowname-f-sys.md#getShowName-(System-API)) |
| [getShowName](arkts-telephony-sim-getshowname-f-sys.md#getShowName-(System-API)) |
| [getShowNumber](arkts-telephony-sim-getshownumber-f-sys.md#getShowNumber-(System-API)) |
| [getShowNumber](arkts-telephony-sim-getshownumber-f-sys.md#getShowNumber-(System-API)) |
| [getSimAuthentication](arkts-telephony-sim-getsimauthentication-f-sys.md#getSimAuthentication-(System-API)) |
| [getSimGid1](arkts-telephony-sim-getsimgid1-f-sys.md#getSimGid1-(System-API)) |
| [getSimGid1](arkts-telephony-sim-getsimgid1-f-sys.md#getSimGid1-(System-API)) |
| [getSimIccId](arkts-telephony-sim-getsimiccid-f-sys.md#getSimIccId-(System-API)) |
| [getSimIccId](arkts-telephony-sim-getsimiccid-f-sys.md#getSimIccId-(System-API)) |
| [getSimTelephoneNumber](arkts-telephony-sim-getsimtelephonenumber-f-sys.md#getSimTelephoneNumber-(System-API)) |
| [getSimTelephoneNumber](arkts-telephony-sim-getsimtelephonenumber-f-sys.md#getSimTelephoneNumber-(System-API)) |
| [getVoiceMailIdentifier](arkts-telephony-sim-getvoicemailidentifier-f-sys.md#getVoiceMailIdentifier-(System-API)) |
| [getVoiceMailIdentifier](arkts-telephony-sim-getvoicemailidentifier-f-sys.md#getVoiceMailIdentifier-(System-API)) |
| [getVoiceMailNumber](arkts-telephony-sim-getvoicemailnumber-f-sys.md#getVoiceMailNumber-(System-API)) |
| [getVoiceMailNumber](arkts-telephony-sim-getvoicemailnumber-f-sys.md#getVoiceMailNumber-(System-API)) |
| [isOperatorSimCard](arkts-telephony-sim-isoperatorsimcard-f-sys.md#isOperatorSimCard-(System-API)) |
| [queryIccDiallingNumbers](arkts-telephony-sim-queryiccdiallingnumbers-f-sys.md#queryIccDiallingNumbers-(System-API)) |
| [queryIccDiallingNumbers](arkts-telephony-sim-queryiccdiallingnumbers-f-sys.md#queryIccDiallingNumbers-(System-API)) |
| [sendEnvelopeCmd](arkts-telephony-sim-sendenvelopecmd-f-sys.md#sendEnvelopeCmd-(System-API)) |
| [sendEnvelopeCmd](arkts-telephony-sim-sendenvelopecmd-f-sys.md#sendEnvelopeCmd-(System-API)) |
| [sendTerminalResponseCmd](arkts-telephony-sim-sendterminalresponsecmd-f-sys.md#sendTerminalResponseCmd-(System-API)) |
| [sendTerminalResponseCmd](arkts-telephony-sim-sendterminalresponsecmd-f-sys.md#sendTerminalResponseCmd-(System-API)) |
| [setDefaultVoiceSlotId](arkts-telephony-sim-setdefaultvoiceslotid-f-sys.md#setDefaultVoiceSlotId-(System-API)) |
| [setDefaultVoiceSlotId](arkts-telephony-sim-setdefaultvoiceslotid-f-sys.md#setDefaultVoiceSlotId-(System-API)) |
| [setLockState](arkts-telephony-sim-setlockstate-f-sys.md#setLockState-(System-API)) |
| [setLockState](arkts-telephony-sim-setlockstate-f-sys.md#setLockState-(System-API)) |
| [setShowName](arkts-telephony-sim-setshowname-f-sys.md#setShowName-(System-API)) |
| [setShowName](arkts-telephony-sim-setshowname-f-sys.md#setShowName-(System-API)) |
| [setShowNumber](arkts-telephony-sim-setshownumber-f-sys.md#setShowNumber-(System-API)) |
| [setShowNumber](arkts-telephony-sim-setshownumber-f-sys.md#setShowNumber-(System-API)) |
| [setSimLabelIndex](arkts-telephony-sim-setsimlabelindex-f-sys.md#setSimLabelIndex-(System-API)) |
| [setVoiceMailInfo](arkts-telephony-sim-setvoicemailinfo-f-sys.md#setVoiceMailInfo-(System-API)) |
| [setVoiceMailInfo](arkts-telephony-sim-setvoicemailinfo-f-sys.md#setVoiceMailInfo-(System-API)) |
| [unlockPin](arkts-telephony-sim-unlockpin-f-sys.md#unlockPin-(System-API)) |
| [unlockPin](arkts-telephony-sim-unlockpin-f-sys.md#unlockPin-(System-API)) |
| [unlockPin2](arkts-telephony-sim-unlockpin2-f-sys.md#unlockPin2-(System-API)) |
| [unlockPin2](arkts-telephony-sim-unlockpin2-f-sys.md#unlockPin2-(System-API)) |
| [unlockPuk](arkts-telephony-sim-unlockpuk-f-sys.md#unlockPuk-(System-API)) |
| [unlockPuk](arkts-telephony-sim-unlockpuk-f-sys.md#unlockPuk-(System-API)) |
| [unlockPuk2](arkts-telephony-sim-unlockpuk2-f-sys.md#unlockPuk2-(System-API)) |
| [unlockPuk2](arkts-telephony-sim-unlockpuk2-f-sys.md#unlockPuk2-(System-API)) |
| [unlockSimLock](arkts-telephony-sim-unlocksimlock-f-sys.md#unlockSimLock-(System-API)) |
| [unlockSimLock](arkts-telephony-sim-unlocksimlock-f-sys.md#unlockSimLock-(System-API)) |
| [updateIccDiallingNumbers](arkts-telephony-sim-updateiccdiallingnumbers-f-sys.md#updateIccDiallingNumbers-(System-API)) |
| [updateIccDiallingNumbers](arkts-telephony-sim-updateiccdiallingnumbers-f-sys.md#updateIccDiallingNumbers-(System-API)) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [IccAccountInfo](arkts-telephony-sim-iccaccountinfo-i.md) |
| [SimLabel](arkts-telephony-sim-simlabel-i.md) |

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DiallingNumbersInfo](arkts-telephony-sim-diallingnumbersinfo-i-sys.md) |
| [IccAccountInfo](arkts-telephony-sim-iccaccountinfo-i-sys.md) |
| [LockInfo](arkts-telephony-sim-lockinfo-i-sys.md) |
| [LockStatusResponse](arkts-telephony-sim-lockstatusresponse-i-sys.md) |
| [OperatorConfig](arkts-telephony-sim-operatorconfig-i-sys.md) |
| [PersoLockInfo](arkts-telephony-sim-persolockinfo-i-sys.md) |
| [SimAuthenticationResponse](arkts-telephony-sim-simauthenticationresponse-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CardType](arkts-telephony-sim-cardtype-e.md) |
| [SimState](arkts-telephony-sim-simstate-e.md) |
| [SimType](arkts-telephony-sim-simtype-e.md) |

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AuthType](arkts-telephony-sim-authtype-e-sys.md) |
| [ContactType](arkts-telephony-sim-contacttype-e-sys.md) |
| [DsdsMode](arkts-telephony-sim-dsdsmode-e-sys.md) |
| [LockState](arkts-telephony-sim-lockstate-e-sys.md) |
| [LockType](arkts-telephony-sim-locktype-e-sys.md) |
| [OperatorConfigKey](arkts-telephony-sim-operatorconfigkey-e-sys.md) |
| [OperatorSimCard](arkts-telephony-sim-operatorsimcard-e-sys.md) |
| [PersoLockType](arkts-telephony-sim-persolocktype-e-sys.md) |
<!--DelEnd-->
