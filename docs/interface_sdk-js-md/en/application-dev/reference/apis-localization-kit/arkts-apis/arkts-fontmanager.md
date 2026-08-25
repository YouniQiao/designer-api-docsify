# @ohos.fontManager(Font Management)

This module provides system applications with the capabilities to install and uninstall third-party fonts and migrate font data. Specifically: <br>- Installing font files from a specified path (.ttf and .ttc formats are supported). <br>- Uninstalling installed fonts by font name. <br>- Starting a font data migration task during device upgrades, and providing callbacks for migration progress and results.

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Global.FontManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { fontManager } from '@kit.LocalizationKit';
```

## Summary

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [dataMigration(Font Management)](arkts-localization-fontmanager-datamigration-f-sys.md) |
| [installFont(Font Management)](arkts-localization-fontmanager-installfont-f-sys.md) |
| [uninstallFont(Font Management)](arkts-localization-fontmanager-uninstallfont-f-sys.md) |
<!--DelEnd-->

<!--Del-->
### Interfaces(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DataMigrationCallback(Font Management)](arkts-localization-fontmanager-datamigrationcallback-i-sys.md) |
| [DataMigrationProgress(Font Management)](arkts-localization-fontmanager-datamigrationprogress-i-sys.md) |
<!--DelEnd-->
