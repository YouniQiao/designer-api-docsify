# stopManualNetworkScan（系统接口）

## 导入模块

```TypeScript
import { radio } from 'kits/@kit.TelephonyKit';
```

## stopManualNetworkScan

```TypeScript
function stopManualNetworkScan(slotId: int): Promise<void>
```

Stop ManualNetworkScan.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-radio-function stopManualNetworkScan(slotId: int): Promise<void>--><!--Device-radio-function stopManualNetworkScan(slotId: int): Promise<void>-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Indicates the card slot index number. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | the promise return stopManualNetworkScan. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 8300999 | Unknown error. |
| 202 | Nonsystem applications use system APIs. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## 示例

```TypeScript
radio.startManualNetworkScan(0, (err: BusinessError, data: radio.NetworkSearchRealTimeResult) => {
    if (err) {
        console.error(`startManualNetworkScan failed, callback: err->${JSON.stringify(err)}`);
        return;
    }
    console.info(`startManualNetworkScan success, callback: data->${JSON.stringify(data)}`);
    radio.stopManualNetworkScan(0);
});
```

