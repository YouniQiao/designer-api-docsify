# AnalysisToolResult（系统接口）

Result of an analysis tool execution.

**起始版本：** 26.1.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.1.0。

<!--Device-photoAccessHelper-interface AnalysisToolResult--><!--Device-photoAccessHelper-interface AnalysisToolResult-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## errCode

```TypeScript
errCode: int
```

Error code of the tool execution. The value 0 indicates success.Possible error codes:&lt;br&gt;23800203 - Temperature is too high.&lt;br&gt;23800204 - Battery level is too low.&lt;br&gt;23800205 - Storage space is insufficient.&lt;br&gt;23800206 - Power saving mode is enabled.&lt;br&gt;23800207 - Intelligent analysis service is already running.&lt;br&gt;23800208 - Intelligent analysis switch is disabled.&lt;br&gt;23800209 - Analysis service error. Check the logs for details.&lt;br&gt;23800301 - Internal system error.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 26.1.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AnalysisToolResult-errCode: int--><!--Device-AnalysisToolResult-errCode: int-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## result

```TypeScript
result?: string
```

Result of the tool execution, in JSON string format.

**类型：** string

**起始版本：** 26.1.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AnalysisToolResult-result?: string--><!--Device-AnalysisToolResult-result?: string-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

