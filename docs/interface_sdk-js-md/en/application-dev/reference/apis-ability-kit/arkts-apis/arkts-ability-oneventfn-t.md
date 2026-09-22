# OnEventFn

```TypeScript
type OnEventFn = (event: CliToolEvent) => void
```

Defines the callback function type for receiving CLI tool events.

**Since:** 26.0.1

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [CliToolEvent](arkts-ability-clitoolevent-i.md) | Yes | The event sent by cli tool. |
