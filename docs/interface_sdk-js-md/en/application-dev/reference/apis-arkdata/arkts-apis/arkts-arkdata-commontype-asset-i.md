# Asset

记录资产附件（文件、图片、视频等类型文件）的相关信息。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-commonType-interface Asset--><!--Device-commonType-interface Asset-End-->

**System capability:** SystemCapability.DistributedDataManager.CommonType

## Modules to Import

```TypeScript
import { commonType } from 'kits/@kit.ArkData';
```

## createTime

```TypeScript
createTime: string
```

资产被创建出来的时间。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Asset-createTime: string--><!--Device-Asset-createTime: string-End-->

**System capability:** SystemCapability.DistributedDataManager.CommonType

## modifyTime

```TypeScript
modifyTime: string
```

资产最后一次被修改的时间。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Asset-modifyTime: string--><!--Device-Asset-modifyTime: string-End-->

**System capability:** SystemCapability.DistributedDataManager.CommonType

## name

```TypeScript
name: string
```

资产的名称。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Asset-name: string--><!--Device-Asset-name: string-End-->

**System capability:** SystemCapability.DistributedDataManager.CommonType

## path

```TypeScript
path: string
```

资产在应用沙箱里的路径。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Asset-path: string--><!--Device-Asset-path: string-End-->

**System capability:** SystemCapability.DistributedDataManager.CommonType

## size

```TypeScript
size: string
```

资产占用空间的大小。确保在全链路中保持统一、一致的存储格式与取值逻辑。建议所有系统节点均采用标准化处理方式（单位为字节（Byte），取值为非负整数）。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Asset-size: string--><!--Device-Asset-size: string-End-->

**System capability:** SystemCapability.DistributedDataManager.CommonType

## status

```TypeScript
status?: AssetStatus
```

资产的状态，默认值为ASSET_NORMAL。

**Type:** [AssetStatus](arkts-arkdata-relationalstore-assetstatus-e.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Asset-status?: AssetStatus--><!--Device-Asset-status?: AssetStatus-End-->

**System capability:** SystemCapability.DistributedDataManager.CommonType

## uri

```TypeScript
uri: string
```

资产的uri，在系统里的绝对路径。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-Asset-uri: string--><!--Device-Asset-uri: string-End-->

**System capability:** SystemCapability.DistributedDataManager.CommonType

