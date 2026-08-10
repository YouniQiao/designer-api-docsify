# WatermarkCallback

```TypeScript
type WatermarkCallback = (jobId: string, fd: int) => void
```

定义用来注册强制水印处理的监听事件时使用的回调类型。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-print-type WatermarkCallback = (jobId: string, fd: int) => void--><!--Device-print-type WatermarkCallback = (jobId: string, fd: int) => void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| jobId | string | Yes | 表示当前打印任务的id。 |
| fd | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 表示当前文件的文件描述符。 |

