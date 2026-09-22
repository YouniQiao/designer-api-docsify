# MonitorDecoratorOptions

```TypeScript
declare interface MonitorDecoratorOptions
```

Represents the configuration options of the **@Monitor** decorator.

**Since:** 26.0.0

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## enableWildcard

```TypeScript
enableWildcard?: boolean
```

Whether to support the wildcard capability. The value **true** indicates to enable the wildcard capability, allowing the use of wildcards (**'*'**) in the path for fuzzy monitoring, and **false** indicates to disable the wildcard capability. The default value is **true**.

**Type:** boolean

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
