# setSimLabelIndex（系统接口）

## setSimLabelIndex

```TypeScript
function setSimLabelIndex(simId: number, simLabelIndex: number): Promise<void>
```

设置SIM卡标签索引。

**起始版本：** 23

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-sim-function setSimLabelIndex(simId: int, simLabelIndex: int): Promise<void>--><!--Device-sim-function setSimLabelIndex(simId: int, simLabelIndex: int): Promise<void>-End-->

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [simId](arkts-telephony-sim-iccaccountinfo-i.md) | number | 是 |
| [simLabelIndex](arkts-telephony-sim-iccaccountinfo-i-sys.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-内部错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-输入参数不在处理范围内) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.setSimLabelIndex(1,  0).then(() => {
    console.info(`setSimLabelIndex success.`);
}).catch((err: BusinessError) => {
    console.error(`setSimLabelIndex failed, promise: err->${JSON.stringify(err)}`);
});
```
