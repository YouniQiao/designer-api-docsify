# getAddressesByNameWithOptions

## Modules to Import

```TypeScript
import { connection } from '@kit.NetworkKit';
```

## getAddressesByNameWithOptions

```TypeScript
function getAddressesByNameWithOptions(host: string, option?: QueryOptions): Promise<Array<NetAddress>>
```

Resolves a host name to obtain all IP addresses with specified query option.

**Since:** 23

**Required permissions:** ohos.permission.INTERNET

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function getAddressesByNameWithOptions(host: string, option?: QueryOptions): Promise<Array<NetAddress>>--><!--Device-connection-function getAddressesByNameWithOptions(host: string, option?: QueryOptions): Promise<Array<NetAddress>>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| host | string | Yes |
| option | [QueryOptions](arkts-network-connection-queryoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;NetAddress & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [2100001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-network-kit/errorcode-net-connection.md#2100001-invalid-parameter-value) |
| [2100002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-network-kit/errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-network-kit/errorcode-net-connection.md#2100003-system-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
let option: connection.QueryOptions = {
  family: connection.FamilyType.FAMILY_TYPE_IPV4
};
connection.getAddressesByNameWithOptions("www.example.com", option).then((data: connection.NetAddress[]) => {
  console.info(`Succeeded to get data: ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`get ERROR msg: ${JSON.stringify(err)}`)
});
```
