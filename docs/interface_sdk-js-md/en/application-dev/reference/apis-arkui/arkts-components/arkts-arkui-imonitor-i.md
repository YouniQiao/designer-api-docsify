# IMonitor

Define IMonitor interface

**Since:** 12

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## value

```TypeScript
value<T>(path?: string): IMonitorValue<T> | undefined
```

Return the pair of the value before the most recent change and current value for given path. If path does not exist, return undefined; If path is not specified, return the value pair corresponding to the first path in dirty.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [IMonitorValue](arkts-arkui-imonitorvalue-i.md)&lt;T&gt; \| undefined |  |

## dirty

```TypeScript
dirty: Array<string>
```

Array of changed paths(keys)

**Type:** Array&lt;string&gt;

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
