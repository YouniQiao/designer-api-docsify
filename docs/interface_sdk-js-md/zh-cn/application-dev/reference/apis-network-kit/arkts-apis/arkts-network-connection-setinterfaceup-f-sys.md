# setInterfaceUp（系统接口）

## 导入模块

```TypeScript
import { connection } from '@kit.NetworkKit';
```

## setInterfaceUp

```TypeScript
function setInterfaceUp(ifaceName: string): Promise<void>
```

将指定的网卡接口设置为启用状态，使其可以收发网络数据包，参与网络通信；启用后的网卡接口可以被路由子系统选择用于数据传输；系统可以检测到该网络的存在并尝试建立连接，使用Promise异步回调。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为26.0.0。

**需要权限：** ohos.permission.CONNECTIVITY_INTERNAL

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [ifaceName](arkts-network-ethernet-ethernetdeviceinfos-i-sys.md) | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |
