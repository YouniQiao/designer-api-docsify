# setInterfaceUp（系统接口）

## 导入模块

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## setInterfaceUp

```TypeScript
function setInterfaceUp(ifaceName: string): Promise<void>
```

Set a specific interface up.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**需要权限：** ohos.permission.CONNECTIVITY_INTERNAL

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-connection-function setInterfaceUp(ifaceName: string): Promise<void>--><!--Device-connection-function setInterfaceUp(ifaceName: string): Promise<void>-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ifaceName | string | 是 | the name of the interface to set up. &lt;br&gt;Value range:(0,1024] &lt;br&gt;Name of the actual network adapter to be started If the network adapter exists, try to up the network adapter. If the network adapter does not exist or does not meet the up condition, the network adapter fails to be up. The network adapter exists in the kernel, and the network adapter meets the up condition. None None |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2100003 | System internal error. |
| 201 | Permission denied. |
| 202 | Non-system applications use system APIs. |

