# createStream（系统接口）

## 导入模块

```TypeScript
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
```

## createStream

```TypeScript
function createStream(sessionId: int, param: StreamParam): Promise<int>
```

Creating a Stream.

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sessionId | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| param | [StreamParam](arkts-distributedservice-abilityconnectionmanager-streamparam-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: Promise & lt;number & gt;<br>ArkTS-Sta：Promise & lt;int & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [32300001](../errorcode-device-manager.md#32300001-重复创建传输流) |
| [32300003](../errorcode-device-manager.md#32300003-比特率不支持) |
| [32300004](../errorcode-device-manager.md#32300004-色彩空间不支持) |

**示例**

```TypeScript
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

hilog.info(0x0000, 'testTag', 'startStream');
let sessionId = 100;
// 创建传输流，配置名称为'receive'，角色为SOURCE（发送流）
abilityConnectionManager.createStream(sessionId ,{name: 'receive', role: 0}).then(async (streamId) => {
  // 配置Surface参数
  let surfaceParam: abilityConnectionManager.SurfaceParam = {
    width: 640,
    height: 480,
    format: 1
  }
  // 获取Surface唯一标识符
  let surfaceId = abilityConnectionManager.getSurfaceId(streamId, surfaceParam);
  hilog.info(0x0000, 'testTag', 'surfaceId is ' + surfaceId);
  // 将SurfaceID存储到全局状态管理中，供后续UI组件使用
  AppStorage.setOrCreate<string>('surfaceId', surfaceId);
  // 启动传输流
  abilityConnectionManager.startStream(streamId);
})
```
