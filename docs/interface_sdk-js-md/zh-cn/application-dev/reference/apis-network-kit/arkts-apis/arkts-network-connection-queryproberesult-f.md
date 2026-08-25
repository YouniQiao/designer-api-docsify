# queryProbeResult

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## queryProbeResult

```TypeScript
function queryProbeResult(destination: string, duration: number): Promise<ProbeResultInfo>
```

查询网络探测结果。若出现异常（例如断网），导致发送请求失败，则接口会立即返回，不再进行后续探测。本接口使用Promise方式作为异步方法。

> **说明：**&gt;
> 此接口用于对目标主机进行一段持续时间的网络探测，以获取丢包率和RTT信息。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.INTERNET

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [destination](arkts-network-connection-routeinfo-i.md) | string | 是 |
| duration | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[ProbeResultInfo](arkts-network-connection-proberesultinfo-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [2100001](../errorcode-net-connection.md#2100001-非法参数值) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |
