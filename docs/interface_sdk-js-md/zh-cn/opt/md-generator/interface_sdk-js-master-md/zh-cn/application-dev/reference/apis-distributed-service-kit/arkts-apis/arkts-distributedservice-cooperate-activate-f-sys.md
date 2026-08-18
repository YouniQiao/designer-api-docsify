# activate（系统接口）

## 导入模块

```TypeScript
```

## activate

```TypeScript
function activate(targetNetworkId: string, inputDeviceId: number, callback: AsyncCallback<void>): void
```

启动键鼠穿越，使用Callback异步回调。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [activateCooperate](arkts-distributedservice-cooperate-activatecooperate-f-sys.md#activatecooperate系统接口)(targetNetworkId: string, inputDeviceId: int, callback: AsyncCallback&lt;void&gt;)

<!--Device-cooperate-function activate(targetNetworkId: string, inputDeviceId: number, callback: AsyncCallback<void>): void--><!--Device-cooperate-function activate(targetNetworkId: string, inputDeviceId: number, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Msdp.DeviceStatus.Cooperate

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| targetNetworkId | string | 是 |
| inputDeviceId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [20900001](../../apis-distributedservice-kit/errorcode-devicestatus.md#20900001-操作输入设备失败) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let targetNetworkId = "networkId";
let inputDeviceId = 0;
try {
  cooperate.activate(targetNetworkId, inputDeviceId, (error: BusinessError) => {
    if (error) {
      console.error(`Start Keyboard mouse crossing failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
      return;
    }
    console.info(`Start Keyboard mouse crossing success.`);
  });
} catch (error) {
  console.error(`Start Keyboard mouse crossing failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
}
```


## activate

```TypeScript
function activate(targetNetworkId: string, inputDeviceId: number): Promise<void>
```

启动键鼠穿越，使用Promise异步回调。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [activateCooperate](arkts-distributedservice-cooperate-activatecooperate-f-sys.md#activatecooperate系统接口)(targetNetworkId: string, inputDeviceId: int)

<!--Device-cooperate-function activate(targetNetworkId: string, inputDeviceId: number): Promise<void>--><!--Device-cooperate-function activate(targetNetworkId: string, inputDeviceId: number): Promise<void>-End-->

**系统能力：** SystemCapability.Msdp.DeviceStatus.Cooperate

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| targetNetworkId | string | 是 |
| inputDeviceId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [20900001](../../apis-distributedservice-kit/errorcode-devicestatus.md#20900001-操作输入设备失败) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let targetNetworkId = "networkId";
let inputDeviceId = 0;
try {
  cooperate.activate(targetNetworkId, inputDeviceId).then(() => {
    console.info(`Start Keyboard mouse crossing success.`);
  }, (error: BusinessError) => {
    console.error(`Start Keyboard mouse crossing failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
  });
} catch (error) {
  console.error(`Start Keyboard mouse crossing failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
}
```
