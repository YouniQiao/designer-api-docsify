# @ohos.telephony.sim(SIM卡管理)

SIM卡管理模块提供了SIM卡管理的基础能力，包括获取指定卡槽SIM卡的ISO国家码、归属PLMN号、服务提供商名称、SIM卡状态、卡类型、是否插卡、是否激活等。

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Telephony.CoreService

## 导入模块

```TypeScript
import { sim } from '@kit.TelephonyKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [getActiveSimAccountInfoList(SIM卡管理)](arkts-telephony-sim-getactivesimaccountinfolist-f.md) |
| [getActiveSimAccountInfoList(SIM卡管理)](arkts-telephony-sim-getactivesimaccountinfolist-f.md) |
| [getCardType(SIM卡管理)](arkts-telephony-sim-getcardtype-f.md) |
| [getCardType(SIM卡管理)](arkts-telephony-sim-getcardtype-f.md) |
| [getCardTypeSync(SIM卡管理)](arkts-telephony-sim-getcardtypesync-f.md) |
| [getDefaultVoiceSimId(SIM卡管理)](arkts-telephony-sim-getdefaultvoicesimid-f.md) |
| [getDefaultVoiceSimId(SIM卡管理)](arkts-telephony-sim-getdefaultvoicesimid-f.md) |
| [getDefaultVoiceSlotId(SIM卡管理)](arkts-telephony-sim-getdefaultvoiceslotid-f.md) |
| [getDefaultVoiceSlotId(SIM卡管理)](arkts-telephony-sim-getdefaultvoiceslotid-f.md) |
| [getISOCountryCodeForSim(SIM卡管理)](arkts-telephony-sim-getisocountrycodeforsim-f.md) |
| [getISOCountryCodeForSim(SIM卡管理)](arkts-telephony-sim-getisocountrycodeforsim-f.md) |
| [getISOCountryCodeForSimSync(SIM卡管理)](arkts-telephony-sim-getisocountrycodeforsimsync-f.md) |
| [getMaxSimCount(SIM卡管理)](arkts-telephony-sim-getmaxsimcount-f.md) |
| [getOpKey(SIM卡管理)](arkts-telephony-sim-getopkey-f.md) |
| [getOpKey(SIM卡管理)](arkts-telephony-sim-getopkey-f.md) |
| [getOpKeySync(SIM卡管理)](arkts-telephony-sim-getopkeysync-f.md) |
| [getOpName(SIM卡管理)](arkts-telephony-sim-getopname-f.md) |
| [getOpName(SIM卡管理)](arkts-telephony-sim-getopname-f.md) |
| [getOpNameSync(SIM卡管理)](arkts-telephony-sim-getopnamesync-f.md) |
| [getSimAccountInfo(SIM卡管理)](arkts-telephony-sim-getsimaccountinfo-f.md) |
| [getSimAccountInfo(SIM卡管理)](arkts-telephony-sim-getsimaccountinfo-f.md) |
| [getSimLabel(SIM卡管理)](arkts-telephony-sim-getsimlabel-f.md) |
| [getSimLabel(SIM卡管理)](arkts-telephony-sim-getsimlabel-f.md) |
| [getSimLabelSync(SIM卡管理)](arkts-telephony-sim-getsimlabelsync-f.md) |
| [getSimOperatorNumeric(SIM卡管理)](arkts-telephony-sim-getsimoperatornumeric-f.md) |
| [getSimOperatorNumeric(SIM卡管理)](arkts-telephony-sim-getsimoperatornumeric-f.md) |
| [getSimOperatorNumericSync(SIM卡管理)](arkts-telephony-sim-getsimoperatornumericsync-f.md) |
| [getSimSpn(SIM卡管理)](arkts-telephony-sim-getsimspn-f.md) |
| [getSimSpn(SIM卡管理)](arkts-telephony-sim-getsimspn-f.md) |
| [getSimSpnSync(SIM卡管理)](arkts-telephony-sim-getsimspnsync-f.md) |
| [getSimState(SIM卡管理)](arkts-telephony-sim-getsimstate-f.md) |
| [getSimState(SIM卡管理)](arkts-telephony-sim-getsimstate-f.md) |
| [getSimStateSync(SIM卡管理)](arkts-telephony-sim-getsimstatesync-f.md) |
| [hasOperatorPrivileges(SIM卡管理)](arkts-telephony-sim-hasoperatorprivileges-f.md) |
| [hasOperatorPrivileges(SIM卡管理)](arkts-telephony-sim-hasoperatorprivileges-f.md) |
| [hasSimCard(SIM卡管理)](arkts-telephony-sim-hassimcard-f.md) |
| [hasSimCard(SIM卡管理)](arkts-telephony-sim-hassimcard-f.md) |
| [hasSimCardSync(SIM卡管理)](arkts-telephony-sim-hassimcardsync-f.md) |
| [isSimActive(SIM卡管理)](arkts-telephony-sim-issimactive-f.md) |
| [isSimActive(SIM卡管理)](arkts-telephony-sim-issimactive-f.md) |
| [isSimActiveSync(SIM卡管理)](arkts-telephony-sim-issimactivesync-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [activateSim(SIM卡管理)](arkts-telephony-sim-activatesim-f-sys.md) |
| [activateSim(SIM卡管理)](arkts-telephony-sim-activatesim-f-sys.md) |
| [addIccDiallingNumbers(SIM卡管理)](arkts-telephony-sim-addiccdiallingnumbers-f-sys.md) |
| [addIccDiallingNumbers(SIM卡管理)](arkts-telephony-sim-addiccdiallingnumbers-f-sys.md) |
| [alterPin(SIM卡管理)](arkts-telephony-sim-alterpin-f-sys.md) |
| [alterPin(SIM卡管理)](arkts-telephony-sim-alterpin-f-sys.md) |
| [alterPin2(SIM卡管理)](arkts-telephony-sim-alterpin2-f-sys.md) |
| [alterPin2(SIM卡管理)](arkts-telephony-sim-alterpin2-f-sys.md) |
| [deactivateSim(SIM卡管理)](arkts-telephony-sim-deactivatesim-f-sys.md) |
| [deactivateSim(SIM卡管理)](arkts-telephony-sim-deactivatesim-f-sys.md) |
| [delIccDiallingNumbers(SIM卡管理)](arkts-telephony-sim-deliccdiallingnumbers-f-sys.md) |
| [delIccDiallingNumbers(SIM卡管理)](arkts-telephony-sim-deliccdiallingnumbers-f-sys.md) |
| [getAllSimAccountInfoList(SIM卡管理)](arkts-telephony-sim-getallsimaccountinfolist-f-sys.md) |
| [getAllSimAccountInfoList(SIM卡管理)](arkts-telephony-sim-getallsimaccountinfolist-f-sys.md) |
| [getDsdsMode(SIM卡管理)](arkts-telephony-sim-getdsdsmode-f-sys.md) |
| [getDsdsMode(SIM卡管理)](arkts-telephony-sim-getdsdsmode-f-sys.md) |
| [getIMSI(SIM卡管理)](arkts-telephony-sim-getimsi-f-sys.md) |
| [getIMSI(SIM卡管理)](arkts-telephony-sim-getimsi-f-sys.md) |
| [getLockState(SIM卡管理)](arkts-telephony-sim-getlockstate-f-sys.md) |
| [getLockState(SIM卡管理)](arkts-telephony-sim-getlockstate-f-sys.md) |
| [getOperatorConfigs(SIM卡管理)](arkts-telephony-sim-getoperatorconfigs-f-sys.md) |
| [getOperatorConfigs(SIM卡管理)](arkts-telephony-sim-getoperatorconfigs-f-sys.md) |
| [getShowName(SIM卡管理)](arkts-telephony-sim-getshowname-f-sys.md) |
| [getShowName(SIM卡管理)](arkts-telephony-sim-getshowname-f-sys.md) |
| [getShowNumber(SIM卡管理)](arkts-telephony-sim-getshownumber-f-sys.md) |
| [getShowNumber(SIM卡管理)](arkts-telephony-sim-getshownumber-f-sys.md) |
| [getSimAuthentication(SIM卡管理)](arkts-telephony-sim-getsimauthentication-f-sys.md) |
| [getSimGid1(SIM卡管理)](arkts-telephony-sim-getsimgid1-f-sys.md) |
| [getSimGid1(SIM卡管理)](arkts-telephony-sim-getsimgid1-f-sys.md) |
| [getSimIccId(SIM卡管理)](arkts-telephony-sim-getsimiccid-f-sys.md) |
| [getSimIccId(SIM卡管理)](arkts-telephony-sim-getsimiccid-f-sys.md) |
| [getSimTelephoneNumber(SIM卡管理)](arkts-telephony-sim-getsimtelephonenumber-f-sys.md) |
| [getSimTelephoneNumber(SIM卡管理)](arkts-telephony-sim-getsimtelephonenumber-f-sys.md) |
| [getVoiceMailIdentifier(SIM卡管理)](arkts-telephony-sim-getvoicemailidentifier-f-sys.md) |
| [getVoiceMailIdentifier(SIM卡管理)](arkts-telephony-sim-getvoicemailidentifier-f-sys.md) |
| [getVoiceMailNumber(SIM卡管理)](arkts-telephony-sim-getvoicemailnumber-f-sys.md) |
| [getVoiceMailNumber(SIM卡管理)](arkts-telephony-sim-getvoicemailnumber-f-sys.md) |
| [isOperatorSimCard(SIM卡管理)](arkts-telephony-sim-isoperatorsimcard-f-sys.md) |
| [queryIccDiallingNumbers(SIM卡管理)](arkts-telephony-sim-queryiccdiallingnumbers-f-sys.md) |
| [queryIccDiallingNumbers(SIM卡管理)](arkts-telephony-sim-queryiccdiallingnumbers-f-sys.md) |
| [sendEnvelopeCmd(SIM卡管理)](arkts-telephony-sim-sendenvelopecmd-f-sys.md) |
| [sendEnvelopeCmd(SIM卡管理)](arkts-telephony-sim-sendenvelopecmd-f-sys.md) |
| [sendTerminalResponseCmd(SIM卡管理)](arkts-telephony-sim-sendterminalresponsecmd-f-sys.md) |
| [sendTerminalResponseCmd(SIM卡管理)](arkts-telephony-sim-sendterminalresponsecmd-f-sys.md) |
| [setDefaultVoiceSlotId(SIM卡管理)](arkts-telephony-sim-setdefaultvoiceslotid-f-sys.md) |
| [setDefaultVoiceSlotId(SIM卡管理)](arkts-telephony-sim-setdefaultvoiceslotid-f-sys.md) |
| [setLockState(SIM卡管理)](arkts-telephony-sim-setlockstate-f-sys.md) |
| [setLockState(SIM卡管理)](arkts-telephony-sim-setlockstate-f-sys.md) |
| [setShowName(SIM卡管理)](arkts-telephony-sim-setshowname-f-sys.md) |
| [setShowName(SIM卡管理)](arkts-telephony-sim-setshowname-f-sys.md) |
| [setShowNumber(SIM卡管理)](arkts-telephony-sim-setshownumber-f-sys.md) |
| [setShowNumber(SIM卡管理)](arkts-telephony-sim-setshownumber-f-sys.md) |
| [setSimLabelIndex(SIM卡管理)](arkts-telephony-sim-setsimlabelindex-f-sys.md) |
| [setVoiceMailInfo(SIM卡管理)](arkts-telephony-sim-setvoicemailinfo-f-sys.md) |
| [setVoiceMailInfo(SIM卡管理)](arkts-telephony-sim-setvoicemailinfo-f-sys.md) |
| [unlockPin(SIM卡管理)](arkts-telephony-sim-unlockpin-f-sys.md) |
| [unlockPin(SIM卡管理)](arkts-telephony-sim-unlockpin-f-sys.md) |
| [unlockPin2(SIM卡管理)](arkts-telephony-sim-unlockpin2-f-sys.md) |
| [unlockPin2(SIM卡管理)](arkts-telephony-sim-unlockpin2-f-sys.md) |
| [unlockPuk(SIM卡管理)](arkts-telephony-sim-unlockpuk-f-sys.md) |
| [unlockPuk(SIM卡管理)](arkts-telephony-sim-unlockpuk-f-sys.md) |
| [unlockPuk2(SIM卡管理)](arkts-telephony-sim-unlockpuk2-f-sys.md) |
| [unlockPuk2(SIM卡管理)](arkts-telephony-sim-unlockpuk2-f-sys.md) |
| [unlockSimLock(SIM卡管理)](arkts-telephony-sim-unlocksimlock-f-sys.md) |
| [unlockSimLock(SIM卡管理)](arkts-telephony-sim-unlocksimlock-f-sys.md) |
| [updateIccDiallingNumbers(SIM卡管理)](arkts-telephony-sim-updateiccdiallingnumbers-f-sys.md) |
| [updateIccDiallingNumbers(SIM卡管理)](arkts-telephony-sim-updateiccdiallingnumbers-f-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [IccAccountInfo(SIM卡管理)](arkts-telephony-sim-iccaccountinfo-i.md) |
| [SimLabel(SIM卡管理)](arkts-telephony-sim-simlabel-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [DiallingNumbersInfo(SIM卡管理)](arkts-telephony-sim-diallingnumbersinfo-i-sys.md) |
| [IccAccountInfo(SIM卡管理)](arkts-telephony-sim-iccaccountinfo-i-sys.md) |
| [LockInfo(SIM卡管理)](arkts-telephony-sim-lockinfo-i-sys.md) |
| [LockStatusResponse(SIM卡管理)](arkts-telephony-sim-lockstatusresponse-i-sys.md) |
| [OperatorConfig(SIM卡管理)](arkts-telephony-sim-operatorconfig-i-sys.md) |
| [PersoLockInfo(SIM卡管理)](arkts-telephony-sim-persolockinfo-i-sys.md) |
| [SimAuthenticationResponse(SIM卡管理)](arkts-telephony-sim-simauthenticationresponse-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [CardType(SIM卡管理)](arkts-telephony-sim-cardtype-e.md) |
| [SimState(SIM卡管理)](arkts-telephony-sim-simstate-e.md) |
| [SimType(SIM卡管理)](arkts-telephony-sim-simtype-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [AuthType(SIM卡管理)](arkts-telephony-sim-authtype-e-sys.md) |
| [ContactType(SIM卡管理)](arkts-telephony-sim-contacttype-e-sys.md) |
| [DsdsMode(SIM卡管理)](arkts-telephony-sim-dsdsmode-e-sys.md) |
| [LockState(SIM卡管理)](arkts-telephony-sim-lockstate-e-sys.md) |
| [LockType(SIM卡管理)](arkts-telephony-sim-locktype-e-sys.md) |
| [OperatorConfigKey(SIM卡管理)](arkts-telephony-sim-operatorconfigkey-e-sys.md) |
| [OperatorSimCard(SIM卡管理)](arkts-telephony-sim-operatorsimcard-e-sys.md) |
| [PersoLockType(SIM卡管理)](arkts-telephony-sim-persolocktype-e-sys.md) |
<!--DelEnd-->
