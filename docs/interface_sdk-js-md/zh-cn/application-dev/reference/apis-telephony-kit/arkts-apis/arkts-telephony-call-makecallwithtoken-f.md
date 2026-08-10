# makeCallWithToken

## 导入模块

```TypeScript
import { call } from 'kits/@kit.TelephonyKit';
```

## makeCallWithToken

```TypeScript
function makeCallWithToken(phoneNumber: string, options?: MakeCallOptions): Promise<string>
```

Go to the dial screen and the called number is displayed.The authentication challenge value is returned.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-call-function makeCallWithToken(phoneNumber: string, options?: MakeCallOptions): Promise<string>--><!--Device-call-function makeCallWithToken(phoneNumber: string, options?: MakeCallOptions): Promise<string>-End-->

**系统能力：** SystemCapability.Applications.Contacts

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| phoneNumber | string | 是 | Indicates the called number. |
| options | [MakeCallOptions](arkts-telephony-call-makecalloptions-i.md) | 否 | Indicates additional information carried in the call. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise used to return access token by the makeCall. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 8300999 | Unknown error code. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## 示例

```TypeScript
import { call } from '@kit.TelephonyKit';

// 设置通话结束后是否返回当前App与应用是否开启自定义无障碍功能
let makeOptions: call.MakeCallOptions = {
  isHideDialScreen: true,
  isCustomAccessibility : true
}

call.makeCallWithToken("138xxxxxxxx", makeOptions).then(() => {
    console.info(`makeCallWithToken success`);
}).catch((err: BusinessError) => {
    console.error(`makeCallWithToken fail, promise: err->${JSON.stringify(err)}`);
});
```

