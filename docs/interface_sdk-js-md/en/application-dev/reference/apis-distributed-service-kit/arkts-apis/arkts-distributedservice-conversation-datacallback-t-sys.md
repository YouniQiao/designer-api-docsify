# DataCallback (System API)

```TypeScript
type DataCallback = (deviceId: string, msg: ArrayBuffer) => void
```

数据接收回调函数类型。

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-conversation-type DataCallback = (deviceId: string, msg: ArrayBuffer) => void--><!--Device-conversation-type DataCallback = (deviceId: string, msg: ArrayBuffer) => void-End-->

**System capability:** SystemCapability.Communication.SoftBus.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | string | Yes | 发送数据的源设备的networkId或UDID。 |
| msg | ArrayBuffer | Yes | 接收到的数据内容，为ArrayBuffer格式的二进制数据，数据格式与发送端发送的数据格式一致， 由应用层协议定义。 |

