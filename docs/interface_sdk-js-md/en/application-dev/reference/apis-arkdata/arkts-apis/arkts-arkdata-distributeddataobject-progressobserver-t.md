# ProgressObserver

```TypeScript
type ProgressObserver = (sessionId: string, progress: int) => void
```

定义传输进度的监听回调函数。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-distributedDataObject-type ProgressObserver = (sessionId: string, progress: int) => void--><!--Device-distributedDataObject-type ProgressObserver = (sessionId: string, progress: int) => void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sessionId | string | Yes | 标识变更对象的sessionId。长度不大于128字节，且只能包含字母、数字或下划线_。 |
| progress | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 标识资产传输进度。取值范围为[-1, 100]，取值为整数，-1表示获取进度失败，100表示传输完成。 |

