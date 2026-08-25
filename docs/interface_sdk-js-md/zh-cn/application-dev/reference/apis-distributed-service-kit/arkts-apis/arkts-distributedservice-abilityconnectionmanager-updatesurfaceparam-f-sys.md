# updateSurfaceParam（系统接口）

## 导入模块

```TypeScript
import { abilityConnectionManager } from 'kits/@kit.DistributedServiceKit';
```

## updateSurfaceParam

```TypeScript
function updateSurfaceParam(streamId: number, param: SurfaceParam): void
```

更新与传输流绑定的Surface的配置信息，使新的配置参数生效。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| streamId | number | 是 |
| param | [SurfaceParam](arkts-distributedservice-abilityconnectionmanager-surfaceparam-i-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
