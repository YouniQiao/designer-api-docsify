# IMonitor

Define IMonitor interface

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface IMonitor--><!--Device-unnamed-export declare interface IMonitor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
value<T>(path?: string): IMonitorValue<T> | undefined
```

Return the pair of the value before the most recent change and current value for given path. If path does not exist, return undefined; If path is not specified, return the value pair corresponding to the first path in dirty.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IMonitor-value<T>(path?: string): IMonitorValue<T> | undefined--><!--Device-IMonitor-value<T>(path?: string): IMonitorValue<T> | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | No | Listened property name |

**Return value:**

| Type | Description |
| --- | --- |
| [IMonitorValue](arkts-na-decorator-imonitorvalue-i.md)&lt;T&gt; |  |

## dirty

```TypeScript
dirty: Array<string>
```

Array of changed paths(keys)

**Type:** Array&lt;string&gt;

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IMonitor-dirty: Array<string>--><!--Device-IMonitor-dirty: Array<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

