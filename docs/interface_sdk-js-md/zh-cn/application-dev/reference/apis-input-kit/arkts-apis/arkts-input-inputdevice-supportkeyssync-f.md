# supportKeysSync

## 导入模块

```TypeScript
import { inputDevice } from 'kits/@kit.InputKit';
```

## supportKeysSync

```TypeScript
function supportKeysSync(deviceId: number, keys: Array<KeyCode>): Array<boolean>
```

查询指定id的输入设备对指定键值的支持情况。

**起始版本：** 10

**系统能力：** SystemCapability.MultimodalInput.Input.InputDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | number | 是 |
| keys | Array&lt;[KeyCode](arkts-input-multimodalinput-keycode-keycode-e.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
