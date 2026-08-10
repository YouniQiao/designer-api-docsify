# queryProbeResult

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## queryProbeResult

```TypeScript
function queryProbeResult(destination: string, duration: int): Promise<ProbeResultInfo>
```

Query a network probe result.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**需要权限：** ohos.permission.INTERNET

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-connection-function queryProbeResult(destination: string, duration: int): Promise<ProbeResultInfo>--><!--Device-connection-function queryProbeResult(destination: string, duration: int): Promise<ProbeResultInfo>-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| destination | string | 是 | the distination domain or address. |
| duration | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | probe duration. Unit: second. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;ProbeResultInfo&gt; | The promise returned by the function. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2100001 | Invalid parameter value. |
| 2100003 | Internal error. |
| 201 | Permission denied. |

## 示例

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let dest: string = "www.example.com";
let duration: number = 10;

connection.queryProbeResult(dest, duration).then((data: connection.ProbeResultInfo) => {
    console.info(`Succeeded to get LossRate: ${data.lossRate}, Succeeded to get RTT: ${data.rtt}`);
}).catch((err: BusinessError) => {
    console.error(`Failed to get request. Code:${err.code}, message:${err.message}`);
});
```

