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

> **NOTE：**&gt;
> The APIs of this module can be called only by a device administrator application that is enabled. For details, see
> [MDM Kit Development](../../../mdm/mdm-kit-guide.md).&gt;
> The global restriction policies are provided by **restrictions**. To disable Wi-Fi globally, see
> [@ohos.enterprise.restrictions](arkts-enterprise-restrictions.md).

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { wifiManager } from 'kits/@kit.MDMKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addAllowedWifiList(Wi-Fi Management)](arkts-mdm-wifimanager-addallowedwifilist-f.md) |
| [addDisallowedWifiList(Wi-Fi Management)](arkts-mdm-wifimanager-adddisallowedwifilist-f.md) |
| [getAllowedWifiList(Wi-Fi Management)](arkts-mdm-wifimanager-getallowedwifilist-f.md) |
| [getAllowedWifiList(Wi-Fi Management)](arkts-mdm-wifimanager-getallowedwifilist-f.md) |
| [getDisallowedWifiList(Wi-Fi Management)](arkts-mdm-wifimanager-getdisallowedwifilist-f.md) |
| [getDisallowedWifiList(Wi-Fi Management)](arkts-mdm-wifimanager-getdisallowedwifilist-f.md) |
| [isWifiActiveSync(Wi-Fi Management)](arkts-mdm-wifimanager-iswifiactivesync-f.md) |
| [removeAllowedWifiList(Wi-Fi Management)](arkts-mdm-wifimanager-removeallowedwifilist-f.md) |
| [removeDisallowedWifiList(Wi-Fi Management)](arkts-mdm-wifimanager-removedisallowedwifilist-f.md) |
| [setWifiProfileSync(Wi-Fi Management)](arkts-mdm-wifimanager-setwifiprofilesync-f.md) |
| [turnOffWifi(Wi-Fi Management)](arkts-mdm-wifimanager-turnoffwifi-f.md) |
| [turnOnWifi(Wi-Fi Management)](arkts-mdm-wifimanager-turnonwifi-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [isWifiActive(Wi-Fi Management)](arkts-mdm-wifimanager-iswifiactive-f-sys.md) |
| [isWifiActive(Wi-Fi Management)](arkts-mdm-wifimanager-iswifiactive-f-sys.md) |
| [isWifiDisabled(Wi-Fi Management)](arkts-mdm-wifimanager-iswifidisabled-f-sys.md) |
| [setWifiDisabled(Wi-Fi Management)](arkts-mdm-wifimanager-setwifidisabled-f-sys.md) |
| [setWifiProfile(Wi-Fi Management)](arkts-mdm-wifimanager-setwifiprofile-f-sys.md) |
| [setWifiProfile(Wi-Fi Management)](arkts-mdm-wifimanager-setwifiprofile-f-sys.md) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [IpProfile(Wi-Fi Management)](arkts-mdm-wifimanager-ipprofile-i.md) |
| [WifiAccessInfo(Wi-Fi Management)](arkts-mdm-wifimanager-wifiaccessinfo-i.md) |
| [WifiEapProfile(Wi-Fi Management)](arkts-mdm-wifimanager-wifieapprofile-i.md) |
| [WifiProfile(Wi-Fi Management)](arkts-mdm-wifimanager-wifiprofile-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [EapMethod(Wi-Fi Management)](arkts-mdm-wifimanager-eapmethod-e.md) |
| [IpType(Wi-Fi Management)](arkts-mdm-wifimanager-iptype-e.md) |
| [Phase2Method(Wi-Fi Management)](arkts-mdm-wifimanager-phase2method-e.md) |
| [WifiSecurityType(Wi-Fi Management)](arkts-mdm-wifimanager-wifisecuritytype-e.md) |
