# isManualNetworkScanning（系统接口）

## 导入模块

```TypeScript
import { radio } from '@kit.TelephonyKit';
```

## isManualNetworkScanning

```TypeScript
function isManualNetworkScanning(slotId: int): Promise<boolean>
```

确定当前手动网络扫描是否正在进行

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.GET_TELEPHONY_STATE

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

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
radio.isManualNetworkScanning(0).then((state: boolean) => {
    console.info(`isManualNetworkScanning success, state->${JSON.stringify(state)}`);
}).catch((err: BusinessError) => {
    console.error(`isManualNetworkScanning failed, promise: err->${JSON.stringify(err)}`);
});
```
