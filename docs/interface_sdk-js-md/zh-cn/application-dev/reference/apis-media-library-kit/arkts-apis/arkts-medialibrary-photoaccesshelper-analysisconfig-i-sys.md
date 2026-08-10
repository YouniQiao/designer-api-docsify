# AnalysisConfig（系统接口）

Defines the asset analysis configuration.

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

<!--Device-photoAccessHelper-interface AnalysisConfig--><!--Device-photoAccessHelper-interface AnalysisConfig-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## extraInfos

```TypeScript
extraInfos?: string
```

Extended information in JSON string format.

Length range: (0, 500].

**类型：** string

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AnalysisConfig-extraInfos?: string--><!--Device-AnalysisConfig-extraInfos?: string-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## types

```TypeScript
types: AnalysisType[]
```

Array of intelligent analysis types. The maximum size of the array is the number of members defined by the   
[AnalysisType](arkts-medialibrary-photoaccesshelper-analysistype-e-sys.md) enum.

**类型：** [AnalysisType](arkts-medialibrary-photoaccesshelper-analysistype-e-sys.md)[]

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AnalysisConfig-types: AnalysisType[]--><!--Device-AnalysisConfig-types: AnalysisType[]-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## uris

```TypeScript
uris: string[]
```

Asset URI array.

Length range: [0, 100].

**类型：** string[]

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AnalysisConfig-uris: string[]--><!--Device-AnalysisConfig-uris: string[]-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

