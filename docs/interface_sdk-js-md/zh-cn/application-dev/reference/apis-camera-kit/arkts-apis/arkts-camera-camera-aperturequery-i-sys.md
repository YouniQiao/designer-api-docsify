# ApertureQuery

物理光圈查询对象。

**起始版本：** 24

**系统能力：** SystemCapability.Multimedia.Camera.Core

## 导入模块

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## getSupportedVirtualApertures

```TypeScript
getSupportedVirtualApertures(): Array<number>
```

获取支持的虚拟光圈列表。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Array & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
