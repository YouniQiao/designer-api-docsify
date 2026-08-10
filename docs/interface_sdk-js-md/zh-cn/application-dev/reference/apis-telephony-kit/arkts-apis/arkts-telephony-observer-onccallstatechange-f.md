# onCCallStateChange

## 导入模块

```TypeScript
import { observer } from 'kits/@kit.TelephonyKit';
```

## onCCallStateChange

```TypeScript
function onCCallStateChange(callback: Callback<CCallStateInfo>, options?: ObserverOptions): void
```

Called when the carrier call state changes.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.MANAGE_CALL_FOR_DEVICES

<!--Device-observer-function onCCallStateChange(callback: Callback<CCallStateInfo>, options?: ObserverOptions): void--><!--Device-observer-function onCCallStateChange(callback: Callback<CCallStateInfo>, options?: ObserverOptions): void-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;CCallStateInfo&gt; | 是 | Indicates the callback for getting the carrier call state. |
| options | [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) | 否 | Indicates the options for observer. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 8800999 | Unknown error. |
| 8800002 | Service connection failed. |
| 8800003 | System internal error. |
| 8800001 | Invalid parameter value. |
| 201 | Permission denied. |

## 示例

```TypeScript
import { call, observer } from '@kit.TelephonyKit';

let callback: (data: observer.CCallStateInfo) => void = (data: observer.CCallStateInfo) => {
    console.info("onCCallStateChange, data:" + JSON.stringify(data));
}
let options: observer.ObserverOptions = {
    slotId: 0
}

observer.onCCallStateChange(callback, options);
observer.onCCallStateChange(callback);
```

