# @ohos.fontManager(Font Management)

This module provides system applications with the capabilities to install and uninstall third-party fonts and migrate font data. Specifically:   
- Installing font files from a specified path (.ttf and .ttc formats are supported).   
- Uninstalling installed fonts by font name.   
- Starting a font data migration task during device upgrades, and providing callbacks for migration progress and results.

**Since:** 19

**System capability:** SystemCapability.Global.FontManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import fontManager from '@kit.LocalizationKit';
```

## Summary

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [dataMigration(Font Management)](arkts-localization-fontmanager-datamigration-f-sys.md) | Data migration API used during device upgrades to start a migration task, providing real-time feedback on migration progress and results through a callback function. |
| [installFont(Font Management)](arkts-localization-fontmanager-installfont-f-sys.md) | Installs a font file from a specified path into the system font library. This API uses a promise to return the result. After successful installation, applications can use the font by its font name. |
| [uninstallFont(Font Management)](arkts-localization-fontmanager-uninstallfont-f-sys.md) | Uninstalls an installed font file from the system font library by font name. This API uses a promise to return the result. |
<!--DelEnd-->

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [DataMigrationCallback(Font Management)](arkts-localization-fontmanager-datamigrationcallback-i-sys.md) | Callback API type used during data migration, defining the callback methods for the data migration process. You must implement all methods of this API to receive heartbeat notifications, progress updates, and the final result during migration. |
| [DataMigrationProgress(Font Management)](arkts-localization-fontmanager-datamigrationprogress-i-sys.md) | Describes the progress information of data migration, including the progress percentage and estimated remaining time. This API is the parameter type of the `onProgress` API in the data migration callback. |
<!--DelEnd-->
