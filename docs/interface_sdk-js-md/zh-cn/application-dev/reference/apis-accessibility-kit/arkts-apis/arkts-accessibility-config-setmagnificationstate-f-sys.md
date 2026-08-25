# setMagnificationState（系统接口）

## 导入模块

```TypeScript
import { config } from 'kits/@kit.AccessibilityKit';
```

## setMagnificationState

```TypeScript
function setMagnificationState(state: boolean): void
```

设置放大效果的启用状态。放大效果依赖放大手势功能，仅在放大手势功能已启用的前提下，本接口的设置才会生效。

**起始版本：** 20

**需要权限：** ohos.permission.WRITE_ACCESSIBILITY_CONFIG

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| state | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [9300007](../errorcode-accessibility.md#9300007-触发放大功能失败) |
