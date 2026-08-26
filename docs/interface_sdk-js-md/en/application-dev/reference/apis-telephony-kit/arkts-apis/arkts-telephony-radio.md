# @ohos.telephony.radio(Network Search)

The **radio** module provides basic network search management functions. Using the APIs provided by this module, you can obtain the radio access technology (RAT) used in the CS and PS domains, network status, current network selection mode, ISO country code of the registered network, ID of the slot in which the primary card is located, list of signal strengths of the registered network for the SIM card in the specified slot, and carrier name. Besides, you can check whether the current device supports New Radio \(NR\) and whether the radio service is enabled on the primary SIM card. The CS domain refers to the Circuit Switched domain, and the PS domain refers to the Packet Switched domain.

**Since:** 6

**System capability:** SystemCapability.Telephony.CoreService

## Modules to Import

```TypeScript
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getISOCountryCodeForNetwork(Network Search)](arkts-telephony-radio-getisocountrycodefornetwork-f.md) | Obtains the ISO country code of the network with which the SIM card in the specified slot is registered. This API uses an asynchronous callback to return the result. |
| [getISOCountryCodeForNetwork(Network Search)](arkts-telephony-radio-getisocountrycodefornetwork-f.md) | Obtains the ISO country code of the network with which the SIM card in the specified slot is registered. This API uses a promise to return the result. |
| [getISOCountryCodeForNetworkSync(Network Search)](arkts-telephony-radio-getisocountrycodefornetworksync-f.md) | Obtains the ISO country code of the network with which the SIM card in the specified slot is registered. |
| [getNetworkSelectionMode(Network Search)](arkts-telephony-radio-getnetworkselectionmode-f.md) | Obtains the network selection mode of the SIM card in the specified slot. This API uses an asynchronous callback to return the result. |
| [getNetworkSelectionMode(Network Search)](arkts-telephony-radio-getnetworkselectionmode-f.md) | Obtains the network selection mode of the SIM card in the specified slot. This API uses a promise to return the result. |
| [getNetworkState(Network Search)](arkts-telephony-radio-getnetworkstate-f.md) | Obtains the network status of the SIM card in the specified slot. This API uses an asynchronous callback to return the result.  **Required permission**: ohos.permission.GET_NETWORK_INFO |
| [getNetworkState(Network Search)](arkts-telephony-radio-getnetworkstate-f.md) | Obtains the network status of the SIM card in the specified slot. This API uses a promise to return the result.  **Required permission**: ohos.permission.GET_NETWORK_INFO |
| [getNetworkState(Network Search)](arkts-telephony-radio-getnetworkstate-f.md) | Obtains the network status. This API uses an asynchronous callback to return the result.  **Required permission**: ohos.permission.GET_NETWORK_INFO |
| [getOperatorName(Network Search)](arkts-telephony-radio-getoperatorname-f.md) | Obtains the carrier name of the SIM card in the specified slot. This API uses an asynchronous callback to return the result. |
| [getOperatorName(Network Search)](arkts-telephony-radio-getoperatorname-f.md) | Obtains the carrier name of the SIM card in the specified slot. This API uses a promise to return the result. |
| [getOperatorNameSync(Network Search)](arkts-telephony-radio-getoperatornamesync-f.md) | Obtains the carrier name of the SIM card in the specified slot. |
| [getPrimarySlotId(Network Search)](arkts-telephony-radio-getprimaryslotid-f.md) | Obtains the ID of the slot in which the primary card is located. This API uses an asynchronous callback to return the result. |
| [getPrimarySlotId(Network Search)](arkts-telephony-radio-getprimaryslotid-f.md) | Obtains the ID of the slot in which the primary card is located. This API uses a promise to return the result. |
| [getRadioTech(Network Search)](arkts-telephony-radio-getradiotech-f.md) | Obtains the RAT used in the CS and PS domains for the SIM card in the specified slot. This API uses an asynchronous callback to return the result. The CS domain refers to the Circuit Switched domain, and the PS domain refers to the Packet Switched domain.  **Required permission**: ohos.permission.GET_NETWORK_INFO |
| [getRadioTech(Network Search)](arkts-telephony-radio-getradiotech-f.md) | Obtains the RAT used in the CS and PS domains for the SIM card in the specified slot. This API uses a promise to return the result. The CS domain refers to the Circuit Switched domain, and the PS domain refers to the Packet Switched domain.  **Required permission**: ohos.permission.GET_NETWORK_INFO |
| [getRadioTechSync(Network Search)](arkts-telephony-radio-getradiotechsync-f.md) | Obtains the RAT used in the CS and PS domains for the SIM card in the specified slot. The CS domain refers to the Circuit Switched domain, and the PS domain refers to the Packet Switched domain.  **Required permission**: ohos.permission.GET_NETWORK_INFO |
| [getSignalInformation(Network Search)](arkts-telephony-radio-getsignalinformation-f.md) | Obtains a list of signal strengths of the network with which the SIM card in the specified slot is registered. This API uses an asynchronous callback to return the result. |
| [getSignalInformation(Network Search)](arkts-telephony-radio-getsignalinformation-f.md) | Obtains a list of signal strengths of the network with which the SIM card in the specified slot is registered. This API uses a promise to return the result. |
| [getSignalInformationSync(Network Search)](arkts-telephony-radio-getsignalinformationsync-f.md) | Obtains a list of signal strengths of the network with which the SIM card in the specified slot is registered. |
| [isNrSupported(Network Search)](arkts-telephony-radio-isnrsupported-f.md) | Checks whether the current device supports NR. |
| [isNrSupported(Network Search)](arkts-telephony-radio-isnrsupported-f.md) | Checks whether the SIM card in the specified slot supports NR. |
| [isNRSupported(Network Search)](arkts-telephony-radio-isnrsupported-f.md) | Checks whether the current device supports NR. |
| [isNRSupported(Network Search)](arkts-telephony-radio-isnrsupported-f.md) | Checks whether the SIM card in the specified slot supports NR. |
| [isRadioOn(Network Search)](arkts-telephony-radio-isradioon-f.md) | Checks whether the radio service is enabled on the SIM card in the specified slot. This API uses an asynchronous callback to return the result.  **Required permission**: ohos.permission.GET_NETWORK_INFO |
| [isRadioOn(Network Search)](arkts-telephony-radio-isradioon-f.md) | Checks whether the radio service is enabled on the SIM card in the specified slot. This API uses a promise to return the result.  **Required permission**: ohos.permission.GET_NETWORK_INFO |
| [isRadioOn(Network Search)](arkts-telephony-radio-isradioon-f.md) | Checks whether the radio service is enabled on the primary SIM card. This API uses an asynchronous callback to return the result.  **Required permission**: ohos.permission.GET_NETWORK_INFO |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [factoryReset(Network Search)](arkts-telephony-radio-factoryreset-f-sys.md) | Reset all network settings of telephony. |
| [getBasebandVersion(Network Search)](arkts-telephony-radio-getbasebandversion-f-sys.md) | Get the version of Baseband. |
| [getBasebandVersion(Network Search)](arkts-telephony-radio-getbasebandversion-f-sys.md) | Get the version of Baseband. |
| [getCellInformation(Network Search)](arkts-telephony-radio-getcellinformation-f-sys.md) | Get the current cell information. |
| [getCellInformation(Network Search)](arkts-telephony-radio-getcellinformation-f-sys.md) | Get the current cell information. |
| [getCellInformation(Network Search)](arkts-telephony-radio-getcellinformation-f-sys.md) | Get the current cell information. |
| [getIMEI(Network Search)](arkts-telephony-radio-getimei-f-sys.md) | Obtains the IMEI of a specified card slot of the device. |
| [getIMEI(Network Search)](arkts-telephony-radio-getimei-f-sys.md) | Obtains the IMEI of a specified card slot of the device. |
| [getIMEI(Network Search)](arkts-telephony-radio-getimei-f-sys.md) | Obtains the IMEI of a specified card slot of the device. |
| [getIMEISV(Network Search)](arkts-telephony-radio-getimeisv-f-sys.md) | Obtains the software version number of a specified card slot of the device. |
| [getImsRegInfo(Network Search)](arkts-telephony-radio-getimsreginfo-f-sys.md) | Get the IMS registration state info of specified IMS service type. |
| [getImsRegInfo(Network Search)](arkts-telephony-radio-getimsreginfo-f-sys.md) | Get the IMS registration state info of specified IMS service type. |
| [getMEID(Network Search)](arkts-telephony-radio-getmeid-f-sys.md) | Obtains the MEID of a specified card slot of the device. |
| [getMEID(Network Search)](arkts-telephony-radio-getmeid-f-sys.md) | Obtains the MEID of a specified card slot of the device. |
| [getMEID(Network Search)](arkts-telephony-radio-getmeid-f-sys.md) | Obtains the MEID of a specified card slot of the device. |
| [getNetworkCapability(Network Search)](arkts-telephony-radio-getnetworkcapability-f-sys.md) | Get the network capability state according to the specified capability type. |
| [getNetworkCapability(Network Search)](arkts-telephony-radio-getnetworkcapability-f-sys.md) | Get the network capability state according to the specified capability type. |
| [getNetworkSearchInformation(Network Search)](arkts-telephony-radio-getnetworksearchinformation-f-sys.md) | Get network search information. |
| [getNetworkSearchInformation(Network Search)](arkts-telephony-radio-getnetworksearchinformation-f-sys.md) | Get network search information. |
| [getNrOptionMode(Network Search)](arkts-telephony-radio-getnroptionmode-f-sys.md) | Get the option mode of NR. |
| [getNrOptionMode(Network Search)](arkts-telephony-radio-getnroptionmode-f-sys.md) | Get the option mode of NR. |
| [getNrOptionMode(Network Search)](arkts-telephony-radio-getnroptionmode-f-sys.md) | Get the option mode of NR. |
| [getNROptionMode(Network Search)](arkts-telephony-radio-getnroptionmode-f-sys.md) | Get the option mode of NR. |
| [getNROptionMode(Network Search)](arkts-telephony-radio-getnroptionmode-f-sys.md) | Get the option mode of NR. |
| [getPreferredNetwork(Network Search)](arkts-telephony-radio-getpreferrednetwork-f-sys.md) | Get the preferred network for the specified SIM card slot. |
| [getPreferredNetwork(Network Search)](arkts-telephony-radio-getpreferrednetwork-f-sys.md) | Get the preferred network for the specified SIM card slot. |
| [getUniqueDeviceId(Network Search)](arkts-telephony-radio-getuniquedeviceid-f-sys.md) | Obtains the unique device ID of a specified card slot of the device.If the device is registered with a 3GPP-compliant network, the international mobile equipment identity (IMEI) is returned. If the device is registered with a 3GPP2-compliant network, the mobile equipment identifier (MEID) is returned. |
| [getUniqueDeviceId(Network Search)](arkts-telephony-radio-getuniquedeviceid-f-sys.md) | Obtains the unique device ID of a specified card slot of the device.If the device is registered with a 3GPP-compliant network, the international mobile equipment identity (IMEI) is returned. If the device is registered with a 3GPP2-compliant network, the mobile equipment identifier (MEID) is returned. |
| [getUniqueDeviceId(Network Search)](arkts-telephony-radio-getuniquedeviceid-f-sys.md) | Obtains the unique device ID of a specified card slot of the device.If the device is registered with a 3GPP-compliant network, the international mobile equipment identity (IMEI) is returned. If the device is registered with a 3GPP2-compliant network, the mobile equipment identifier (MEID) is returned. |
| [isManualNetworkScanning(Network Search)](arkts-telephony-radio-ismanualnetworkscanning-f-sys.md) | Determine whether the current manual network scan is in progress. |
| off(Network Search) | Unsubscribe from imsRegStateChange event. |
| on(Network Search) | Called when the IMS registration state of specified IMS service type corresponding to a monitored {@code slotId} updates. |
| [sendUpdateCellLocationRequest(Network Search)](arkts-telephony-radio-sendupdatecelllocationrequest-f-sys.md) | Actively requests to update location information. |
| [sendUpdateCellLocationRequest(Network Search)](arkts-telephony-radio-sendupdatecelllocationrequest-f-sys.md) | Actively requests to update location information. |
| [sendUpdateCellLocationRequest(Network Search)](arkts-telephony-radio-sendupdatecelllocationrequest-f-sys.md) | Actively requests to update location information. |
| [setNetworkCapability(Network Search)](arkts-telephony-radio-setnetworkcapability-f-sys.md) | Set the type and state for the specified network capability. |
| [setNetworkCapability(Network Search)](arkts-telephony-radio-setnetworkcapability-f-sys.md) | Set the type and state for the specified network capability. |
| [setNetworkSelectionMode(Network Search)](arkts-telephony-radio-setnetworkselectionmode-f-sys.md) | Set the current network selection mode. |
| [setNetworkSelectionMode(Network Search)](arkts-telephony-radio-setnetworkselectionmode-f-sys.md) | Set the current network selection mode. |
| [setNROptionMode(Network Search)](arkts-telephony-radio-setnroptionmode-f-sys.md) | Set the NR option mode. |
| [setNROptionMode(Network Search)](arkts-telephony-radio-setnroptionmode-f-sys.md) | Set the NR option mode. |
| [setPreferredNetwork(Network Search)](arkts-telephony-radio-setpreferrednetwork-f-sys.md) | Set the preferred network for the specified SIM card slot. |
| [setPreferredNetwork(Network Search)](arkts-telephony-radio-setpreferrednetwork-f-sys.md) | Set the preferred network for the specified SIM card slot. |
| [setPrimarySlotId(Network Search)](arkts-telephony-radio-setprimaryslotid-f-sys.md) | Set the index number of the main SIM card slot. |
| [setPrimarySlotId(Network Search)](arkts-telephony-radio-setprimaryslotid-f-sys.md) | Set the index number of the main SIM card slot. |
| [startManualNetworkScan(Network Search)](arkts-telephony-radio-startmanualnetworkscan-f-sys.md) | start ManualNetworkScan , Real-time report. |
| [stopManualNetworkScan(Network Search)](arkts-telephony-radio-stopmanualnetworkscan-f-sys.md) | Stop ManualNetworkScan. |
| [turnOffRadio(Network Search)](arkts-telephony-radio-turnoffradio-f-sys.md) | Turn off the radio service. |
| [turnOffRadio(Network Search)](arkts-telephony-radio-turnoffradio-f-sys.md) | Turn off the radio service. |
| [turnOffRadio(Network Search)](arkts-telephony-radio-turnoffradio-f-sys.md) | Turn off the radio service. |
| [turnOnRadio(Network Search)](arkts-telephony-radio-turnonradio-f-sys.md) | Turn on the radio service. |
| [turnOnRadio(Network Search)](arkts-telephony-radio-turnonradio-f-sys.md) | Turn on the radio service. |
| [turnOnRadio(Network Search)](arkts-telephony-radio-turnonradio-f-sys.md) | Turn on the radio service. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [CellInformation(Network Search)](arkts-telephony-radio-cellinformation-i.md) | Defines the cell information. |
| [NetworkRadioTech(Network Search)](arkts-telephony-radio-networkradiotech-i.md) | Defines the radio access technology for the packet switched (PS) or circuit switched (CS) network. |
| [NetworkState(Network Search)](arkts-telephony-radio-networkstate-i.md) | Defines the network status. |
| [SignalInformation(Network Search)](arkts-telephony-radio-signalinformation-i.md) | Defines the signal strength. |

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [CdmaCellInformation(Network Search)](arkts-telephony-radio-cdmacellinformation-i-sys.md) | Obtains CDMA cell information. |
| [CellInformation(Network Search)](arkts-telephony-radio-cellinformation-i-sys.md) | Defines the cell information. |
| [GsmCellInformation(Network Search)](arkts-telephony-radio-gsmcellinformation-i-sys.md) | Obtains GSM cell information. |
| [ImsRegInfo(Network Search)](arkts-telephony-radio-imsreginfo-i-sys.md) | Indicates IMS registration information. |
| [LteCellInformation(Network Search)](arkts-telephony-radio-ltecellinformation-i-sys.md) | Obtains LTE cell information. |
| [NetworkInformation(Network Search)](arkts-telephony-radio-networkinformation-i-sys.md) | Obtains the network information. |
| [NetworkSearchRealTimeResult(Network Search)](arkts-telephony-radio-networksearchrealtimeresult-i-sys.md) | Indicates the results of manual network scan |
| [NetworkSearchResult(Network Search)](arkts-telephony-radio-networksearchresult-i-sys.md) | Obtains the network search results. |
| [NetworkSelectionModeOptions(Network Search)](arkts-telephony-radio-networkselectionmodeoptions-i-sys.md) | Obtains the network selection mode option. |
| [NrCellInformation(Network Search)](arkts-telephony-radio-nrcellinformation-i-sys.md) | Obtains NR cell information. |
| [TdscdmaCellInformation(Network Search)](arkts-telephony-radio-tdscdmacellinformation-i-sys.md) | Obtains TDSCDMA cell information. |
| [WcdmaCellInformation(Network Search)](arkts-telephony-radio-wcdmacellinformation-i-sys.md) | Obtains WCDMA cell information. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [NetworkSelectionMode(Network Search)](arkts-telephony-radio-networkselectionmode-e.md) | Enumerates network selection modes. |
| [NetworkType(Network Search)](arkts-telephony-radio-networktype-e.md) | Enumerates network types. |
| [NsaState(Network Search)](arkts-telephony-radio-nsastate-e.md) | Enumerates NSA network states. |
| [RadioTechnology(Network Search)](arkts-telephony-radio-radiotechnology-e.md) | Enumerates radio access technologies. |
| [RegState(Network Search)](arkts-telephony-radio-regstate-e.md) | Defines the network registration status of the device. |

<!--Del-->
### Enums(System API)

| Name | Description |
| --- | --- |
| [ImsRegState(Network Search)](arkts-telephony-radio-imsregstate-e-sys.md) | Obtains IMS registration status. |
| [ImsRegTech(Network Search)](arkts-telephony-radio-imsregtech-e-sys.md) | Indicates IMS registration technology. |
| [ImsServiceType(Network Search)](arkts-telephony-radio-imsservicetype-e-sys.md) | Indicates the type of IMS service. |
| [NetworkCapabilityState(Network Search)](arkts-telephony-radio-networkcapabilitystate-e-sys.md) | Enum for network capability state. |
| [NetworkCapabilityType(Network Search)](arkts-telephony-radio-networkcapabilitytype-e-sys.md) | Enum for network capability type. |
| [NetworkInformationState(Network Search)](arkts-telephony-radio-networkinformationstate-e-sys.md) | Obtains network information status. |
| [NrOptionMode(Network Search)](arkts-telephony-radio-nroptionmode-e-sys.md) | Obtains the option mode of NR. |
| [NROptionMode(Network Search)](arkts-telephony-radio-nroptionmode-e-sys.md) | Obtains the option mode of NR. |
| [PreferredNetworkMode(Network Search)](arkts-telephony-radio-preferrednetworkmode-e-sys.md) | Indicates the preferred network. |
<!--DelEnd-->
