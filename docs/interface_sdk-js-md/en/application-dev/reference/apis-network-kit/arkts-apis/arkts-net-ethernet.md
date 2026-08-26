# @ohos.net.ethernet(Ethernet Connection Management)

The **ethernet** module provides Ethernet management functions such as configuring a network proxy and obtaining the network IP address.

**Since:** 9

**System capability:** SystemCapability.Communication.NetManager.Ethernet

## Modules to Import

```TypeScript
import ethernet from '@kit.NetworkKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getMacAddress(Ethernet Connection Management)](arkts-network-ethernet-getmacaddress-f.md) | Obtains the names and MAC addresses of all Ethernet NICs. This API uses a promise to return the result.  **Required permission**: ohos.permission.GET_ETHERNET_LOCAL_MAC |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [disableEthernetInterface(Ethernet Connection Management)](arkts-network-ethernet-disableethernetinterface-f-sys.md) | Disable the ethernet interface. |
| [enableEthernetInterface(Ethernet Connection Management)](arkts-network-ethernet-enableethernetinterface-f-sys.md) | Enable the ethernet interface. |
| [getAllActiveIfaces(Ethernet Connection Management)](arkts-network-ethernet-getallactiveifaces-f-sys.md) | Obtains the active network interface. This API uses an asynchronous callback to return the result. |
| [getAllActiveIfaces(Ethernet Connection Management)](arkts-network-ethernet-getallactiveifaces-f-sys.md) | Obtains the active network interface. This API uses a promise to return the result. |
| [getEthernetDeviceInfos(Ethernet Connection Management)](arkts-network-ethernet-getethernetdeviceinfos-f-sys.md) | Obtains the device information (such as the vendor name, product name, and maximum connection rate) of the local Ethernet NIC. This API uses a promise to return the result. |
| [getIfaceConfig(Ethernet Connection Management)](arkts-network-ethernet-getifaceconfig-f-sys.md) | Obtains the information about a specified network interface. This API uses an asynchronous callback to return the result. |
| [getIfaceConfig(Ethernet Connection Management)](arkts-network-ethernet-getifaceconfig-f-sys.md) | Obtains the information about a specified network interface. This API uses a promise to return the result. |
| [isEthernetEnabled(Ethernet Connection Management)](arkts-network-ethernet-isethernetenabled-f-sys.md) | Check whether the global ethernet switch is enabled. |
| [isIfaceActive(Ethernet Connection Management)](arkts-network-ethernet-isifaceactive-f-sys.md) | Checks whether the interface is activated. This API uses an asynchronous callback to return the result. |
| [isIfaceActive(Ethernet Connection Management)](arkts-network-ethernet-isifaceactive-f-sys.md) | Checks whether the interface is activated. This API uses a promise to return the result. |
| off(Ethernet Connection Management) | Unregisters the observer for NIC hot swap events. This API uses an asynchronous callback to return the result. |
| on(Ethernet Connection Management) | Registers the observer for NIC hot swap events. This API uses an asynchronous callback to return the result. |
| [setIfaceConfig(Ethernet Connection Management)](arkts-network-ethernet-setifaceconfig-f-sys.md) | Sets the network interface configuration information. This API uses an asynchronous callback to return the result. |
| [setIfaceConfig(Ethernet Connection Management)](arkts-network-ethernet-setifaceconfig-f-sys.md) | Sets the network interface configuration information. This API uses a promise to return the result. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [MacAddressInfo(Ethernet Connection Management)](arkts-network-ethernet-macaddressinfo-i.md) | Defines the name and MAC address of an Ethernet NIC. |

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [EthernetDeviceInfos(Ethernet Connection Management)](arkts-network-ethernet-ethernetdeviceinfos-i-sys.md) | Defines Ethernet device information. |
| [InterfaceConfiguration(Ethernet Connection Management)](arkts-network-ethernet-interfaceconfiguration-i-sys.md) | Defines the network configuration for the Ethernet connection. |
| [InterfaceStateInfo(Ethernet Connection Management)](arkts-network-ethernet-interfacestateinfo-i-sys.md) | Listens for status changes of an Ethernet NIC. |
<!--DelEnd-->

<!--Del-->
### Enums(System API)

| Name | Description |
| --- | --- |
| [DeviceConnectionType(Ethernet Connection Management)](arkts-network-ethernet-deviceconnectiontype-e-sys.md) | Enumerates Ethernet device connection modes. |
| [IPSetMode(Ethernet Connection Management)](arkts-network-ethernet-ipsetmode-e-sys.md) | Defines the configuration mode of the Ethernet connection. |
<!--DelEnd-->

### Types

| Name | Description |
| --- | --- |
| [HttpProxy(Ethernet Connection Management)](arkts-network-ethernet-httpproxy-t.md) | Defines the network proxy configuration. |
