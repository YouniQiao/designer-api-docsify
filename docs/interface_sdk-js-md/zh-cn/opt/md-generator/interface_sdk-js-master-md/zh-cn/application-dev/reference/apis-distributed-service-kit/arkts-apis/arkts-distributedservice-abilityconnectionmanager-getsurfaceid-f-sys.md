# getSurfaceId（系统接口）

## getSurfaceId

```TypeScript
function getSurfaceId(streamId: number, param: SurfaceParam): string
```

Obtains the transmission surface.

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-abilityConnectionManager-function getSurfaceId(streamId: int, param: SurfaceParam): string--><!--Device-abilityConnectionManager-function getSurfaceId(streamId: int, param: SurfaceParam): string-End-->

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| streamId | number | 是 |
| param | [SurfaceParam](arkts-distributedservice-abilityconnectionmanager-surfaceparam-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

hilog.info(0x0000, 'testTag', 'getSurfaceId');
let sessionId = 100;
abilityConnectionManager.createStream(sessionId, {name: 'receive', role: 0}).then(async (streamId) => {
  let surfaceParam: abilityConnectionManager.SurfaceParam = {
    width: 640,
    height: 480,
    format: 1
  }
  let surfaceId = abilityConnectionManager.getSurfaceId(streamId, surfaceParam);
})
```
