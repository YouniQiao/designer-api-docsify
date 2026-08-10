# OnEventFn（系统接口）

```TypeScript
type OnEventFn = (event: CliToolEvent) => void
```

Defines cli event callback function.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-type OnEventFn = (event: CliToolEvent) => void--><!--Device-unnamed-type OnEventFn = (event: CliToolEvent) => void-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [CliToolEvent](arkts-ability-clitoolevent-i-sys.md) | 是 | The event sent by cli tool. |

