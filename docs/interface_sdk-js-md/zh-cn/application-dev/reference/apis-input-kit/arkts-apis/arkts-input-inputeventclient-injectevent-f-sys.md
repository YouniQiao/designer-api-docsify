# injectEvent（系统接口）

## 导入模块

```TypeScript
import { inputEventClient } from 'kits/@kit.InputKit';
```

## injectEvent

```TypeScript
function injectEvent({ KeyEvent: KeyEvent }): void
```

按键(包括单个按键和组合键)注入。

**起始版本：** 8

**需要权限：** 
- API版本12+：ohos.permission.INJECT_INPUT_EVENT

**系统能力：** SystemCapability.MultimodalInput.Input.InputSimulator

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| { KeyEvent: KeyEvent } | 0.0 | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
