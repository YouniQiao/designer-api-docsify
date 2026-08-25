# resetMemory（系统接口）

## 导入模块

```TypeScript
import { eSIM } from 'kits/@kit.TelephonyKit';
```

## resetMemory

```TypeScript
function resetMemory(slotId: number, options?:ResetOption): Promise<ResultCode>
```

清除所有特定配置文件并重置eUICC。使用Promise异步回调。

**起始版本：** 18

**需要权限：** ohos.permission.SET_TELEPHONY_ESIM_STATE

**系统能力：** SystemCapability.Telephony.CoreService.Esim

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |
| options | [ResetOption](arkts-telephony-esim-resetoption-e-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;ResultCode & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3120001](../errorcode-telephony.md#3120001-服务连接失败) |
| [3120002](../errorcode-telephony.md#3120002-系统内部错误) |
