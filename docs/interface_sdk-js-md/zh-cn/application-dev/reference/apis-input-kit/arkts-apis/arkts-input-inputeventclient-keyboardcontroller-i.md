# KeyboardController

提供模拟按键操作的功能。模拟按键操作序列必须满足以下要求：
1. 按键只能在抬起状态下被按下，或者在该按键是最近按下的按键且未抬起的情况下被按下。
2. 按键只能在被按下后才能抬起。
3. 最多可以同时按下并保持五个按键。

**起始版本：** 26.0.0

**系统能力：** SystemCapability.MultimodalInput.Input.InputSimulator

## 导入模块

```TypeScript
import { inputEventClient } from 'kits/@kit.InputKit';
```

## pressKey

```TypeScript
pressKey(keyCode: KeyCode): Promise<void>
```

按下按键。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.CONTROL_DEVICE

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.MultimodalInput.Input.InputSimulator

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyCode | [KeyCode](arkts-input-multimodalinput-keycode-keycode-e.md) | 是 |

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

## releaseKey

```TypeScript
releaseKey(keyCode: KeyCode): Promise<void>
```

抬起按键。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.CONTROL_DEVICE

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.MultimodalInput.Input.InputSimulator

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| keyCode | [KeyCode](arkts-input-multimodalinput-keycode-keycode-e.md) | 是 |

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
