# @ohos.settingsLite

/*
 Copyright (c) 2026 Huawei Device Co., Ltd.
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 /


**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the FA model.

<!--Device-unnamed-declare namespace settingsLite--><!--Device-unnamed-declare namespace settingsLite-End-->

**System capability:** SystemCapability.Applications.Settings.Core.Lite

## Modules to Import

```TypeScript
import { settingsLite } from '@kit.BasicServicesKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [isDoubleClickAppForSelf](arkts-basicservices-settingslite-isdoubleclickappforself-f.md#isDoubleClickAppForSelf) | 1. Checks whether the application started by double-pressing the function key is the application itself. 2. This API is triggered to check whether double-pressing the function key starts the application itself. |
| [openDoubleClickSettingsPage](arkts-basicservices-settingslite-opendoubleclicksettingspage-f.md#openDoubleClickSettingsPage) | Opens the settings page for double-pressing the function key. |
| [openNfcSettingsPage](arkts-basicservices-settingslite-opennfcsettingspage-f.md#openNfcSettingsPage) | Opens the NFC settings page. |
| [openPinSettingPage](arkts-basicservices-settingslite-openpinsettingpage-f.md#openPinSettingPage) | Opens the password settings page. |

### Interfaces

| Name | Description |
| --- | --- |
| [ClickCallback](arkts-basicservices-settingslite-clickcallback-i.md) | Defines a callback used to return whether the application started by double-pressing the function key is the application itself. |

