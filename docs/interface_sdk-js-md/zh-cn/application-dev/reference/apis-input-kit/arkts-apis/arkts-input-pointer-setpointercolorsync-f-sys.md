# setPointerColorSync（系统接口）

## 导入模块

```TypeScript
import { pointer } from 'kits/@kit.InputKit';
```

## setPointerColorSync

```TypeScript
function setPointerColorSync(color: number): void
```

设置鼠标光标颜色，使用同步方式进行设置。

> **说明：**&gt;
> 设置和调试时，需连接外部设备，如鼠标、蓝牙等。

**起始版本：** 10

**系统能力：** SystemCapability.MultimodalInput.Input.Pointer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
