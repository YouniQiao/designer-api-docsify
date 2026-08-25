# MouseController

提供模拟鼠标操作的功能。模拟鼠标操作序列必须满足以下要求：
1. 鼠标按键只能在抬起状态下被按下。
2. 鼠标按键只能在被按下后才能抬起。
3. 有效的轴事件序列必须先调用beginAxis开始事件，然后调用零次或多次updateAxis更新事件，最后调用endAxis结束事件。

4. 同一时间只能有一个进行中的轴事件序列。

**起始版本：** 26.0.0

**系统能力：** SystemCapability.MultimodalInput.Input.InputSimulator

## 导入模块

```TypeScript
import { inputEventClient } from 'kits/@kit.InputKit';
```

## beginAxis

```TypeScript
beginAxis(axis: Axis, value: number): Promise<void>
```

开始轴事件。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.CONTROL_DEVICE

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.MultimodalInput.Input.InputSimulator

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| axis | [Axis](arkts-input-multimodalinput-mouseevent-axis-e.md) | 是 |
| value | number | 是 |

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

## endAxis

```TypeScript
endAxis(axis: Axis): Promise<void>
```

结束轴事件。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.CONTROL_DEVICE

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.MultimodalInput.Input.InputSimulator

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| axis | [Axis](arkts-input-multimodalinput-mouseevent-axis-e.md) | 是 |

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

## moveTo

```TypeScript
moveTo(displayId: number, displayX: number, displayY: number): Promise<void>
```

将鼠标光标移动到指定的显示器坐标。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.CONTROL_DEVICE

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.MultimodalInput.Input.InputSimulator

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| displayId | number | 是 |
| displayX | number | 是 |
| displayY | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [4300002](../errorcode-inputeventclient.md#4300002-显示器不存在) |
| [3800001](../errorcode-infraredemitter.md#3800001-多模输入服务内部错误) |

## pressButton

```TypeScript
pressButton(button: Button): Promise<void>
```

按下鼠标按键。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.CONTROL_DEVICE

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.MultimodalInput.Input.InputSimulator

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| button | [Button](arkts-input-multimodalinput-mouseevent-button-e.md) | 是 |

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

## releaseButton

```TypeScript
releaseButton(button: Button): Promise<void>
```

抬起鼠标按键。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.CONTROL_DEVICE

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.MultimodalInput.Input.InputSimulator

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| button | [Button](arkts-input-multimodalinput-mouseevent-button-e.md) | 是 |

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

## updateAxis

```TypeScript
updateAxis(axis: Axis, value: number): Promise<void>
```

更新轴事件。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.CONTROL_DEVICE

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.MultimodalInput.Input.InputSimulator

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| axis | [Axis](arkts-input-multimodalinput-mouseevent-axis-e.md) | 是 |
| value | number | 是 |

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
