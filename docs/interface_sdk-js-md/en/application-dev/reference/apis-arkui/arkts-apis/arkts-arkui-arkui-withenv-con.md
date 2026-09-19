# Constants

## WithEnv

```TypeScript
export declare const WithEnv: WithEnvInterface
```

The **WithEnv** component is used to set a local environment variable scope for a child component tree. Developers can use this component to provide custom environment variables for descendant components, or set system environment variables.

> **NOTE:** 
> 
> - Custom environment variables can be set through [customEnv](arkts-arkui-arkui-withenv-withenvattribute-c.md#customenv).
> - System environment variable keys can be set through [env](arkts-arkui-arkui-withenv-withenvattribute-c.md#env). They are stored in [WritableEnvKey](../arkts-components/arkts-arkui-writableenvkey-c.md).
> - When **WithEnv** is nested, the nearest scope takes effect for environment variables with the same name.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## WithEnvInstance

```TypeScript
export declare const WithEnvInstance: WithEnvAttribute
```

Define WithEnv Logic Component Instance.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
