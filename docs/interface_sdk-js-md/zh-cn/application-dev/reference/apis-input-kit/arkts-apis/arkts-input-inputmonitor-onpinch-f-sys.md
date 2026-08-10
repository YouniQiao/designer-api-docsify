# onPinch（系统接口）

## 导入模块

```TypeScript
import { inputMonitor } from 'kits/@kit.InputKit';
```

## onPinch

```TypeScript
function onPinch(receiver: Callback<Pinch>): void
```

监听全局触控板的捏合事件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function onPinch(receiver: Callback<Pinch>): void--><!--Device-inputMonitor-function onPinch(receiver: Callback<Pinch>): void-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.InputMonitor

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| receiver | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[Pinch](arkts-input-multimodalinput-gestureevent-pinch-i.md)&gt; | 是 | 回调函数，异步上报捏合输入事件。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 202 | SystemAPI permit error. |


## onPinch

```TypeScript
function onPinch(fingers: int, receiver: Callback<Pinch>): void
```

监听全局触控板的捏合事件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function onPinch(fingers: int, receiver: Callback<Pinch>): void--><!--Device-inputMonitor-function onPinch(fingers: int, receiver: Callback<Pinch>): void-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.InputMonitor

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fingers | int | 是 | 捏合的手指数，手指数不能小于0，当前仅支持收到捏合手势的回调。 |
| receiver | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[Pinch](arkts-input-multimodalinput-gestureevent-pinch-i.md)&gt; | 是 | 回调函数，异步上报捏合输入事件。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission denied. |
| 202 | SystemAPI permit error. |

