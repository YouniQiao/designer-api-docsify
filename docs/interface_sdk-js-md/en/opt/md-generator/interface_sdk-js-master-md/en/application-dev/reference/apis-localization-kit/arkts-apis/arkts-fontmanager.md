# @ohos.fontManager

This module provides system applications with the capabilities to install and uninstall third-party fonts and migrate font data. Specifically:&lt;br&gt;- Installing font files from a specified path (.ttf and .ttc formats are supported).&lt;br&gt;- Uninstalling installed fonts by font name.&lt;br&gt;- Starting a font data migration task during device upgrades, and providing callbacks for migration progress and results.

**Since:** 19

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

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [dataMigration](arkts-localization-fontmanager-datamigration-f-sys.md#datamigration) |
| [installFont](arkts-localization-fontmanager-installfont-f-sys.md#installfont) |
| [uninstallFont](arkts-localization-fontmanager-uninstallfont-f-sys.md#uninstallfont) |
<!--DelEnd-->

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DataMigrationCallback](arkts-localization-fontmanager-datamigrationcallback-i-sys.md) |
| [DataMigrationProgress](arkts-localization-fontmanager-datamigrationprogress-i-sys.md) |
<!--DelEnd-->
