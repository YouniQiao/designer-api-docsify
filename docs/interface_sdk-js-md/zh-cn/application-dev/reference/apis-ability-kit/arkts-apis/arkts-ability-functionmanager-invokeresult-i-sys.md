# InvokeResult（系统接口）

Encapsulates the success or failure status of function invocation.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

<!--Device-functionManager-interface InvokeResult--><!--Device-functionManager-interface InvokeResult-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { functionManager } from 'kits/@kit.AbilityKit';
```

## data

```TypeScript
data?: any
```

The returned data on success. The type can be any JSON value.Only present when {@link InvokeResult.success } is true.

**类型：** any

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InvokeResult-data?: any--><!--Device-InvokeResult-data?: any-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

## errorCode

```TypeScript
errorCode?: number
```

The error code on failure (numeric).Only present when {@link InvokeResult.success } is false.

**类型：** number

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InvokeResult-errorCode?: number--><!--Device-InvokeResult-errorCode?: number-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

## errorMsg

```TypeScript
errorMsg?: string
```

The error description on failure.Only present when {@link InvokeResult.success } is false.

**类型：** string

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InvokeResult-errorMsg?: string--><!--Device-InvokeResult-errorMsg?: string-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

## success

```TypeScript
success: boolean
```

Indicates whether the invocation was successful (at business logic level).true: Invocation succeeded, {@link InvokeResult.data } contains the returned data.false: Invocation failed, {@link InvokeResult.errorCode } and {@link InvokeResult.errorMsg } contain error information.

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-InvokeResult-success: boolean--><!--Device-InvokeResult-success: boolean-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

