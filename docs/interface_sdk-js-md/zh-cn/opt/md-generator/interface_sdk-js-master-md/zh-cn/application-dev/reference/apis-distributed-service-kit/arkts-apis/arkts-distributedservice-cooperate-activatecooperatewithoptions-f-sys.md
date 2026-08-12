# activateCooperateWithOptions（系统接口）

## activateCooperateWithOptions

```TypeScript
function activateCooperateWithOptions(targetNetworkId: string, inputDeviceId: number,
    cooperateOptions?: CooperateOptions
  ): Promise<void>
```

启动键鼠穿越，使用选项开始屏幕跳转。

**起始版本：** 20

**需要权限：** ohos.permission.COOPERATE_MANAGER

<!--Device-cooperate-function activateCooperateWithOptions(targetNetworkId: string, inputDeviceId: int,    cooperateOptions?: CooperateOptions  ): Promise<void>--><!--Device-cooperate-function activateCooperateWithOptions(targetNetworkId: string, inputDeviceId: int,    cooperateOptions?: CooperateOptions  ): Promise<void>-End-->

**系统能力：** SystemCapability.Msdp.DeviceStatus.Cooperate

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| targetNetworkId | string | 是 |
| inputDeviceId | number | 是 |
| cooperateOptions | [CooperateOptions](arkts-distributedservice-cooperate-cooperateoptions-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [20900001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-distributedservice-kit/errorcode-devicestatus.md#20900001-操作输入设备失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let targetNetworkId = "networkId";
let inputDeviceId = 0;
try {
  cooperate.activateCooperateWithOptions(targetNetworkId, inputDeviceId).then(() => {
    console.info(`activateCooperateWithOptions success.`);
  }, (error: BusinessError) => {
    console.error(`activateCooperateWithOptions, error: ${JSON.stringify(error, [`code`, `message`])}`);
  });
} catch (error) {
  console.error(`activateCooperateWithOptions, error: ${JSON.stringify(error, [`code`, `message`])}`);
}
```
