# getMouseScrollDirection（系统接口）

## 导入模块

```TypeScript
import { pointer } from 'kits/@kit.InputKit';
```

## getMouseScrollDirection

```TypeScript
function getMouseScrollDirection(): Promise<boolean>
```

获取鼠标滚轮滚动方向，使用Promise异步回调。

**起始版本：** 24

**需要权限：** ohos.permission.INPUT_DEVICE_CONTROLLER

**系统能力：** SystemCapability.MultimodalInput.Input.Pointer

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [3800001](../errorcode-infraredemitter.md#3800001-多模输入服务内部错误) |
