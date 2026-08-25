# @ohos.telephony.sim(SIM Management)

The **sim** module provides basic SIM card management functions. With the APIs provided by this module, you can obtain the ISO country code, home PLMN ID, service provider name, SIM card status, type, installation status, and activation status of the SIM card in the specified slot.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Telephony.CoreService

## Modules to Import

```TypeScript
import { sim } from '@kit.TelephonyKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getActiveSimAccountInfoList(SIM Management)](arkts-telephony-sim-getactivesimaccountinfolist-f.md) |
| [getActiveSimAccountInfoList(SIM Management)](arkts-telephony-sim-getactivesimaccountinfolist-f.md) |
| [getCardType(SIM Management)](arkts-telephony-sim-getcardtype-f.md) |
| [getCardType(SIM Management)](arkts-telephony-sim-getcardtype-f.md) |
| [getCardTypeSync(SIM Management)](arkts-telephony-sim-getcardtypesync-f.md) |
| [getDefaultVoiceSimId(SIM Management)](arkts-telephony-sim-getdefaultvoicesimid-f.md) |
| [getDefaultVoiceSimId(SIM Management)](arkts-telephony-sim-getdefaultvoicesimid-f.md) |
| [getDefaultVoiceSlotId(SIM Management)](arkts-telephony-sim-getdefaultvoiceslotid-f.md) |
| [getDefaultVoiceSlotId(SIM Management)](arkts-telephony-sim-getdefaultvoiceslotid-f.md) |
| [getISOCountryCodeForSim(SIM Management)](arkts-telephony-sim-getisocountrycodeforsim-f.md) |
| [getISOCountryCodeForSim(SIM Management)](arkts-telephony-sim-getisocountrycodeforsim-f.md) |
| [getISOCountryCodeForSimSync(SIM Management)](arkts-telephony-sim-getisocountrycodeforsimsync-f.md) |
| [getMaxSimCount(SIM Management)](arkts-telephony-sim-getmaxsimcount-f.md) |
| [getOpKey(SIM Management)](arkts-telephony-sim-getopkey-f.md) |
| [getOpKey(SIM Management)](arkts-telephony-sim-getopkey-f.md) |
| [getOpKeySync(SIM Management)](arkts-telephony-sim-getopkeysync-f.md) |
| [getOpName(SIM Management)](arkts-telephony-sim-getopname-f.md) |
| [getOpName(SIM Management)](arkts-telephony-sim-getopname-f.md) |
| [getOpNameSync(SIM Management)](arkts-telephony-sim-getopnamesync-f.md) |
| [getSimAccountInfo(SIM Management)](arkts-telephony-sim-getsimaccountinfo-f.md) |
| [getSimAccountInfo(SIM Management)](arkts-telephony-sim-getsimaccountinfo-f.md) |
| [getSimLabel(SIM Management)](arkts-telephony-sim-getsimlabel-f.md) |
| [getSimLabel(SIM Management)](arkts-telephony-sim-getsimlabel-f.md) |
| [getSimLabelSync(SIM Management)](arkts-telephony-sim-getsimlabelsync-f.md) |
| [getSimOperatorNumeric(SIM Management)](arkts-telephony-sim-getsimoperatornumeric-f.md) |
| [getSimOperatorNumeric(SIM Management)](arkts-telephony-sim-getsimoperatornumeric-f.md) |
| [getSimOperatorNumericSync(SIM Management)](arkts-telephony-sim-getsimoperatornumericsync-f.md) |
| [getSimSpn(SIM Management)](arkts-telephony-sim-getsimspn-f.md) |
| [getSimSpn(SIM Management)](arkts-telephony-sim-getsimspn-f.md) |
| [getSimSpnSync(SIM Management)](arkts-telephony-sim-getsimspnsync-f.md) |
| [getSimState(SIM Management)](arkts-telephony-sim-getsimstate-f.md) |
| [getSimState(SIM Management)](arkts-telephony-sim-getsimstate-f.md) |
| [getSimStateSync(SIM Management)](arkts-telephony-sim-getsimstatesync-f.md) |
| [hasOperatorPrivileges(SIM Management)](arkts-telephony-sim-hasoperatorprivileges-f.md) |
| [hasOperatorPrivileges(SIM Management)](arkts-telephony-sim-hasoperatorprivileges-f.md) |
| [hasSimCard(SIM Management)](arkts-telephony-sim-hassimcard-f.md) |
| [hasSimCard(SIM Management)](arkts-telephony-sim-hassimcard-f.md) |
| [hasSimCardSync(SIM Management)](arkts-telephony-sim-hassimcardsync-f.md) |
| [isSimActive(SIM Management)](arkts-telephony-sim-issimactive-f.md) |
| [isSimActive(SIM Management)](arkts-telephony-sim-issimactive-f.md) |
| [isSimActiveSync(SIM Management)](arkts-telephony-sim-issimactivesync-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [activateSim(SIM Management)](arkts-telephony-sim-activatesim-f-sys.md) |
| [activateSim(SIM Management)](arkts-telephony-sim-activatesim-f-sys.md) |
| [addIccDiallingNumbers(SIM Management)](arkts-telephony-sim-addiccdiallingnumbers-f-sys.md) |
| [addIccDiallingNumbers(SIM Management)](arkts-telephony-sim-addiccdiallingnumbers-f-sys.md) |
| [alterPin(SIM Management)](arkts-telephony-sim-alterpin-f-sys.md) |
| [alterPin(SIM Management)](arkts-telephony-sim-alterpin-f-sys.md) |
| [alterPin2(SIM Management)](arkts-telephony-sim-alterpin2-f-sys.md) |
| [alterPin2(SIM Management)](arkts-telephony-sim-alterpin2-f-sys.md) |
| [deactivateSim(SIM Management)](arkts-telephony-sim-deactivatesim-f-sys.md) |
| [deactivateSim(SIM Management)](arkts-telephony-sim-deactivatesim-f-sys.md) |
| [delIccDiallingNumbers(SIM Management)](arkts-telephony-sim-deliccdiallingnumbers-f-sys.md) |
| [delIccDiallingNumbers(SIM Management)](arkts-telephony-sim-deliccdiallingnumbers-f-sys.md) |
| [getAllSimAccountInfoList(SIM Management)](arkts-telephony-sim-getallsimaccountinfolist-f-sys.md) |
| [getAllSimAccountInfoList(SIM Management)](arkts-telephony-sim-getallsimaccountinfolist-f-sys.md) |
| [getDsdsMode(SIM Management)](arkts-telephony-sim-getdsdsmode-f-sys.md) |
| [getDsdsMode(SIM Management)](arkts-telephony-sim-getdsdsmode-f-sys.md) |
| [getIMSI(SIM Management)](arkts-telephony-sim-getimsi-f-sys.md) |
| [getIMSI(SIM Management)](arkts-telephony-sim-getimsi-f-sys.md) |
| [getLockState(SIM Management)](arkts-telephony-sim-getlockstate-f-sys.md) |
| [getLockState(SIM Management)](arkts-telephony-sim-getlockstate-f-sys.md) |
| [getOperatorConfigs(SIM Management)](arkts-telephony-sim-getoperatorconfigs-f-sys.md) |
| [getOperatorConfigs(SIM Management)](arkts-telephony-sim-getoperatorconfigs-f-sys.md) |
| [getShowName(SIM Management)](arkts-telephony-sim-getshowname-f-sys.md) |
| [getShowName(SIM Management)](arkts-telephony-sim-getshowname-f-sys.md) |
| [getShowNumber(SIM Management)](arkts-telephony-sim-getshownumber-f-sys.md) |
| [getShowNumber(SIM Management)](arkts-telephony-sim-getshownumber-f-sys.md) |
| [getSimAuthentication(SIM Management)](arkts-telephony-sim-getsimauthentication-f-sys.md) |
| [getSimGid1(SIM Management)](arkts-telephony-sim-getsimgid1-f-sys.md) |
| [getSimGid1(SIM Management)](arkts-telephony-sim-getsimgid1-f-sys.md) |
| [getSimIccId(SIM Management)](arkts-telephony-sim-getsimiccid-f-sys.md) |
| [getSimIccId(SIM Management)](arkts-telephony-sim-getsimiccid-f-sys.md) |
| [getSimTelephoneNumber(SIM Management)](arkts-telephony-sim-getsimtelephonenumber-f-sys.md) |
| [getSimTelephoneNumber(SIM Management)](arkts-telephony-sim-getsimtelephonenumber-f-sys.md) |
| [getVoiceMailIdentifier(SIM Management)](arkts-telephony-sim-getvoicemailidentifier-f-sys.md) |
| [getVoiceMailIdentifier(SIM Management)](arkts-telephony-sim-getvoicemailidentifier-f-sys.md) |
| [getVoiceMailNumber(SIM Management)](arkts-telephony-sim-getvoicemailnumber-f-sys.md) |
| [getVoiceMailNumber(SIM Management)](arkts-telephony-sim-getvoicemailnumber-f-sys.md) |
| [isOperatorSimCard(SIM Management)](arkts-telephony-sim-isoperatorsimcard-f-sys.md) |
| [queryIccDiallingNumbers(SIM Management)](arkts-telephony-sim-queryiccdiallingnumbers-f-sys.md) |
| [queryIccDiallingNumbers(SIM Management)](arkts-telephony-sim-queryiccdiallingnumbers-f-sys.md) |
| [sendEnvelopeCmd(SIM Management)](arkts-telephony-sim-sendenvelopecmd-f-sys.md) |
| [sendEnvelopeCmd(SIM Management)](arkts-telephony-sim-sendenvelopecmd-f-sys.md) |
| [sendTerminalResponseCmd(SIM Management)](arkts-telephony-sim-sendterminalresponsecmd-f-sys.md) |
| [sendTerminalResponseCmd(SIM Management)](arkts-telephony-sim-sendterminalresponsecmd-f-sys.md) |
| [setDefaultVoiceSlotId(SIM Management)](arkts-telephony-sim-setdefaultvoiceslotid-f-sys.md) |
| [setDefaultVoiceSlotId(SIM Management)](arkts-telephony-sim-setdefaultvoiceslotid-f-sys.md) |
| [setLockState(SIM Management)](arkts-telephony-sim-setlockstate-f-sys.md) |
| [setLockState(SIM Management)](arkts-telephony-sim-setlockstate-f-sys.md) |
| [setShowName(SIM Management)](arkts-telephony-sim-setshowname-f-sys.md) |
| [setShowName(SIM Management)](arkts-telephony-sim-setshowname-f-sys.md) |
| [setShowNumber(SIM Management)](arkts-telephony-sim-setshownumber-f-sys.md) |
| [setShowNumber(SIM Management)](arkts-telephony-sim-setshownumber-f-sys.md) |
| [setSimLabelIndex(SIM Management)](arkts-telephony-sim-setsimlabelindex-f-sys.md) |
| [setVoiceMailInfo(SIM Management)](arkts-telephony-sim-setvoicemailinfo-f-sys.md) |
| [setVoiceMailInfo(SIM Management)](arkts-telephony-sim-setvoicemailinfo-f-sys.md) |
| [unlockPin(SIM Management)](arkts-telephony-sim-unlockpin-f-sys.md) |
| [unlockPin(SIM Management)](arkts-telephony-sim-unlockpin-f-sys.md) |
| [unlockPin2(SIM Management)](arkts-telephony-sim-unlockpin2-f-sys.md) |
| [unlockPin2(SIM Management)](arkts-telephony-sim-unlockpin2-f-sys.md) |
| [unlockPuk(SIM Management)](arkts-telephony-sim-unlockpuk-f-sys.md) |
| [unlockPuk(SIM Management)](arkts-telephony-sim-unlockpuk-f-sys.md) |
| [unlockPuk2(SIM Management)](arkts-telephony-sim-unlockpuk2-f-sys.md) |
| [unlockPuk2(SIM Management)](arkts-telephony-sim-unlockpuk2-f-sys.md) |
| [unlockSimLock(SIM Management)](arkts-telephony-sim-unlocksimlock-f-sys.md) |
| [unlockSimLock(SIM Management)](arkts-telephony-sim-unlocksimlock-f-sys.md) |
| [updateIccDiallingNumbers(SIM Management)](arkts-telephony-sim-updateiccdiallingnumbers-f-sys.md) |
| [updateIccDiallingNumbers(SIM Management)](arkts-telephony-sim-updateiccdiallingnumbers-f-sys.md) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [IccAccountInfo(SIM Management)](arkts-telephony-sim-iccaccountinfo-i.md) |
| [SimLabel(SIM Management)](arkts-telephony-sim-simlabel-i.md) |

<!--Del-->
### Interfaces(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DiallingNumbersInfo(SIM Management)](arkts-telephony-sim-diallingnumbersinfo-i-sys.md) |
| [IccAccountInfo(SIM Management)](arkts-telephony-sim-iccaccountinfo-i-sys.md) |
| [LockInfo(SIM Management)](arkts-telephony-sim-lockinfo-i-sys.md) |
| [LockStatusResponse(SIM Management)](arkts-telephony-sim-lockstatusresponse-i-sys.md) |
| [OperatorConfig(SIM Management)](arkts-telephony-sim-operatorconfig-i-sys.md) |
| [PersoLockInfo(SIM Management)](arkts-telephony-sim-persolockinfo-i-sys.md) |
| [SimAuthenticationResponse(SIM Management)](arkts-telephony-sim-simauthenticationresponse-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CardType(SIM Management)](arkts-telephony-sim-cardtype-e.md) |
| [SimState(SIM Management)](arkts-telephony-sim-simstate-e.md) |
| [SimType(SIM Management)](arkts-telephony-sim-simtype-e.md) |

<!--Del-->
### Enums(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AuthType(SIM Management)](arkts-telephony-sim-authtype-e-sys.md) |
| [ContactType(SIM Management)](arkts-telephony-sim-contacttype-e-sys.md) |
| [DsdsMode(SIM Management)](arkts-telephony-sim-dsdsmode-e-sys.md) |
| [LockState(SIM Management)](arkts-telephony-sim-lockstate-e-sys.md) |
| [LockType(SIM Management)](arkts-telephony-sim-locktype-e-sys.md) |
| [OperatorConfigKey(SIM Management)](arkts-telephony-sim-operatorconfigkey-e-sys.md) |
| [OperatorSimCard(SIM Management)](arkts-telephony-sim-operatorsimcard-e-sys.md) |
| [PersoLockType(SIM Management)](arkts-telephony-sim-persolocktype-e-sys.md) |
<!--DelEnd-->
