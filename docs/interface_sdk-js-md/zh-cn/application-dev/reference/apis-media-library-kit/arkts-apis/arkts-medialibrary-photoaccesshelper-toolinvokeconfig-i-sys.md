# ToolInvokeConfig（系统接口）

Configuration for invoking an analysis tool.

**起始版本：** 26.1.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.1.0。

<!--Device-photoAccessHelper-interface ToolInvokeConfig--><!--Device-photoAccessHelper-interface ToolInvokeConfig-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## param

```TypeScript
param?: string
```

Parameters of the analysis tool to invoke, in JSON string format. The total length must not exceed 16KB.

**类型：** string

**起始版本：** 26.1.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolInvokeConfig-param?: string--><!--Device-ToolInvokeConfig-param?: string-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## type

```TypeScript
type: AnalysisToolType
```

Type of the analysis tool to invoke.

**类型：** [AnalysisToolType](arkts-medialibrary-photoaccesshelper-analysistooltype-e-sys.md)

**起始版本：** 26.1.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolInvokeConfig-type: AnalysisToolType--><!--Device-ToolInvokeConfig-type: AnalysisToolType-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

