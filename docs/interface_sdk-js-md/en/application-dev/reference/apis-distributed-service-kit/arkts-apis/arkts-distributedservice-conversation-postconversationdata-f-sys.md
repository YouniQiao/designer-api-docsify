# postConversationData (System API)

## Modules to Import

```TypeScript
import { conversation } from 'kits/@kit.DistributedServiceKit';
```

## postConversationData

```TypeScript
function postConversationData(
    deviceId: string,
    bundleName: string,
    abilityName: string,
    msg: ArrayBuffer
  ): Promise<void>
```

向目标设备发送会话数据。目标设备须为同一账号下的可信设备。以目标设备的networkId或UDID进行设备寻址，数据发送至目标设备上与指定Bundle名和Ability名匹配的已注册监听应用。典型使用场景包括：跨设备协同指令发送。

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC and ohos.permission.sec.ACCESS_UDID

**Model restriction:** This API can be used only in the stage model.

<!--Device-conversation-function postConversationData(    deviceId: string,    bundleName: string,    abilityName: string,    msg: ArrayBuffer  ): Promise<void>--><!--Device-conversation-function postConversationData(    deviceId: string,    bundleName: string,    abilityName: string,    msg: ArrayBuffer  ): Promise<void>-End-->

**System capability:** SystemCapability.Communication.SoftBus.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | string | Yes | 目标设备的networkId或UDID。可通过调用 [getTrustedDevices()](arkts-distributedservice-conversation-gettrusteddevices-f-sys.md#gettrusteddevices)获取。networkId、UDID的长度都应为64字节。 传入无效值时返回错误码401。 |
| bundleName | string | Yes | 数据发送目标Bundle名，Bundle名长度范围为1-127字节，需与目标设备上通过 [registerConversationListener](arkts-distributedservice-conversation-registerconversationlistener-f-sys.md#registerconversationlistener)注册会话监听的应用Bundle名一致。 不满足此要求时，数据将无法送达目标应用。传入无效或空值时返回错误码401。 |
| abilityName | string | Yes | 数据发送目标Ability名，Ability名长度范围为1-127字节，需与目标设备上已注册会话监听的 Ability名一致。不满足此要求时，数据将无法送达目标应用。传入无效或空值时返回错误码401。 |
| msg | ArrayBuffer | Yes | 要发送的数据内容，一次调用最大支持发送10240字节。数据结构由应用层协议定义。传入空数据或 无效数据时返回错误码401。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回值的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Invalid parameter. The deviceId, bundleName, abilityName or msg is invalid or empty. |
| 801 | Capability not supported. |
| 201 | Permission denied. The application does not have the required permission to access distributed data. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 2004004 | Timeout while waiting for acknowledgement from the remote side. |
| 2004002 | Failed to start ability on the remote side. |
| 2004003 | Failed to send data. |
| 2000001 | Internal error. |
| 2004001 | Remote system version is too low. |

## Examples

```TypeScript
import { conversation } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let deviceId: string = 'device_network_id_or_udid'; // deviceId is the network ID or UDID of the target device obtained by calling conversation.getTrustedDevices().
  let bundleName: string = 'com.example.demo';
  let abilityName: string = 'EntryAbility';
  let msg: ArrayBuffer = new ArrayBuffer(10);
  let view = new Uint8Array(msg);
  view[0] = 1;

  conversation.postConversationData(deviceId, bundleName, abilityName, msg).then(() => {
    console.info(`postConversationData success`);
  }).catch((err: BusinessError) => {
    console.error(`postConversationData errCode: ${err.code}, errMessage: ${err.message}`);
  });
} catch (err) {
  const e: BusinessError = err as BusinessError;
  console.error(`postConversationData errCode: ${e.code}, errMessage: ${e.message}`);
}
```

