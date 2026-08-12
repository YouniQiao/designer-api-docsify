# @ohos.telephony.radio

Provides interfaces for applications to obtain the network state, cell information, signal information,and device ID of the wireless cellular network (WCN), and provides a callback registration mechanism to listen for changes of the network, cell, and signal status of the WCN.

**Since:** 6

<!--Device-unnamed-declare namespace radio--><!--Device-unnamed-declare namespace radio-End-->

**System capability:** SystemCapability.Telephony.CoreService

## Modules to Import

```TypeScript
import { radio } from '@kit.TelephonyKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getISOCountryCodeForNetwork](arkts-telephony-radio-getisocountrycodefornetwork-f.md#getisocountrycodefornetwork) |
| [getISOCountryCodeForNetwork](arkts-telephony-radio-getisocountrycodefornetwork-f.md#getisocountrycodefornetwork-1) |
| [getISOCountryCodeForNetworkSync](arkts-telephony-radio-getisocountrycodefornetworksync-f.md#getisocountrycodefornetworksync) |
| [getNetworkSelectionMode](arkts-telephony-radio-getnetworkselectionmode-f.md#getnetworkselectionmode) |
| [getNetworkSelectionMode](arkts-telephony-radio-getnetworkselectionmode-f.md#getnetworkselectionmode-1) |
| [getNetworkState](arkts-telephony-radio-getnetworkstate-f.md#getnetworkstate) |
| [getNetworkState](arkts-telephony-radio-getnetworkstate-f.md#getnetworkstate-1) |
| [getNetworkState](arkts-telephony-radio-getnetworkstate-f.md#getnetworkstate-2) |
| [getOperatorName](arkts-telephony-radio-getoperatorname-f.md#getoperatorname) |
| [getOperatorName](arkts-telephony-radio-getoperatorname-f.md#getoperatorname-1) |
| [getOperatorNameSync](arkts-telephony-radio-getoperatornamesync-f.md#getoperatornamesync) |
| [getPrimarySlotId](arkts-telephony-radio-getprimaryslotid-f.md#getprimaryslotid) |
| [getPrimarySlotId](arkts-telephony-radio-getprimaryslotid-f.md#getprimaryslotid-1) |
| [getRadioTech](arkts-telephony-radio-getradiotech-f.md#getradiotech) |
| [getRadioTech](arkts-telephony-radio-getradiotech-f.md#getradiotech-1) |
| [getRadioTechSync](arkts-telephony-radio-getradiotechsync-f.md#getradiotechsync) |
| [getSignalInformation](arkts-telephony-radio-getsignalinformation-f.md#getsignalinformation) |
| [getSignalInformation](arkts-telephony-radio-getsignalinformation-f.md#getsignalinformation-1) |
| [getSignalInformationSync](arkts-telephony-radio-getsignalinformationsync-f.md#getsignalinformationsync) |
| [isNRSupported](arkts-telephony-radio-isnrsupported-f.md#isnrsupported) |
| [isNRSupported](arkts-telephony-radio-isnrsupported-f.md#isnrsupported-1) |
| [isNrSupported](arkts-telephony-radio-isnrsupported-f.md#isnrsupported) |
| [isNrSupported](arkts-telephony-radio-isnrsupported-f.md#isnrsupported-1) |
| [isRadioOn](arkts-telephony-radio-isradioon-f.md#isradioon) |
| [isRadioOn](arkts-telephony-radio-isradioon-f.md#isradioon-1) |
| [isRadioOn](arkts-telephony-radio-isradioon-f.md#isradioon-2) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [factoryReset](arkts-telephony-radio-factoryreset-f-sys.md#factoryreset) |
| [getBasebandVersion](arkts-telephony-radio-getbasebandversion-f-sys.md#getbasebandversion) |
| [getBasebandVersion](arkts-telephony-radio-getbasebandversion-f-sys.md#getbasebandversion-1) |
| [getCellInformation](arkts-telephony-radio-getcellinformation-f-sys.md#getcellinformation) |
| [getCellInformation](arkts-telephony-radio-getcellinformation-f-sys.md#getcellinformation-1) |
| [getCellInformation](arkts-telephony-radio-getcellinformation-f-sys.md#getcellinformation-2) |
| [getIMEI](arkts-telephony-radio-getimei-f-sys.md#getimei) |
| [getIMEI](arkts-telephony-radio-getimei-f-sys.md#getimei-1) |
| [getIMEI](arkts-telephony-radio-getimei-f-sys.md#getimei-2) |
| [getIMEISV](arkts-telephony-radio-getimeisv-f-sys.md#getimeisv) |
| [getImsRegInfo](arkts-telephony-radio-getimsreginfo-f-sys.md#getimsreginfo) |
| [getImsRegInfo](arkts-telephony-radio-getimsreginfo-f-sys.md#getimsreginfo-1) |
| [getMEID](arkts-telephony-radio-getmeid-f-sys.md#getmeid) |
| [getMEID](arkts-telephony-radio-getmeid-f-sys.md#getmeid-1) |
| [getMEID](arkts-telephony-radio-getmeid-f-sys.md#getmeid-2) |
| [getNROptionMode](arkts-telephony-radio-getnroptionmode-f-sys.md#getnroptionmode) |
| [getNROptionMode](arkts-telephony-radio-getnroptionmode-f-sys.md#getnroptionmode-1) |
| [getNetworkCapability](arkts-telephony-radio-getnetworkcapability-f-sys.md#getnetworkcapability) |
| [getNetworkCapability](arkts-telephony-radio-getnetworkcapability-f-sys.md#getnetworkcapability-1) |
| [getNetworkSearchInformation](arkts-telephony-radio-getnetworksearchinformation-f-sys.md#getnetworksearchinformation) |
| [getNetworkSearchInformation](arkts-telephony-radio-getnetworksearchinformation-f-sys.md#getnetworksearchinformation-1) |
| [getNrOptionMode](arkts-telephony-radio-getnroptionmode-f-sys.md#getnroptionmode) |
| [getNrOptionMode](arkts-telephony-radio-getnroptionmode-f-sys.md#getnroptionmode-1) |
| [getNrOptionMode](arkts-telephony-radio-getnroptionmode-f-sys.md#getnroptionmode-2) |
| [getPreferredNetwork](arkts-telephony-radio-getpreferrednetwork-f-sys.md#getpreferrednetwork) |
| [getPreferredNetwork](arkts-telephony-radio-getpreferrednetwork-f-sys.md#getpreferrednetwork-1) |
| [getUniqueDeviceId](arkts-telephony-radio-getuniquedeviceid-f-sys.md#getuniquedeviceid) |
| [getUniqueDeviceId](arkts-telephony-radio-getuniquedeviceid-f-sys.md#getuniquedeviceid-1) |
| [getUniqueDeviceId](arkts-telephony-radio-getuniquedeviceid-f-sys.md#getuniquedeviceid-2) |
| [isManualNetworkScanning](arkts-telephony-radio-ismanualnetworkscanning-f-sys.md#ismanualnetworkscanning) |
| [off](arkts-telephony-radio-off-f-sys.md#off) |
| [on](arkts-telephony-radio-on-f-sys.md#on) |
| [sendUpdateCellLocationRequest](arkts-telephony-radio-sendupdatecelllocationrequest-f-sys.md#sendupdatecelllocationrequest) |
| [sendUpdateCellLocationRequest](arkts-telephony-radio-sendupdatecelllocationrequest-f-sys.md#sendupdatecelllocationrequest-1) |
| [sendUpdateCellLocationRequest](arkts-telephony-radio-sendupdatecelllocationrequest-f-sys.md#sendupdatecelllocationrequest-2) |
| [setNROptionMode](arkts-telephony-radio-setnroptionmode-f-sys.md#setnroptionmode) |
| [setNROptionMode](arkts-telephony-radio-setnroptionmode-f-sys.md#setnroptionmode-1) |
| [setNetworkCapability](arkts-telephony-radio-setnetworkcapability-f-sys.md#setnetworkcapability) |
| [setNetworkCapability](arkts-telephony-radio-setnetworkcapability-f-sys.md#setnetworkcapability-1) |
| [setNetworkSelectionMode](arkts-telephony-radio-setnetworkselectionmode-f-sys.md#setnetworkselectionmode) |
| [setNetworkSelectionMode](arkts-telephony-radio-setnetworkselectionmode-f-sys.md#setnetworkselectionmode-1) |
| [setPreferredNetwork](arkts-telephony-radio-setpreferrednetwork-f-sys.md#setpreferrednetwork) |
| [setPreferredNetwork](arkts-telephony-radio-setpreferrednetwork-f-sys.md#setpreferrednetwork-1) |
| [setPrimarySlotId](arkts-telephony-radio-setprimaryslotid-f-sys.md#setprimaryslotid) |
| [setPrimarySlotId](arkts-telephony-radio-setprimaryslotid-f-sys.md#setprimaryslotid-1) |
| [startManualNetworkScan](arkts-telephony-radio-startmanualnetworkscan-f-sys.md#startmanualnetworkscan) |
| [stopManualNetworkScan](arkts-telephony-radio-stopmanualnetworkscan-f-sys.md#stopmanualnetworkscan) |
| [turnOffRadio](arkts-telephony-radio-turnoffradio-f-sys.md#turnoffradio) |
| [turnOffRadio](arkts-telephony-radio-turnoffradio-f-sys.md#turnoffradio-1) |
| [turnOffRadio](arkts-telephony-radio-turnoffradio-f-sys.md#turnoffradio-2) |
| [turnOnRadio](arkts-telephony-radio-turnonradio-f-sys.md#turnonradio) |
| [turnOnRadio](arkts-telephony-radio-turnonradio-f-sys.md#turnonradio-1) |
| [turnOnRadio](arkts-telephony-radio-turnonradio-f-sys.md#turnonradio-2) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CellInformation](arkts-telephony-radio-cellinformation-i.md) |
| [NetworkRadioTech](arkts-telephony-radio-networkradiotech-i.md) |
| [NetworkState](arkts-telephony-radio-networkstate-i.md) |
| [SignalInformation](arkts-telephony-radio-signalinformation-i.md) |

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CdmaCellInformation](arkts-telephony-radio-cdmacellinformation-i-sys.md) |
| [CellInformation](arkts-telephony-radio-cellinformation-i-sys.md) |
| [GsmCellInformation](arkts-telephony-radio-gsmcellinformation-i-sys.md) |
| [ImsRegInfo](arkts-telephony-radio-imsreginfo-i-sys.md) |
| [LteCellInformation](arkts-telephony-radio-ltecellinformation-i-sys.md) |
| [NetworkInformation](arkts-telephony-radio-networkinformation-i-sys.md) |
| [NetworkSearchRealTimeResult](arkts-telephony-radio-networksearchrealtimeresult-i-sys.md) |
| [NetworkSearchResult](arkts-telephony-radio-networksearchresult-i-sys.md) |
| [NetworkSelectionModeOptions](arkts-telephony-radio-networkselectionmodeoptions-i-sys.md) |
| [NrCellInformation](arkts-telephony-radio-nrcellinformation-i-sys.md) |
| [TdscdmaCellInformation](arkts-telephony-radio-tdscdmacellinformation-i-sys.md) |
| [WcdmaCellInformation](arkts-telephony-radio-wcdmacellinformation-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [NetworkSelectionMode](arkts-telephony-radio-networkselectionmode-e.md) |
| [NetworkType](arkts-telephony-radio-networktype-e.md) |
| [NsaState](arkts-telephony-radio-nsastate-e.md) |
| [RadioTechnology](arkts-telephony-radio-radiotechnology-e.md) |
| [RegState](arkts-telephony-radio-regstate-e.md) |

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ImsRegState](arkts-telephony-radio-imsregstate-e-sys.md) |
| [ImsRegTech](arkts-telephony-radio-imsregtech-e-sys.md) |
| [ImsServiceType](arkts-telephony-radio-imsservicetype-e-sys.md) |
| [NROptionMode](arkts-telephony-radio-nroptionmode-e-sys.md) |
| [NetworkCapabilityState](arkts-telephony-radio-networkcapabilitystate-e-sys.md) |
| [NetworkCapabilityType](arkts-telephony-radio-networkcapabilitytype-e-sys.md) |
| [NetworkInformationState](arkts-telephony-radio-networkinformationstate-e-sys.md) |
| [NrOptionMode](arkts-telephony-radio-nroptionmode-e-sys.md) |
| [PreferredNetworkMode](arkts-telephony-radio-preferrednetworkmode-e-sys.md) |
<!--DelEnd-->
