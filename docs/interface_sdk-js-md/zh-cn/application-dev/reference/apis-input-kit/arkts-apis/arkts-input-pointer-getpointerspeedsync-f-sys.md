# getPointerSpeedSync（系统接口）

## 导入模块

```TypeScript
import { pointer } from 'kits/@kit.InputKit';
```

## getPointerSpeedSync

```TypeScript
function getPointerSpeedSync(): number
```

使用同步方式获取当前鼠标移动速度。

**起始版本：** 10

**系统能力：** SystemCapability.MultimodalInput.Input.Pointer

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
