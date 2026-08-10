# @ohos.settingsLite

Defines the lite settings capability for wearables.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为24。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-unnamed-declare namespace settingsLite--><!--Device-unnamed-declare namespace settingsLite-End-->

**系统能力：** SystemCapability.Applications.Settings.Core.Lite

## 导入模块

```TypeScript
import { settingsLite } from 'kits/@kit.BasicServicesKit';
```

## 汇总

### 函数

| 名称 | 说明 |
| --- | --- |
| [isDoubleClickAppForSelf](arkts-basicservices-settingslite-isdoubleclickappforself-f.md#isdoubleclickappforself) | 1. Checks whether the application started by double-pressing the function key is the application itself.2. This API is triggered to check whether double-pressing the function key starts the application itself. |
| [openDoubleClickSettingsPage](arkts-basicservices-settingslite-opendoubleclicksettingspage-f.md#opendoubleclicksettingspage) | Opens the settings page for double-pressing the function key. |
| [openNfcSettingsPage](arkts-basicservices-settingslite-opennfcsettingspage-f.md#opennfcsettingspage) | Opens the NFC settings page. |
| [openPinSettingPage](arkts-basicservices-settingslite-openpinsettingpage-f.md#openpinsettingpage) | Opens the password settings page. |

### 接口

| 名称 | 说明 |
| --- | --- |
| [ClickCallback](arkts-basicservices-settingslite-clickcallback-i.md) | Defines a callback used to return whether the application started by double-pressing the function key is the application itself. |

