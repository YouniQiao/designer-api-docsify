# setCallTransfer（系统接口）

## setCallTransfer

```TypeScript
function setCallTransfer(slotId: number, info: CallTransferInfo, callback: AsyncCallback<void>): void
```

设置呼叫转移信息。使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function setCallTransfer(slotId: int, info: CallTransferInfo, callback: AsyncCallback<void>): void--><!--Device-call-function setCallTransfer(slotId: int, info: CallTransferInfo, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |
| info | [CallTransferInfo](arkts-telephony-call-calltransferinfo-i-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let callTransferInfo: call.CallTransferInfo = {
    transferNum: "111",
    type: call.CallTransferType.TRANSFER_TYPE_BUSY,
    settingType: call.CallTransferSettingType.CALL_TRANSFER_ENABLE
}
call.setCallTransfer(0, callTransferInfo, (err: BusinessError) => {
    if (err) {
        console.error(`setCallTransfer fail, err->${JSON.stringify(err)}`);
    } else {
        console.info(`setCallTransfer success.`);
    }
});
```


## setCallTransfer

```TypeScript
function setCallTransfer(slotId: number, info: CallTransferInfo): Promise<void>
```

设置呼叫转移信息。使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function setCallTransfer(slotId: int, info: CallTransferInfo): Promise<void>--><!--Device-call-function setCallTransfer(slotId: int, info: CallTransferInfo): Promise<void>-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |
| info | [CallTransferInfo](arkts-telephony-call-calltransferinfo-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let callTransferInfo: call.CallTransferInfo = {
    transferNum: "111",
    type: call.CallTransferType.TRANSFER_TYPE_BUSY,
    settingType: call.CallTransferSettingType.CALL_TRANSFER_ENABLE
}
call.setCallTransfer(0, callTransferInfo).then(() => {
    console.info(`setCallTransfer success.`);
}).catch((err: BusinessError) => {
    console.error(`setCallTransfer fail, promise: err->${JSON.stringify(err)}`);
});
```
