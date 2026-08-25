# getInfraredFrequencies

## 导入模块

```TypeScript
import { infraredEmitter } from 'kits/@kit.InputKit';
```

## getInfraredFrequencies

```TypeScript
function getInfraredFrequencies(): Array<InfraredFrequency>
```

查询设备支持的红外信号的频率范围。建议先使用[hasIrEmitter]接口查询设备是否支持红外发射器。

**起始版本：** 15

**需要权限：** ohos.permission.MANAGE_INPUT_INFRARED_EMITTER

**系统能力：** SystemCapability.MultimodalInput.Input.InfraredEmitter

**返回值：**

| 类型 |
| --- |
| Array&lt;[InfraredFrequency](arkts-input-infraredemitter-infraredfrequency-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
