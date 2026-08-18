# sendData

## 导入模块

```TypeScript
```

## sendData

```TypeScript
function sendData(sessionId: number, data: ArrayBuffer): Promise<void>
```

应用连接成功后，设备A或设备B可向对端设备发送[ArrayBuffer](../../../arkts-utils/arraybuffer-object.md)字节流。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-abilityConnectionManager-function sendData(sessionId: int, data: ArrayBuffer): Promise<void>--><!--Device-abilityConnectionManager-function sendData(sessionId: int, data: ArrayBuffer): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sessionId | number | 是 |
| data | ArrayBuffer | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { util } from '@kit.ArkTS';

let textEncoder = util.TextEncoder.create("utf-8");
const arrayBuffer  = textEncoder.encodeInto("data send success");

let sessionId = 100;
abilityConnectionManager.sendData(sessionId, arrayBuffer.buffer).then(() => {
  hilog.info(0x0000, 'testTag', "sendData success");
}).catch(() => {
  hilog.error(0x0000, 'testTag', "sendData failed");
})
```
