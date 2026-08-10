# onSwipeInward（系统接口）

## 导入模块

```TypeScript
import { inputMonitor } from 'kits/@kit.InputKit';
```

## onSwipeInward

```TypeScript
function onSwipeInward(receiver: Callback<SwipeInward>): void
```

监听向内滑动事件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function onSwipeInward(receiver: Callback<SwipeInward>): void--><!--Device-inputMonitor-function onSwipeInward(receiver: Callback<SwipeInward>): void-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.InputMonitor

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| receiver | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SwipeInward](arkts-input-multimodalinput-gestureevent-swipeinward-i-sys.md)&gt; | 是 | 用于接收上报数据的回调函数。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 201 | Permission denied. |
| 202 | SystemAPI permit error. |

