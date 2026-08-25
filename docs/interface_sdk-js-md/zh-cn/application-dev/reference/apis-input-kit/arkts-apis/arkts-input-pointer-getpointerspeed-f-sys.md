# getPointerSpeed（系统接口）

## 导入模块

```TypeScript
import { pointer } from 'kits/@kit.InputKit';
```

## getPointerSpeed

```TypeScript
function getPointerSpeed(callback: AsyncCallback<number>): void
```

获取鼠标移动速度，使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.MultimodalInput.Input.Pointer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |


## getPointerSpeed

```TypeScript
function getPointerSpeed(): Promise<number>
```

获取当前鼠标移动速度，使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.MultimodalInput.Input.Pointer

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
