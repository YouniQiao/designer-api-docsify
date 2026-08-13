# @ohos.enterprise.wifiManager

This module provides Wi-Fi management capabilities for enterprise devices, including querying the Wi-Fi enabling status, configuring Wi-Fi connections, and managing the Wi-Fi list. **Use cases:** - Configuring Wi-Fi connections for enterprise devices in batches, simplifying the device initialization process - Controlling the Wi-Fi networks that devices can connect to, implementing network access compliance management - Managing the Wi-Fi switch of enterprise devices and unifying network policies **Benefits:** - Improve enterprise network management efficiency and reduces IT O&M costs. - Ensure that devices connect only to secure Wi-Fi networks, reducing security risks. - Implement unified management and control of network policies to meet enterprise compliance requirements. > **NOTE：**> > The APIs of this module can be called only by a device administrator application that is enabled. For details, see > [MDM Kit Development](../../../mdm/mdm-kit-guide.md). > > The global restriction policies are provided by **restrictions**. To disable Wi-Fi globally, see > [@ohos.enterprise.restrictions](arkts-enterprise-restrictions.md#@ohos.enterprise.restrictions).

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace wifiManager--><!--Device-unnamed-declare namespace wifiManager-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.MDMKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addAllowedWifiList](arkts-mdm-wifimanager-addallowedwifilist-f.md#addAllowedWifiList) |
| [addDisallowedWifiList](arkts-mdm-wifimanager-adddisallowedwifilist-f.md#addDisallowedWifiList) |
| [getAllowedWifiList](arkts-mdm-wifimanager-getallowedwifilist-f.md#getAllowedWifiList) |
| [getAllowedWifiList](arkts-mdm-wifimanager-getallowedwifilist-f.md#getAllowedWifiList) |
| [getDisallowedWifiList](arkts-mdm-wifimanager-getdisallowedwifilist-f.md#getDisallowedWifiList) |
| [getDisallowedWifiList](arkts-mdm-wifimanager-getdisallowedwifilist-f.md#getDisallowedWifiList) |
| [isWifiActiveSync](arkts-mdm-wifimanager-iswifiactivesync-f.md#isWifiActiveSync) |
| [removeAllowedWifiList](arkts-mdm-wifimanager-removeallowedwifilist-f.md#removeAllowedWifiList) |
| [removeDisallowedWifiList](arkts-mdm-wifimanager-removedisallowedwifilist-f.md#removeDisallowedWifiList) |
| [setWifiProfileSync](arkts-mdm-wifimanager-setwifiprofilesync-f.md#setWifiProfileSync) |
| [turnOffWifi](arkts-mdm-wifimanager-turnoffwifi-f.md#turnOffWifi) |
| [turnOnWifi](arkts-mdm-wifimanager-turnonwifi-f.md#turnOnWifi) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [isWifiActive](arkts-mdm-wifimanager-iswifiactive-f-sys.md#isWifiActive-(System-API)) |
| [isWifiActive](arkts-mdm-wifimanager-iswifiactive-f-sys.md#isWifiActive-(System-API)) |
| [isWifiDisabled](arkts-mdm-wifimanager-iswifidisabled-f-sys.md#isWifiDisabled-(System-API)) |
| [setWifiDisabled](arkts-mdm-wifimanager-setwifidisabled-f-sys.md#setWifiDisabled-(System-API)) |
| [setWifiProfile](arkts-mdm-wifimanager-setwifiprofile-f-sys.md#setWifiProfile-(System-API)) |
| [setWifiProfile](arkts-mdm-wifimanager-setwifiprofile-f-sys.md#setWifiProfile-(System-API)) |
<!--DelEnd-->

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
