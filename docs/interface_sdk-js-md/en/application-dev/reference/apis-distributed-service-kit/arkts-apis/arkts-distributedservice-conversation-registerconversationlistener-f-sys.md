# registerConversationListener (System API)

## Modules to Import

```TypeScript
import { conversation } from 'kits/@kit.DistributedServiceKit';
```

## registerConversationListener

```TypeScript
function registerConversationListener(
    bundleName: string,
    abilityName: string,
    dataCallback: DataCallback
  ): void
```

注册会话监听，接收来自同一账号下可信设备的数据。当远端设备通过  
[postConversationData](arkts-distributedservice-conversation-postconversationdata-f-sys.md#postconversationdata)发送数据到达本地设备后，数据分发至与Bundle名和Ability名匹配的已注册回调函数。同一Bundle名和Ability名只能注册一个监听器，重复注册将覆盖之前已注册的监听器。

**配对调用**：需与注销监听器[unregisterConversationListener](arkts-distributedservice-conversation-unregisterconversationlistener-f-sys.md#unregisterconversationlistener)配对使用，不再需要接收消息时应调用注销监听器以释放资源，未注销会导致资源持续占用。

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC and ohos.permission.sec.ACCESS_UDID

**Model restriction:** This API can be used only in the stage model.

<!--Device-conversation-function registerConversationListener(    bundleName: string,    abilityName: string,    dataCallback: DataCallback  ): void--><!--Device-conversation-function registerConversationListener(    bundleName: string,    abilityName: string,    dataCallback: DataCallback  ): void-End-->

**System capability:** SystemCapability.Communication.SoftBus.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 接收数据的Bundle名，Bundle名长度范围为1-127字节，需与本应用的Bundle名一致。 不满足此要求时，监听器无法正确接收数据。传入无效或空值时返回错误码401。 |
| abilityName | string | Yes | 接收数据的Ability名，Ability名长度范围为1-127字节，需与本应用中的Ability名一致。 不满足此要求时，监听器无法正确接收数据。传入无效或空值时返回错误码401。 |
| dataCallback | [DataCallback](arkts-distributedservice-conversation-datacallback-t-sys.md) | Yes | 收到数据时的回调函数，用于接收跨设备数据。传入无效值时返回错误码401。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Invalid parameter. The bundleName, abilityName or dataCallback is invalid or empty. |
| 801 | Capability not supported. |
| 201 | Permission denied. The application does not have the required permission to access distributed data. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 2000001 | Internal error. |

## Examples

```TypeScript
import { conversation } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let bundleName: string = 'com.example.demo';
  let abilityName: string = 'EntryAbility';

  conversation.registerConversationListener(bundleName, abilityName, (deviceId: string, msg: ArrayBuffer) => {
    console.info(`received message, deviceId: ${deviceId}, msg length: ${msg.byteLength}`);
  });
  console.info(`registerConversationListener success`);
} catch (err) {
  const e: BusinessError = err as BusinessError;
  console.error(`registerConversationListener errCode: ${e.code}, errMessage: ${e.message}`);
}
```

