# @ohos.fontManager(字体管理)

本模块为系统应用提供第三方字体的安装、卸载以及字体数据迁移能力。具体为：  
- 安装指定路径的字体文件（支持.ttf、.ttc格式）。  
- 根据字体名称卸载已安装的字体。  
- 在设备升级期间启动字体数据迁移任务，并提供迁移进度和结果回调。

**起始版本：** 19

**系统能力：** SystemCapability.Global.FontManager

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { fontManager } from 'kits/@kit.LocalizationKit';
```

## 汇总

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [dataMigration(字体管理)](arkts-localization-fontmanager-datamigration-f-sys.md) |
| [installFont(字体管理)](arkts-localization-fontmanager-installfont-f-sys.md) |
| [uninstallFont(字体管理)](arkts-localization-fontmanager-uninstallfont-f-sys.md) |
<!--DelEnd-->

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [DataMigrationCallback(字体管理)](arkts-localization-fontmanager-datamigrationcallback-i-sys.md) |
| [DataMigrationProgress(字体管理)](arkts-localization-fontmanager-datamigrationprogress-i-sys.md) |
<!--DelEnd-->
