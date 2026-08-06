# @ohos.enterprise.deviceSettings(Device Settings Management)

This module provides enterprise device settings capabilities, including setting and obtaining the device screen-off time, system time, power policy, Eye Comfort mode, default input method, wallpaper, and hidden setting items.
    **NOTE**  
    
    The APIs of this module can be called only by a device administrator application that is enabled. For details, see  
    \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare namespace deviceSettings--><!--Device-unnamed-declare namespace deviceSettings-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Summary

### Functions

| Name | Description |
| --- | --- |
| [addHiddenSettingsMenu](arkts-mdm-devicesettings-addhiddensettingsmenu-f.md#addhiddensettingsmenu) | Adds a setting item to the hidden setting item list of the current user. Then the setting item is hidden in the current user's settings menu and cannot be found in settings search. Even if the setting item is located through some means, it cannot be opened when tapped. The settings take effect immediately after the API is called. The Settings application does not need to be restarted. |
| [getHiddenSettingsMenu](arkts-mdm-devicesettings-gethiddensettingsmenu-f.md#gethiddensettingsmenu) | Obtains the hidden setting item list of the current user. |
| [getPowerPolicy](arkts-mdm-devicesettings-getpowerpolicy-f.md#getpowerpolicy) | Obtains the power policy. |
| [getScreenOffTime](arkts-mdm-devicesettings-getscreenofftime-f.md#getscreenofftime) | Obtains the device screen-off time. This API uses an asynchronous callback to return the result. |
| [getScreenOffTime](arkts-mdm-devicesettings-getscreenofftime-f.md#getscreenofftime-1) | Obtains the device screen-off time. This API uses an asynchronous promise to return the result. |
| [getValue](arkts-mdm-devicesettings-getvalue-f.md#getvalue) | Obtains a device setting policy. |
| [getValueForAccount](arkts-mdm-devicesettings-getvalueforaccount-f.md#getvalueforaccount) | Obtains the device policy of a specified user. This API allows you to obtain a specific parameter of a given user,such as obtaining the device name of user 100. |
| [installUserCertificate](arkts-mdm-devicesettings-installusercertificate-f.md#installusercertificate) | Installs a user certificate. This API uses a callback to return the result. |
| [installUserCertificate](arkts-mdm-devicesettings-installusercertificate-f.md#installusercertificate-1) | Installs a user certificate. This API uses a promise to return the result. |
| [removeHiddenSettingsMenu](arkts-mdm-devicesettings-removehiddensettingsmenu-f.md#removehiddensettingsmenu) | Removes a setting item from the hidden setting item list of the current user. Setting items in the hidden setting item list are hidden in the current user's settings menu and cannot be found in settings search. Even if a setting item is located through some means, it cannot be opened when tapped. If the remaining hidden setting item list is empty after the removal, all setting items are displayed. The settings take effect immediately after the API is called. The Settings application does not need to be restarted.  Since API version 26.0.0, if you call  [setDisallowedPolicyForAccount]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ to disable [SUPER\_\_\_ESCAPED\_UNDERSCORE\_\_\_HUB]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ and then call this API to remove SuperHub from the hidden setting item list, a policy conflict occurs and error code 9200010 is reported. |
| [setHomeWallpaper](arkts-mdm-devicesettings-sethomewallpaper-f.md#sethomewallpaper) | Sets the home screen wallpaper. This API uses a promise to return the result. |
| [setPowerPolicy](arkts-mdm-devicesettings-setpowerpolicy-f.md#setpowerpolicy) | Sets the power policy. |
| [setScreenOffTime](arkts-mdm-devicesettings-setscreenofftime-f.md#setscreenofftime) | Sets the device screen-off time. |
| [setSwitchStatus](arkts-mdm-devicesettings-setswitchstatus-f.md#setswitchstatus) | Sets the state of a switch. This API can enable or disable NearLink, Bluetooth, Wi-Fi, and NFC. After the setting is applied, users can manually enable or disable them. Bluetooth and NFC can be forced on. Once set, they cannot be manually turned on or off by the user. If a switch has been disabled through the  [setDisallowedPolicy]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ API, error code 203will be reported when you attempt to set the state of the switch through this API. In this case, you need to use the [setDisallowedPolicy]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ API to enable the switch. When multiple MDM applications are present on the device, there are no conflicts among the switch states set by different MDM applications. The policy set last takes effect. The three states, on (user can manually enable/disable), off (user can manually enable/disable), and forced on (user cannot manually disable), can be switched arbitrarily, and no conflict occurs. |
| [setUnlockWallpaper](arkts-mdm-devicesettings-setunlockwallpaper-f.md#setunlockwallpaper) | Sets the lock screen wallpaper. This API uses a promise to return the result. Enterprise device administrator applications can use this API to uniformly set the lock screen wallpaper for enterprise devices, for purposes such as corporate branding or security control. |
| [setValue](arkts-mdm-devicesettings-setvalue-f.md#setvalue) | Sets the device policy. |
| [setValueForAccount](arkts-mdm-devicesettings-setvalueforaccount-f.md#setvalueforaccount) | Sets the device policy for a specified user. This API allows you to set a specific parameter for a given user, such as setting the device name for user 100. |
| [uninstallUserCertificate](arkts-mdm-devicesettings-uninstallusercertificate-f.md#uninstallusercertificate) | Uninstalls a user certificate. This API uses a callback to return the result. |
| [uninstallUserCertificate](arkts-mdm-devicesettings-uninstallusercertificate-f.md#uninstallusercertificate-1) | Uninstalls a user certificate. This API uses a promise to return the result. |

### Interfaces

| Name | Description |
| --- | --- |
| [CertBlob](arkts-mdm-devicesettings-certblob-i.md) | Represents the certificate information. |
| [PowerPolicy](arkts-mdm-devicesettings-powerpolicy-i.md) | Represents the power policy. |

### Enums

| Name | Description |
| --- | --- |
| [PowerPolicyAction](arkts-mdm-devicesettings-powerpolicyaction-e.md) | Enumerates the actions that can be performed to apply the power policy. |
| [PowerScene](arkts-mdm-devicesettings-powerscene-e.md) | Defines the scenario to which the power policy applies. |
| [SettingsItem](arkts-mdm-devicesettings-settingsitem-e.md) | Policy type. |
| [SettingsMenu](arkts-mdm-devicesettings-settingsmenu-e.md) | Describes the setting item list. |
| [SwitchKey](arkts-mdm-devicesettings-switchkey-e.md) | Enumerates switch names. |
| [SwitchStatus](arkts-mdm-devicesettings-switchstatus-e.md) | Enumerates switch states. |

