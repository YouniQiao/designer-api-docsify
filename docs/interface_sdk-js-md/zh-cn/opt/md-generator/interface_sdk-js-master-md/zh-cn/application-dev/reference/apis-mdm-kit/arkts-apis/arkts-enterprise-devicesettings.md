# @ohos.enterprise.deviceSettings

本模块提供企业设备设置能力，支持设置和获取设备息屏时间、系统时间、电源策略、护眼模式、默认输入法、壁纸、隐藏设置项等。 > **说明：** > > 本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../../../mdm/mdm-kit-guide.md)。

**起始版本：** 10

<!--Device-unnamed-declare namespace deviceSettings--><!--Device-unnamed-declare namespace deviceSettings-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
```

## 汇总

### 函数

| 名称 |
| --- |
| [addHiddenSettingsMenu](arkts-mdm-devicesettings-addhiddensettingsmenu-f.md#addhiddensettingsmenu) |
| [getHiddenSettingsMenu](arkts-mdm-devicesettings-gethiddensettingsmenu-f.md#gethiddensettingsmenu) |
| [getValue](arkts-mdm-devicesettings-getvalue-f.md#getvalue) |
| [getValueForAccount](arkts-mdm-devicesettings-getvalueforaccount-f.md#getvalueforaccount) |
| [removeHiddenSettingsMenu](arkts-mdm-devicesettings-removehiddensettingsmenu-f.md#removehiddensettingsmenu) |
| [setHomeWallpaper](arkts-mdm-devicesettings-sethomewallpaper-f.md#sethomewallpaper) |
| [setSwitchStatus](arkts-mdm-devicesettings-setswitchstatus-f.md#setswitchstatus) |
| [setUnlockWallpaper](arkts-mdm-devicesettings-setunlockwallpaper-f.md#setunlockwallpaper) |
| [setValue](arkts-mdm-devicesettings-setvalue-f.md#setvalue) |
| [setValueForAccount](arkts-mdm-devicesettings-setvalueforaccount-f.md#setvalueforaccount) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [getPowerPolicy](arkts-mdm-devicesettings-getpowerpolicy-f-sys.md#getpowerpolicy系统接口) |
| [getScreenOffTime](arkts-mdm-devicesettings-getscreenofftime-f-sys.md#getscreenofftime系统接口) |
| [getScreenOffTime](arkts-mdm-devicesettings-getscreenofftime-f-sys.md#getscreenofftime系统接口) |
| [installUserCertificate](arkts-mdm-devicesettings-installusercertificate-f-sys.md#installusercertificate系统接口) |
| [installUserCertificate](arkts-mdm-devicesettings-installusercertificate-f-sys.md#installusercertificate系统接口) |
| [setPowerPolicy](arkts-mdm-devicesettings-setpowerpolicy-f-sys.md#setpowerpolicy系统接口) |
| [setScreenOffTime](arkts-mdm-devicesettings-setscreenofftime-f-sys.md#setscreenofftime系统接口) |
| [uninstallUserCertificate](arkts-mdm-devicesettings-uninstallusercertificate-f-sys.md#uninstallusercertificate系统接口) |
| [uninstallUserCertificate](arkts-mdm-devicesettings-uninstallusercertificate-f-sys.md#uninstallusercertificate系统接口) |
<!--DelEnd-->

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [CertBlob](arkts-mdm-devicesettings-certblob-i-sys.md) |
| [PowerPolicy](arkts-mdm-devicesettings-powerpolicy-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [SettingsItem](arkts-mdm-devicesettings-settingsitem-e.md) |
| [SettingsMenu](arkts-mdm-devicesettings-settingsmenu-e.md) |
| [SwitchKey](arkts-mdm-devicesettings-switchkey-e.md) |
| [SwitchStatus](arkts-mdm-devicesettings-switchstatus-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [PowerPolicyAction](arkts-mdm-devicesettings-powerpolicyaction-e-sys.md) |
| [PowerScene](arkts-mdm-devicesettings-powerscene-e-sys.md) |
<!--DelEnd-->
