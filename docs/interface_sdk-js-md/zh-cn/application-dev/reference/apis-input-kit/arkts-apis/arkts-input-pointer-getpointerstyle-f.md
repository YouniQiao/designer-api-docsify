# getPointerStyle

## 导入模块

```TypeScript
import { pointer } from 'kits/@kit.InputKit';
```

## getPointerStyle

```TypeScript
function getPointerStyle(windowId: number, callback: AsyncCallback<PointerStyle>): void
```

获取指定窗口的鼠标样式类型，此接口仅支持获取本应用进程内窗口的鼠标样式类型，使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.MultimodalInput.Input.Pointer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| windowId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;PointerStyle&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## getPointerStyle

```TypeScript
function getPointerStyle(windowId: number): Promise<PointerStyle>
```

获取鼠标样式类型，此接口仅支持获取本应用进程内窗口的鼠标样式类型，使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.MultimodalInput.Input.Pointer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| windowId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;PointerStyle & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
