# getAllSystemHotkeys

## 导入模块

```TypeScript
import { inputConsumer } from 'kits/@kit.InputKit';
```

## getAllSystemHotkeys

```TypeScript
function getAllSystemHotkeys(): Promise<Array<HotkeyOptions>>
```

获取所有系统快捷键，使用Promise异步回调。

**起始版本：** 14

**系统能力：** SystemCapability.MultimodalInput.Input.InputConsumer

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[HotkeyOptions](arkts-input-inputconsumer-hotkeyoptions-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
