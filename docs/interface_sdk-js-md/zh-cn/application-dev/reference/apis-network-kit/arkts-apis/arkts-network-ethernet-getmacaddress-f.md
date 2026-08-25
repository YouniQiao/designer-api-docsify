# getMacAddress

## 导入模块

```TypeScript
import { ethernet } from 'kits/@kit.NetworkKit';
```

## getMacAddress

```TypeScript
function getMacAddress(): Promise<Array<MacAddressInfo>>
```

获取所有以太网网卡名称及对应网卡的MAC地址信息，使用Promise方式作为异步方法。

**起始版本：** 14

**需要权限：** ohos.permission.GET_ETHERNET_LOCAL_MAC

**系统能力：** SystemCapability.Communication.NetManager.Ethernet

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[MacAddressInfo](arkts-network-ethernet-macaddressinfo-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [2200002](../errorcode-net-ethernet.md#2200002-连接服务失败) |
| [2201005](../errorcode-net-ethernet.md#2201005-设备信息不存在) |
