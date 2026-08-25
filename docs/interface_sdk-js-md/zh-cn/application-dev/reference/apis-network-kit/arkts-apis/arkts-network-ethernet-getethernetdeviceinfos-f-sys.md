# getEthernetDeviceInfos（系统接口）

## 导入模块

```TypeScript
import { ethernet } from 'kits/@kit.NetworkKit';
```

## getEthernetDeviceInfos

```TypeScript
function getEthernetDeviceInfos(): Promise<Array<EthernetDeviceInfos>>
```

获取本机以太网卡的设备信息（如供应商名称、产品名称、最大连接速率等）使用Promise异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.GET_NETWORK_INFO

**系统能力：** SystemCapability.Communication.NetManager.Ethernet

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[EthernetDeviceInfos](arkts-network-ethernet-ethernetdeviceinfos-i-sys.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [2201005](../errorcode-net-ethernet.md#2201005-设备信息不存在) |
