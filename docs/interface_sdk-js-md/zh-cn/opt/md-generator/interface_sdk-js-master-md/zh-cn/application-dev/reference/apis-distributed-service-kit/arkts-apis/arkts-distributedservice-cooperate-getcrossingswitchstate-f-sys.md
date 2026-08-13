# getCrossingSwitchState（系统接口）

## getCrossingSwitchState

```TypeScript
function getCrossingSwitchState(networkId: string, callback: AsyncCallback<boolean>): void
```

获取目标设备键鼠穿越开关的状态，使用Callback异步回调。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [getCooperateSwitchState](arkts-distributedservice-cooperate-getcooperateswitchstate-f-sys.md#getCooperateSwitchState（系统接口）)(networkId: string, callback: AsyncCallback&lt;boolean&gt;)

<!--Device-cooperate-function getCrossingSwitchState(networkId: string, callback: AsyncCallback<boolean>): void--><!--Device-cooperate-function getCrossingSwitchState(networkId: string, callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.Msdp.DeviceStatus.Cooperate

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| networkId | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let deviceDescriptor = "networkId";
try {
  cooperate.getCrossingSwitchState(deviceDescriptor, (error: BusinessError, data: boolean) => {
    if (error) {
      console.error(`Get the status failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
      return;
    }
    console.info(`Get the status success, data: ${JSON.stringify(data)}`);
  });
} catch (error) {
  console.error(`Get the status failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
}
```


## getCrossingSwitchState

```TypeScript
function getCrossingSwitchState(networkId: string): Promise<boolean>
```

获取目标设备键鼠穿越开关的状态，使用Promise异步方式返回结果。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [getCooperateSwitchState](arkts-distributedservice-cooperate-getcooperateswitchstate-f-sys.md#getCooperateSwitchState（系统接口）)(networkId: string)

<!--Device-cooperate-function getCrossingSwitchState(networkId: string): Promise<boolean>--><!--Device-cooperate-function getCrossingSwitchState(networkId: string): Promise<boolean>-End-->

**系统能力：** SystemCapability.Msdp.DeviceStatus.Cooperate

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| networkId | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let deviceDescriptor = "networkId";
try {
  cooperate.getCrossingSwitchState(deviceDescriptor).then((data: boolean) => {
    console.info(`Get the status success, data: ${JSON.stringify(data)}`);
  }, (error: BusinessError) => {
    console.error(`Get the status failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
  });
} catch (error) {
  console.error(`Get the status failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
}
```
