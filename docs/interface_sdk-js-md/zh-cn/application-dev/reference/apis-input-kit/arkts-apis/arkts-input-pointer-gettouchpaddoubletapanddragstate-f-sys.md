# getTouchpadDoubleTapAndDragState（系统接口）

## 导入模块

```TypeScript
import { pointer } from 'kits/@kit.InputKit';
```

## getTouchpadDoubleTapAndDragState

```TypeScript
function getTouchpadDoubleTapAndDragState(callback: AsyncCallback<boolean>): void
```

获取触控板双击拖拽开关的开启状态，使用callback异步回调。

**起始版本：** 14

**系统能力：** SystemCapability.MultimodalInput.Input.Pointer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## getTouchpadDoubleTapAndDragState

```TypeScript
function getTouchpadDoubleTapAndDragState(): Promise<boolean>
```

获取触控板双击拖拽开关的开启状态，使用Promise异步回调。

**起始版本：** 14

**系统能力：** SystemCapability.MultimodalInput.Input.Pointer

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
