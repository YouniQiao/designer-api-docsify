# @ohos.fontManager

This module provides system applications with the capabilities to install and uninstall third-party fonts and migrate font data. Specifically:&lt;br&gt;- Installing font files from a specified path (.ttf and .ttc formats are supported).&lt;br&gt;- Uninstalling installed fonts by font name.&lt;br&gt;- Starting a font data migration task during device upgrades, and providing callbacks for migration progress and results.

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace fontManager--><!--Device-unnamed-declare namespace fontManager-End-->

**System capability:** SystemCapability.Global.FontManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { fontManager } from 'kits/@kit.LocalizationKit';
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

