# isPointerVisible

## 导入模块

```TypeScript
import { pointer } from 'kits/@kit.InputKit';
```

## isPointerVisible

```TypeScript
function isPointerVisible(callback: AsyncCallback<boolean>): void
```

获取鼠标光标显示状态，使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.MultimodalInput.Input.Pointer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## isPointerVisible

```TypeScript
function isPointerVisible(): Promise<boolean>
```

获取鼠标光标显示状态，使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.MultimodalInput.Input.Pointer

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |
