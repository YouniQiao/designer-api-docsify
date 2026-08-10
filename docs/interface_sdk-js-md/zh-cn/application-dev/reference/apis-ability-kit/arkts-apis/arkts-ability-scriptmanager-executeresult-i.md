# ExecuteResult

Result of arkTS script execution.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

<!--Device-scriptManager-interface ExecuteResult--><!--Device-scriptManager-interface ExecuteResult-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

## 导入模块

```TypeScript
import { scriptManager } from 'kits/@kit.AbilityKit';
```

## code

```TypeScript
code: number
```

Indicates result code.The value range is all integers.

**类型：** number

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-ExecuteResult-code: number--><!--Device-ExecuteResult-code: number-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

## flags

```TypeScript
flags?: number
```

Indicates the URIs read and write permissions which consistent with {@link Want#flags},flags must be one of {@link wantConstant#Flags#FLAG_AUTH_READ_URI_PERMISSION},{@link wantConstant#Flags#FLAG_AUTH_WRITE_URI_PERMISSION},{@link wantConstant#Flags#FLAG_AUTH_READ_URI_PERMISSION}|{@link wantConstant#Flags#FLAG_AUTH_WRITE_URI_PERMISSION}.The value range is all integers.

**类型：** number

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-ExecuteResult-flags?: number--><!--Device-ExecuteResult-flags?: number-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

## result

```TypeScript
result?: Record<string, Object>
```

Indicates execute result.

**类型：** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Object&gt;

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-ExecuteResult-result?: Record<string, Object>--><!--Device-ExecuteResult-result?: Record<string, Object>-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

## uris

```TypeScript
uris?: Array<string>
```

Indicates the URIs will be authorized to the caller.

**类型：** Array&lt;string&gt;

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-ExecuteResult-uris?: Array<string>--><!--Device-ExecuteResult-uris?: Array<string>-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

