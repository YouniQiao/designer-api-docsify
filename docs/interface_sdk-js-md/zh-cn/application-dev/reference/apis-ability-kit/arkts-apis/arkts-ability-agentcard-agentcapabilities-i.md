# AgentCapabilities

Defines optional capabilities supported by an agent.

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

<!--Device-unnamed-export interface AgentCapabilities--><!--Device-unnamed-export interface AgentCapabilities-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

## extendedAgentCard

```TypeScript
extendedAgentCard?: boolean
```

Indicates if the agent supports providing an extended agent card when authenticated.

**类型：** boolean

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-AgentCapabilities-extendedAgentCard?: boolean--><!--Device-AgentCapabilities-extendedAgentCard?: boolean-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

## extension

```TypeScript
extension?: string
```

The protocol extension supported by the agent.

**类型：** string

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-AgentCapabilities-extension?: string--><!--Device-AgentCapabilities-extension?: string-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

## pushNotifications

```TypeScript
pushNotifications?: boolean
```

Indicates if the agent supports sending push notifications for asynchronous task updates.

**类型：** boolean

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-AgentCapabilities-pushNotifications?: boolean--><!--Device-AgentCapabilities-pushNotifications?: boolean-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

## stateTransitionHistory

```TypeScript
stateTransitionHistory?: boolean
```

If the Agent exposes task state change history.

**类型：** boolean

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-AgentCapabilities-stateTransitionHistory?: boolean--><!--Device-AgentCapabilities-stateTransitionHistory?: boolean-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

## streaming

```TypeScript
streaming?: boolean
```

Indicates if the agent supports streaming responses.

**类型：** boolean

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-AgentCapabilities-streaming?: boolean--><!--Device-AgentCapabilities-streaming?: boolean-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

