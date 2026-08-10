# activateCooperateWithOptions (System API)

## Modules to Import

```TypeScript
import { cooperate } from 'kits/@kit.DistributedServiceKit';
```

## activateCooperateWithOptions

```TypeScript
function activateCooperateWithOptions(targetNetworkId: string, inputDeviceId: int,
    cooperateOptions?: CooperateOptions
  ): Promise<void>
```

启动键鼠穿越，使用选项开始屏幕跳转。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.COOPERATE_MANAGER

<!--Device-cooperate-function activateCooperateWithOptions(targetNetworkId: string, inputDeviceId: int,    cooperateOptions?: CooperateOptions  ): Promise<void>--><!--Device-cooperate-function activateCooperateWithOptions(targetNetworkId: string, inputDeviceId: int,    cooperateOptions?: CooperateOptions  ): Promise<void>-End-->

**System capability:** SystemCapability.Msdp.DeviceStatus.Cooperate

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| targetNetworkId | string | Yes | 键鼠穿越目标设备描述符。 |
| inputDeviceId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 发起穿越操作的输入设备ID。 |
| cooperateOptions | [CooperateOptions](arkts-distributedservice-cooperate-cooperateoptions-i-sys.md) | No | 穿越可选控制参数，用于控制穿出点具体位置等。不设置此参数时，本接口能力 与[cooperate.activateCooperate](arkts-distributedservice-cooperate-activatecooperate-f-sys.md#activatecooperate) 相同。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission denied. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 20900001 | Service exception. Possible causes: &lt;br&gt;1. A system error, such as null pointer, container-related exception, or IPC exception. &lt;br&gt;2. N-API invocation exception or invalid N-API status. |

## Examples

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

