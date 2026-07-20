# @ohos.net.ethernet

Provides interfaces to manage ethernet.

**Since:** 9

<!--Device-unnamed-declare namespace ethernet--><!--Device-unnamed-declare namespace ethernet-End-->

**System capability:** SystemCapability.Communication.NetManager.Ethernet

## Modules to Import

```TypeScript
import { ethernet } from '@kit.NetworkKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getMacAddress](arkts-network-ethernet-getmacaddress-f.md#getmacaddress) | Get the ethernet mac address list. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [disableEthernetInterface](arkts-network-ethernet-disableethernetinterface-f-sys.md#disableethernetinterface) | Disable the ethernet interface. |
| [enableEthernetInterface](arkts-network-ethernet-enableethernetinterface-f-sys.md#enableethernetinterface) | Enable the ethernet interface. |
| [getAllActiveIfaces](arkts-network-ethernet-getallactiveifaces-f-sys.md#getallactiveifaces) | Gets the names of all active network interfaces. |
| [getAllActiveIfaces](arkts-network-ethernet-getallactiveifaces-f-sys.md#getallactiveifaces-1) | Gets the names of all active network interfaces. |
| [getEthernetDeviceInfos](arkts-network-ethernet-getethernetdeviceinfos-f-sys.md#getethernetdeviceinfos) | Get the ethernet mac address list. |
| [getIfaceConfig](arkts-network-ethernet-getifaceconfig-f-sys.md#getifaceconfig) | Get the specified network interface information. |
| [getIfaceConfig](arkts-network-ethernet-getifaceconfig-f-sys.md#getifaceconfig-1) | Get the specified network interface information. |
| [isEthernetEnabled](arkts-network-ethernet-isethernetenabled-f-sys.md#isethernetenabled) | Check whether the global ethernet switch is enabled. |
| [isIfaceActive](arkts-network-ethernet-isifaceactive-f-sys.md#isifaceactive) | Check whether the specified network is active. |
| [isIfaceActive](arkts-network-ethernet-isifaceactive-f-sys.md#isifaceactive-1) | Check whether the specified network is active. |
| [off](arkts-network-ethernet-off-f-sys.md#off) | Unregister a callback from the ethernet interface active state change. |
| [on](arkts-network-ethernet-on-f-sys.md#on) | Register a callback for the ethernet interface active state change. |
| [setIfaceConfig](arkts-network-ethernet-setifaceconfig-f-sys.md#setifaceconfig) | Set the specified network interface parameters. |
| [setIfaceConfig](arkts-network-ethernet-setifaceconfig-f-sys.md#setifaceconfig-1) | Set the specified network interface parameters. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [MacAddressInfo](arkts-network-ethernet-macaddressinfo-i.md) | Defines the mac address info of the Ethernet. |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [EthernetDeviceInfos](arkts-network-ethernet-ethernetdeviceinfos-i-sys.md) | Defines the device information of the Ethernet. |
| [InterfaceConfiguration](arkts-network-ethernet-interfaceconfiguration-i-sys.md) | Defines the network configuration for the Ethernet connection. |
| [InterfaceStateInfo](arkts-network-ethernet-interfacestateinfo-i-sys.md) | The interface is used to monitor network interface status changes. |
<!--DelEnd-->

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [DeviceConnectionType](arkts-network-ethernet-deviceconnectiontype-e-sys.md) | Defines the Device Connection Mode of the Ethernet. |
| [IPSetMode](arkts-network-ethernet-ipsetmode-e-sys.md) | Defines the configuration mode of the Ethernet connection. |
<!--DelEnd-->

### Types

| Name | Description |
| --- | --- |
| [HttpProxy](arkts-network-ethernet-httpproxy-t.md) |  |

