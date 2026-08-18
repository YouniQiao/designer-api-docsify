# @ohos.dlpSetDlpFeature(DLP)

/*
 Copyright (c) 2026 Huawei Device Co., Ltd.
 Licensed under the Apache License, Version 2.0 (the "License"),
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 /


**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace dlpSetDlpFeature--><!--Device-unnamed-declare namespace dlpSetDlpFeature-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { dlpSetDlpFeature } from '@kit.DataProtectionKit';
```

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [setDlpFeature](arkts-dataprotection-dlpsetdlpfeature-setdlpfeature-f-sys.md#setdlpfeature) | Sets the DLP status. This API uses a promise to return the result. The system enables or disables the DLP protection function based on the DLP status specified using this API. When this feature is enabled, right-click the file to be encrypted, and the encryption option is displayed in the shortcut menu. Files in .txt, .pdf, .xls, .xlsx, .ppt, .pptx, .doc, and .docx formats can be encrypted. This API is used to enable or disable the DLP function in enterprise policies. |
<!--DelEnd-->

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [DLPFeatureInfo](arkts-dataprotection-dlpsetdlpfeature-dlpfeatureinfo-i-sys.md) | Sets the DLP status. |
| [StatusInfoResult](arkts-dataprotection-dlpsetdlpfeature-statusinforesult-i-sys.md) | Describes the DLP settings. |
<!--DelEnd-->

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [DlpFeatureStatus](arkts-dataprotection-dlpsetdlpfeature-dlpfeaturestatus-e-sys.md) | Enumerates DLP statuses. |
<!--DelEnd-->

