# @ohos.telephony.radio

Provides interfaces for applications to obtain the network state, cell information, signal information, and device ID of the wireless cellular network (WCN), and provides a callback registration mechanism to listen for changes of the network, cell, and signal status of the WCN.

**Since:** 23

**Deprecated since:** -1

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
| [getISOCountryCodeForNetwork](arkts-telephony-radio-getisocountrycodefornetwork-f.md#getISOCountryCodeForNetwork) |
| [getISOCountryCodeForNetwork](arkts-telephony-radio-getisocountrycodefornetwork-f.md#getISOCountryCodeForNetwork) |
| [getISOCountryCodeForNetworkSync](arkts-telephony-radio-getisocountrycodefornetworksync-f.md#getISOCountryCodeForNetworkSync) |
| [getNetworkSelectionMode](arkts-telephony-radio-getnetworkselectionmode-f.md#getNetworkSelectionMode) |
| [getNetworkSelectionMode](arkts-telephony-radio-getnetworkselectionmode-f.md#getNetworkSelectionMode) |
| [getNetworkState](arkts-telephony-radio-getnetworkstate-f.md#getNetworkState) |
| [getNetworkState](arkts-telephony-radio-getnetworkstate-f.md#getNetworkState) |
| [getNetworkState](arkts-telephony-radio-getnetworkstate-f.md#getNetworkState) |
| [getOperatorName](arkts-telephony-radio-getoperatorname-f.md#getOperatorName) |
| [getOperatorName](arkts-telephony-radio-getoperatorname-f.md#getOperatorName) |
| [getOperatorNameSync](arkts-telephony-radio-getoperatornamesync-f.md#getOperatorNameSync) |
| [getPrimarySlotId](arkts-telephony-radio-getprimaryslotid-f.md#getPrimarySlotId) |
| [getPrimarySlotId](arkts-telephony-radio-getprimaryslotid-f.md#getPrimarySlotId) |
| [getRadioTech](arkts-telephony-radio-getradiotech-f.md#getRadioTech) |
| [getRadioTech](arkts-telephony-radio-getradiotech-f.md#getRadioTech) |
| [getRadioTechSync](arkts-telephony-radio-getradiotechsync-f.md#getRadioTechSync) |
| [getSignalInformation](arkts-telephony-radio-getsignalinformation-f.md#getSignalInformation) |
| [getSignalInformation](arkts-telephony-radio-getsignalinformation-f.md#getSignalInformation) |
| [getSignalInformationSync](arkts-telephony-radio-getsignalinformationsync-f.md#getSignalInformationSync) |
| [isNRSupported](arkts-telephony-radio-isnrsupported-f.md) |
| [isNRSupported](arkts-telephony-radio-isnrsupported-f.md#isNRSupported) |
| [isNrSupported](arkts-telephony-radio-isnrsupported-f.md) |
| [isNrSupported](arkts-telephony-radio-isnrsupported-f.md#isNRSupported) |
| [isRadioOn](arkts-telephony-radio-isradioon-f.md#isRadioOn) |
| [isRadioOn](arkts-telephony-radio-isradioon-f.md#isRadioOn) |
| [isRadioOn](arkts-telephony-radio-isradioon-f.md#isRadioOn) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [factoryReset](arkts-telephony-radio-factoryreset-f-sys.md#factoryReset-(System-API)) |
| [getBasebandVersion](arkts-telephony-radio-getbasebandversion-f-sys.md#getBasebandVersion-(System-API)) |
| [getBasebandVersion](arkts-telephony-radio-getbasebandversion-f-sys.md#getBasebandVersion-(System-API)) |
| [getCellInformation](arkts-telephony-radio-getcellinformation-f-sys.md#getCellInformation-(System-API)) |
| [getCellInformation](arkts-telephony-radio-getcellinformation-f-sys.md#getCellInformation-(System-API)) |
| [getCellInformation](arkts-telephony-radio-getcellinformation-f-sys.md#getCellInformation-(System-API)) |
| [getIMEI](arkts-telephony-radio-getimei-f-sys.md#getIMEI-(System-API)) |
| [getIMEI](arkts-telephony-radio-getimei-f-sys.md#getIMEI-(System-API)) |
| [getIMEI](arkts-telephony-radio-getimei-f-sys.md#getIMEI-(System-API)) |
| [getIMEISV](arkts-telephony-radio-getimeisv-f-sys.md#getIMEISV-(System-API)) |
| [getImsRegInfo](arkts-telephony-radio-getimsreginfo-f-sys.md#getImsRegInfo-(System-API)) |
| [getImsRegInfo](arkts-telephony-radio-getimsreginfo-f-sys.md#getImsRegInfo-(System-API)) |
| [getMEID](arkts-telephony-radio-getmeid-f-sys.md#getMEID-(System-API)) |
| [getMEID](arkts-telephony-radio-getmeid-f-sys.md#getMEID-(System-API)) |
| [getMEID](arkts-telephony-radio-getmeid-f-sys.md#getMEID-(System-API)) |
| [getNROptionMode](arkts-telephony-radio-getnroptionmode-f-sys.md) |
| [getNROptionMode](arkts-telephony-radio-getnroptionmode-f-sys.md#getNROptionMode) |
| [getNetworkCapability](arkts-telephony-radio-getnetworkcapability-f-sys.md#getNetworkCapability-(System-API)) |
| [getNetworkCapability](arkts-telephony-radio-getnetworkcapability-f-sys.md#getNetworkCapability-(System-API)) |
| [getNetworkSearchInformation](arkts-telephony-radio-getnetworksearchinformation-f-sys.md#getNetworkSearchInformation-(System-API)) |
| [getNetworkSearchInformation](arkts-telephony-radio-getnetworksearchinformation-f-sys.md#getNetworkSearchInformation-(System-API)) |
| [getNrOptionMode](arkts-telephony-radio-getnroptionmode-f-sys.md) |
| [getNrOptionMode](arkts-telephony-radio-getnroptionmode-f-sys.md#getNROptionMode) |
| [getNrOptionMode](arkts-telephony-radio-getnroptionmode-f-sys.md#getNROptionMode) |
| [getPreferredNetwork](arkts-telephony-radio-getpreferrednetwork-f-sys.md#getPreferredNetwork-(System-API)) |
| [getPreferredNetwork](arkts-telephony-radio-getpreferrednetwork-f-sys.md#getPreferredNetwork-(System-API)) |
| [getUniqueDeviceId](arkts-telephony-radio-getuniquedeviceid-f-sys.md#getUniqueDeviceId-(System-API)) |
| [getUniqueDeviceId](arkts-telephony-radio-getuniquedeviceid-f-sys.md#getUniqueDeviceId-(System-API)) |
| [getUniqueDeviceId](arkts-telephony-radio-getuniquedeviceid-f-sys.md#getUniqueDeviceId-(System-API)) |
| [isManualNetworkScanning](arkts-telephony-radio-ismanualnetworkscanning-f-sys.md#isManualNetworkScanning-(System-API)) |
| [offImsRegStateChange](arkts-telephony-radio-offimsregstatechange-f-sys.md#offImsRegStateChange-(System-API)) |
| [off_imsRegStateChange](arkts-telephony-radio-offimsregstatechange-f-sys.md) |
| [onImsRegStateChange](arkts-telephony-radio-onimsregstatechange-f-sys.md#onImsRegStateChange-(System-API)) |
| [on_imsRegStateChange](arkts-telephony-radio-onimsregstatechange-f-sys.md) |
| [sendUpdateCellLocationRequest](arkts-telephony-radio-sendupdatecelllocationrequest-f-sys.md#sendUpdateCellLocationRequest-(System-API)) |
| [sendUpdateCellLocationRequest](arkts-telephony-radio-sendupdatecelllocationrequest-f-sys.md#sendUpdateCellLocationRequest-(System-API)) |
| [sendUpdateCellLocationRequest](arkts-telephony-radio-sendupdatecelllocationrequest-f-sys.md#sendUpdateCellLocationRequest-(System-API)) |
| [setNROptionMode](arkts-telephony-radio-setnroptionmode-f-sys.md#setNROptionMode-(System-API)) |
| [setNROptionMode](arkts-telephony-radio-setnroptionmode-f-sys.md#setNROptionMode-(System-API)) |
| [setNetworkCapability](arkts-telephony-radio-setnetworkcapability-f-sys.md#setNetworkCapability-(System-API)) |
| [setNetworkCapability](arkts-telephony-radio-setnetworkcapability-f-sys.md#setNetworkCapability-(System-API)) |
| [setNetworkSelectionMode](arkts-telephony-radio-setnetworkselectionmode-f-sys.md#setNetworkSelectionMode-(System-API)) |
| [setNetworkSelectionMode](arkts-telephony-radio-setnetworkselectionmode-f-sys.md#setNetworkSelectionMode-(System-API)) |
| [setPreferredNetwork](arkts-telephony-radio-setpreferrednetwork-f-sys.md#setPreferredNetwork-(System-API)) |
| [setPreferredNetwork](arkts-telephony-radio-setpreferrednetwork-f-sys.md#setPreferredNetwork-(System-API)) |
| [setPrimarySlotId](arkts-telephony-radio-setprimaryslotid-f-sys.md#setPrimarySlotId-(System-API)) |
| [setPrimarySlotId](arkts-telephony-radio-setprimaryslotid-f-sys.md#setPrimarySlotId-(System-API)) |
| [startManualNetworkScan](arkts-telephony-radio-startmanualnetworkscan-f-sys.md#startManualNetworkScan-(System-API)) |
| [stopManualNetworkScan](arkts-telephony-radio-stopmanualnetworkscan-f-sys.md#stopManualNetworkScan-(System-API)) |
| [turnOffRadio](arkts-telephony-radio-turnoffradio-f-sys.md#turnOffRadio-(System-API)) |
| [turnOffRadio](arkts-telephony-radio-turnoffradio-f-sys.md#turnOffRadio-(System-API)) |
| [turnOffRadio](arkts-telephony-radio-turnoffradio-f-sys.md#turnOffRadio-(System-API)) |
| [turnOnRadio](arkts-telephony-radio-turnonradio-f-sys.md#turnOnRadio-(System-API)) |
| [turnOnRadio](arkts-telephony-radio-turnonradio-f-sys.md#turnOnRadio-(System-API)) |
| [turnOnRadio](arkts-telephony-radio-turnonradio-f-sys.md#turnOnRadio-(System-API)) |
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
