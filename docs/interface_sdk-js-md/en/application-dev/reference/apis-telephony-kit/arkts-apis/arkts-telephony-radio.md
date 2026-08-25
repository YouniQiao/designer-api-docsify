# @ohos.telephony.radio(Network Search)

The **radio** module provides basic network search management functions. Using the APIs provided by this module, you can obtain the radio access technology (RAT) used in the CS and PS domains, network status, current network selection mode, ISO country code of the registered network, ID of the slot in which the primary card is located, list of signal strengths of the registered network for the SIM card in the specified slot, and carrier name. Besides, you can check whether the current device supports New Radio \(NR\) and whether the radio service is enabled on the primary SIM card. The CS domain refers to the Circuit Switched domain, and the PS domain refers to the Packet Switched domain.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Telephony.CoreService

## Modules to Import

```TypeScript
import { radio } from '@kit.TelephonyKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getISOCountryCodeForNetwork(Network Search)](arkts-telephony-radio-getisocountrycodefornetwork-f.md) |
| [getISOCountryCodeForNetwork(Network Search)](arkts-telephony-radio-getisocountrycodefornetwork-f.md) |
| [getISOCountryCodeForNetworkSync(Network Search)](arkts-telephony-radio-getisocountrycodefornetworksync-f.md) |
| [getNetworkSelectionMode(Network Search)](arkts-telephony-radio-getnetworkselectionmode-f.md) |
| [getNetworkSelectionMode(Network Search)](arkts-telephony-radio-getnetworkselectionmode-f.md) |
| [getNetworkState(Network Search)](arkts-telephony-radio-getnetworkstate-f.md) |
| [getNetworkState(Network Search)](arkts-telephony-radio-getnetworkstate-f.md) |
| [getNetworkState(Network Search)](arkts-telephony-radio-getnetworkstate-f.md) |
| [getOperatorName(Network Search)](arkts-telephony-radio-getoperatorname-f.md) |
| [getOperatorName(Network Search)](arkts-telephony-radio-getoperatorname-f.md) |
| [getOperatorNameSync(Network Search)](arkts-telephony-radio-getoperatornamesync-f.md) |
| [getPrimarySlotId(Network Search)](arkts-telephony-radio-getprimaryslotid-f.md) |
| [getPrimarySlotId(Network Search)](arkts-telephony-radio-getprimaryslotid-f.md) |
| [getRadioTech(Network Search)](arkts-telephony-radio-getradiotech-f.md) |
| [getRadioTech(Network Search)](arkts-telephony-radio-getradiotech-f.md) |
| [getRadioTechSync(Network Search)](arkts-telephony-radio-getradiotechsync-f.md) |
| [getSignalInformation(Network Search)](arkts-telephony-radio-getsignalinformation-f.md) |
| [getSignalInformation(Network Search)](arkts-telephony-radio-getsignalinformation-f.md) |
| [getSignalInformationSync(Network Search)](arkts-telephony-radio-getsignalinformationsync-f.md) |
| [isNrSupported(Network Search)](arkts-telephony-radio-isnrsupported-f.md) |
| [isNrSupported(Network Search)](arkts-telephony-radio-isnrsupported-f.md) |
| [isNRSupported(Network Search)](arkts-telephony-radio-isnrsupported-f.md) |
| [isNRSupported(Network Search)](arkts-telephony-radio-isnrsupported-f.md) |
| [isRadioOn(Network Search)](arkts-telephony-radio-isradioon-f.md) |
| [isRadioOn(Network Search)](arkts-telephony-radio-isradioon-f.md) |
| [isRadioOn(Network Search)](arkts-telephony-radio-isradioon-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [factoryReset(Network Search)](arkts-telephony-radio-factoryreset-f-sys.md) |
| [getBasebandVersion(Network Search)](arkts-telephony-radio-getbasebandversion-f-sys.md) |
| [getBasebandVersion(Network Search)](arkts-telephony-radio-getbasebandversion-f-sys.md) |
| [getCellInformation(Network Search)](arkts-telephony-radio-getcellinformation-f-sys.md) |
| [getCellInformation(Network Search)](arkts-telephony-radio-getcellinformation-f-sys.md) |
| [getCellInformation(Network Search)](arkts-telephony-radio-getcellinformation-f-sys.md) |
| [getIMEI(Network Search)](arkts-telephony-radio-getimei-f-sys.md) |
| [getIMEI(Network Search)](arkts-telephony-radio-getimei-f-sys.md) |
| [getIMEI(Network Search)](arkts-telephony-radio-getimei-f-sys.md) |
| [getIMEISV(Network Search)](arkts-telephony-radio-getimeisv-f-sys.md) |
| [getImsRegInfo(Network Search)](arkts-telephony-radio-getimsreginfo-f-sys.md) |
| [getImsRegInfo(Network Search)](arkts-telephony-radio-getimsreginfo-f-sys.md) |
| [getMEID(Network Search)](arkts-telephony-radio-getmeid-f-sys.md) |
| [getMEID(Network Search)](arkts-telephony-radio-getmeid-f-sys.md) |
| [getMEID(Network Search)](arkts-telephony-radio-getmeid-f-sys.md) |
| [getNetworkCapability(Network Search)](arkts-telephony-radio-getnetworkcapability-f-sys.md) |
| [getNetworkCapability(Network Search)](arkts-telephony-radio-getnetworkcapability-f-sys.md) |
| [getNetworkSearchInformation(Network Search)](arkts-telephony-radio-getnetworksearchinformation-f-sys.md) |
| [getNetworkSearchInformation(Network Search)](arkts-telephony-radio-getnetworksearchinformation-f-sys.md) |
| [getNrOptionMode(Network Search)](arkts-telephony-radio-getnroptionmode-f-sys.md) |
| [getNrOptionMode(Network Search)](arkts-telephony-radio-getnroptionmode-f-sys.md) |
| [getNrOptionMode(Network Search)](arkts-telephony-radio-getnroptionmode-f-sys.md) |
| [getNROptionMode(Network Search)](arkts-telephony-radio-getnroptionmode-f-sys.md) |
| [getNROptionMode(Network Search)](arkts-telephony-radio-getnroptionmode-f-sys.md) |
| [getPreferredNetwork(Network Search)](arkts-telephony-radio-getpreferrednetwork-f-sys.md) |
| [getPreferredNetwork(Network Search)](arkts-telephony-radio-getpreferrednetwork-f-sys.md) |
| [getUniqueDeviceId(Network Search)](arkts-telephony-radio-getuniquedeviceid-f-sys.md) |
| [getUniqueDeviceId(Network Search)](arkts-telephony-radio-getuniquedeviceid-f-sys.md) |
| [getUniqueDeviceId(Network Search)](arkts-telephony-radio-getuniquedeviceid-f-sys.md) |
| [isManualNetworkScanning(Network Search)](arkts-telephony-radio-ismanualnetworkscanning-f-sys.md) |
| [off(Network Search)](arkts-telephony-radio-off-f-sys.md#offimsregstatechange) |
| [offImsRegStateChange(Network Search)](arkts-telephony-radio-offimsregstatechange-f-sys.md) |
| [on(Network Search)](arkts-telephony-radio-on-f-sys.md#onimsregstatechange) |
| [onImsRegStateChange(Network Search)](arkts-telephony-radio-onimsregstatechange-f-sys.md) |
| [sendUpdateCellLocationRequest(Network Search)](arkts-telephony-radio-sendupdatecelllocationrequest-f-sys.md) |
| [sendUpdateCellLocationRequest(Network Search)](arkts-telephony-radio-sendupdatecelllocationrequest-f-sys.md) |
| [sendUpdateCellLocationRequest(Network Search)](arkts-telephony-radio-sendupdatecelllocationrequest-f-sys.md) |
| [setNetworkCapability(Network Search)](arkts-telephony-radio-setnetworkcapability-f-sys.md) |
| [setNetworkCapability(Network Search)](arkts-telephony-radio-setnetworkcapability-f-sys.md) |
| [setNetworkSelectionMode(Network Search)](arkts-telephony-radio-setnetworkselectionmode-f-sys.md) |
| [setNetworkSelectionMode(Network Search)](arkts-telephony-radio-setnetworkselectionmode-f-sys.md) |
| [setNROptionMode(Network Search)](arkts-telephony-radio-setnroptionmode-f-sys.md) |
| [setNROptionMode(Network Search)](arkts-telephony-radio-setnroptionmode-f-sys.md) |
| [setPreferredNetwork(Network Search)](arkts-telephony-radio-setpreferrednetwork-f-sys.md) |
| [setPreferredNetwork(Network Search)](arkts-telephony-radio-setpreferrednetwork-f-sys.md) |
| [setPrimarySlotId(Network Search)](arkts-telephony-radio-setprimaryslotid-f-sys.md) |
| [setPrimarySlotId(Network Search)](arkts-telephony-radio-setprimaryslotid-f-sys.md) |
| [startManualNetworkScan(Network Search)](arkts-telephony-radio-startmanualnetworkscan-f-sys.md) |
| [stopManualNetworkScan(Network Search)](arkts-telephony-radio-stopmanualnetworkscan-f-sys.md) |
| [turnOffRadio(Network Search)](arkts-telephony-radio-turnoffradio-f-sys.md) |
| [turnOffRadio(Network Search)](arkts-telephony-radio-turnoffradio-f-sys.md) |
| [turnOffRadio(Network Search)](arkts-telephony-radio-turnoffradio-f-sys.md) |
| [turnOnRadio(Network Search)](arkts-telephony-radio-turnonradio-f-sys.md) |
| [turnOnRadio(Network Search)](arkts-telephony-radio-turnonradio-f-sys.md) |
| [turnOnRadio(Network Search)](arkts-telephony-radio-turnonradio-f-sys.md) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CellInformation(Network Search)](arkts-telephony-radio-cellinformation-i.md) |
| [NetworkRadioTech(Network Search)](arkts-telephony-radio-networkradiotech-i.md) |
| [NetworkState(Network Search)](arkts-telephony-radio-networkstate-i.md) |
| [SignalInformation(Network Search)](arkts-telephony-radio-signalinformation-i.md) |

<!--Del-->
### Interfaces(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CdmaCellInformation(Network Search)](arkts-telephony-radio-cdmacellinformation-i-sys.md) |
| [CellInformation(Network Search)](arkts-telephony-radio-cellinformation-i-sys.md) |
| [GsmCellInformation(Network Search)](arkts-telephony-radio-gsmcellinformation-i-sys.md) |
| [ImsRegInfo(Network Search)](arkts-telephony-radio-imsreginfo-i-sys.md) |
| [LteCellInformation(Network Search)](arkts-telephony-radio-ltecellinformation-i-sys.md) |
| [NetworkInformation(Network Search)](arkts-telephony-radio-networkinformation-i-sys.md) |
| [NetworkSearchRealTimeResult(Network Search)](arkts-telephony-radio-networksearchrealtimeresult-i-sys.md) |
| [NetworkSearchResult(Network Search)](arkts-telephony-radio-networksearchresult-i-sys.md) |
| [NetworkSelectionModeOptions(Network Search)](arkts-telephony-radio-networkselectionmodeoptions-i-sys.md) |
| [NrCellInformation(Network Search)](arkts-telephony-radio-nrcellinformation-i-sys.md) |
| [TdscdmaCellInformation(Network Search)](arkts-telephony-radio-tdscdmacellinformation-i-sys.md) |
| [WcdmaCellInformation(Network Search)](arkts-telephony-radio-wcdmacellinformation-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [NetworkSelectionMode(Network Search)](arkts-telephony-radio-networkselectionmode-e.md) |
| [NetworkType(Network Search)](arkts-telephony-radio-networktype-e.md) |
| [NsaState(Network Search)](arkts-telephony-radio-nsastate-e.md) |
| [RadioTechnology(Network Search)](arkts-telephony-radio-radiotechnology-e.md) |
| [RegState(Network Search)](arkts-telephony-radio-regstate-e.md) |

<!--Del-->
### Enums(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ImsRegState(Network Search)](arkts-telephony-radio-imsregstate-e-sys.md) |
| [ImsRegTech(Network Search)](arkts-telephony-radio-imsregtech-e-sys.md) |
| [ImsServiceType(Network Search)](arkts-telephony-radio-imsservicetype-e-sys.md) |
| [NetworkCapabilityState(Network Search)](arkts-telephony-radio-networkcapabilitystate-e-sys.md) |
| [NetworkCapabilityType(Network Search)](arkts-telephony-radio-networkcapabilitytype-e-sys.md) |
| [NetworkInformationState(Network Search)](arkts-telephony-radio-networkinformationstate-e-sys.md) |
| [NrOptionMode(Network Search)](arkts-telephony-radio-nroptionmode-e-sys.md) |
| [NROptionMode(Network Search)](arkts-telephony-radio-nroptionmode-e-sys.md) |
| [PreferredNetworkMode(Network Search)](arkts-telephony-radio-preferrednetworkmode-e-sys.md) |
<!--DelEnd-->
