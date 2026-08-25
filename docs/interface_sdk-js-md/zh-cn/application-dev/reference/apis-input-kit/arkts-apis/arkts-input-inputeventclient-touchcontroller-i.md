# TouchController

提供模拟触控操作的功能。模拟触控操作序列必须满足以下要求：
1. 所有触点的displayId必须相同。
2. 每个触点都必须以`touchDown()`开始，以`touchUp()`结束，中间可包含多个`touchMove()`。

**起始版本：** 26.0.0

**系统能力：** SystemCapability.MultimodalInput.Input.InputSimulator

## 导入模块

```TypeScript
import { inputEventClient } from 'kits/@kit.InputKit';
```

## touchDown

```TypeScript
touchDown(touch: TouchPoint): Promise<void>
```

触点按下。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.CONTROL_DEVICE

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.MultimodalInput.Input.InputSimulator

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| touch | [TouchPoint](../../apis-arkui/arkts-apis/arkts-arkui-touchpoint-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [4300001](../errorcode-inputeventclient.md#4300001-状态错误) |
| [4300002](../errorcode-inputeventclient.md#4300002-显示器不存在) |
| [3800001](../errorcode-infraredemitter.md#3800001-多模输入服务内部错误) |

## touchMove

```TypeScript
touchMove(touch: TouchPoint): Promise<void>
```

触点移动。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.CONTROL_DEVICE

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.MultimodalInput.Input.InputSimulator

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| touch | [TouchPoint](../../apis-arkui/arkts-apis/arkts-arkui-touchpoint-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [4300001](../errorcode-inputeventclient.md#4300001-状态错误) |
| [3800001](../errorcode-infraredemitter.md#3800001-多模输入服务内部错误) |

## touchUp

```TypeScript
touchUp(touch: TouchPoint): Promise<void>
```

触点抬起。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.CONTROL_DEVICE

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.MultimodalInput.Input.InputSimulator

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| touch | [TouchPoint](../../apis-arkui/arkts-apis/arkts-arkui-touchpoint-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [4300001](../errorcode-inputeventclient.md#4300001-状态错误) |
| [3800001](../errorcode-infraredemitter.md#3800001-多模输入服务内部错误) |
