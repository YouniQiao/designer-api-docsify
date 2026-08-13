# @ohos.enterprise.deviceSettings

This module provides enterprise device settings capabilities, including setting and obtaining the device screen-off time, system time, power policy, Eye Comfort mode, default input method, wallpaper, and hidden setting items. > **NOTE：**> > The APIs of this module can be called only by a device administrator application that is enabled. For details, see > [MDM Kit Development](../../../mdm/mdm-kit-guide.md).

**Since:** 10

**Deprecated since:** -1

<!--Device-unnamed-declare namespace deviceSettings--><!--Device-unnamed-declare namespace deviceSettings-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { deviceSettings } from '@kit.MDMKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addHiddenSettingsMenu](arkts-mdm-devicesettings-addhiddensettingsmenu-f.md#addHiddenSettingsMenu) |
| [getHiddenSettingsMenu](arkts-mdm-devicesettings-gethiddensettingsmenu-f.md#getHiddenSettingsMenu) |
| [getValue](arkts-mdm-devicesettings-getvalue-f.md#getValue) |
| [getValueForAccount](arkts-mdm-devicesettings-getvalueforaccount-f.md#getValueForAccount) |
| [removeHiddenSettingsMenu](arkts-mdm-devicesettings-removehiddensettingsmenu-f.md#removeHiddenSettingsMenu) |
| [setHomeWallpaper](arkts-mdm-devicesettings-sethomewallpaper-f.md#setHomeWallpaper) |
| [setSwitchStatus](arkts-mdm-devicesettings-setswitchstatus-f.md#setSwitchStatus) |
| [setUnlockWallpaper](arkts-mdm-devicesettings-setunlockwallpaper-f.md#setUnlockWallpaper) |
| [setValue](arkts-mdm-devicesettings-setvalue-f.md#setValue) |
| [setValueForAccount](arkts-mdm-devicesettings-setvalueforaccount-f.md#setValueForAccount) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getPowerPolicy](arkts-mdm-devicesettings-getpowerpolicy-f-sys.md#getPowerPolicy-(System-API)) |
| [getScreenOffTime](arkts-mdm-devicesettings-getscreenofftime-f-sys.md#getScreenOffTime-(System-API)) |
| [getScreenOffTime](arkts-mdm-devicesettings-getscreenofftime-f-sys.md#getScreenOffTime-(System-API)) |
| [installUserCertificate](arkts-mdm-devicesettings-installusercertificate-f-sys.md#installUserCertificate-(System-API)) |
| [installUserCertificate](arkts-mdm-devicesettings-installusercertificate-f-sys.md#installUserCertificate-(System-API)) |
| [setPowerPolicy](arkts-mdm-devicesettings-setpowerpolicy-f-sys.md#setPowerPolicy-(System-API)) |
| [setScreenOffTime](arkts-mdm-devicesettings-setscreenofftime-f-sys.md#setScreenOffTime-(System-API)) |
| [uninstallUserCertificate](arkts-mdm-devicesettings-uninstallusercertificate-f-sys.md#uninstallUserCertificate-(System-API)) |
| [uninstallUserCertificate](arkts-mdm-devicesettings-uninstallusercertificate-f-sys.md#uninstallUserCertificate-(System-API)) |
<!--DelEnd-->

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CertBlob](arkts-mdm-devicesettings-certblob-i-sys.md) |
| [PowerPolicy](arkts-mdm-devicesettings-powerpolicy-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [SettingsItem](arkts-mdm-devicesettings-settingsitem-e.md) |
| [SettingsMenu](arkts-mdm-devicesettings-settingsmenu-e.md) |
| [SwitchKey](arkts-mdm-devicesettings-switchkey-e.md) |
| [SwitchStatus](arkts-mdm-devicesettings-switchstatus-e.md) |

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [PowerPolicyAction](arkts-mdm-devicesettings-powerpolicyaction-e-sys.md) |
| [PowerScene](arkts-mdm-devicesettings-powerscene-e-sys.md) |
<!--DelEnd-->
