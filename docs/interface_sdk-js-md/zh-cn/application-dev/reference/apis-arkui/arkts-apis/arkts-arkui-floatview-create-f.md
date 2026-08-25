# create

## 导入模块

```TypeScript
import { floatView } from 'kits/@kit.ArkUI';
```

## create

```TypeScript
function create(config: FloatViewConfiguration): Promise<FloatViewController>
```

创建标准悬浮窗控制器。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [FloatViewConfiguration](arkts-arkui-floatview-floatviewconfiguration-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[FloatViewController](arkts-arkui-floatview-floatviewcontroller-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300016](../errorcode-window.md#1300016-参数校验错误) |
