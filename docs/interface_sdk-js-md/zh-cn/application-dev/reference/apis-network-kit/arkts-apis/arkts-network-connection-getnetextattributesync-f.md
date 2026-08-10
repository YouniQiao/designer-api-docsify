# getNetExtAttributeSync

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## getNetExtAttributeSync

```TypeScript
function getNetExtAttributeSync(netHandle: NetHandle): string
```

Get the network extended attribute for a {@link NetHandle} object.To invoke this method, you must have the {@code ohos.permission.GET_NETWORK_INFO} permission.

**起始版本：** 20

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为20。

**需要权限：** ohos.permission.GET_NETWORK_INFO

<!--Device-connection-function getNetExtAttributeSync(netHandle: NetHandle): string--><!--Device-connection-function getNetExtAttributeSync(netHandle: NetHandle): string-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netHandle | [NetHandle](arkts-network-connection-nethandle-i.md) | 是 | Indicates the network to be queried. See {@link NetHandle}. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | The netExtAttribute string returned by the function. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 201 | Permission denied. |

## 示例

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let netHandle = connection.getDefaultNetSync();
if (netHandle.netId != 0) {
  let netExtAttribute: string = connection.getNetExtAttributeSync(netHandle);
  console.info("Succeeded to getNetExtAttribute: " + netExtAttribute);
}
```

