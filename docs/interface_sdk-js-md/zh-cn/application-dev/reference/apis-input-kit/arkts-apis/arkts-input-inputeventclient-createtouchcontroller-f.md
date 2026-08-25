# createTouchController

## 导入模块

```TypeScript
import { inputEventClient } from 'kits/@kit.InputKit';
```

## createTouchController

```TypeScript
function createTouchController(): Promise<TouchController>
```

创建触控控制器，用于模拟触控操作。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.CONTROL_DEVICE

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.MultimodalInput.Input.InputSimulator

**返回值：**

| 类型 |
| --- |
| Promise&lt;[TouchController](arkts-input-inputeventclient-touchcontroller-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3800001](../errorcode-infraredemitter.md#3800001-多模输入服务内部错误) |
