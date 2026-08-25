# @ohos.enterprise.deviceSettings(设备设置管理)

本模块提供企业设备设置能力，支持设置和获取设备息屏时间、系统时间、电源策略、护眼模式、默认输入法、壁纸、隐藏设置项等。

> **说明：**&gt;
> 本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../../../mdm/mdm-kit-guide.md)。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

## 导入模块

```TypeScript
import { deviceSettings } from '@kit.MDMKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [addHiddenSettingsMenu(设备设置管理)](arkts-mdm-devicesettings-addhiddensettingsmenu-f.md) |
| [getHiddenSettingsMenu(设备设置管理)](arkts-mdm-devicesettings-gethiddensettingsmenu-f.md) |
| [getValue(设备设置管理)](arkts-mdm-devicesettings-getvalue-f.md) |
| [getValueForAccount(设备设置管理)](arkts-mdm-devicesettings-getvalueforaccount-f.md) |
| [removeHiddenSettingsMenu(设备设置管理)](arkts-mdm-devicesettings-removehiddensettingsmenu-f.md) |
| [setHomeWallpaper(设备设置管理)](arkts-mdm-devicesettings-sethomewallpaper-f.md) |
| [setSwitchStatus(设备设置管理)](arkts-mdm-devicesettings-setswitchstatus-f.md) |
| [setUnlockWallpaper(设备设置管理)](arkts-mdm-devicesettings-setunlockwallpaper-f.md) |
| [setValue(设备设置管理)](arkts-mdm-devicesettings-setvalue-f.md) |
| [setValueForAccount(设备设置管理)](arkts-mdm-devicesettings-setvalueforaccount-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [getPowerPolicy(设备设置管理)](arkts-mdm-devicesettings-getpowerpolicy-f-sys.md) |
| [getScreenOffTime(设备设置管理)](arkts-mdm-devicesettings-getscreenofftime-f-sys.md) |
| [getScreenOffTime(设备设置管理)](arkts-mdm-devicesettings-getscreenofftime-f-sys.md) |
| [installUserCertificate(设备设置管理)](arkts-mdm-devicesettings-installusercertificate-f-sys.md) |
| [installUserCertificate(设备设置管理)](arkts-mdm-devicesettings-installusercertificate-f-sys.md) |
| [setPowerPolicy(设备设置管理)](arkts-mdm-devicesettings-setpowerpolicy-f-sys.md) |
| [setScreenOffTime(设备设置管理)](arkts-mdm-devicesettings-setscreenofftime-f-sys.md) |
| [uninstallUserCertificate(设备设置管理)](arkts-mdm-devicesettings-uninstallusercertificate-f-sys.md) |
| [uninstallUserCertificate(设备设置管理)](arkts-mdm-devicesettings-uninstallusercertificate-f-sys.md) |
<!--DelEnd-->

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [CertBlob(设备设置管理)](arkts-mdm-devicesettings-certblob-i-sys.md) |
| [PowerPolicy(设备设置管理)](arkts-mdm-devicesettings-powerpolicy-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [SettingsItem(设备设置管理)](arkts-mdm-devicesettings-settingsitem-e.md) |
| [SettingsMenu(设备设置管理)](arkts-mdm-devicesettings-settingsmenu-e.md) |
| [SwitchKey(设备设置管理)](arkts-mdm-devicesettings-switchkey-e.md) |
| [SwitchStatus(设备设置管理)](arkts-mdm-devicesettings-switchstatus-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [PowerPolicyAction(设备设置管理)](arkts-mdm-devicesettings-powerpolicyaction-e-sys.md) |
| [PowerScene(设备设置管理)](arkts-mdm-devicesettings-powerscene-e-sys.md) |
<!--DelEnd-->
