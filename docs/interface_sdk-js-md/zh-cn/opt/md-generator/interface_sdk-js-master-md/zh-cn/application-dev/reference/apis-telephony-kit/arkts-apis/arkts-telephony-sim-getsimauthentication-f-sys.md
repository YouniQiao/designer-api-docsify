# getSimAuthentication（系统接口）

## getSimAuthentication

```TypeScript
function getSimAuthentication(slotId: number, authType: AuthType, authData: string): Promise<SimAuthenticationResponse>
```

Performs SIM card authentication.

**起始版本：** 14

**需要权限：** ohos.permission.GET_TELEPHONY_STATE

<!--Device-sim-function getSimAuthentication(slotId: int, authType: AuthType, authData: string): Promise<SimAuthenticationResponse>--><!--Device-sim-function getSimAuthentication(slotId: int, authType: AuthType, authData: string): Promise<SimAuthenticationResponse>-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |
| authType | [AuthType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-authtype-e-sys.md) | 是 |
| authData | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;SimAuthenticationResponse&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [8301002](../errorcode-telephony.md#8301002-sim卡读取数据或者更新数据失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [8300004](../errorcode-telephony.md#8300004-未识别sim卡) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getSimAuthentication(0, sim.AuthType.SIM_AUTH_EAP_SIM_TYPE, "test").then(() => {
    console.info(`getSimAuthentication success.`);
}).catch((err: BusinessError) => {
    console.error(`getSimAuthentication failed, promise: err->${JSON.stringify(err)}`);
});
```
