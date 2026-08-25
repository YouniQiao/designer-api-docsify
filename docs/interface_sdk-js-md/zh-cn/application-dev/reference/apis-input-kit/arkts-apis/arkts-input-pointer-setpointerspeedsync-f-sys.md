# setPointerSpeedSync（系统接口）

## 导入模块

```TypeScript
import { pointer } from 'kits/@kit.InputKit';
```

## setPointerSpeedSync

```TypeScript
function setPointerSpeedSync(speed: number): void
```

使用同步方式设置鼠标移动速度。

**起始版本：** 10

**系统能力：** SystemCapability.MultimodalInput.Input.Pointer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| speed | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
