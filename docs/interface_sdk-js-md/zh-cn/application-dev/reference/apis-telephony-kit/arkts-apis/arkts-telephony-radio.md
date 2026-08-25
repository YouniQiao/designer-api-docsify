# @ohos.telephony.radio(网络搜索)

网络搜索模块提供管理网络搜索的一些基础功能，包括获取当前接入的CS域和PS域无线接入技术、获取网络状态、获取当前选网模式、获取注册网络所在国家的ISO国家码、获取主卡所在卡槽的索引号、获取指定SIM卡槽对应的注册网络信号强度信息列表、 获取运营商名称，判断当前设备是否支持NR(New Radio)、判断主卡的Radio是否打开等。其中，CS域为电路交换域，PS为分组交换域。

**起始版本：** 6

**ArkTS模式：** ArkTS-Dyn起始版本为6；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Telephony.CoreService

## 导入模块

```TypeScript
import { radio } from '@kit.TelephonyKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [getISOCountryCodeForNetwork(网络搜索)](arkts-telephony-radio-getisocountrycodefornetwork-f.md) |
| [getISOCountryCodeForNetwork(网络搜索)](arkts-telephony-radio-getisocountrycodefornetwork-f.md) |
| [getISOCountryCodeForNetworkSync(网络搜索)](arkts-telephony-radio-getisocountrycodefornetworksync-f.md) |
| [getNetworkSelectionMode(网络搜索)](arkts-telephony-radio-getnetworkselectionmode-f.md) |
| [getNetworkSelectionMode(网络搜索)](arkts-telephony-radio-getnetworkselectionmode-f.md) |
| [getNetworkState(网络搜索)](arkts-telephony-radio-getnetworkstate-f.md) |
| [getNetworkState(网络搜索)](arkts-telephony-radio-getnetworkstate-f.md) |
| [getNetworkState(网络搜索)](arkts-telephony-radio-getnetworkstate-f.md) |
| [getOperatorName(网络搜索)](arkts-telephony-radio-getoperatorname-f.md) |
| [getOperatorName(网络搜索)](arkts-telephony-radio-getoperatorname-f.md) |
| [getOperatorNameSync(网络搜索)](arkts-telephony-radio-getoperatornamesync-f.md) |
| [getPrimarySlotId(网络搜索)](arkts-telephony-radio-getprimaryslotid-f.md) |
| [getPrimarySlotId(网络搜索)](arkts-telephony-radio-getprimaryslotid-f.md) |
| [getRadioTech(网络搜索)](arkts-telephony-radio-getradiotech-f.md) |
| [getRadioTech(网络搜索)](arkts-telephony-radio-getradiotech-f.md) |
| [getRadioTechSync(网络搜索)](arkts-telephony-radio-getradiotechsync-f.md) |
| [getSignalInformation(网络搜索)](arkts-telephony-radio-getsignalinformation-f.md) |
| [getSignalInformation(网络搜索)](arkts-telephony-radio-getsignalinformation-f.md) |
| [getSignalInformationSync(网络搜索)](arkts-telephony-radio-getsignalinformationsync-f.md) |
| [isNrSupported(网络搜索)](arkts-telephony-radio-isnrsupported-f.md) |
| [isNrSupported(网络搜索)](arkts-telephony-radio-isnrsupported-f.md) |
| [isNRSupported(网络搜索)](arkts-telephony-radio-isnrsupported-f.md) |
| [isNRSupported(网络搜索)](arkts-telephony-radio-isnrsupported-f.md) |
| [isRadioOn(网络搜索)](arkts-telephony-radio-isradioon-f.md) |
| [isRadioOn(网络搜索)](arkts-telephony-radio-isradioon-f.md) |
| [isRadioOn(网络搜索)](arkts-telephony-radio-isradioon-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [factoryReset(网络搜索)](arkts-telephony-radio-factoryreset-f-sys.md) |
| [getBasebandVersion(网络搜索)](arkts-telephony-radio-getbasebandversion-f-sys.md) |
| [getBasebandVersion(网络搜索)](arkts-telephony-radio-getbasebandversion-f-sys.md) |
| [getCellInformation(网络搜索)](arkts-telephony-radio-getcellinformation-f-sys.md) |
| [getCellInformation(网络搜索)](arkts-telephony-radio-getcellinformation-f-sys.md) |
| [getCellInformation(网络搜索)](arkts-telephony-radio-getcellinformation-f-sys.md) |
| [getIMEI(网络搜索)](arkts-telephony-radio-getimei-f-sys.md) |
| [getIMEI(网络搜索)](arkts-telephony-radio-getimei-f-sys.md) |
| [getIMEI(网络搜索)](arkts-telephony-radio-getimei-f-sys.md) |
| [getIMEISV(网络搜索)](arkts-telephony-radio-getimeisv-f-sys.md) |
| [getImsRegInfo(网络搜索)](arkts-telephony-radio-getimsreginfo-f-sys.md) |
| [getImsRegInfo(网络搜索)](arkts-telephony-radio-getimsreginfo-f-sys.md) |
| [getMEID(网络搜索)](arkts-telephony-radio-getmeid-f-sys.md) |
| [getMEID(网络搜索)](arkts-telephony-radio-getmeid-f-sys.md) |
| [getMEID(网络搜索)](arkts-telephony-radio-getmeid-f-sys.md) |
| [getNetworkCapability(网络搜索)](arkts-telephony-radio-getnetworkcapability-f-sys.md) |
| [getNetworkCapability(网络搜索)](arkts-telephony-radio-getnetworkcapability-f-sys.md) |
| [getNetworkSearchInformation(网络搜索)](arkts-telephony-radio-getnetworksearchinformation-f-sys.md) |
| [getNetworkSearchInformation(网络搜索)](arkts-telephony-radio-getnetworksearchinformation-f-sys.md) |
| [getNrOptionMode(网络搜索)](arkts-telephony-radio-getnroptionmode-f-sys.md) |
| [getNrOptionMode(网络搜索)](arkts-telephony-radio-getnroptionmode-f-sys.md) |
| [getNrOptionMode(网络搜索)](arkts-telephony-radio-getnroptionmode-f-sys.md) |
| [getNROptionMode(网络搜索)](arkts-telephony-radio-getnroptionmode-f-sys.md) |
| [getNROptionMode(网络搜索)](arkts-telephony-radio-getnroptionmode-f-sys.md) |
| [getPreferredNetwork(网络搜索)](arkts-telephony-radio-getpreferrednetwork-f-sys.md) |
| [getPreferredNetwork(网络搜索)](arkts-telephony-radio-getpreferrednetwork-f-sys.md) |
| [getUniqueDeviceId(网络搜索)](arkts-telephony-radio-getuniquedeviceid-f-sys.md) |
| [getUniqueDeviceId(网络搜索)](arkts-telephony-radio-getuniquedeviceid-f-sys.md) |
| [getUniqueDeviceId(网络搜索)](arkts-telephony-radio-getuniquedeviceid-f-sys.md) |
| [isManualNetworkScanning(网络搜索)](arkts-telephony-radio-ismanualnetworkscanning-f-sys.md) |
| [off(网络搜索)](arkts-telephony-radio-off-f-sys.md#offimsregstatechange) |
| [offImsRegStateChange(网络搜索)](arkts-telephony-radio-offimsregstatechange-f-sys.md) |
| [on(网络搜索)](arkts-telephony-radio-on-f-sys.md#onimsregstatechange) |
| [onImsRegStateChange(网络搜索)](arkts-telephony-radio-onimsregstatechange-f-sys.md) |
| [sendUpdateCellLocationRequest(网络搜索)](arkts-telephony-radio-sendupdatecelllocationrequest-f-sys.md) |
| [sendUpdateCellLocationRequest(网络搜索)](arkts-telephony-radio-sendupdatecelllocationrequest-f-sys.md) |
| [sendUpdateCellLocationRequest(网络搜索)](arkts-telephony-radio-sendupdatecelllocationrequest-f-sys.md) |
| [setNetworkCapability(网络搜索)](arkts-telephony-radio-setnetworkcapability-f-sys.md) |
| [setNetworkCapability(网络搜索)](arkts-telephony-radio-setnetworkcapability-f-sys.md) |
| [setNetworkSelectionMode(网络搜索)](arkts-telephony-radio-setnetworkselectionmode-f-sys.md) |
| [setNetworkSelectionMode(网络搜索)](arkts-telephony-radio-setnetworkselectionmode-f-sys.md) |
| [setNROptionMode(网络搜索)](arkts-telephony-radio-setnroptionmode-f-sys.md) |
| [setNROptionMode(网络搜索)](arkts-telephony-radio-setnroptionmode-f-sys.md) |
| [setPreferredNetwork(网络搜索)](arkts-telephony-radio-setpreferrednetwork-f-sys.md) |
| [setPreferredNetwork(网络搜索)](arkts-telephony-radio-setpreferrednetwork-f-sys.md) |
| [setPrimarySlotId(网络搜索)](arkts-telephony-radio-setprimaryslotid-f-sys.md) |
| [setPrimarySlotId(网络搜索)](arkts-telephony-radio-setprimaryslotid-f-sys.md) |
| [startManualNetworkScan(网络搜索)](arkts-telephony-radio-startmanualnetworkscan-f-sys.md) |
| [stopManualNetworkScan(网络搜索)](arkts-telephony-radio-stopmanualnetworkscan-f-sys.md) |
| [turnOffRadio(网络搜索)](arkts-telephony-radio-turnoffradio-f-sys.md) |
| [turnOffRadio(网络搜索)](arkts-telephony-radio-turnoffradio-f-sys.md) |
| [turnOffRadio(网络搜索)](arkts-telephony-radio-turnoffradio-f-sys.md) |
| [turnOnRadio(网络搜索)](arkts-telephony-radio-turnonradio-f-sys.md) |
| [turnOnRadio(网络搜索)](arkts-telephony-radio-turnonradio-f-sys.md) |
| [turnOnRadio(网络搜索)](arkts-telephony-radio-turnonradio-f-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [CellInformation(网络搜索)](arkts-telephony-radio-cellinformation-i.md) |
| [NetworkRadioTech(网络搜索)](arkts-telephony-radio-networkradiotech-i.md) |
| [NetworkState(网络搜索)](arkts-telephony-radio-networkstate-i.md) |
| [SignalInformation(网络搜索)](arkts-telephony-radio-signalinformation-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [CdmaCellInformation(网络搜索)](arkts-telephony-radio-cdmacellinformation-i-sys.md) |
| [CellInformation(网络搜索)](arkts-telephony-radio-cellinformation-i-sys.md) |
| [GsmCellInformation(网络搜索)](arkts-telephony-radio-gsmcellinformation-i-sys.md) |
| [ImsRegInfo(网络搜索)](arkts-telephony-radio-imsreginfo-i-sys.md) |
| [LteCellInformation(网络搜索)](arkts-telephony-radio-ltecellinformation-i-sys.md) |
| [NetworkInformation(网络搜索)](arkts-telephony-radio-networkinformation-i-sys.md) |
| [NetworkSearchRealTimeResult(网络搜索)](arkts-telephony-radio-networksearchrealtimeresult-i-sys.md) |
| [NetworkSearchResult(网络搜索)](arkts-telephony-radio-networksearchresult-i-sys.md) |
| [NetworkSelectionModeOptions(网络搜索)](arkts-telephony-radio-networkselectionmodeoptions-i-sys.md) |
| [NrCellInformation(网络搜索)](arkts-telephony-radio-nrcellinformation-i-sys.md) |
| [TdscdmaCellInformation(网络搜索)](arkts-telephony-radio-tdscdmacellinformation-i-sys.md) |
| [WcdmaCellInformation(网络搜索)](arkts-telephony-radio-wcdmacellinformation-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [NetworkSelectionMode(网络搜索)](arkts-telephony-radio-networkselectionmode-e.md) |
| [NetworkType(网络搜索)](arkts-telephony-radio-networktype-e.md) |
| [NsaState(网络搜索)](arkts-telephony-radio-nsastate-e.md) |
| [RadioTechnology(网络搜索)](arkts-telephony-radio-radiotechnology-e.md) |
| [RegState(网络搜索)](arkts-telephony-radio-regstate-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [ImsRegState(网络搜索)](arkts-telephony-radio-imsregstate-e-sys.md) |
| [ImsRegTech(网络搜索)](arkts-telephony-radio-imsregtech-e-sys.md) |
| [ImsServiceType(网络搜索)](arkts-telephony-radio-imsservicetype-e-sys.md) |
| [NetworkCapabilityState(网络搜索)](arkts-telephony-radio-networkcapabilitystate-e-sys.md) |
| [NetworkCapabilityType(网络搜索)](arkts-telephony-radio-networkcapabilitytype-e-sys.md) |
| [NetworkInformationState(网络搜索)](arkts-telephony-radio-networkinformationstate-e-sys.md) |
| [NrOptionMode(网络搜索)](arkts-telephony-radio-nroptionmode-e-sys.md) |
| [NROptionMode(网络搜索)](arkts-telephony-radio-nroptionmode-e-sys.md) |
| [PreferredNetworkMode(网络搜索)](arkts-telephony-radio-preferrednetworkmode-e-sys.md) |
<!--DelEnd-->
