# setPointerStyleSync

## 导入模块

```TypeScript
import { pointer } from 'kits/@kit.InputKit';
```

## setPointerStyleSync

```TypeScript
function setPointerStyleSync(windowId: number, pointerStyle: PointerStyle): void
```

设置指定窗口的鼠标样式类型，使用同步方式返回结果。此接口仅支持设置本应用进程内窗口的鼠标样式类型，如需通过UIExtensionAbility进程设置宿主窗口的鼠标样式类型，请参阅 [setCursor](../../../reference/apis-arkui/arkts-apis-uicontext-cursorcontroller.md#setcursor12)。

**起始版本：** 10

**系统能力：** SystemCapability.MultimodalInput.Input.Pointer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| windowId | number | 是 |
| pointerStyle | [PointerStyle](../../apis-arkui/arkts-apis/arkts-arkui-pointerstyle-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
