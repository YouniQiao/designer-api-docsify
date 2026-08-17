# @ohos.fontManager

/*
 Copyright (c) 2025 Huawei Device Co., Ltd.
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


**Since:** 23

<!--Device-unnamed-declare namespace fontManager--><!--Device-unnamed-declare namespace fontManager-End-->

**System capability:** SystemCapability.Global.FontManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { fontManager } from 'fontManager';
```

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [dataMigration](arkts-localization-fontmanager-datamigration-f-sys.md#datamigration) | Data migration API used during device upgrades to start a migration task, providing real-time feedback on migration progress and results through a callback function. |
| [installFont](arkts-localization-fontmanager-installfont-f-sys.md#installfont) | Installs a font file from a specified path into the system font library. This API uses a promise to return the result. After successful installation, applications can use the font by its font name. |
| [uninstallFont](arkts-localization-fontmanager-uninstallfont-f-sys.md#uninstallfont) | Uninstalls an installed font file from the system font library by font name. This API uses a promise to return the result. |
<!--DelEnd-->

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [DataMigrationCallback](arkts-localization-fontmanager-datamigrationcallback-i-sys.md) | Callback API type used during data migration, defining the callback methods for the data migration process. You must implement all methods of this API to receive heartbeat notifications, progress updates, and the final result during migration. |
| [DataMigrationProgress](arkts-localization-fontmanager-datamigrationprogress-i-sys.md) | Describes the progress information of data migration, including the progress percentage and estimated remaining time. This API is the parameter type of the `onProgress` API in the data migration callback. |
<!--DelEnd-->

