# BundleStats

获取捆绑包统计信息。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.FileManagement.StorageService.SpatialStatistics

## 导入模块

```TypeScript
import { storageStatistics } from '@kit.CoreFileKit';
```

## appSize

```TypeScript
appSize: long
```

应用安装文件大小（单位为Byte）。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.FileManagement.StorageService.SpatialStatistics

## cacheSize

```TypeScript
cacheSize: long
```

应用缓存文件大小（单位为Byte）。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.FileManagement.StorageService.SpatialStatistics

## dataSize

```TypeScript
dataSize: long
```

应用文件存储大小（除应用安装文件）（单位为Byte）。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.FileManagement.StorageService.SpatialStatistics
