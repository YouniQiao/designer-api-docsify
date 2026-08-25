# getKioskStatus（系统接口）

## 导入模块

```TypeScript
import { kioskManager } from 'kits/@kit.AbilityKit';
```

## getKioskStatus

```TypeScript
function getKioskStatus(): Promise<KioskStatus>
```

获取系统Kiosk模式的状态信息（包括当前系统是否处于Kiosk模式、进入Kiosk模式应用的名称和UID）。使用Promise异步回调。 该接口仅在Phone、PC/2in1和Tablet设备中可正常调用，在其他设备中返回801错误码。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;KioskStatus & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
