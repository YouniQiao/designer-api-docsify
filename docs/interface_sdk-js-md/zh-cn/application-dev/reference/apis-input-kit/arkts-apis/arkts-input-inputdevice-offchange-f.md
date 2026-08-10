# offChange

## 导入模块

```TypeScript
import { inputDevice } from 'kits/@kit.InputKit';
```

## offChange

```TypeScript
function offChange(listener?: Callback<DeviceListener>): void
```

Stops listening for an input device event.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-inputDevice-function offChange(listener?: Callback<DeviceListener>): void--><!--Device-inputDevice-function offChange(listener?: Callback<DeviceListener>): void-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.InputDevice

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| listener | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DeviceListener&gt; | 否 | Callback for the input device event. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

