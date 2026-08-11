# @ohos.telephony.sim

Provides applications with APIs for obtaining SIM card status, card file information, and card specifications.SIM cards include SIM, USIM, and CSIM cards.

**Since:** 6

<!--Device-unnamed-declare namespace sim--><!--Device-unnamed-declare namespace sim-End-->

**System capability:** SystemCapability.Telephony.CoreService

## Modules to Import

```TypeScript
import { sim } from 'kits/@kit.TelephonyKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getActiveSimAccountInfoList](arkts-telephony-sim-getactivesimaccountinfolist-f.md#getactivesimaccountinfolist) |
| [getActiveSimAccountInfoList](arkts-telephony-sim-getactivesimaccountinfolist-f.md#getactivesimaccountinfolist-1) |
| [getCardType](arkts-telephony-sim-getcardtype-f.md#getcardtype) |
| [getCardType](arkts-telephony-sim-getcardtype-f.md#getcardtype-1) |
| [getCardTypeSync](arkts-telephony-sim-getcardtypesync-f.md#getcardtypesync) |
| [getDefaultVoiceSimId](arkts-telephony-sim-getdefaultvoicesimid-f.md#getdefaultvoicesimid) |
| [getDefaultVoiceSimId](arkts-telephony-sim-getdefaultvoicesimid-f.md#getdefaultvoicesimid-1) |
| [getDefaultVoiceSlotId](arkts-telephony-sim-getdefaultvoiceslotid-f.md#getdefaultvoiceslotid) |
| [getDefaultVoiceSlotId](arkts-telephony-sim-getdefaultvoiceslotid-f.md#getdefaultvoiceslotid-1) |
| [getISOCountryCodeForSim](arkts-telephony-sim-getisocountrycodeforsim-f.md#getisocountrycodeforsim) |
| [getISOCountryCodeForSim](arkts-telephony-sim-getisocountrycodeforsim-f.md#getisocountrycodeforsim-1) |
| [getISOCountryCodeForSimSync](arkts-telephony-sim-getisocountrycodeforsimsync-f.md#getisocountrycodeforsimsync) |
| [getMaxSimCount](arkts-telephony-sim-getmaxsimcount-f.md#getmaxsimcount) |
| [getOpKey](arkts-telephony-sim-getopkey-f.md#getopkey) |
| [getOpKey](arkts-telephony-sim-getopkey-f.md#getopkey-1) |
| [getOpKeySync](arkts-telephony-sim-getopkeysync-f.md#getopkeysync) |
| [getOpName](arkts-telephony-sim-getopname-f.md#getopname) |
| [getOpName](arkts-telephony-sim-getopname-f.md#getopname-1) |
| [getOpNameSync](arkts-telephony-sim-getopnamesync-f.md#getopnamesync) |
| [getSimAccountInfo](arkts-telephony-sim-getsimaccountinfo-f.md#getsimaccountinfo) |
| [getSimAccountInfo](arkts-telephony-sim-getsimaccountinfo-f.md#getsimaccountinfo-1) |
| [getSimLabel](arkts-telephony-sim-getsimlabel-f.md#getsimlabel) |
| [getSimLabel](arkts-telephony-sim-getsimlabel-f.md#getsimlabel-1) |
| [getSimLabelSync](arkts-telephony-sim-getsimlabelsync-f.md#getsimlabelsync) |
| [getSimOperatorNumeric](arkts-telephony-sim-getsimoperatornumeric-f.md#getsimoperatornumeric) |
| [getSimOperatorNumeric](arkts-telephony-sim-getsimoperatornumeric-f.md#getsimoperatornumeric-1) |
| [getSimOperatorNumericSync](arkts-telephony-sim-getsimoperatornumericsync-f.md#getsimoperatornumericsync) |
| [getSimSpn](arkts-telephony-sim-getsimspn-f.md#getsimspn) |
| [getSimSpn](arkts-telephony-sim-getsimspn-f.md#getsimspn-1) |
| [getSimSpnSync](arkts-telephony-sim-getsimspnsync-f.md#getsimspnsync) |
| [getSimState](arkts-telephony-sim-getsimstate-f.md#getsimstate) |
| [getSimState](arkts-telephony-sim-getsimstate-f.md#getsimstate-1) |
| [getSimStateSync](arkts-telephony-sim-getsimstatesync-f.md#getsimstatesync) |
| [hasOperatorPrivileges](arkts-telephony-sim-hasoperatorprivileges-f.md#hasoperatorprivileges) |
| [hasOperatorPrivileges](arkts-telephony-sim-hasoperatorprivileges-f.md#hasoperatorprivileges-1) |
| [hasSimCard](arkts-telephony-sim-hassimcard-f.md#hassimcard) |
| [hasSimCard](arkts-telephony-sim-hassimcard-f.md#hassimcard-1) |
| [hasSimCardSync](arkts-telephony-sim-hassimcardsync-f.md#hassimcardsync) |
| [isSimActive](arkts-telephony-sim-issimactive-f.md#issimactive) |
| [isSimActive](arkts-telephony-sim-issimactive-f.md#issimactive-1) |
| [isSimActiveSync](arkts-telephony-sim-issimactivesync-f.md#issimactivesync) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [activateSim](arkts-telephony-sim-activatesim-f-sys.md#activatesim) |
| [activateSim](arkts-telephony-sim-activatesim-f-sys.md#activatesim-1) |
| [addIccDiallingNumbers](arkts-telephony-sim-addiccdiallingnumbers-f-sys.md#addiccdiallingnumbers) |
| [addIccDiallingNumbers](arkts-telephony-sim-addiccdiallingnumbers-f-sys.md#addiccdiallingnumbers-1) |
| [alterPin](arkts-telephony-sim-alterpin-f-sys.md#alterpin) |
| [alterPin](arkts-telephony-sim-alterpin-f-sys.md#alterpin-1) |
| [alterPin2](arkts-telephony-sim-alterpin2-f-sys.md#alterpin2) |
| [alterPin2](arkts-telephony-sim-alterpin2-f-sys.md#alterpin2-1) |
| [deactivateSim](arkts-telephony-sim-deactivatesim-f-sys.md#deactivatesim) |
| [deactivateSim](arkts-telephony-sim-deactivatesim-f-sys.md#deactivatesim-1) |
| [delIccDiallingNumbers](arkts-telephony-sim-deliccdiallingnumbers-f-sys.md#deliccdiallingnumbers) |
| [delIccDiallingNumbers](arkts-telephony-sim-deliccdiallingnumbers-f-sys.md#deliccdiallingnumbers-1) |
| [getAllSimAccountInfoList](arkts-telephony-sim-getallsimaccountinfolist-f-sys.md#getallsimaccountinfolist) |
| [getAllSimAccountInfoList](arkts-telephony-sim-getallsimaccountinfolist-f-sys.md#getallsimaccountinfolist-1) |
| [getDsdsMode](arkts-telephony-sim-getdsdsmode-f-sys.md#getdsdsmode) |
| [getDsdsMode](arkts-telephony-sim-getdsdsmode-f-sys.md#getdsdsmode-1) |
| [getIMSI](arkts-telephony-sim-getimsi-f-sys.md#getimsi) |
| [getIMSI](arkts-telephony-sim-getimsi-f-sys.md#getimsi-1) |
| [getLockState](arkts-telephony-sim-getlockstate-f-sys.md#getlockstate) |
| [getLockState](arkts-telephony-sim-getlockstate-f-sys.md#getlockstate-1) |
| [getOperatorConfigs](arkts-telephony-sim-getoperatorconfigs-f-sys.md#getoperatorconfigs) |
| [getOperatorConfigs](arkts-telephony-sim-getoperatorconfigs-f-sys.md#getoperatorconfigs-1) |
| [getShowName](arkts-telephony-sim-getshowname-f-sys.md#getshowname) |
| [getShowName](arkts-telephony-sim-getshowname-f-sys.md#getshowname-1) |
| [getShowNumber](arkts-telephony-sim-getshownumber-f-sys.md#getshownumber) |
| [getShowNumber](arkts-telephony-sim-getshownumber-f-sys.md#getshownumber-1) |
| [getSimAuthentication](arkts-telephony-sim-getsimauthentication-f-sys.md#getsimauthentication) |
| [getSimGid1](arkts-telephony-sim-getsimgid1-f-sys.md#getsimgid1) |
| [getSimGid1](arkts-telephony-sim-getsimgid1-f-sys.md#getsimgid1-1) |
| [getSimIccId](arkts-telephony-sim-getsimiccid-f-sys.md#getsimiccid) |
| [getSimIccId](arkts-telephony-sim-getsimiccid-f-sys.md#getsimiccid-1) |
| [getSimTelephoneNumber](arkts-telephony-sim-getsimtelephonenumber-f-sys.md#getsimtelephonenumber) |
| [getSimTelephoneNumber](arkts-telephony-sim-getsimtelephonenumber-f-sys.md#getsimtelephonenumber-1) |
| [getVoiceMailIdentifier](arkts-telephony-sim-getvoicemailidentifier-f-sys.md#getvoicemailidentifier) |
| [getVoiceMailIdentifier](arkts-telephony-sim-getvoicemailidentifier-f-sys.md#getvoicemailidentifier-1) |
| [getVoiceMailNumber](arkts-telephony-sim-getvoicemailnumber-f-sys.md#getvoicemailnumber) |
| [getVoiceMailNumber](arkts-telephony-sim-getvoicemailnumber-f-sys.md#getvoicemailnumber-1) |
| [isOperatorSimCard](arkts-telephony-sim-isoperatorsimcard-f-sys.md#isoperatorsimcard) |
| [queryIccDiallingNumbers](arkts-telephony-sim-queryiccdiallingnumbers-f-sys.md#queryiccdiallingnumbers) |
| [queryIccDiallingNumbers](arkts-telephony-sim-queryiccdiallingnumbers-f-sys.md#queryiccdiallingnumbers-1) |
| [sendEnvelopeCmd](arkts-telephony-sim-sendenvelopecmd-f-sys.md#sendenvelopecmd) |
| [sendEnvelopeCmd](arkts-telephony-sim-sendenvelopecmd-f-sys.md#sendenvelopecmd-1) |
| [sendTerminalResponseCmd](arkts-telephony-sim-sendterminalresponsecmd-f-sys.md#sendterminalresponsecmd) |
| [sendTerminalResponseCmd](arkts-telephony-sim-sendterminalresponsecmd-f-sys.md#sendterminalresponsecmd-1) |
| [setDefaultVoiceSlotId](arkts-telephony-sim-setdefaultvoiceslotid-f-sys.md#setdefaultvoiceslotid) |
| [setDefaultVoiceSlotId](arkts-telephony-sim-setdefaultvoiceslotid-f-sys.md#setdefaultvoiceslotid-1) |
| [setLockState](arkts-telephony-sim-setlockstate-f-sys.md#setlockstate) |
| [setLockState](arkts-telephony-sim-setlockstate-f-sys.md#setlockstate-1) |
| [setShowName](arkts-telephony-sim-setshowname-f-sys.md#setshowname) |
| [setShowName](arkts-telephony-sim-setshowname-f-sys.md#setshowname-1) |
| [setShowNumber](arkts-telephony-sim-setshownumber-f-sys.md#setshownumber) |
| [setShowNumber](arkts-telephony-sim-setshownumber-f-sys.md#setshownumber-1) |
| [setSimLabelIndex](arkts-telephony-sim-setsimlabelindex-f-sys.md#setsimlabelindex) |
| [setVoiceMailInfo](arkts-telephony-sim-setvoicemailinfo-f-sys.md#setvoicemailinfo) |
| [setVoiceMailInfo](arkts-telephony-sim-setvoicemailinfo-f-sys.md#setvoicemailinfo-1) |
| [unlockPin](arkts-telephony-sim-unlockpin-f-sys.md#unlockpin) |
| [unlockPin](arkts-telephony-sim-unlockpin-f-sys.md#unlockpin-1) |
| [unlockPin2](arkts-telephony-sim-unlockpin2-f-sys.md#unlockpin2) |
| [unlockPin2](arkts-telephony-sim-unlockpin2-f-sys.md#unlockpin2-1) |
| [unlockPuk](arkts-telephony-sim-unlockpuk-f-sys.md#unlockpuk) |
| [unlockPuk](arkts-telephony-sim-unlockpuk-f-sys.md#unlockpuk-1) |
| [unlockPuk2](arkts-telephony-sim-unlockpuk2-f-sys.md#unlockpuk2) |
| [unlockPuk2](arkts-telephony-sim-unlockpuk2-f-sys.md#unlockpuk2-1) |
| [unlockSimLock](arkts-telephony-sim-unlocksimlock-f-sys.md#unlocksimlock) |
| [unlockSimLock](arkts-telephony-sim-unlocksimlock-f-sys.md#unlocksimlock-1) |
| [updateIccDiallingNumbers](arkts-telephony-sim-updateiccdiallingnumbers-f-sys.md#updateiccdiallingnumbers) |
| [updateIccDiallingNumbers](arkts-telephony-sim-updateiccdiallingnumbers-f-sys.md#updateiccdiallingnumbers-1) |
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
