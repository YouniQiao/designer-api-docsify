# onCooperateMouseEvent（系统接口）

## 导入模块

```TypeScript
import { cooperate } from 'kits/@kit.DistributedServiceKit';
```

## onCooperateMouseEvent

```TypeScript
function onCooperateMouseEvent(networkId: string, callback: Callback<MouseLocation>): void
```

Enables listening for mouse pointer position information on the specified device for cooperation.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.COOPERATE_MANAGER

<!--Device-cooperate-function onCooperateMouseEvent(networkId: string, callback: Callback<MouseLocation>): void--><!--Device-cooperate-function onCooperateMouseEvent(networkId: string, callback: Callback<MouseLocation>): void-End-->

**系统能力：** SystemCapability.Msdp.DeviceStatus.Cooperate

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| networkId | string | 是 | Specified device. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;MouseLocation&gt; | 是 | Callback for receiving reported events. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. &lt;br&gt;3. Parameter verification failed. |
| 201 | Permission denied. |
| 202 | Permission verification failed. A non-system application calls a system API. |

