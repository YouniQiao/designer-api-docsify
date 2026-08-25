# create

## 导入模块

```TypeScript
import { floatingBall } from 'kits/@kit.ArkUI';
```

## create

```TypeScript
function create(config: FloatingBallConfiguration): Promise<FloatingBallController>
```

创建闪控球控制器，使用Promise异步回调。

**起始版本：** 20

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [FloatingBallConfiguration](arkts-arkui-floatingball-floatingballconfiguration-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[FloatingBallController](arkts-arkui-floatingball-floatingballcontroller-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300019](../errorcode-window.md#1300019-闪控球参数校验错误) |
| [1300023](../errorcode-window.md#1300023-闪控球内部错误) |
