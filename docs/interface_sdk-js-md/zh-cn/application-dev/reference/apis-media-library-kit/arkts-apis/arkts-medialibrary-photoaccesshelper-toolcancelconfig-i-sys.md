# ToolCancelConfig（系统接口）

Configuration for canceling an analysis tool.

**起始版本：** 26.1.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.1.0。

<!--Device-photoAccessHelper-interface ToolCancelConfig--><!--Device-photoAccessHelper-interface ToolCancelConfig-End-->

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

Parameters for canceling the analysis tool, in JSON string format. The total length must not exceed 16KB.

**类型：** string

**起始版本：** 26.1.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolCancelConfig-param?: string--><!--Device-ToolCancelConfig-param?: string-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## taskId

```TypeScript
taskId: string
```

Task ID to cancel. It is a valid ID returned by **invokeAnalysisTool**.

**类型：** string

**起始版本：** 26.1.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ToolCancelConfig-taskId: string--><!--Device-ToolCancelConfig-taskId: string-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

