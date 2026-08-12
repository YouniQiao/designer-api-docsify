# @ohos.enterprise.wifiManager(Wi-Fi Management)

This module provides Wi-Fi management capabilities for enterprise devices, including querying the Wi-Fi enabling status, configuring Wi-Fi connections, and managing the Wi-Fi list.

**Use cases:**

- Configuring Wi-Fi connections for enterprise devices in batches, simplifying the device initialization process  
- Controlling the Wi-Fi networks that devices can connect to, implementing network access compliance management  
- Managing the Wi-Fi switch of enterprise devices and unifying network policies

**Benefits:**

- Improve enterprise network management efficiency and reduces IT O&M costs.  
- Ensure that devices connect only to secure Wi-Fi networks, reducing security risks.  
- Implement unified management and control of network policies to meet enterprise compliance requirements.

> **NOTE：**
> 
> The APIs of this module can be called only by a device administrator application that is enabled. For details, see
> [MDM Kit Development](../../../mdm/mdm-kit-guide.md).
> 
> The global restriction policies are provided by **restrictions**. To disable Wi-Fi globally, see
> [@ohos.enterprise.restrictions](arkts-enterprise-restrictions.md#restrictions).

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace wifiManager--><!--Device-unnamed-declare namespace wifiManager-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.MDMKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addAllowedWifiList](arkts-mdm-wifimanager-addallowedwifilist-f.md#addallowedwifilist) |
| [addDisallowedWifiList](arkts-mdm-wifimanager-adddisallowedwifilist-f.md#adddisallowedwifilist) |
| [getAllowedWifiList](arkts-mdm-wifimanager-getallowedwifilist-f.md#getallowedwifilist) |
| [getAllowedWifiList](arkts-mdm-wifimanager-getallowedwifilist-f.md#getallowedwifilist-1) |
| [getDisallowedWifiList](arkts-mdm-wifimanager-getdisallowedwifilist-f.md#getdisallowedwifilist) |
| [getDisallowedWifiList](arkts-mdm-wifimanager-getdisallowedwifilist-f.md#getdisallowedwifilist-1) |
| [isWifiActive](arkts-mdm-wifimanager-iswifiactive-f.md#iswifiactive) |
| [isWifiActive](arkts-mdm-wifimanager-iswifiactive-f.md#iswifiactive-1) |
| [isWifiActiveSync](arkts-mdm-wifimanager-iswifiactivesync-f.md#iswifiactivesync) |
| [isWifiDisabled](arkts-mdm-wifimanager-iswifidisabled-f.md#iswifidisabled) |
| [removeAllowedWifiList](arkts-mdm-wifimanager-removeallowedwifilist-f.md#removeallowedwifilist) |
| [removeDisallowedWifiList](arkts-mdm-wifimanager-removedisallowedwifilist-f.md#removedisallowedwifilist) |
| [setWifiDisabled](arkts-mdm-wifimanager-setwifidisabled-f.md#setwifidisabled) |
| [setWifiProfile](arkts-mdm-wifimanager-setwifiprofile-f.md#setwifiprofile) |
| [setWifiProfile](arkts-mdm-wifimanager-setwifiprofile-f.md#setwifiprofile-1) |
| [setWifiProfileSync](arkts-mdm-wifimanager-setwifiprofilesync-f.md#setwifiprofilesync) |
| [turnOffWifi](arkts-mdm-wifimanager-turnoffwifi-f.md#turnoffwifi) |
| [turnOnWifi](arkts-mdm-wifimanager-turnonwifi-f.md#turnonwifi) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [IpProfile](arkts-mdm-wifimanager-ipprofile-i.md) |
| [WifiAccessInfo](arkts-mdm-wifimanager-wifiaccessinfo-i.md) |
| [WifiEapProfile](arkts-mdm-wifimanager-wifieapprofile-i.md) |
| [WifiProfile](arkts-mdm-wifimanager-wifiprofile-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [EapMethod](arkts-mdm-wifimanager-eapmethod-e.md) |
| [IpType](arkts-mdm-wifimanager-iptype-e.md) |
| [Phase2Method](arkts-mdm-wifimanager-phase2method-e.md) |
| [WifiSecurityType](arkts-mdm-wifimanager-wifisecuritytype-e.md) |
