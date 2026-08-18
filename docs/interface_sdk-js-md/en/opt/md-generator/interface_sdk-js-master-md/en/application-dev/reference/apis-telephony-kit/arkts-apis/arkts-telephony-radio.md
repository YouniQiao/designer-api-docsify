# @ohos.telephony.radio

Provides interfaces for applications to obtain the network state, cell information, signal information, and device ID of the wireless cellular network (WCN), and provides a callback registration mechanism to listen for changes of the network, cell, and signal status of the WCN.

**Since:** 23

<!--Device-unnamed-declare namespace radio--><!--Device-unnamed-declare namespace radio-End-->

**System capability:** SystemCapability.Telephony.CoreService

## Modules to Import

```TypeScript
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getISOCountryCodeForNetwork](arkts-telephony-radio-getisocountrycodefornetwork-f.md#getisocountrycodefornetwork) |
| [getISOCountryCodeForNetwork](arkts-telephony-radio-getisocountrycodefornetwork-f.md#getisocountrycodefornetwork) |
| [getISOCountryCodeForNetworkSync](arkts-telephony-radio-getisocountrycodefornetworksync-f.md#getisocountrycodefornetworksync) |
| [getNetworkSelectionMode](arkts-telephony-radio-getnetworkselectionmode-f.md#getnetworkselectionmode) |
| [getNetworkSelectionMode](arkts-telephony-radio-getnetworkselectionmode-f.md#getnetworkselectionmode) |
| [getNetworkState](arkts-telephony-radio-getnetworkstate-f.md#getnetworkstate) |
| [getNetworkState](arkts-telephony-radio-getnetworkstate-f.md#getnetworkstate) |
| [getNetworkState](arkts-telephony-radio-getnetworkstate-f.md#getnetworkstate) |
| [getOperatorName](arkts-telephony-radio-getoperatorname-f.md#getoperatorname) |
| [getOperatorName](arkts-telephony-radio-getoperatorname-f.md#getoperatorname) |
| [getOperatorNameSync](arkts-telephony-radio-getoperatornamesync-f.md#getoperatornamesync) |
| [getPrimarySlotId](arkts-telephony-radio-getprimaryslotid-f.md#getprimaryslotid) |
| [getPrimarySlotId](arkts-telephony-radio-getprimaryslotid-f.md#getprimaryslotid) |
| [getRadioTech](arkts-telephony-radio-getradiotech-f.md#getradiotech) |
| [getRadioTech](arkts-telephony-radio-getradiotech-f.md#getradiotech) |
| [getRadioTechSync](arkts-telephony-radio-getradiotechsync-f.md#getradiotechsync) |
| [getSignalInformation](arkts-telephony-radio-getsignalinformation-f.md#getsignalinformation) |
| [getSignalInformation](arkts-telephony-radio-getsignalinformation-f.md#getsignalinformation) |
| [getSignalInformationSync](arkts-telephony-radio-getsignalinformationsync-f.md#getsignalinformationsync) |
| [isNRSupported](arkts-telephony-radio-isnrsupported-f.md#isnrsupported) |
| [isNRSupported](arkts-telephony-radio-isnrsupported-f.md#isnrsupported) |
| [isNrSupported](arkts-telephony-radio-isnrsupported-f.md#isnrsupported) |
| [isNrSupported](arkts-telephony-radio-isnrsupported-f.md#isnrsupported) |
| [isRadioOn](arkts-telephony-radio-isradioon-f.md#isradioon) |
| [isRadioOn](arkts-telephony-radio-isradioon-f.md#isradioon) |
| [isRadioOn](arkts-telephony-radio-isradioon-f.md#isradioon) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [factoryReset](arkts-telephony-radio-factoryreset-f-sys.md#factoryreset-system-api) |
| [getBasebandVersion](arkts-telephony-radio-getbasebandversion-f-sys.md#getbasebandversion-system-api) |
| [getBasebandVersion](arkts-telephony-radio-getbasebandversion-f-sys.md#getbasebandversion-system-api) |
| [getCellInformation](arkts-telephony-radio-getcellinformation-f-sys.md#getcellinformation-system-api) |
| [getCellInformation](arkts-telephony-radio-getcellinformation-f-sys.md#getcellinformation-system-api) |
| [getCellInformation](arkts-telephony-radio-getcellinformation-f-sys.md#getcellinformation-system-api) |
| [getIMEI](arkts-telephony-radio-getimei-f-sys.md#getimei-system-api) |
| [getIMEI](arkts-telephony-radio-getimei-f-sys.md#getimei-system-api) |
| [getIMEI](arkts-telephony-radio-getimei-f-sys.md#getimei-system-api) |
| [getIMEISV](arkts-telephony-radio-getimeisv-f-sys.md#getimeisv-system-api) |
| [getImsRegInfo](arkts-telephony-radio-getimsreginfo-f-sys.md#getimsreginfo-system-api) |
| [getImsRegInfo](arkts-telephony-radio-getimsreginfo-f-sys.md#getimsreginfo-system-api) |
| [getMEID](arkts-telephony-radio-getmeid-f-sys.md#getmeid-system-api) |
| [getMEID](arkts-telephony-radio-getmeid-f-sys.md#getmeid-system-api) |
| [getMEID](arkts-telephony-radio-getmeid-f-sys.md#getmeid-system-api) |
| [getNROptionMode](arkts-telephony-radio-getnroptionmode-f-sys.md) |
| [getNROptionMode](arkts-telephony-radio-getnroptionmode-f-sys.md#getnroptionmode) |
| [getNetworkCapability](arkts-telephony-radio-getnetworkcapability-f-sys.md#getnetworkcapability-system-api) |
| [getNetworkCapability](arkts-telephony-radio-getnetworkcapability-f-sys.md#getnetworkcapability-system-api) |
| [getNetworkSearchInformation](arkts-telephony-radio-getnetworksearchinformation-f-sys.md#getnetworksearchinformation-system-api) |
| [getNetworkSearchInformation](arkts-telephony-radio-getnetworksearchinformation-f-sys.md#getnetworksearchinformation-system-api) |
| [getNrOptionMode](arkts-telephony-radio-getnroptionmode-f-sys.md) |
| [getNrOptionMode](arkts-telephony-radio-getnroptionmode-f-sys.md#getnroptionmode) |
| [getNrOptionMode](arkts-telephony-radio-getnroptionmode-f-sys.md#getnroptionmode) |
| [getPreferredNetwork](arkts-telephony-radio-getpreferrednetwork-f-sys.md#getpreferrednetwork-system-api) |
| [getPreferredNetwork](arkts-telephony-radio-getpreferrednetwork-f-sys.md#getpreferrednetwork-system-api) |
| [getUniqueDeviceId](arkts-telephony-radio-getuniquedeviceid-f-sys.md#getuniquedeviceid-system-api) |
| [getUniqueDeviceId](arkts-telephony-radio-getuniquedeviceid-f-sys.md#getuniquedeviceid-system-api) |
| [getUniqueDeviceId](arkts-telephony-radio-getuniquedeviceid-f-sys.md#getuniquedeviceid-system-api) |
| [isManualNetworkScanning](arkts-telephony-radio-ismanualnetworkscanning-f-sys.md#ismanualnetworkscanning-system-api) |
| [offImsRegStateChange](arkts-telephony-radio-offimsregstatechange-f-sys.md#offimsregstatechange) |
| [off_imsRegStateChange](arkts-telephony-radio-offimsregstatechange-f-sys.md#offimsregstatechange) |
| [onImsRegStateChange](arkts-telephony-radio-onimsregstatechange-f-sys.md#onimsregstatechange) |
| [on_imsRegStateChange](arkts-telephony-radio-onimsregstatechange-f-sys.md#onimsregstatechange) |
| [sendUpdateCellLocationRequest](arkts-telephony-radio-sendupdatecelllocationrequest-f-sys.md#sendupdatecelllocationrequest-system-api) |
| [sendUpdateCellLocationRequest](arkts-telephony-radio-sendupdatecelllocationrequest-f-sys.md#sendupdatecelllocationrequest-system-api) |
| [sendUpdateCellLocationRequest](arkts-telephony-radio-sendupdatecelllocationrequest-f-sys.md#sendupdatecelllocationrequest-system-api) |
| [setNROptionMode](arkts-telephony-radio-setnroptionmode-f-sys.md#setnroptionmode-system-api) |
| [setNROptionMode](arkts-telephony-radio-setnroptionmode-f-sys.md#setnroptionmode-system-api) |
| [setNetworkCapability](arkts-telephony-radio-setnetworkcapability-f-sys.md#setnetworkcapability-system-api) |
| [setNetworkCapability](arkts-telephony-radio-setnetworkcapability-f-sys.md#setnetworkcapability-system-api) |
| [setNetworkSelectionMode](arkts-telephony-radio-setnetworkselectionmode-f-sys.md#setnetworkselectionmode-system-api) |
| [setNetworkSelectionMode](arkts-telephony-radio-setnetworkselectionmode-f-sys.md#setnetworkselectionmode-system-api) |
| [setPreferredNetwork](arkts-telephony-radio-setpreferrednetwork-f-sys.md#setpreferrednetwork-system-api) |
| [setPreferredNetwork](arkts-telephony-radio-setpreferrednetwork-f-sys.md#setpreferrednetwork-system-api) |
| [setPrimarySlotId](arkts-telephony-radio-setprimaryslotid-f-sys.md#setprimaryslotid-system-api) |
| [setPrimarySlotId](arkts-telephony-radio-setprimaryslotid-f-sys.md#setprimaryslotid-system-api) |
| [startManualNetworkScan](arkts-telephony-radio-startmanualnetworkscan-f-sys.md#startmanualnetworkscan-system-api) |
| [stopManualNetworkScan](arkts-telephony-radio-stopmanualnetworkscan-f-sys.md#stopmanualnetworkscan-system-api) |
| [turnOffRadio](arkts-telephony-radio-turnoffradio-f-sys.md#turnoffradio-system-api) |
| [turnOffRadio](arkts-telephony-radio-turnoffradio-f-sys.md#turnoffradio-system-api) |
| [turnOffRadio](arkts-telephony-radio-turnoffradio-f-sys.md#turnoffradio-system-api) |
| [turnOnRadio](arkts-telephony-radio-turnonradio-f-sys.md#turnonradio-system-api) |
| [turnOnRadio](arkts-telephony-radio-turnonradio-f-sys.md#turnonradio-system-api) |
| [turnOnRadio](arkts-telephony-radio-turnonradio-f-sys.md#turnonradio-system-api) |
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
