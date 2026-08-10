# IMonitor

当监听的变量变化时，状态管理框架侧将回调开发者注册的函数，并传入变化信息。变化信息的类型即为IMonitor类型。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface IMonitor--><!--Device-unnamed-export declare interface IMonitor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
value<T>(path?: string): IMonitorValue<T> | undefined
```

获取指定path的变化信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IMonitor-value<T>(path?: string): IMonitorValue<T> | undefined--><!--Device-IMonitor-value<T>(path?: string): IMonitorValue<T> | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | No | 可选，被监听变量的路径。未指定时默认使用变化路径数组dirty中的第一个路径。 |

**Return value:**

| Type | Description |
| --- | --- |
| [IMonitorValue](../arkts-components/arkts-arkui-imonitorvalue-i.md)&lt;T&gt; |  |

## dirty

```TypeScript
dirty: Array<string>
```

变化路径的数组。

**Type:** Array&lt;string&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IMonitor-dirty: Array<string>--><!--Device-IMonitor-dirty: Array<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

