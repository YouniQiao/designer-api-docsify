# @ohos.enterprise.deviceSettings(Device Settings Management)

This module provides enterprise device settings capabilities, including setting and obtaining the device screen-off time, system time, power policy, Eye Comfort mode, default input method, wallpaper, and hidden setting items.

> **NOTE：**&gt;
> The APIs of this module can be called only by a device administrator application that is enabled. For details, see
> [MDM Kit Development](../../../mdm/mdm-kit-guide.md).

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { deviceSettings } from '@kit.MDMKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addHiddenSettingsMenu(Device Settings Management)](arkts-mdm-devicesettings-addhiddensettingsmenu-f.md) |
| [getHiddenSettingsMenu(Device Settings Management)](arkts-mdm-devicesettings-gethiddensettingsmenu-f.md) |
| [getValue(Device Settings Management)](arkts-mdm-devicesettings-getvalue-f.md) |
| [getValueForAccount(Device Settings Management)](arkts-mdm-devicesettings-getvalueforaccount-f.md) |
| [removeHiddenSettingsMenu(Device Settings Management)](arkts-mdm-devicesettings-removehiddensettingsmenu-f.md) |
| [setHomeWallpaper(Device Settings Management)](arkts-mdm-devicesettings-sethomewallpaper-f.md) |
| [setSwitchStatus(Device Settings Management)](arkts-mdm-devicesettings-setswitchstatus-f.md) |
| [setUnlockWallpaper(Device Settings Management)](arkts-mdm-devicesettings-setunlockwallpaper-f.md) |
| [setValue(Device Settings Management)](arkts-mdm-devicesettings-setvalue-f.md) |
| [setValueForAccount(Device Settings Management)](arkts-mdm-devicesettings-setvalueforaccount-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getPowerPolicy(Device Settings Management)](arkts-mdm-devicesettings-getpowerpolicy-f-sys.md) |
| [getScreenOffTime(Device Settings Management)](arkts-mdm-devicesettings-getscreenofftime-f-sys.md) |
| [getScreenOffTime(Device Settings Management)](arkts-mdm-devicesettings-getscreenofftime-f-sys.md) |
| [installUserCertificate(Device Settings Management)](arkts-mdm-devicesettings-installusercertificate-f-sys.md) |
| [installUserCertificate(Device Settings Management)](arkts-mdm-devicesettings-installusercertificate-f-sys.md) |
| [setPowerPolicy(Device Settings Management)](arkts-mdm-devicesettings-setpowerpolicy-f-sys.md) |
| [setScreenOffTime(Device Settings Management)](arkts-mdm-devicesettings-setscreenofftime-f-sys.md) |
| [uninstallUserCertificate(Device Settings Management)](arkts-mdm-devicesettings-uninstallusercertificate-f-sys.md) |
| [uninstallUserCertificate(Device Settings Management)](arkts-mdm-devicesettings-uninstallusercertificate-f-sys.md) |
<!--DelEnd-->

<!--Del-->
### Interfaces(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CertBlob(Device Settings Management)](arkts-mdm-devicesettings-certblob-i-sys.md) |
| [PowerPolicy(Device Settings Management)](arkts-mdm-devicesettings-powerpolicy-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [SettingsItem(Device Settings Management)](arkts-mdm-devicesettings-settingsitem-e.md) |
| [SettingsMenu(Device Settings Management)](arkts-mdm-devicesettings-settingsmenu-e.md) |
| [SwitchKey(Device Settings Management)](arkts-mdm-devicesettings-switchkey-e.md) |
| [SwitchStatus(Device Settings Management)](arkts-mdm-devicesettings-switchstatus-e.md) |

<!--Del-->
### Enums(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [PowerPolicyAction(Device Settings Management)](arkts-mdm-devicesettings-powerpolicyaction-e-sys.md) |
| [PowerScene(Device Settings Management)](arkts-mdm-devicesettings-powerscene-e-sys.md) |
<!--DelEnd-->
