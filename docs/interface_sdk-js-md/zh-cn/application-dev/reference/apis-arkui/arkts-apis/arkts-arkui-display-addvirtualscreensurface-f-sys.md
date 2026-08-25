# addVirtualScreenSurface（系统接口）

## 导入模块

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## addVirtualScreenSurface

```TypeScript
function addVirtualScreenSurface(screenId: number, surfaceId: string, surfaceRegion?: Rect): Promise<void>
```

为虚拟屏幕添加surface。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| screenId | number | 是 |
| surfaceId | string | 是 |
| surfaceRegion | [Rect](../../apis-form-kit/arkts-apis/arkts-form-forminfo-rect-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1400001](../errorcode-display.md#1400001-无效的显示设备) |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |
| [1400004](../errorcode-display.md#1400004-参数异常) |
