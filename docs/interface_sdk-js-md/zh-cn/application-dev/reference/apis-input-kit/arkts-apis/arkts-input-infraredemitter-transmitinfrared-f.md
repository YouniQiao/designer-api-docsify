# transmitInfrared

## 导入模块

```TypeScript
import { infraredEmitter } from 'kits/@kit.InputKit';
```

## transmitInfrared

```TypeScript
function transmitInfrared(infraredFrequency: number, pattern: Array<number>): void
```

产生特定频率和特定电平大小的红外信号。

**起始版本：** 15

**需要权限：** ohos.permission.MANAGE_INPUT_INFRARED_EMITTER

**系统能力：** SystemCapability.MultimodalInput.Input.InfraredEmitter

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| infraredFrequency | number | 是 |
| [pattern](../../apis-sensor-service-kit/arkts-apis/arkts-sensorservice-vibrator-vibratefrompattern-i.md) | Array & lt;number & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
