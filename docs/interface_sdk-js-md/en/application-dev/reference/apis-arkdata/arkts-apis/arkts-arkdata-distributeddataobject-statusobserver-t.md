# StatusObserver

```TypeScript
type StatusObserver = (sessionId: string, networkId: string, status: string) => void
```

定义获取分布式对象状态变更的监听回调函数。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-distributedDataObject-type StatusObserver = (sessionId: string, networkId: string, status: string) => void--><!--Device-distributedDataObject-type StatusObserver = (sessionId: string, networkId: string, status: string) => void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sessionId | string | Yes | 标识变更对象的sessionId。长度不大于128字节，且只能包含字母、数字或下划线_。 |
| networkId | string | Yes | 对端设备的网络标识。要求字符串非空且长度不超过255字节。 |
| status | string | Yes | 标识分布式对象的状态，可能的取值有'online'（上线）、'offline'（下线）和'restore'（恢复）。 |

