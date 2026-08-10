# on（系统接口）

## 导入模块

```TypeScript
import { radio } from 'kits/@kit.TelephonyKit';
```

## on('imsRegStateChange')

```TypeScript
function on(type: 'imsRegStateChange', slotId: int, imsType: ImsServiceType, callback: Callback<ImsRegInfo>): void
```

Called when the IMS registration state of specified IMS service type corresponding to a monitored {@code slotId} updates.

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**需要权限：** ohos.permission.GET_TELEPHONY_STATE

<!--Device-radio-function on(type: 'imsRegStateChange', slotId: int, imsType: ImsServiceType, callback: Callback<ImsRegInfo>): void--><!--Device-radio-function on(type: 'imsRegStateChange', slotId: int, imsType: ImsServiceType, callback: Callback<ImsRegInfo>): void-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'imsRegStateChange' | 是 | Event type. Indicates the imsRegStateChange event to be subscribed to. |
| slotId | int | 是 | Indicates the card slot index number, ranging from 0 to the maximum card slot index number supported by the device. |
| imsType | [ImsServiceType](arkts-telephony-radio-imsservicetype-e-sys.md) | 是 | Indicates the ims service type of the {@link ImsServiceType}. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ImsRegInfo&gt; | 是 | Indicates the callback for getting an instance of the {@link ImsRegInfo} class. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |
| 201 | Permission denied. |
| 8300999 | Unknown error. |
| 202 | Non-system applications use system APIs. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## 示例

```TypeScript
let slotId: number = 0;
let mode: radio.ImsServiceType = radio.ImsServiceType.TYPE_VIDEO;
radio.on('imsRegStateChange', slotId, mode, (data: radio.ImsRegInfo) => {
    console.info(`on imsRegStateChange success, callback: data->${JSON.stringify(data)}`);
});
```

