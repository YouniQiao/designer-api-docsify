# @ohos.enterprise.deviceSettings(Device Settings Management)

This module provides enterprise device settings capabilities, including setting and obtaining the device screen-off time, system time, power policy, Eye Comfort mode, default input method, wallpaper, and hidden setting items.

> **NOTE：**
> 
> The APIs of this module can be called only by a device administrator application that is enabled. For details, see
> [MDM Kit Development](../../../mdm/mdm-kit-guide.md).

**Since:** 12

<!--Device-unnamed-declare namespace deviceSettings--><!--Device-unnamed-declare namespace deviceSettings-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { deviceSettings } from '@kit.MDMKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addHiddenSettingsMenu](arkts-mdm-devicesettings-addhiddensettingsmenu-f.md#addhiddensettingsmenu) |
| [getHiddenSettingsMenu](arkts-mdm-devicesettings-gethiddensettingsmenu-f.md#gethiddensettingsmenu) |
| [getPowerPolicy](arkts-mdm-devicesettings-getpowerpolicy-f.md#getpowerpolicy) |
| [getScreenOffTime](arkts-mdm-devicesettings-getscreenofftime-f.md#getscreenofftime) |
| [getScreenOffTime](arkts-mdm-devicesettings-getscreenofftime-f.md#getscreenofftime-1) |
| [getValue](arkts-mdm-devicesettings-getvalue-f.md#getvalue) |
| [getValueForAccount](arkts-mdm-devicesettings-getvalueforaccount-f.md#getvalueforaccount) |
| [installUserCertificate](arkts-mdm-devicesettings-installusercertificate-f.md#installusercertificate) |
| [installUserCertificate](arkts-mdm-devicesettings-installusercertificate-f.md#installusercertificate-1) |
| [removeHiddenSettingsMenu](arkts-mdm-devicesettings-removehiddensettingsmenu-f.md#removehiddensettingsmenu) |
| [setHomeWallpaper](arkts-mdm-devicesettings-sethomewallpaper-f.md#sethomewallpaper) |
| [setPowerPolicy](arkts-mdm-devicesettings-setpowerpolicy-f.md#setpowerpolicy) |
| [setScreenOffTime](arkts-mdm-devicesettings-setscreenofftime-f.md#setscreenofftime) |
| [setSwitchStatus](arkts-mdm-devicesettings-setswitchstatus-f.md#setswitchstatus) |
| [setUnlockWallpaper](arkts-mdm-devicesettings-setunlockwallpaper-f.md#setunlockwallpaper) |
| [setValue](arkts-mdm-devicesettings-setvalue-f.md#setvalue) |
| [setValueForAccount](arkts-mdm-devicesettings-setvalueforaccount-f.md#setvalueforaccount) |
| [uninstallUserCertificate](arkts-mdm-devicesettings-uninstallusercertificate-f.md#uninstallusercertificate) |
| [uninstallUserCertificate](arkts-mdm-devicesettings-uninstallusercertificate-f.md#uninstallusercertificate-1) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CertBlob](arkts-mdm-devicesettings-certblob-i.md) |
| [PowerPolicy](arkts-mdm-devicesettings-powerpolicy-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [PowerPolicyAction](arkts-mdm-devicesettings-powerpolicyaction-e.md) |
| [PowerScene](arkts-mdm-devicesettings-powerscene-e.md) |
| [SettingsItem](arkts-mdm-devicesettings-settingsitem-e.md) |
| [SettingsMenu](arkts-mdm-devicesettings-settingsmenu-e.md) |
| [SwitchKey](arkts-mdm-devicesettings-switchkey-e.md) |
| [SwitchStatus](arkts-mdm-devicesettings-switchstatus-e.md) |
