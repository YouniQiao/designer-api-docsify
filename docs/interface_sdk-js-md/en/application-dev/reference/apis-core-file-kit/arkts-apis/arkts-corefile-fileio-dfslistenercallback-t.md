# DfsListenerCallback

```TypeScript
type DfsListenerCallback = (networkId: string, status: int) => void
```

DfsListener Callback function.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-fileIo-type DfsListenerCallback = (networkId: string, status: int) => void--><!--Device-fileIo-type DfsListenerCallback = (networkId: string, status: int) => void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| networkId | string | Yes | 设备的网络Id。 |
| status | int | Yes | 分布式文件系统的状态码（以connectDfs回调onStatus的特定错误码作为入参）。 触发场景为connectDfs调用过程中出现对端设备异常，对应错误码为：- 13900046：软件造成连接中断。 |

