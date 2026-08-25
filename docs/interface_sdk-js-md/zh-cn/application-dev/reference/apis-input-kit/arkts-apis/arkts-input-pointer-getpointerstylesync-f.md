# getPointerStyleSync

## 导入模块

```TypeScript
import { pointer } from 'kits/@kit.InputKit';
```

## getPointerStyleSync

```TypeScript
function getPointerStyleSync(windowId: number): PointerStyle
```

查询指定窗口的鼠标样式类型，如向东箭头、向西箭头、向南箭头、向北箭头等。此接口仅支持获取本应用进程内窗口的鼠标样式类型。

**起始版本：** 10

**系统能力：** SystemCapability.MultimodalInput.Input.Pointer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| windowId | number | 是 |

**返回值：**

| 类型 |
| --- |
| [PointerStyle](../../apis-arkui/arkts-apis/arkts-arkui-pointerstyle-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
