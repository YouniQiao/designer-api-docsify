# hasIrEmitter

## 导入模块

```TypeScript
import { infraredEmitter } from 'kits/@kit.InputKit';
```

## hasIrEmitter

```TypeScript
function hasIrEmitter(): Promise<boolean>
```

查询设备是否配备红外发射器。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.MANAGE_INPUT_INFRARED_EMITTER

**系统能力：** SystemCapability.MultimodalInput.Input.InfraredEmitter

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [3800001](../errorcode-infraredemitter.md#3800001-多模输入服务内部错误) |
