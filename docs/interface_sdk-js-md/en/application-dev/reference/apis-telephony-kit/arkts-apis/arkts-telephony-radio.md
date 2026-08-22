# @ohos.telephony.radio

Provides interfaces for applications to obtain the network state, cell information, signal information, and device ID of the wireless cellular network (WCN), and provides a callback registration mechanism to listen for changes of the network, cell, and signal status of the WCN.

@namespace radio

**Since:** 23

<!--Device-unnamed-declare namespace radio--><!--Device-unnamed-declare namespace radio-End-->

**System capability:** SystemCapability.Telephony.CoreService

## Modules to Import

```TypeScript
import { radio } from '@kit.TelephonyKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getISOCountryCodeForNetwork](arkts-telephony-radio-getisocountrycodefornetwork-f.md) | Obtains the ISO-defined country code of the country where the registered network is deployed. |
| [getISOCountryCodeForNetwork](arkts-telephony-radio-getisocountrycodefornetwork-f.md) | Obtains the ISO-defined country code of the country where the registered network is deployed. |
| [getISOCountryCodeForNetworkSync](arkts-telephony-radio-getisocountrycodefornetworksync-f.md) | Obtains the ISO-defined country code of the country where the registered network is deployed. |
| [getNetworkSelectionMode](arkts-telephony-radio-getnetworkselectionmode-f.md) | Obtains the network search mode of the SIM card in a specified slot. |
| [getNetworkSelectionMode](arkts-telephony-radio-getnetworkselectionmode-f.md) | Obtains the network search mode of the SIM card in a specified slot. |
| [getNetworkState](arkts-telephony-radio-getnetworkstate-f.md) | Obtains the network state of the registered network. |
| [getNetworkState](arkts-telephony-radio-getnetworkstate-f.md) | Obtains the network state of the registered network. |
| [getNetworkState](arkts-telephony-radio-getnetworkstate-f.md) | Obtains the network state of the registered network. |
| [getOperatorName](arkts-telephony-radio-getoperatorname-f.md) | Get the operator name of the specified SIM card slot. |
| [getOperatorName](arkts-telephony-radio-getoperatorname-f.md) | Get the operator name of the specified SIM card slot. |
| [getOperatorNameSync](arkts-telephony-radio-getoperatornamesync-f.md) | Get the operator name of the specified SIM card slot. |
| [getPrimarySlotId](arkts-telephony-radio-getprimaryslotid-f.md) | Obtains the index number of the card slot where the primary card is located if multiple SIM cards are inserted. |
| [getPrimarySlotId](arkts-telephony-radio-getprimaryslotid-f.md) | Obtains the index number of the card slot where the primary card is located if multiple SIM cards are inserted. |
| [getRadioTech](arkts-telephony-radio-getradiotech-f.md) | Obtains radio access technology (RAT) of the registered network. The system returns RAT of the packet service (PS) and circuit service (CS) domain. |
| [getRadioTech](arkts-telephony-radio-getradiotech-f.md) | Obtains radio access technology (RAT) of the registered network. The system returns RAT of the packet service (PS) and circuit service (CS) domain. |
| [getRadioTechSync](arkts-telephony-radio-getradiotechsync-f.md) | Obtains radio access technology (RAT) of the registered network. |
| [getSignalInformation](arkts-telephony-radio-getsignalinformation-f.md) | Obtains the list of signal strength information of the registered network corresponding to a specified SIM card. |
| [getSignalInformation](arkts-telephony-radio-getsignalinformation-f.md) | Obtains the list of signal strength information of the registered network corresponding to a specified SIM card. |
| [getSignalInformationSync](arkts-telephony-radio-getsignalinformationsync-f.md) | Obtains the list of signal strength information of the registered network corresponding to a specified SIM card. |
| [isNrSupported](arkts-telephony-radio-isnrsupported-f.md) | Checks whether the device supports 5G New Radio (NR). |
| [isNrSupported](arkts-telephony-radio-isnrsupported-f.md) | Checks whether the device supports 5G New Radio (NR) by according card slot. |
| [isNRSupported](arkts-telephony-radio-isnrsupported-f.md) | Checks whether the device supports 5G New Radio (NR). |
| [isNRSupported](arkts-telephony-radio-isnrsupported-f.md) | Checks whether the device supports 5G New Radio (NR) by according card slot. |
| [isRadioOn](arkts-telephony-radio-isradioon-f.md) | Checks whether the radio service is enabled. |
| [isRadioOn](arkts-telephony-radio-isradioon-f.md) | Checks whether the radio service is enabled. |
| [isRadioOn](arkts-telephony-radio-isradioon-f.md) | Checks whether the radio service is enabled. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [factoryReset](arkts-telephony-radio-factoryreset-f-sys.md) | Reset all network settings of telephony. |
| [getBasebandVersion](arkts-telephony-radio-getbasebandversion-f-sys.md) | Get the version of Baseband. |
| [getBasebandVersion](arkts-telephony-radio-getbasebandversion-f-sys.md) | Get the version of Baseband. |
| [getCellInformation](arkts-telephony-radio-getcellinformation-f-sys.md) | Get the current cell information. |
| [getCellInformation](arkts-telephony-radio-getcellinformation-f-sys.md) | Get the current cell information. |
| [getCellInformation](arkts-telephony-radio-getcellinformation-f-sys.md) | Get the current cell information. |
| [getIMEI](arkts-telephony-radio-getimei-f-sys.md) | Obtains the IMEI of a specified card slot of the device. |
| [getIMEI](arkts-telephony-radio-getimei-f-sys.md) | Obtains the IMEI of a specified card slot of the device. |
| [getIMEI](arkts-telephony-radio-getimei-f-sys.md) | Obtains the IMEI of a specified card slot of the device. |
| [getIMEISV](arkts-telephony-radio-getimeisv-f-sys.md) | Obtains the software version number of a specified card slot of the device. |
| [getImsRegInfo](arkts-telephony-radio-getimsreginfo-f-sys.md) | Get the IMS registration state info of specified IMS service type. |
| [getImsRegInfo](arkts-telephony-radio-getimsreginfo-f-sys.md) | Get the IMS registration state info of specified IMS service type. |
| [getMEID](arkts-telephony-radio-getmeid-f-sys.md) | Obtains the MEID of a specified card slot of the device. |
| [getMEID](arkts-telephony-radio-getmeid-f-sys.md) | Obtains the MEID of a specified card slot of the device. |
| [getMEID](arkts-telephony-radio-getmeid-f-sys.md) | Obtains the MEID of a specified card slot of the device. |
| [getNetworkCapability](arkts-telephony-radio-getnetworkcapability-f-sys.md) | Get the network capability state according to the specified capability type. |
| [getNetworkCapability](arkts-telephony-radio-getnetworkcapability-f-sys.md) | Get the network capability state according to the specified capability type. |
| [getNetworkSearchInformation](arkts-telephony-radio-getnetworksearchinformation-f-sys.md) | Get network search information. |
| [getNetworkSearchInformation](arkts-telephony-radio-getnetworksearchinformation-f-sys.md) | Get network search information. |
| [getNrOptionMode](arkts-telephony-radio-getnroptionmode-f-sys.md) | Get the option mode of NR. |
| [getNrOptionMode](arkts-telephony-radio-getnroptionmode-f-sys.md) | Get the option mode of NR. |
| [getNrOptionMode](arkts-telephony-radio-getnroptionmode-f-sys.md) | Get the option mode of NR. |
| [getNROptionMode](arkts-telephony-radio-getnroptionmode-f-sys.md) | Get the option mode of NR. |
| [getNROptionMode](arkts-telephony-radio-getnroptionmode-f-sys.md) | Get the option mode of NR. |
| [getPreferredNetwork](arkts-telephony-radio-getpreferrednetwork-f-sys.md) | Get the preferred network for the specified SIM card slot. |
| [getPreferredNetwork](arkts-telephony-radio-getpreferrednetwork-f-sys.md) | Get the preferred network for the specified SIM card slot. |
| [getUniqueDeviceId](arkts-telephony-radio-getuniquedeviceid-f-sys.md) | Obtains the unique device ID of a specified card slot of the device. |
| [getUniqueDeviceId](arkts-telephony-radio-getuniquedeviceid-f-sys.md) | Obtains the unique device ID of a specified card slot of the device. |
| [getUniqueDeviceId](arkts-telephony-radio-getuniquedeviceid-f-sys.md) | Obtains the unique device ID of a specified card slot of the device. |
| [isManualNetworkScanning](arkts-telephony-radio-ismanualnetworkscanning-f-sys.md) | Determine whether the current manual network scan is in progress. |
| [off_imsRegStateChange](arkts-telephony-radio-offimsregstatechange-f-sys.md) | Unsubscribe from imsRegStateChange event. |
| [offImsRegStateChange](arkts-telephony-radio-offimsregstatechange-f-sys.md) | Unsubscribe from imsRegStateChange event. |
| [on_imsRegStateChange](arkts-telephony-radio-onimsregstatechange-f-sys.md) | Called when the IMS registration state of specified IMS service type corresponding to a monitored {@code slotId} updates. |
| [onImsRegStateChange](arkts-telephony-radio-onimsregstatechange-f-sys.md) | Called when the IMS registration state of specified IMS service type corresponding to a monitored {@code slotId} updates. |
| [sendUpdateCellLocationRequest](arkts-telephony-radio-sendupdatecelllocationrequest-f-sys.md) | Actively requests to update location information. |
| [sendUpdateCellLocationRequest](arkts-telephony-radio-sendupdatecelllocationrequest-f-sys.md) | Actively requests to update location information. |
| [sendUpdateCellLocationRequest](arkts-telephony-radio-sendupdatecelllocationrequest-f-sys.md) | Actively requests to update location information. |
| [setNetworkCapability](arkts-telephony-radio-setnetworkcapability-f-sys.md) | Set the type and state for the specified network capability. |
| [setNetworkCapability](arkts-telephony-radio-setnetworkcapability-f-sys.md) | Set the type and state for the specified network capability. |
| [setNetworkSelectionMode](arkts-telephony-radio-setnetworkselectionmode-f-sys.md) | Set the current network selection mode. |
| [setNetworkSelectionMode](arkts-telephony-radio-setnetworkselectionmode-f-sys.md) | Set the current network selection mode. |
| [setNROptionMode](arkts-telephony-radio-setnroptionmode-f-sys.md) | Set the NR option mode. |
| [setNROptionMode](arkts-telephony-radio-setnroptionmode-f-sys.md) | Set the NR option mode. |
| [setPreferredNetwork](arkts-telephony-radio-setpreferrednetwork-f-sys.md) | Set the preferred network for the specified SIM card slot. |
| [setPreferredNetwork](arkts-telephony-radio-setpreferrednetwork-f-sys.md) | Set the preferred network for the specified SIM card slot. |
| [setPrimarySlotId](arkts-telephony-radio-setprimaryslotid-f-sys.md) | Set the index number of the main SIM card slot. |
| [setPrimarySlotId](arkts-telephony-radio-setprimaryslotid-f-sys.md) | Set the index number of the main SIM card slot. |
| [startManualNetworkScan](arkts-telephony-radio-startmanualnetworkscan-f-sys.md) | start ManualNetworkScan , Real-time report. |
| [stopManualNetworkScan](arkts-telephony-radio-stopmanualnetworkscan-f-sys.md) | Stop ManualNetworkScan. |
| [turnOffRadio](arkts-telephony-radio-turnoffradio-f-sys.md) | Turn off the radio service. |
| [turnOffRadio](arkts-telephony-radio-turnoffradio-f-sys.md) | Turn off the radio service. |
| [turnOffRadio](arkts-telephony-radio-turnoffradio-f-sys.md) | Turn off the radio service. |
| [turnOnRadio](arkts-telephony-radio-turnonradio-f-sys.md) | Turn on the radio service. |
| [turnOnRadio](arkts-telephony-radio-turnonradio-f-sys.md) | Turn on the radio service. |
| [turnOnRadio](arkts-telephony-radio-turnonradio-f-sys.md) | Turn on the radio service. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [CellInformation](arkts-telephony-radio-cellinformation-i.md) | Obtains current cell information. |
| [NetworkRadioTech](arkts-telephony-radio-networkradiotech-i.md) | Describes the radio access technology (RAT) of registered network. |
| [NetworkState](arkts-telephony-radio-networkstate-i.md) | Describes the network registration state. |
| [SignalInformation](arkts-telephony-radio-signalinformation-i.md) | Returns child class objects specific to the network type. |

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [CdmaCellInformation](arkts-telephony-radio-cdmacellinformation-i-sys.md) | Obtains CDMA cell information. |
| [CellInformation](arkts-telephony-radio-cellinformation-i-sys.md) | Obtains current cell information. |
| [GsmCellInformation](arkts-telephony-radio-gsmcellinformation-i-sys.md) | Obtains GSM cell information. |
| [ImsRegInfo](arkts-telephony-radio-imsreginfo-i-sys.md) | Indicates IMS registration information. |
| [LteCellInformation](arkts-telephony-radio-ltecellinformation-i-sys.md) | Obtains LTE cell information. |
| [NetworkInformation](arkts-telephony-radio-networkinformation-i-sys.md) | Obtains the network information. |
| [NetworkSearchRealTimeResult](arkts-telephony-radio-networksearchrealtimeresult-i-sys.md) | Indicates the results of manual network scan |
| [NetworkSearchResult](arkts-telephony-radio-networksearchresult-i-sys.md) | Obtains the network search results. |
| [NetworkSelectionModeOptions](arkts-telephony-radio-networkselectionmodeoptions-i-sys.md) | Obtains the network selection mode option. |
| [NrCellInformation](arkts-telephony-radio-nrcellinformation-i-sys.md) | Obtains NR cell information. |
| [TdscdmaCellInformation](arkts-telephony-radio-tdscdmacellinformation-i-sys.md) | Obtains TDSCDMA cell information. |
| [WcdmaCellInformation](arkts-telephony-radio-wcdmacellinformation-i-sys.md) | Obtains WCDMA cell information. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [NetworkSelectionMode](arkts-telephony-radio-networkselectionmode-e.md) | Obtains the network selection mode. |
| [NetworkType](arkts-telephony-radio-networktype-e.md) | Describes the network type. |
| [NsaState](arkts-telephony-radio-nsastate-e.md) | Describes the nsa state. |
| [RadioTechnology](arkts-telephony-radio-radiotechnology-e.md) | Describes the radio access technology. |
| [RegState](arkts-telephony-radio-regstate-e.md) | Describes the network registration state. |

<!--Del-->
### Enums(System API)

| Name | Description |
| --- | --- |
| [ImsRegState](arkts-telephony-radio-imsregstate-e-sys.md) | Obtains IMS registration status. |
| [ImsRegTech](arkts-telephony-radio-imsregtech-e-sys.md) | Indicates IMS registration technology. |
| [ImsServiceType](arkts-telephony-radio-imsservicetype-e-sys.md) | Indicates the type of IMS service. |
| [NetworkCapabilityState](arkts-telephony-radio-networkcapabilitystate-e-sys.md) | Enum for network capability state. |
| [NetworkCapabilityType](arkts-telephony-radio-networkcapabilitytype-e-sys.md) | Enum for network capability type. |
| [NetworkInformationState](arkts-telephony-radio-networkinformationstate-e-sys.md) | Obtains network information status. |
| [NrOptionMode](arkts-telephony-radio-nroptionmode-e-sys.md) | Obtains the option mode of NR. |
| [NROptionMode](arkts-telephony-radio-nroptionmode-e-sys.md) | Obtains the option mode of NR. |
| [PreferredNetworkMode](arkts-telephony-radio-preferrednetworkmode-e-sys.md) | Indicates the preferred network. |
<!--DelEnd-->

