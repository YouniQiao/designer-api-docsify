# stopManualNetworkScan（系统接口）

## 导入模块

```TypeScript
import { radio } from '@kit.TelephonyKit';
```

## stopManualNetworkScan

```TypeScript
function stopManualNetworkScan(slotId: int): Promise<void>
```

停止手动搜网

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |

**示例**

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
