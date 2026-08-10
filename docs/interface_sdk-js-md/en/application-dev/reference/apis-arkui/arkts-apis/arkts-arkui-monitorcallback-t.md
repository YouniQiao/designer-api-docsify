# MonitorCallback

```TypeScript
export type MonitorCallback = (iMonitor: IMonitor) => void
```

触发监听时被调用的回调函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type MonitorCallback = (iMonitor: IMonitor) => void--><!--Device-unnamed-export type MonitorCallback = (iMonitor: IMonitor) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| iMonitor | [IMonitor](arkts-arkui-decorator-imonitor-i.md) | Yes | 保存触发监听前后的值以及路径。 |

