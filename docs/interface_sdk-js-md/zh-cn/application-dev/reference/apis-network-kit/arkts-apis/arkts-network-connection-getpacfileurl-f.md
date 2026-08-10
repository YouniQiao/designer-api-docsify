# getPacFileUrl

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## getPacFileUrl

```TypeScript
function getPacFileUrl(): string
```

Obtain the URL {@link pacFileUrl} of the current PAC script.

**起始版本：** 20

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为20。

<!--Device-connection-function getPacFileUrl(): string--><!--Device-connection-function getPacFileUrl(): string-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | Returns the URL of the current PAC script or empty string if there is no PAC script. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2100002 | Failed to connect to the service. |

## 示例

```TypeScript
import { connection } from '@kit.NetworkKit';

let pacFileUrl = connection.getPacFileUrl();
console.info("Succeeded to get pacFileUrl");
```

